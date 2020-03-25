import pytest
from hama.dict import MGraph


def test_query():
    graph = MGraph()
    graph.load()
    assert (graph.query('') == False)
    assert (graph.query('nbjc') == True)
    assert (graph.query('xxx') == False)
