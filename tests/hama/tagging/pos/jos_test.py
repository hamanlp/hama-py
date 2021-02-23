import pytest

from hama.tagging import jc, jos, jx, postpositions


def test_jos():
    text = ""
    assert postpositions(text) == jos(text)
