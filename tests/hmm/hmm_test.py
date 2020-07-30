import pytest
from hama.tagging.hmm import TagHMM


def test_query():
    hmm = TagHMM()

    hmm.unload()
    with pytest.raises(Exception):
        hmm.query("s", "s")

    hmm.load()
    with pytest.raises(Exception):
        hmm.query("gibberish", "tag")
    hmm.query("s", "s")


def test_wrong_attr():
    hmm = TagHMM()
    assert hmm.foofoo == None


def test_unload():
    hmm = TagHMM()
    hmm.unload()
    assert hmm.hmm == None
    assert hmm.t2i == None
