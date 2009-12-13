from plex import *
from utils import run_scanner

def test12():
    lex = Lexicon(
        [
            (Str("'") + Rep(AnyBut("'")) + Str("'"), TEXT),
            (AnyChar, IGNORE)
        ],
        debug = None,
        timings = None,
    )

    run_scanner(lex, "test12", trace = False)
