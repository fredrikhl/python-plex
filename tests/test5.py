from plex import *
from utils import run_scanner

def test0():
    letters = "abc"
    spaces = " \t\n"
    all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*/{} \t\n"

    letter = Any(letters)
    space = Any(" \t\n")

    ident = Rep1(letter)
    spaces = Rep1(space)
    begin_comment = Str("{")
    end_comment = Str("}")

    lex = Lexicon(
        [
            (ident, 'ident'),
            (spaces, IGNORE),
            (begin_comment, Begin('comment')),
            State('comment', [
                (end_comment, Begin('')),
                (AnyBut("}"), IGNORE),
            ])
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test5")
