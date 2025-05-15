import logging
import sys

from chesscrypto.System.Log import log
from chesscrypto.Players.ChessCryptoCECP import ChessCryptoCECP


if len(sys.argv) == 1 or sys.argv[1:] == ["debug"]:
    if "debug" in sys.argv[1:]:
        log.logger.setLevel(logging.DEBUG)
    else:
        log.logger.setLevel(logging.WARNING)

    chesscrypto = ChessCryptoCECP()
else:
    print("Unknown argument(s):", repr(sys.argv))
    sys.exit(0)

chesscrypto.makeReady()
chesscrypto.run()
