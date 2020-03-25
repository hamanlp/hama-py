import pytest
import hama.sequence
from hama.sequence.similarity.adjacent_char import _generate_pairs


def test_generate_pairs():
    s1 = ['F', 'R', 'A', 'N', 'C', 'E']
    assert (_generate_pairs(s1) == ['FR', 'RA', 'AN', 'NC', 'CE'])
    s2 = []
    assert (_generate_pairs(s2) == [])
    s3 = ['P']
    assert (_generate_pairs(s3) == ['P'])


def test_adjacent_char_cmp():
    s1 = ['F', 'R', 'A', 'N', 'C', 'E']
    s2 = ['FR', 'RE', 'EN', 'NC', 'CH']
    assert (hama.sequence.adjacent_char_cmp(s1, s2) == 0.4)
