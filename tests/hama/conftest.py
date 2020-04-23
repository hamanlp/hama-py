import pytest
import hama


def pytest_runtest_setup(item):
    hama.init()
