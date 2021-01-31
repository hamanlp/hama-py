import pytest

from hama.tagging.dict import Dict


def test_query():
    dict = Dict()

    dict.unload()
    with pytest.raises(Exception):
        dict.query("")

    dict.load()
    assert dict.query("") == []
    assert set(dict.query("아버지")) == set(["nc"])
    assert set(dict.query("가")) == set(["ep", "xp", "nc", "jc", "ec"])


def test_wrong_attr():
    dict = Dict()
    assert dict.booboo == None


def test_unload():
    dict = Dict()
    dict.unload()
    assert dict.dict == None
