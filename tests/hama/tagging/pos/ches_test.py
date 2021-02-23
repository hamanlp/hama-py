import pytest

from hama.tagging import ches, nb, nc, nn, nouns, np


def test_nouns():
    text = "복실복실 푸들"
    assert nouns(text) == ["푸들"]


def test_ches():
    text = ""
    assert nouns(text) == ches(text)
