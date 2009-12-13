from plex import *
from utils import run_scanner

def test0():
    spaces = Rep1(Any(" \t\n"))

    lex = Lexicon(
        [
            (Bol + Rep1(Str("a")),       'begin'),
            (      Rep1(Str("b")),       'middle'),
            (      Rep1(Str("c")) + Eol, 'end'),
            (Bol + Rep1(Str("d")) + Eol, 'everything'),
            (spaces, IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test7")
