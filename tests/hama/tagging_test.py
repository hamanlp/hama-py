import pytest
from hama.tagging import tag
from hama.tagging.tagging import (candidate_tags, score_tag_seq, best_morpheme_seq,
        tag_word)


def test_candidate_tags():
    assert (candidate_tags([]) == [])
    seq = ['아버지', '가']
    ct1 = candidate_tags(seq)
    assert (set(ct1[0]) == set(['nc']))
    assert (set(ct1[1]) == set(['ep', 'xp', 'nc', 'jc', 'ec']))


def test_score_tag_seq():
    pass


def test_best_morpheme_seq():
    with pytest.raises(Exception):
        best_morpheme_seq('', 1, 0, 'BEGIN', False)

    word = '아버지가'
    bms1 = best_morpheme_seq(word, 0, 0, 'BEGIN', True)
    assert (bms1[1] == None)
    assert (bms1[2] == None)

    bms2 = best_morpheme_seq(word, 4, 0, 'BEGIN', True)
    assert (bms2[1] == ['아버지', '가'])
    assert (bms2[2] == ('nc', 'jc'))

    bms3 = best_morpheme_seq(word, 4, 0, 'BEGIN', False)
    assert (bms3[1] == ['아버지', '가'])
    assert (bms3[2] == ('nc', 'jc'))


def test_tag_word():
    word = '아버지가'
    tags = tag_word(word, 'BEGIN', True)
    assert (tags[1] == ('nc', 'jc'))


def test_tag():
    text = '돼지가 아니라 하마입니다.'
    tags = tag(text)
    #print(tags)

    text = '밥주세요.'
    tags = tag(text, zipped=True)
    #print(tags)

    text = '프론트엔드 에서도 돌아갑니다'
    tags = tag(text)
    #print(tags)
