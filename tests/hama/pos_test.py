import pytest
from hama.tagging import nouns


def test_nouns():
    text = "복실복실 푸들"
    assert (nouns(text) == ['푸들'])
