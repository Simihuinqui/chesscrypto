#!/bin/sh

cd lib

zip ../chesscrypto-engine.pyz __main__.py chesscrypto/__init__.py chesscrypto/Players/__init__.py chesscrypto/Players/ChessCrypto.py chesscrypto/Players/ChessCryptoCECP.py chesscrypto/Utils/lutils/*.py chesscrypto/Utils/*.py chesscrypto/System/__init__.py chesscrypto/System/conf.py chesscrypto/System/prefix.py chesscrypto/System/Log.py chesscrypto/Variants/*.py

cd ..
echo '#!/usr/bin/env python3' | cat - chesscrypto-engine.pyz > chesscrypto-engine
chmod +x chesscrypto-engine
