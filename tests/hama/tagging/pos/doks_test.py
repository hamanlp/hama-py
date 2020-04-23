import pytest
from hama.tagging import orthotones, doks, ii


def test_doks():
    text = ""
    assert (orthotones(text) == doks(text))
