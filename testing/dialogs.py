import asyncio
import unittest
import sys

from gi.repository import Gtk

from chesscrypto.Utils.const import FEN_START, NORMALCHESS
from chesscrypto.Players.engineNest import discoverer
from chesscrypto.System import uistuff
from chesscrypto.widgets import gamewidget
from chesscrypto.widgets import enginesDialog
from chesscrypto.widgets import newGameDialog
from chesscrypto.widgets.newGameDialog import COPY, CLEAR, PASTE, INITIAL
from chesscrypto.widgets import preferencesDialog
from chesscrypto.widgets.discovererDialog import DiscovererDialog
from chesscrypto.perspectives.games import Games
from chesscrypto.perspectives.welcome import Welcome
from chesscrypto.perspectives import perspective_manager


discoverer.pre_discover()


class DialogTests(unittest.TestCase):
    def setUp(self):
        if sys.platform == "win32":
            from asyncio.windows_events import ProactorEventLoop

            loop = ProactorEventLoop()
            asyncio.set_event_loop(loop)
        else:
            loop = asyncio.SelectorEventLoop()
            asyncio.set_event_loop(loop)

        self.loop = asyncio.get_event_loop()
        self.loop.set_debug(enabled=True)

        widgets = uistuff.GladeWidgets("ChessCrypto.glade")
        gamewidget.setWidgets(widgets)
        perspective_manager.set_widgets(widgets)

        self.welcome_persp = Welcome()
        perspective_manager.add_perspective(self.welcome_persp)

        self.games_persp = Games()
        perspective_manager.add_perspective(self.games_persp)

    def tearDown(self):
        self.games_persp.gamewidgets.clear()

    def test0(self):
        """Open engines dialogs"""

        # engines dialog
        enginesDialog.run(gamewidget.getWidgets())
        engines = [item[1] for item in enginesDialog.engine_dialog.allstore]
        self.assertTrue("ChessCrypto.py" in engines)

    def test1(self):
        """Open new game dialog"""

        dialog = newGameDialog.NewGameMode()

        async def coro(dialog):
            def on_gmwidg_created(persp, gmwidg, event):
                event.set()

            event = asyncio.Event()
            self.games_persp.connect("gmwidg_created", on_gmwidg_created, event)

            dialog.run()
            dialog.widgets["newgamedialog"].response(Gtk.ResponseType.OK)

            await event.wait()

        self.loop.run_until_complete(coro(dialog))

    def test2(self):
        """Open setup position dialog"""

        dialog = newGameDialog.SetupPositionExtension()

        async def coro(dialog):
            def on_gmwidg_created(persp, gmwidg, event):
                event.set()

            event = asyncio.Event()
            self.games_persp.connect("gmwidg_created", on_gmwidg_created, event)

            dialog.run(FEN_START, NORMALCHESS)
            dialog.widgets["newgamedialog"].response(INITIAL)
            dialog.widgets["newgamedialog"].response(COPY)
            dialog.widgets["newgamedialog"].response(CLEAR)
            dialog.widgets["newgamedialog"].response(PASTE)
            dialog.widgets["newgamedialog"].response(Gtk.ResponseType.OK)

            await event.wait()

        self.loop.run_until_complete(coro(dialog))

    @unittest.skipIf(
        sys.platform == "win32",
        "Windows produces TypeError: could not get a reference to type class\n"
        + "on line: cls.sourcebuffer = GtkSource.Buffer()",
    )
    def test3(self):
        """Start a new game from enter notation dialog"""

        dialog = newGameDialog.EnterNotationExtension()

        async def coro(dialog):
            def on_gmwidg_created(persp, gmwidg, event):
                event.set()

            event = asyncio.Event()
            self.games_persp.connect("gmwidg_created", on_gmwidg_created, event)

            dialog.run()
            dialog.sourcebuffer.set_text("1. f3 e5 2. g4 Qh4")
            dialog.widgets["newgamedialog"].response(Gtk.ResponseType.OK)

            await event.wait()

        self.loop.run_until_complete(coro(dialog))

        # Show the firs move of the game
        async def coro1():
            def on_shown_changed(view, shown, event):
                if shown == 1:
                    event.set()

            gmwidg = self.games_persp.gamewidgets.pop()
            view = gmwidg.board.view
            board = gmwidg.gamemodel.boards[1]

            event = asyncio.Event()
            view.connect("shownChanged", on_shown_changed, event)

            view.setShownBoard(board)

            await event.wait()

        self.loop.run_until_complete(coro1())

    def test4(self):
        """Open preferences dialog"""

        widgets = gamewidget.getWidgets()
        preferencesDialog.run(widgets)

        notebook = widgets["preferences_notebook"]
        self.assertIsNotNone(preferencesDialog.general_tab)

        notebook.next_page()
        self.assertIsNotNone(preferencesDialog.hint_tab)

        notebook.next_page()
        self.assertIsNotNone(preferencesDialog.theme_tab)

        notebook.next_page()
        self.assertIsNotNone(preferencesDialog.sound_tab)

        notebook.next_page()
        self.assertIsNotNone(preferencesDialog.save_tab)

    def test5(self):
        """Open engine discoverer dialog"""
        dd = DiscovererDialog(discoverer)

        async def coro():
            def on_all_engines_discovered(discoverer, event):
                event.set()

            event = asyncio.Event()
            discoverer.connect(
                "all_engines_discovered", on_all_engines_discovered, event
            )

            asyncio.create_task(dd.start())

            await event.wait()

        self.loop.run_until_complete(coro())


if __name__ == "__main__":
    unittest.main()
