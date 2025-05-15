import asyncio
import os
import unittest

from chesscrypto.Players.engineNest import discoverer
from chesscrypto.System import uistuff
from chesscrypto.widgets import gamewidget
from chesscrypto.widgets.discovererDialog import DiscovererDialog
from chesscrypto.perspectives.games import Games
from chesscrypto.perspectives.learn import Learn
from chesscrypto.perspectives.learn.EndgamesPanel import start_endgame_from, ENDGAMES
from chesscrypto.perspectives.learn.LecturesPanel import start_lecture_from, LECTURES
from chesscrypto.perspectives.learn.LessonsPanel import start_lesson_from, LESSONS
from chesscrypto.perspectives.learn.PuzzlesPanel import start_puzzle_from, PUZZLES
from chesscrypto.perspectives import perspective_manager

# fix PATH on travis
if "/usr/games" not in os.environ["PATH"]:
    os.environ["PATH"] = "/usr/games:%s" % os.environ["PATH"]

discoverer.pre_discover()


class LearnTests(unittest.TestCase):
    def setUp(self):
        widgets = uistuff.GladeWidgets("ChessCrypto.glade")
        gamewidget.setWidgets(widgets)
        perspective_manager.set_widgets(widgets)

        self.games_persp = Games()
        perspective_manager.add_perspective(self.games_persp)

        self.learn_persp = Learn()
        self.learn_persp.create_toolbuttons()
        perspective_manager.add_perspective(self.learn_persp)

        perspective_manager.current_perspective = self.learn_persp

        dd = DiscovererDialog(discoverer)
        self.dd_task = asyncio.create_task(dd.start())

    def test0(self):
        """Init layout"""
        self.learn_persp.activate()
        self.assertEqual(len(self.learn_persp.store), 1)

    def test1(self):
        """Start next endgame"""
        pieces = ENDGAMES[0][0].lower()
        start_endgame_from(pieces)

    def test2(self):
        """Start next lecture"""
        filename = LECTURES[0][0]
        start_lecture_from(filename)

    def test3(self):
        """Start next lesson"""
        filename = LESSONS[0][0]
        start_lesson_from(filename)

    def test4(self):
        """Start next puzzle"""
        filename = PUZZLES[0][0]
        start_puzzle_from(filename)


if __name__ == "__main__":
    unittest.main()
