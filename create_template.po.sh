#!/bin/sh

xgettext --package-name=chesscrypto -L Glade -o lang/chesscrypto.pot glade/*.glade
xgettext --package-name=chesscrypto -L Python -j -o lang/chesscrypto.pot lib/chesscrypto/Main.py lib/chesscrypto/*/*.py lib/chesscrypto/*/*/*.py

sed -i '/#, fuzzy/d' lang/chesscrypto.pot

line=""Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n""
sed -i "/${line}/ s/^/# /" lang/chesscrypto.pot
