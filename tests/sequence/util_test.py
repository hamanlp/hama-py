import pytest
from hama.sequence import insert, cartesian_product


def test_insert():
    l1 = [1, 2, 3, 4, 5]
    l2 = insert(l1, 0, 0)
    assert (l2 == [0, 1, 2, 3, 4, 5])


def test_cartesian_product():
    l1 = ['a', 'b']
    l2 = ['c']
    l3 = ['d', 'e']
    l4 = [('a', 'c', 'd'), ('a', 'c', 'e'), ('b', 'c', 'd'), ('b', 'c', 'e')]
    assert (l4 == cartesian_product(l1, l2, l3))
