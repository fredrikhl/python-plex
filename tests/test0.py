from plex import *
from utils import run_scanner

def test0():
    lex = Lexicon(
        [
            (Str("a"), 'thing'),
            (Any("\n"), IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test0")
