from plex import *
from utils import run_scanner

def test0():
    letter = Range("AZaz") | Any("_")
    digit = Range("09")
    space = Any(" \t\n")

    ident = Seq(letter, Rep(Alt(letter, digit)))
    number = Seq(digit, Rep(digit))
    punct = Any("*()-+=[]{};:<>,./")
    spaces = Seq(space, Rep(space))
    resword = Str("program", "begin", "end", "repeat", "until")

    lex = Lexicon(
        [
            (resword, TEXT),
            (ident, 'ident'),
            (number, 'num'),
            (punct, TEXT),
            (spaces, IGNORE)
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test3")
