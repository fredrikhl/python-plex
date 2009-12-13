import os
from plex import Scanner

here = os.path.abspath(os.path.dirname(__file__))

def run_scanner(lexicon, test_name, scanner_class = Scanner, trace = False):
    in_name = os.path.join(here, test_name + ".in")
    out_name = os.path.join(here, test_name + ".out")
    in_file = open(in_name, "rU")
    if lexicon is None:
        s = scanner_class(in_file, os.path.basename(in_name))
    else:
        s = scanner_class(lexicon, in_file, os.path.basename(in_name))

    s.trace = trace
    output = ''
    while 1:
        value, text = s.read()
        name, line, pos = s.position()
        line = "%s %3d %3d %-10s %s" % (name, line, pos, value, repr(text))
        print(line)
        output += line + "\n"
        if value is None:
            break

    in_file.close()
    out_file = open(out_name, "r")
    assert output == out_file.read()
    out_file.close()

