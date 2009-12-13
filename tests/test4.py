from plex import *
from utils import run_scanner

def test0():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"

    wax = Any("(")
    wane = Any(")")
    letter = Any(letters)
    space = Any(" \t\n")

    def open_paren(s, t):
        s.counter = s.counter + 1

    def close_paren(s, t):
        s.counter = s.counter - 1

    def got_a_letter(s, t):
        if s.counter == 0:
            return 'letter'
        else:
            return None

    lex = Lexicon(
        [
            (wax, open_paren),
            (wane, close_paren),
            (letter, got_a_letter),
            (space, IGNORE)
        ],
        debug = None,
        timings = None
    )

    class MyScanner(Scanner):
        counter = 0
        trace = 0

    run_scanner(lex, "test4", scanner_class = MyScanner)
