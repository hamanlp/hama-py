import pytest
from hama.hmm import TagHMM

def test_wrong_attr():
    hmm = TagHMM()
    asset(hmm.foofoo == None)

def test_unload():
    hmm = TagHMM()
    hmm.unload()
    assert(hmm.hmm == None)

