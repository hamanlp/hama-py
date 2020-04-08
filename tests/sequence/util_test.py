import pytest
from hama.tagging.sequence import (insert, cartesian_product, 
        on_bits, split_after_indices)


def test_insert():
    l1 = [1, 2, 3, 4, 5]
    l2 = insert(l1, 0, 0)
    assert (l2 == [0, 1, 2, 3, 4, 5])

    l3 = [1, 2, 3, 4, 5]
    l4 = insert(l3, len(l3) - 1, 6)
    assert (l4 == [1, 2, 3, 4, 6, 5])


def test_cartesian_product():
    l1 = ['a', 'b']
    l2 = ['c']
    l3 = ['d', 'e']
    l4 = [('a', 'c', 'd'), ('a', 'c', 'e'), ('b', 'c', 'd'), ('b', 'c', 'e')]
    assert (l4 == cartesian_product(l1, l2, l3))


def test_on_bits():
    a = 10
    assert (on_bits(a) == [1, 3])
    b = 2**30
    assert (on_bits(b) == [30])
    c = 0
    assert (on_bits(c) == [])


def test_split_after_indices():
    s = "가나다라마바사"
    i1 = []
    assert (split_after_indices(s, i1) == ['가나다라마바사'])
    i2 = [0]
    assert (split_after_indices(s, i2) == ['가', '나다라마바사'])
    i3 = [0, 2, 5]
    assert (split_after_indices(s, i3) == ['가', '나다', '라마바', '사'])
