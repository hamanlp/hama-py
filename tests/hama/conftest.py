import pytest
from hama.dict import Dict, MGraph


def pytest_runtest_setup(item):
    Dict().load()
    MGraph().load()
