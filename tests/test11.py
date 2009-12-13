from plex import *
from utils import run_scanner

def test11():
    lex = Lexicon(
        [
            (Str("Python"), 'upper-python'),
            (Str("python"), 'lower-python'),
            (NoCase(Str("COBOL", "perl", "Serbo-Croatian")), 'other-language'),
            (NoCase(Str("real") + Case(Str("basic"))), 'real-1'),
            (NoCase(Str("real") + Case(Str("Basic"))), 'real-2'),
            (Any(" \t\n"), IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test11")
