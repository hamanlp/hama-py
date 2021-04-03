import pytest

from hama.string_search import AhoCorasickAutomaton


def test_ac_init():
    ac = AhoCorasickAutomaton()


def test_add_word():
    ac = AhoCorasickAutomaton()
    ac.add_word("hello")


def test_add_words():
    ac = AhoCorasickAutomaton()
    ac.add_words(["hello", "yellow"])


def test_simple_search():
    ac = AhoCorasickAutomaton()
    ac.add_words(["hello", "yellow"])
    assert list(ac.search("")) == []
    assert list(ac.search("hillo")) == []
    assert list(ac.search("hihello")) == [("hello", 2, 6)]


# From: https://www.youtube.com/watch?v=OFKxWFew_L0
def test_substring_search():
    ac = AhoCorasickAutomaton()
    ac.add_words(["A", "AG", "C", "CAA", "GAG", "GC", "GCA"])
    assert list(ac.search("")) == []
    assert list(ac.search("GCAA")) == [
        ("C", 1, 1),
        ("GC", 0, 1),
        ("GCA", 0, 2),
        ("A", 2, 2),
        ("A", 3, 3),
    ]


# From: https://www.youtube.com/watch?v=OFKxWFew_L0
def test_substring_search_1():
    ac = AhoCorasickAutomaton()
    ac.add_words(["A", "AG", "C", "CA", "CAA", "GAG", "GC", "GCA"])
    # print(list(ac.search("GCAA")))
