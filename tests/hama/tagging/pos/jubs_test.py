import pytest

from hama.tagging import affixes, jubs, xp, xs


def test_jubs():
    text = ""
    assert affixes(text) == jubs(text)
