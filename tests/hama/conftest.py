import pytest
from hama.tagging.dict import Dict
from hama.tagging.hmm import TagHMM


def pytest_runtest_setup(item):
    Dict().load()
    TagHMM().load()
