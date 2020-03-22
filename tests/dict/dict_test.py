import pytest
from hama.dict import Dict

def test_query():
    dict = Dict()
    dict.load()
    assert (dict.query('') == [])
    assert (dict.query('아버지') == ['nc'])
    assert (dict.query('가') == ['ep', 'xp', 'nc', 'jc', 'ec'])
