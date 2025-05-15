import asyncio
import os

from chesscrypto.System.prefix import addDataPrefix
from chesscrypto.Utils.const import WHITE, BLACK, LOCAL, WAITING_TO_START, HINT, LESSON
from chesscrypto.Utils.LearnModel import LearnModel
from chesscrypto.Utils.TimeModel import TimeModel
from chesscrypto.Players.Human import Human
from chesscrypto.System import conf
from chesscrypto.perspectives import perspective_manager
from chesscrypto.perspectives.learn.generateLessonsSidepanel import generateLessonsSidepanel
from chesscrypto.perspectives.learn import lessons_solving_progress
from chesscrypto.perspectives.learn.PuzzlesPanel import start_puzzle_game
from chesscrypto.Savers.pgn import PGNFile
from chesscrypto.System.protoopen import protoopen
from chesscrypto.Players.engineNest import discoverer

__title__ = _("Lessons")

__icon__ = addDataPrefix("glade/panel_book.svg")

__desc__ = _('Guided interactive lessons in "guess the move" style')


LESSONS = []
for elem in sorted(os.listdir(path=addDataPrefix("learn/lessons/"))):
    if elem.startswith("lichess_study") and elem.endswith(".pgn"):
        title = elem.replace("beta-lichess-practice-", "")
        title = title[14 : title.find("_by_")].replace("-", " ").capitalize()
        LESSONS.append((elem, title, "lichess.org"))
    elif elem.endswith(".pgn"):
        LESSONS.append((elem, elem.replace("-", " ").capitalize(), "chesscrypto.io"))

# Note: Find the declaration of the class Sidepanel at the end of the file


def start_lesson_from(filename, index=None):
    chessfile = PGNFile(protoopen(addDataPrefix("learn/lessons/%s" % filename)))
    chessfile.limit = 1000
    chessfile.init_tag_database()
    records, plys = chessfile.get_records()

    progress = lessons_solving_progress.get(filename, [0] * chessfile.count)

    if index is None:
        try:
            index = progress.index(0)
        except ValueError:
            index = 0

    rec = records[index]

    timemodel = TimeModel(0, 0)
    gamemodel = LearnModel(timemodel)

    chessfile.loadToModel(rec, -1, gamemodel)

    if len(gamemodel.moves) > 0:
        start_lesson_game(gamemodel, filename, chessfile, records, index, rec)
    else:
        start_puzzle_game(gamemodel, filename, records, index, rec, from_lesson=True)


def start_lesson_game(gamemodel, filename, chessfile, records, index, rec):
    gamemodel.set_learn_data(LESSON, filename, index, len(records))

    # Lichess doesn't export some study data to .pgn like
    # Orientation, Analysis mode, Chapter pinned comment, move hint comments, general fail comment
    if filename.startswith(
        "lichess_study_beta-lichess-practice-checkmating-with-a-knight-and-bishop"
    ):
        if index in (4, 6, 8, 9):
            gamemodel.tags["Orientation"] = "White"
            print(index, '[Orientation "White"]')

    color = gamemodel.boards[0].color
    player_name = conf.get("firstName")

    w_name = player_name if color == WHITE else "ChessCrypto"
    b_name = "ChessCrypto" if color == WHITE else player_name

    p0 = (LOCAL, Human, (WHITE, w_name), w_name)
    p1 = (LOCAL, Human, (BLACK, b_name), b_name)

    def learn_success(gamemodel):
        gamemodel.scores = {}
        chessfile.loadToModel(rec, -1, gamemodel)
        progress = lessons_solving_progress[gamemodel.source]
        progress[gamemodel.current_index] = 1
        lessons_solving_progress[gamemodel.source] = progress
        if "FEN" in gamemodel.tags:
            asyncio.create_task(gamemodel.restart_analyzer(HINT))

    gamemodel.connect("learn_success", learn_success)

    def on_game_started(gamemodel):
        perspective.activate_panel("annotationPanel")
        if "FEN" in gamemodel.tags:
            asyncio.create_task(
                gamemodel.start_analyzer(HINT, force_engine=discoverer.getEngineLearn())
            )

    gamemodel.connect("game_started", on_game_started)

    gamemodel.status = WAITING_TO_START
    perspective = perspective_manager.get_perspective("games")
    asyncio.create_task(perspective.generalStart(gamemodel, p0, p1))


# Sidepanel is a class
Sidepanel = generateLessonsSidepanel(
    solving_progress=lessons_solving_progress,
    learn_category_id=LESSON,
    entries=LESSONS,
    start_from=start_lesson_from,
)
