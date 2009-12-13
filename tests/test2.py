from plex import *
from utils import run_scanner

def test0():
    lex = Lexicon(
        [
            (Seq(Any("ab"), Rep(Any("ab01"))), 'ident'),
            (Seq(Any("01"), Rep(Any("01"))), 'num'),
            (Any(' \n'), IGNORE),
            (Str("abba"), 'abba'),
            (Any('([{!"#') + Rep(AnyBut('!"#}])')) + Any('!"#}])'), IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test2")
