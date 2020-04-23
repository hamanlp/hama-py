import pytest
from hama.tagging import suffixes, eoms, ep, ec, et, ef


def test_eoms():
    text = ""
    assert (suffixes(text) == eoms(text))
