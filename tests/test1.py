from plex import *
from utils import run_scanner

def test0():
    lex = Lexicon(
        [
            (Any("ab") + Rep(Any("ab01")), 'ident'),
            (Any(" \n"), IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test1")
