import re
from hama.sequence import (cartesian_product, on_bits, split_after_indices)
from hama.dict import Dict, MGraph


def tag(text, zipped=False):
    """Produces POS tags for each morpheme in a text.

    Args:
        text (str): Text to separate into morphemes and tag.
        zipped (bool): If True, returns a list of tuples in the 
        form of (morpheme, tag).
        If False, returns a tuple with two lists: morphemes and 
        corresponding tags. Lengths of two lists are the same.
        Defaulted to False.

    Returns:
        list: list containing tuples in the form of:
        (morpheme, tag).
    """
    dic = Dict()
    dic.load()
    mgraph = MGraph()
    mgraph.load()

    morphemes = []
    tags = []
    words = re.findall(r"[\w']+|[.,!?;]", text)
    for word in words:
        w_morphemes, w_tags = tag_word(word)
        morphemes.extend(w_morphemes)
        tags.extend(w_tags)
    if zipped:
        return list(zip(morphemes, tags))
    return (morphemes, tags)


def tag_word(word):
    """Produces POS tags for each morpheme in a single word.

    Args:
        word (str): Word to separate into morphemes and tag.

    Returns:
        tuple: tuple containing two lists: 
        morphemes and corresponding tags.
        Lengths of two lists are the same.
    """
    best_score = 0
    best_ms = [word]  # Current best morpheme sequence.
    best_ts = ['u']  # Current best tag sequence.

    # All possible ways to split the word.
    num_candidates = (len(word) - 1)**2

    for i in range(num_candidates):
        score, ms, ts = best_morpheme_seq(word, i, best_score)
        if score > best_score:
            best_score = score
            best_ms = ms
            best_ts = ts

    assert (len(best_ms) == len(best_ts))
    return (best_ms, best_ts)


def best_morpheme_seq(word, n, curr_best_score):
    """Returns the most probable word partition and
    morpheme tags up until the nth partition of the word.

    Args:
        word (str): Whole word.
        n (int): Which partition scheme (out of 2**(len(word-1))
        possible candidate partitions the function is scoring.
        curr_best_score (float): Current best score.

    Returns:
        tuple: A tuple containing the following:
        (float: Current best score.
         list: Current best word partition.
         list: Current best morpheme tags.)
    """
    assert (n <= (len(word) - 1)**2)

    # Generate nth word partitions, and corresponding
    # candidate tag sequences.
    split_indices = on_bits(n)
    morpheme_seq = split_after_indices(word, split_indices)
    cts = candidate_tags(morpheme_seq)
    tag_seqs = cartesian_product(*cts)

    best_score = curr_best_score
    best_morpheme_seq = None
    best_tag_seq = None

    # Iterate through all tag sequences to obtain
    # highest-scoring tag sequence.
    for tag_seq in tag_seqs:
        score = score_tag_seq(tag_seq)
        if score > best_score:
            best_score = score
            best_morpheme_seq = morpheme_seq
            best_tag_seq = tag_seq

    return best_score, best_morpheme_seq, best_tag_seq


def score_tag_seq(ts):
    """Produces a likeliness score for an ordered tag sequence.

    Args:
        ts (list): Tag sequence to score.

    Returns:
        float: Tag sequence likeliness score.
    """
    ts_string = "".join(ts)
    no_unknowns = [e for e in ts if e != 'u']
    if MGraph().query(ts_string):
        score = 1 + len(no_unknowns) / len(ts)
    else:
        score = len(no_unknowns) / len(ts)
    return score


def candidate_tags(ms):
    """Produces a list of possible tags for each morpheme 
    in a word partition.

    Args:
        ms (list): Morphemem sequence. 
        List of strings, each representing a morpheme.
        Example input value: ['아버지', '가'],

    Returns:
        list: Returns a 2-D list of tags. 
        Length of input and output arrays is the same.
        Example return value: [[nnc], [nc, jc]]
    """
    tags = []
    for m in ms:
        m_tags = Dict().query(m)
        if len(m_tags) > 0:
            tags.append(m_tags)
        else:
            tags.append(['u'])
    assert (len(ms) == len(tags))
    return tags
