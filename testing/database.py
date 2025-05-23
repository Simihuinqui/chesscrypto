import unittest

from chesscrypto.System import uistuff
from chesscrypto.widgets import gamewidget
from chesscrypto.perspectives.games import Games
from chesscrypto.perspectives.database import Database
from chesscrypto.perspectives import perspective_manager


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        widgets = uistuff.GladeWidgets("ChessCrypto.glade")
        gamewidget.setWidgets(widgets)
        perspective_manager.set_widgets(widgets)

        self.games_persp = Games()
        perspective_manager.add_perspective(self.games_persp)

        self.database_persp = Database()
        self.database_persp.create_toolbuttons()
        perspective_manager.add_perspective(self.database_persp)

    def test1(self):
        """Open a .pgn database"""
        filename = "gamefiles/world_matches.pgn"
        self.database_persp.open_chessfile(filename)


if __name__ == "__main__":
    unittest.main()
