import pytest
import hama
from hama.tagging import (candidate_tags, score_tag_seq,
                          candidate_morpheme_seqs, tag_word)

def test_candidate_tags():
    assert (candidate_tags([]) == [])
    seq = ['아버지', '가']
    ct1 = candidate_tags(seq)
    assert(set(ct1[0]) == set(['nc']))
    assert(set(ct1[1]) == set(['ep', 'xp', 'nc', 'jc', 'ec']))


def test_score_tag_seq():
    pass


def test_candidate_morpheme_seqs():
    assert (candidate_morpheme_seqs('') == [])
    word = '아버지가'
    assert (candidate_morpheme_seqs(word) == [['아버지가'], ['아', '버지가'],
                                              ['아버', '지가'], ['아', '버', '지가'],
                                              ['아버지', '가'], ['아', '버지', '가'],
                                              ['아버', '지', '가'],
                                              ['아', '버', '지', '가']])


def test_tag_word():
    word = '아버지가'
    #tags = tag_word(word)
    #print(tags)


def test_tag():
    text = '돼지가 아니라 하마입니다.'
    tags = hama.tag(text)
    print(tags)

    text = '밥주세요.'
    #tags = hama.tag(text, zipped=True)
    #print(tags)

