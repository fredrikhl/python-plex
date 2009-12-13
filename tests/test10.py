# Test traditional regular expression syntax.

from plex.traditional import re, RegexpSyntaxError
from plex import Seq, AnyBut

from nose.tools import assert_raises

def test10():
    assert str(re("")) == "Seq()"
    assert str(re("a")) == "Seq(Char('a'))"
    assert str(re("[a]")) == "Seq(Any('a'))"
    assert str(re("[ab]")) == "Seq(Any('ab'))"
    assert str(re("[abc]")) == "Seq(Any('abc'))"
    assert str(re("[a-c]")) == "Seq(Any('abc'))"
    assert str(re("[a-cd]")) == "Seq(Any('abcd'))"
    assert str(re("[a-cg-i]")) == "Seq(Any('abcghi'))"
    assert str(re("[^a]")) == "Seq(AnyBut('a'))"
    assert str(re("[^a-cg-i]")) == "Seq(AnyBut('abcghi'))"
    assert str(re("[-]")) == "Seq(Any('-'))"
    assert str(re("[-abc]")) == "Seq(Any('-abc'))"
    assert str(re("[abc-]")) == "Seq(Any('abc-'))"
    assert str(re("[]]")) == "Seq(Any(']'))"
    assert str(re("[]-]")) == "Seq(Any(']-'))"
    assert str(re("[^-]")) == "Seq(AnyBut('-'))"
    assert str(re("[^-abc]")) == "Seq(AnyBut('-abc'))"
    assert str(re("[^abc-]")) == "Seq(AnyBut('abc-'))"
    assert str(re("[^]]")) == "Seq(AnyBut(']'))"
    assert str(re("[^]-]")) == "Seq(AnyBut(']-'))"
    assert str(re("a*")) == "Seq(Rep(Char('a')))"
    assert str(re("a+")) == "Seq(Rep1(Char('a')))"
    assert str(re("a?")) == "Seq(Opt(Char('a')))"
    assert str(re("a*+?")) == "Seq(Opt(Rep1(Rep(Char('a')))))"
    assert str(re("ab")) == "Seq(Char('a'),Char('b'))"
    assert str(re("a|b")) == "Alt(Seq(Char('a')),Seq(Char('b')))"
    assert str(re("abcde")) == "Seq(Char('a'),Char('b'),Char('c'),Char('d'),Char('e'))"
    assert str(re("a|b|c|d|e")) == "Alt(Seq(Char('a')),Seq(Char('b')),Seq(Char('c')),Seq(Char('d')),Seq(Char('e')))"
    assert str(re("abc|def|ghi")) == "Alt(Seq(Char('a'),Char('b'),Char('c')),Seq(Char('d'),Char('e'),Char('f')),Seq(Char('g'),Char('h'),Char('i')))"
    assert str(re("abc(def|ghi)")) == "Seq(Char('a'),Char('b'),Char('c'),Alt(Seq(Char('d'),Char('e'),Char('f')),Seq(Char('g'),Char('h'),Char('i'))))"
    assert str(re("ab\(c\[de")) == "Seq(Char('a'),Char('b'),Char('('),Char('c'),Char('['),Char('d'),Char('e'))"
    assert str(re("^abc$")) == "Seq(Bol,Char('a'),Char('b'),Char('c'),Eol)"
    assert_raises(RegexpSyntaxError, re, "abc(de")
    assert_raises(RegexpSyntaxError, re, "abc[de")
    assert_raises(RegexpSyntaxError, re, "abc)de")
