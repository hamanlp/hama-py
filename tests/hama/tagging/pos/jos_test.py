import pytest
from hama.tagging import postpositions, jos, jc, jx


def test_jos():
    text = ""
    assert (postpositions(text) == jos(text))
