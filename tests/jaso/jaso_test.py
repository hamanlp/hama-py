import pytest
from hama import assemble, disassemble

def test_assemble():
    assert assemble([]) == ''
    assert assemble(['ㄱ', 'ㅏ']) == '가'

def test_disassemble():
    pass


