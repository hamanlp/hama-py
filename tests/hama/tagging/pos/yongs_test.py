import pytest

from hama.tagging import pa, predicates, pv, yongs


def test_yongs():
    text = ""
    assert predicates(text) == yongs(text)
