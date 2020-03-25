import pytest
from hama.dict import MGraph


def test_query():
    graph = MGraph()

    with pytest.raises(Exception):
        graph.query('')

    graph.load()
    assert (graph.query('') == False)
    assert (graph.query('nbjc') == True)
    assert (graph.query('xxx') == False)

def test_wrong_attr():
    graph = MGraph()
    assert(graph.booboo == None)

def test_unload():
    graph = MGraph()
    graph.unload()
    assert(graph.dict == None)
