import pytest
from hama.dict import Dict, MGraph
from hama.hmm import TagHMM


def pytest_runtest_setup(item):
    Dict().load()
    MGraph().load()
    TagHMM().load()
