from random import randrange

from chesscrypto.System import conf
from chesscrypto.System import uistuff
from chesscrypto.widgets import mainwindow
from chesscrypto.Savers.remotegame import get_internet_game_providers


class TipOfTheDay:
    def __init__(self):
        self.widgets = uistuff.GladeWidgets("tipoftheday.glade")
        self.widgets["window1"].set_transient_for(mainwindow())
        uistuff.keepWindowSize(
            "tipoftheday", self.widgets["window1"], (320, 240), uistuff.POSITION_CENTER
        )

        self.widgets["checkbutton1"].set_active(conf.get("show_tip_at_startup"))
        self.widgets["checkbutton1"].connect(
            "toggled", lambda w: conf.set("show_tip_at_startup", w.get_active())
        )
        self.widgets["close_button"].connect(
            "clicked", lambda w: self.widgets["window1"].emit("delete-event", None)
        )
        self.widgets["window1"].connect(
            "delete_event", lambda w, a: self.widgets["window1"].destroy()
        )
        self.widgets["back_button"].connect(
            "clicked", lambda w: self.set_currentIndex(self.tips_curindex - 1)
        )
        self.widgets["forward_button"].connect(
            "clicked", lambda w: self.set_currentIndex(self.tips_curindex + 1)
        )

        self.tips_fixed = 2
        self.tips = [
            # chesscrypto facts -- The first tips_fixed messages are always displayed first
            _(
                "chesscrypto is an open-source chess application that can be enhanced by any chess enthusiast: bug reports, source code, documentation, translations, feature requests, user assistance... Let's get in touch at <b>https://chesscrypto.github.io</b>"
            ),
            _(
                "chesscrypto supports a wide range of chess engines, variants, Internet servers, and lessons. It is a perfect desktop application to conveniently improve your chess skills."
            ),
            _(
                "The releases of chesscrypto hold the name of historical world chess champions. Do you know the name of the current world chess champion?"
            ),
            _(
                "Did you know that you can help translate chesscrypto into your own language, <b>Help</b> > <b>Translate chesscrypto</b>."
            ),
            _(
                "A game consists of an opening, a middle-game and an end-game. chesscrypto is able to train you thanks to its opening book, its supported chess engines and its training module."
            ),
            # Chess facts
            _(
                "Did you know that it is possible to finish a chess game in just 2 turns?"
            ),
            _(
                "Did you know that a knight is better placed in the center of the board?"
            ),
            _(
                "Did you know that moving the queen at the very beginning of a game does not offer any particular advantage?"
            ),
            _(
                "Did you know that having two-colored bishops working together is very powerful?"
            ),
            _("Did you know that the rooks are generally engaged late in the game?"),
            _(
                "Did you know that the king can move across two squares under certain conditions? This is called "
                "castling"
                "."
            ),
            _(
                "Did you know that the number of possible chess games exceeds the number of atoms in the Universe?"
            ),
            # General UI
            _(
                "You can start a new game with <b>Game</b> > <b>New Game</b>, then choose the <b>Players</b>, <b>Time Control</b> and <b>Chess Variants</b>."
            ),
            _(
                "You can choose from 20 different difficulties to play against the computer. It will mainly affect the engines available time to think."
            ),
            _(
                "The level 20 engine difficulty gives full autonomy to the chess engine in managing its own time during the game."
            ),
            _(
                "To save a game use <b>Game</b> > <b>Save Game As</b>, provide the filename, and choose where you want it to be saved. At the bottom choose the extension type of the file, and <b>Save</b>."
            ),
            _(
                " "
                "Calling the flag"
                " is the termination of the current game when the time of your opponent is over. If the clock is on your side, click on the menu item <b>Actions</b> > <b>Call Flag</b> to claim the victory."
            ),
            _(
                "Press <b>Ctrl+Z</b> to ask your opponent to rollback the last played move. Against a computer or for an unrated game, undoing is generally automatically accepted."
            ),
            _(
                "To play in <b>Fullscreen mode</b>, just press the key <b>F11</b>. Press it again to exit this mode."
            ),
            _(
                "Many sounds are emitted by chesscrypto while you are playing if you activate them in the preferences: <b>Settings</b> > <b>Preferences</b> > <b>Sound tab</b> > <b>Use sounds in chesscrypto</b>."
            ),
            _(
                "Did you know that a game is generally finished after 20 to 40 moves per player? The estimated duration of a game is displayed when you configure a new game."
            ),
            _(
                "The standard file format to manage chess games is <b>PGN</b>. It stands for "
                "Portable Game Notation"
                ". Do not get confused with PNG which is a common file format to store drawings and pictures."
            ),
            _(
                "You can share a position by using the exchange format <b>FEN</b>, which stands for "
                "Forsyth-Edwards Notation"
                ". This format is also adapted for the chess variants."
            ),
            # Analysis
            _(
                "You must define a chess engine in the preferences in order to use the local chess analysis. By default, chesscrypto recommends the use of the free engine named Stockfish which is renowned to be among the strongest engines in the world."
            ),
            _(
                "<b>Hint mode</b> analyzes your game to show you the best current move. Enable it with the shortcut <b>Ctrl+H</b> or from the <b>View</b> menu."
            ),
            _(
                "<b>Spy mode</b> analyzes the threats and shows the best move that your opponent would play if it was his turn. Enable it with the shortcut <b>Ctrl+Y</b> or from the <b>View</b> menu."
            ),
            _(
                "<b>Ponder</b> is an option available in some chess engines that allows thinking when it is not the engine's turn. Using this feature will consume more resources on your computer."
            ),
            _(
                "<b>MultiPV</b> is an option of some chess engines that shows other possible good moves. They are displayed in the panel <b>Hints</b>. The value can be adapted from that panel with a double-click on the displayed figure."
            ),
            _(
                "You cannot use the local chess analysis mode while you are playing an unterminated game over the Internet. Else you would be a cheater."
            ),
            _(
                "An evaluation of +2.3 is an advantage for White of more than 2 pawns, even if White and Black have the same number of pawns. The position of all the pieces and their mobility are some of the factors that contribute to the engine score."
            ),
            _(
                "chesscrypto includes a chess engine that offers an evaluation for any chess position. Winning against chesscrypto engine is a coherent way to succeed in chess and improve your skills."
            ),
            _(
                "The rating is your strength: 1500 is a good average player, 2000 is a national champion and 2800 is the best human chess champion. You can view the ratings of the players via the <b>Properties</b> in the <b>Game</b> menu. The difference of points gives you your chance to win and the projected evolution of your rating. If your rating is provisional, it is appended with a question mark '?', for example "
                "1399?"
                "."
            ),
            _(
                "Several rating systems exist to evaluate your skills in chess. The most common one is called ELO (from its creator Arpad Elo) which was established in 1970. Schematically, the concept is to engage +/- 20 points for a game and that you will win or lose proportionally to the difference of ELO points you have with your opponent."
            ),
            _(
                "Each chess engine has its own evaluation function. It is normal to get varying scores for the same position when using different engines."
            ),
            # Opening book and EGDB
            _(
                "The opening book gives you the first few moves that are considered to be good from a theoretical perspective. You are free to play any other legal move."
            ),
            _(
                "The <b>Gaviota tables</b> are precalculated positions that tell the final outcome of the current game in terms of win, loss or draw."
            ),
            _(
                "Did you know that your computer is too small to store a 7-piece endgame database? That's why the Gaviota tablebase is limited to 5 pieces."
            ),
            _(
                "A tablebase can be connected either to chesscrypto, or to a compatible chess engine."
            ),
            _(
                "The <b>DTZ</b> is the "
                "distance to zero"
                ", so the remaining possible moves to end the game in a tie as soon as possible."
            ),
            # Variant chess
            _(
                "The chess variants consist of changing the start position, the rules of the game, the types of the pieces... The gameplay is totally modified, so you must use specialized chess engines to play against the computer."
            ),
            _(
                "In Chess960, the order of the main pieces are shuffled in a precise manner. Therefore, you cannot use the opening book and you should change your tactical habits."
            ),
            _(
                "When playing crazyhouse chess, the captured pieces change of ownership and can reappear on the board at a later turn."
            ),
            _(
                "Suicide chess, giveaway chess or antichess are all the same variant: you must give your pieces to your opponent by forcing the captures like at draughts (aka checkers). The outcome of the game can change completely if you make an incorrect move."
            ),
            _(
                "Playing horde in chesscrypto consists in destroying an onslaught of 36 white pawns with a normal set of black pieces."
            ),
            _(
                "You might be interested in playing "
                "King of the hill"
                " where the goal is to either checkmate or to place your king in the middle of the board, instead of protecting it in a corner of the board as usual."
            ),
            _(
                "A lot of fun is offered by atomic chess where one destroys all the surrounding main pieces at each capture."
            ),
            _(
                "The experienced chess players can use blind pieces by starting a new variant game."
            ),
            # Internet chess
            _(
                "You should sign up online to play on an Internet chess server, so that you can find your games later and see the evolution of your rating. In <b>Preferences</b> chesscrypto provides the possibility to save your played games locally as well."
            ),
            _(
                "Time compensation is a feature that doesn't waste your clock time because of the latency of your Internet connection. The module can be downloaded from the menu <b>Edit</b> > <b>Externals</b>."
            ),
            _(
                "You can play against chess engines on an Internet chess server. Use the filter to include or exclude them from the available players."
            ),
            _(
                "The communication with an Internet chess server is not standardized. Therefore, you can only connect to the supported chess servers in chesscrypto, like freechess.org or chessclub.com"
            ),
            _(
                "chesscrypto is able to download chess games remotely from the following websites:"
            )
            + "\n\n"
            + ", ".join(get_internet_game_providers()),
            # Externals
            _(
                "chesscrypto uses the external module Scoutfish to evaluate the chess databases. For example, it is possible to extract the games where some pieces are in precise count or positions."
            ),
            _(
                "Parser/ChessDB is an external module used by chesscrypto to show the expected outcome for a given position."
            ),
            _(
                "SQLite is an internal module used to describe the loaded PGN files, so that chesscrypto can retrieve the games very quickly during a search."
            ),
            _(
                "chesscrypto generates three information files when a PGN file is opened: .sqlite (description), .scout (positions), .bin (book and outcomes). These files can be removed manually if desired."
            ),
            # Lessons
            _(
                "chesscrypto provides offline lessons to learn chess so that you will never be disappointed if you have no Internet connection."
            ),
            _(
                "To start Learning, click on the <b>Book icon</b> available on the <b>Welcome</b> screen. Or choose a category next to the button to start an activity directly."
            ),
            _(
                "The <b>Lectures</b> are commented games to learn step-by-step strategy and principles of some chess techniques. Just watch, read and learn."
            ),
            _(
                "Whatever the number of pawns, an <b>end-game</b> starts when the board consists of certain main pieces : 1 rook vs 1 bishop, 1 queen versus 2 rooks, etc... Knowing the right endgame moves will help you not miss a checkmate!"
            ),
            _(
                "A <b>Puzzle</b> is a set of simple positions classified by themes where you guess the best moves. It helps you understand patterns to perform an accurate attack or defense."
            ),
            _(
                "A <b>Lesson</b> is a complex study that explains the tactics for a given position. It is common to view circles and arrows over the board to focus on the behavior of the pieces, the threats, etc..."
            ),
        ]
        self.tips_seed = conf.get("tips_seed")
        if self.tips_seed == 0:  # Forbidden value
            self.tips_seed = 123456789 + randrange(876543210)
            conf.set("tips_seed", self.tips_seed)
        self.tips_curindex = conf.get("tips_index")
        self.shuffleTips()

    def xorshift(self):
        self.tips_seed ^= (
            (self.tips_seed << 13) ^ (self.tips_seed >> 17) ^ (self.tips_seed << 5)
        )
        return self.tips_fixed + self.tips_seed % (len(self.tips) - self.tips_fixed)

    def shuffleTips(self):
        # Because of the fixed seed, the same shuffled list will be returned.
        # The idea is to manage all the tips above by category but to display
        # them once from a random order that can be reproduced at every run.
        for i in range(len(self.tips) - self.tips_fixed):
            p1 = self.xorshift()
            p2 = self.xorshift()
            if p1 != p2:
                tmp = self.tips[p1]
                self.tips[p1] = self.tips[p2]
                self.tips[p2] = tmp

    def show(self):
        self.set_currentIndex(self.tips_curindex)
        self.widgets["window1"].show()
        self.widgets["window1"].present()

    def set_currentIndex(self, value):
        if len(self.tips) == 0:
            return
        if value < 0:
            value = len(self.tips) - 1
        elif value >= len(self.tips):
            value = 0
        self.tips_curindex = value
        conf.set(
            "tips_index", self.tips_curindex + 1
        )  # To get the next message loaded at the next run
        self.widgets["tipfield"].set_markup(self.tips[value])
