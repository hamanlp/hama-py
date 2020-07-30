import pytest
from hama.tagging import nouns, ches, nc, nb, np, nn


def test_nouns():
    text = "복실복실 푸들"
    assert nouns(text) == ["푸들"]


def test_ches():
    text = ""
    assert nouns(text) == ches(text)
