import pytest
import hama


def test_nouns():
    text = "버스 타고 가자."
    print(hama.tag(text))
    assert(hama.nouns(text) == ['버스'])


