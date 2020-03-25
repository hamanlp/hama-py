import pytest
from hama.dict import Dict

def test_query():
    dict = Dict()
    dict.load()
    assert (dict.query('') == [])
    assert (set(dict.query('아버지')) == set(['nc']))
    assert (set(dict.query('가')) == 
            set(['ep', 'xp', 'nc', 'jc', 'ec']))
