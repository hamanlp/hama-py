import pytest
import hama


def test_ches():
    text = ""
    assert (hama.nouns(text) == hama.ches(text))


def test_yongs():
    text = ""
    assert (hama.predicates(text) == hama.yongs(text))


def test_soos():
    text = ""
    assert (hama.modifiers(text) == hama.soos(text))


def test_doks():
    text = ""
    assert (hama.orthotones(text) == hama.doks(text))
