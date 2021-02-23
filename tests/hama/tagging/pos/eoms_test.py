import pytest

from hama.tagging import ec, ef, eoms, ep, et, suffixes


def test_eoms():
    text = ""
    assert suffixes(text) == eoms(text)
