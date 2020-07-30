import pytest
from hama.tagging import predicates, yongs, pv, pa


def test_yongs():
    text = ""
    assert predicates(text) == yongs(text)
