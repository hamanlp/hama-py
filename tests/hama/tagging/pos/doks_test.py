import pytest

from hama.tagging import doks, ii, orthotones


def test_doks():
    text = ""
    assert orthotones(text) == doks(text)
