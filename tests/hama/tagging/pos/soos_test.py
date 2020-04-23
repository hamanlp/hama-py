import pytest
from hama.tagging import modifiers, soos, mm, ma


def test_soos():
    text = ""
    assert (modifiers(text) == soos(text))
