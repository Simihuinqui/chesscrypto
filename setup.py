#! /usr/bin/env python3

from glob import glob
from os import listdir
from os.path import isdir, isfile
import os
import site
import sys
import subprocess

this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [os.path.join(this_dir, "lib")] + sys.path


msi = False
if "bdist_msi" in sys.argv[1:]:
    try:
        from cx_Freeze import setup, Executable

        msi = True
    except ImportError:
        print("ERROR: can't import cx_Freeze!")
        sys.exit(1)
else:
    from setuptools import setup

if sys.platform == "win32":
    try:
        import gi

        gi.require_version("Gtk", "3.0")
        from gi.repository import Gtk

        print(
            "Gtk version is %s.%s.%s"
            % (Gtk.MAJOR_VERSION, Gtk.MINOR_VERSION, Gtk.MICRO_VERSION),
        )
    except ImportError:
        print("ERROR: chesscrypto in Windows Platform requires to install PyGObject.")
        print("Installing from http://sourceforge.net/projects/pygobjectwin32")
        sys.exit(1)

import importlib.util
import importlib.machinery

spec = importlib.machinery.PathFinder().find_spec("chesscrypto", ["lib"])
chesscrypto = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chesscrypto)

VERSION = ChessCrypto.VERSION

NAME = "chesscrypto"

DESC = "Chess client"

LONG_DESC = ("Chesscrypto is a chess client for playing and analyzing chess games. It is\n"
             "intended to be usable both for those totally new to chess as well as\n"
             "advanced users who want to use a computer to further enhance their play.\n"
             "\n"
             "Chesscrypto has a builtin python chess engine and auto-detects most\n"
             "popular chess engines (Stockfish, Rybka, Houdini, Shredder, GNU Chess,\n"
             "Crafty, Fruit, and many more). These engines are available as opponents,\n"
             "and are used to provide hints and analysis. PyChess also shows analysis\n"
             "from opening books and Gaviota end-game tablebases.\n"
             "\n"
             "When you get sick of playing computer players you can login to FICS (the\n"
             "Free Internet Chess Server) and play against people all over the world.\n"
             "Chesscrypto has a built-in Timeseal client, so you won't lose clock time during\n"
             "a game due to lag. Chesscrypto also has pre-move support, which means you can\n"
             "make (or start making) a move before your opponent has made their move.\n"
             "\n"
             "Chesscrypto has many other features including:\n"
             "- CECP and UCI chess engine support with customizable engine configurations\n"
             "- Polyglot opening book support\n"
             "- Hint and Spy move arrows\n"
             "- Hint, Score, and Annotation panels\n"
             "- Play and analyze games in separate game tabs\n"
             "- 6 chess variants including Chess960, Three Check, and others\n"
             "- Reads and writes PGN, EPD and FEN chess file formats\n"
             "- Undo and pause chess games\n"
             "- Move animation in games\n"
             "- Drag and drop chess files\n"
             "- Optional game move and event sounds\n"
             "- Chess piece themes with 40 built-in piece themes\n"
             "- Legal move highlighting\n"
             "- Direct copy+paste pgn game input via Enter Game Notation open-game dialog\n"
             "- Internationalised text and Figurine Algebraic Notation (FAN) support\n"
             "- Translated into 38 languages (languages with +5% strings translated)\n"
             "- Easy to use and intuitive look and feel")

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: X11 Applications :: GTK",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Games/Entertainment :: Board Games",
]

os.chdir(os.path.abspath(os.path.dirname(__file__)))

# save
stderr = sys.stderr
stdout = sys.stdout

if not isfile("eco.db"):
    print(
        "ERROR: File 'eco.db' is missing, please generate using command:\n"
        "       # PYTHONPATH=lib python3 pgn2ecodb.py",
        file=sys.stderr,
    )
    sys.exit(1)

if not isfile(os.path.abspath("pieces/Spatial.png")):
    print(
        "ERROR: Preview images of pieces themes are missing, please generate using command:\n"
        "       # PYTHONPATH=lib python3 create_theme_preview.py",
        file=sys.stderr,
    )
    sys.exit(1)

# restore
sys.stderr = stderr
sys.stdout = stdout

DATA_FILES = [
    (
        "share/chesscrypto",
        [
            "README.md",
            "AUTHORS",
            "ARTISTS",
            "DOCUMENTERS",
            "LICENSE",
            "TRANSLATORS",
            "chesscrypto_book.bin",
            "eco.db",
        ],
    )
]

# UI
DATA_FILES += [("share/chesscrypto/glade", glob("glade/*.glade"))]
DATA_FILES += [("share/chesscrypto/glade", ["glade/background.jpg"])]
DATA_FILES += [("share/chesscrypto/glade", glob("glade/*.png"))]
DATA_FILES += [("share/chesscrypto/glade/16x16", glob("glade/16x16/*.png"))]
DATA_FILES += [("share/chesscrypto/glade/48x48", glob("glade/48x48/*.png"))]
DATA_FILES += [("share/chesscrypto/glade", glob("glade/*.svg"))]
DATA_FILES += [("share/chesscrypto/flags", glob("flags/*.png"))]
DATA_FILES += [("share/chesscrypto/boards", glob("boards/*.png"))]

# Data
DATA_FILES += [("share/mime/packages", ["chesscrypto.xml"])]
DATA_FILES += [("share/metainfo", ["chesscrypto.metainfo.xml"])]
DATA_FILES += [("share/applications", ["chesscrypto.desktop"])]
DATA_FILES += [("share/icons/hicolor/scalable/apps", ["chesscrypto.svg"])]
if sys.platform == "win32":
    DATA_FILES += [("share/chesscrypto/sounds", glob("sounds/*.wav"))]
    DATA_FILES += [("share/chesscrypto/engines", glob("engines/*.*"))]
else:
    DATA_FILES += [("share/chesscrypto/sounds", glob("sounds/*.ogg"))]
DATA_FILES += [("share/icons/hicolor/24x24/apps", ["chesscrypto.png"])]
DATA_FILES += [
    (
        "share/gtksourceview-3.0/language-specs",
        ["gtksourceview-3.0/language-specs/pgn.lang"],
    )
]

# Piece sets
DATA_FILES += [("share/chesscrypto/pieces", glob("pieces/*.png"))]

if not isfile(os.path.abspath("learn/puzzles/mate_in_4.sqlite")):
    from chesscrypto.Savers.pgn import PGNFile
    from chesscrypto.System.protoopen import protoopen

    # Lectures, puzzles, lessons
    for filename in glob("learn/puzzles/*.pgn"):
        chessfile = PGNFile(protoopen(filename))
        chessfile.init_tag_database()

    for filename in glob("learn/lessons/*.pgn"):
        chessfile = PGNFile(protoopen(filename))
        chessfile.init_tag_database()

DATA_FILES += [("share/chesscrypto/learn/puzzles", glob("learn/puzzles/*.olv"))]
DATA_FILES += [("share/chesscrypto/learn/puzzles", glob("learn/puzzles/*.pgn"))]
DATA_FILES += [("share/chesscrypto/learn/puzzles", glob("learn/puzzles/*.sqlite"))]
DATA_FILES += [("share/chesscrypto/learn/lessons", glob("learn/lessons/*.pgn"))]
DATA_FILES += [("share/chesscrypto/learn/lessons", glob("learn/lessons/*.sqlite"))]
DATA_FILES += [("share/chesscrypto/learn/lectures", glob("learn/lectures/*.txt"))]

for dir in [d for d in listdir("pieces") if isdir(os.path.join("pieces", d))]:
    DATA_FILES += [("share/chesscrypto/pieces/" + dir, glob("pieces/" + dir + "/*.svg"))]

# Manpages
DATA_FILES += [("share/man/man1", ["manpages/chesscrypto.1.gz"])]

# Language
pofile = "LC_MESSAGES/chesscrypto"
if sys.platform == "win32":
    argv0_path = os.path.dirname(os.path.abspath(sys.executable))
    if chesscrypto.MSYS2:
        major, minor, micro, releaselevel, serial = sys.version_info
        msgfmt_path = argv0_path + "/../lib/python{}.{}/tools/i18n/".format(
            major, minor
        )
    else:
        msgfmt_path = argv0_path + "/tools/i18n/"
    msgfmt = f"{os.path.abspath(sys.executable)} {msgfmt_path}msgfmt.py"
else:
    msgfmt = "msgfmt"

pychess_langs = []
for dir in [d for d in listdir("lang") if isdir("lang/" + d) and d != "en"]:
    if sys.platform == "win32":
        command = f"{msgfmt} lang/{dir}/{pofile}.po"
    else:
        command = "{} lang/{}/{}.po -o lang/{}/{}.mo".format(
            msgfmt, dir, pofile, dir, pofile
        )
    subprocess.call(command.split())
    DATA_FILES += [
        ("share/locale/" + dir + "/LC_MESSAGES", ["lang/" + dir + "/" + pofile + ".mo"])
    ]
    pychess_langs.append(dir)

PACKAGES = []

if msi:
    if chesscrypto.MSYS2:
        gtk_data_path = sys.prefix
        gtk_exec_path = os.path.join(sys.prefix, "bin")
        lang_path = os.path.join(sys.prefix, "share", "locale")
    else:
        # Get the site-package folder, not everybody will install
        # Python into C:\PythonXX
        site_dir = site.getsitepackages()[1]
        gtk_data_path = os.path.join(site_dir, "gnome")
        gtk_exec_path = os.path.join(site_dir, "gnome")
        lang_path = os.path.join(site_dir, "gnome", "share", "locale")

    # gtk3.0 .mo files
    gtk_mo = [
        f + "/LC_MESSAGES/gtk30.mo" for f in os.listdir(lang_path) if f in chesscrypto_langs
    ]

    # Collect the list of missing dll when cx_freeze builds the app
    gtk_exec = [
        "libgtksourceview-3.0-1.dll",
        "libjpeg-8.dll",
        "librsvg-2-2.dll",
        "libwinpthread-1.dll",
    ]

    # We need to add all the libraries too (for themes, etc..)
    gtk_data = [
        "etc",
        "lib/gdk-pixbuf-2.0",
        "lib/girepository-1.0",
        "share/icons/Adwaita/icon-theme.cache",
        "share/icons/Adwaita/index.theme",
        "share/icons/Adwaita/16x16",
        "share/icons/Adwaita/scalable",
        "share/glib-2.0",
    ]

    # Create the list of includes as cx_freeze likes
    include_files = []
    for mo in gtk_mo:
        mofile = os.path.join(lang_path, mo)
        if os.path.isfile(mofile):
            include_files.append((mofile, "share/locale/" + mo))

    for dll in gtk_exec:
        include_files.append((os.path.join(gtk_exec_path, dll), dll))

    # Let's add gtk data
    for lib in gtk_data:
        include_files.append((os.path.join(gtk_data_path, lib), lib))

    base = None
    # Lets not open the console while running the app
    if sys.platform == "win32":
        base = "Win32GUI"

    executables = [
        Executable(
            "chesscrypto",
            base=base,
            icon="chesscrypto.ico",
            shortcut_name="ChessCrypto",
            shortcut_dir="DesktopFolder",
        ),
        Executable(
            script="lib/__main__.py", target_name="chesscrypto-engine.exe", base=base
        ),
    ]

    bdist_msi_options = {
        "upgrade_code": "{5167584f-c196-428f-be40-4c861025e90a}",
        "add_to_path": False,
    }

    perspectives = ["chesscrypto.perspectives"]
    for persp in ("welcome", "games", "fics", "database", "learn"):
        perspectives.append("chesscrypto.perspectives.%s" % persp)

    build_exe_options = {
        "path": sys.path + ["lib"],
        "includes": ["gi"],
        "packages": [
            "asyncio",
            "gi",
            "sqlalchemy.dialects.sqlite",
            "sqlalchemy.sql.default_comparator",
            "pexpect",
            "chesscrypto",
        ]
        + perspectives,
        "include_files": include_files,
    }
    if chesscrypto.MSYS2:
        build_exe_options["excludes"] = ["tkinter"]
    else:
        build_exe_options["include_msvcr"] = True

    kwargs = dict(
        options={"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
        executables=executables,
    )

else:
    PACKAGES = [
        "chesscrypto",
        "chesscrypto.gfx",
        "chesscrypto.ic",
        "chesscrypto.ic.managers",
        "chesscrypto.Players",
        "chesscrypto.Savers",
        "chesscrypto.System",
        "chesscrypto.Utils",
        "chesscrypto.Utils.lutils",
        "chesscrypto.Variants",
        "chesscrypto.Database",
        "chesscrypto.widgets",
        "chesscrypto.widgets.pydock",
        "chesscrypto.perspectives",
        "chesscrypto.perspectives.welcome",
        "chesscrypto.perspectives.games",
        "chesscrypto.perspectives.fics",
        "chesscrypto.perspectives.database",
        "chesscrypto.perspectives.learn",
        "chesscrypto.external",
    ]

    kwargs = {}

setup(
    name=NAME,
    version=VERSION,
    author="Chesscrypto team",
    author_email="rolon.a.m@gmail.com",
    maintainer="Inti Simihuinqui",
    classifiers=CLASSIFIERS,
    keywords="crypto gtk chess xboard gnuchess game pgn epd board linux",
    description=DESC,
    long_description=LONG_DESC,
    license="GPL3",
    url="https://chesscrypto.github.io/",
    download_url="https://github.com/chesscrypto/chesscrypto/releases",
    python_requires=">=3.9",
    install_requires=[
        "pexpect",
        "psutil",
        "pycairo",
        "PyGObject",
        "SQLAlchemy>=2",
        "websockets",
    ],
    extras_require={
        "gbulb": [
            "gbulb",
        ],
    },
    package_dir={"": "lib"},
    packages=PACKAGES,
    data_files=DATA_FILES,
    scripts=["chesscrypto"],
    **kwargs,
)
