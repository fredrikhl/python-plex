from plex import *
from utils import run_scanner

def test0():
    letter = Range("AZaz") | Any("_")
    digit = Range("09")
    space = Any(" \t\n")

    ident = letter + Rep(letter | digit)
    resword = Str("program", "unit", "uses", "const", "type", "var",
                  "if", "then", "else", "while", "do", "repeat", "until",
                  "for", "to", "downto", "and", "or", "not",
                  "array", "of", "record", "object")
    number = Rep1(digit)
    string = Str("'") + (Rep(AnyBut("'")) | Str("''")) + Str("'")
    diphthong = Str(":=", "<=", ">=", "<>", "..")
    punct = Any("^&*()-+=[]|;:<>,./")
    spaces = Rep1(space)
    comment_begin = Str("{")
    comment_char = AnyBut("}")
    comment_end = Str("}")

    lex = Lexicon(
        [
            (resword, TEXT),
            (ident, 'ident'),
            (number, 'num'),
            (string, 'str'),
            (punct | diphthong, TEXT),
            (spaces, IGNORE),
            (comment_begin, Begin('comment')),
            State('comment', [
                (comment_char, IGNORE),
                (comment_end, Begin(''))
            ])
        ],
        debug = None,
        timings = None
    )
    run_scanner(lex, "test6")
