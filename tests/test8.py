from plex import *
from utils import run_scanner

def test0():
    spaces = Rep1(Any(" \t\n"))

    lex = Lexicon(
        [
            (Str("ftangftang"), 'two_ftangs'),
            (Str("ftang"),      'one_ftang'),
            (Str("fta"),        'one_fta'),
            (spaces, IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test8")
