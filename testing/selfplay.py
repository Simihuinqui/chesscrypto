import asyncio
import logging
import unittest
import sys
from io import StringIO

from chesscrypto.Savers.pgn import save
from chesscrypto.Players.engineNest import discoverer
from chesscrypto.Utils.GameModel import GameModel
from chesscrypto.Utils.TimeModel import TimeModel
from chesscrypto.Utils.const import (
    WHITE,
    BLACK,

    NORMALCHESS,
    FISCHERRANDOMCHESS,
   
)
from chesscrypto.Variants import variants
from chesscrypto.System.Log import log

log.logger.setLevel(logging.INFO)

discoverer.pre_discover()

PYCHESS_VARIANTS = (
    SCHESS,
    NORMALCHESS,
    CRAZYHOUSECHESS,
    FISCHERRANDOMCHESS,
    LOSERSCHESS,
    SUICIDECHESS,
    THREECHECKCHESS,
    KINGOFTHEHILLCHESS,
    WILDCASTLESHUFFLECHESS,
    ASEANCHESS,
    MAKRUKCHESS,
    CAMBODIANCHESS,
    SITTUYINCHESS,
    GIVEAWAYCHESS,
    ATOMICCHESS,
    HORDECHESS,
    ASYMMETRICRANDOMCHESS,
    RANDOMCHESS,
    WILDCASTLECHESS,
    SHUFFLECHESS,
    CORNERCHESS,
    PLACEMENTCHESS,
)


class CECPTests(unittest.TestCase):
    def setUp(self):
        self.engine = discoverer.getEngineByName("ChessCrypto.py")

    def test(self):
        """Play ChessCrypto-ChessCrypto 1 min variant games"""

        if sys.platform == "win32":
            from asyncio.windows_events import ProactorEventLoop

            loop = ProactorEventLoop()
            asyncio.set_event_loop(loop)
        else:
            loop = asyncio.SelectorEventLoop()
            asyncio.set_event_loop(loop)

        loop = asyncio.get_event_loop()
        loop.set_debug(enabled=True)

        for vari in PYCHESS_VARIANTS:
            variant = variants[vari]

            async def coro():
                self.p0 = await discoverer.initEngine(self.engine, WHITE, False)
                self.p1 = await discoverer.initEngine(self.engine, BLACK, False)

            loop.run_until_complete(coro())

            def optionsCallback(engine):
                engine.setOptionVariant(variant)
                engine.setOptionStrength(1, False)
                engine.setOptionTime(60, 0, 0)

            self.p0.connect("readyForOptions", optionsCallback)
            self.p1.connect("readyForOptions", optionsCallback)

            async def coro(variant):
                self.game = GameModel(TimeModel(60, 0), variant)
                self.game.setPlayers([self.p0, self.p1])

                def on_game_end(game, state, event):
                    event.set()

                event = asyncio.Event()
                self.game.connect("game_ended", on_game_end, event)

                self.p0.prestart()
                self.p1.prestart()

                if self.game.variant.need_initial_board:
                    for player in self.game.players:
                        player.setOptionInitialBoard(self.game)

                print(variant.name)
                self.game.start()

                await event.wait()

                pgn = StringIO()
                print(save(pgn, self.game))

                self.assertIsNone(self.p0.invalid_move)
                self.assertIsNone(self.p1.invalid_move)

            loop.run_until_complete(coro(variant))


if __name__ == "__main__":
    unittest.main()
