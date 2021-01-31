import pytest

from hama.tagging import ma, mm, modifiers, soos


def test_soos():
    text = ""
    assert modifiers(text) == soos(text)
