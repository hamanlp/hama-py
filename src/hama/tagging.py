import re
from hama.sequence import (insert, cartesian_product, adjacent_char_cmp)
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

    candidate_ms = candidate_morpheme_seqs(word)
    best_ms = [word]  # Current best morpheme sequence.
    best_ts = ['u']  # Current best tag sequence.
    best_score = 0
    for cms in candidate_ms:
        ct = candidate_tags(cms)
        tag_seqs = cartesian_product(*ct)

        for ts in tag_seqs:
            s = score_tag_seq(ts)
            if s > best_score:
                best_ms = cms
                best_ts = ts
                best_score = s
    assert (len(best_ms) == len(best_ts))
    return (best_ms, best_ts)


def candidate_morpheme_seqs(word):
    """Produces every possible partition of word 
    into candidate morphemes.

    Args:
        word (string): String to partition into morphemes.

    Returns:
        list: Returns a 2-D array of strings.
        For example, 메롱is partitioned into [[메롱], [메,롱]].
    """

    cache = {}
    partitions = _candidate_morpheme_seqs(cache, word)

    return partitions


def _candidate_morpheme_seqs(cache, word):
    """Recursive helper for candidate_morpheme_seqs.
    Produces every possible partition of word 
    into candidate morphemes.

    Args:
        cache (dict): Dictionary for dynamic programming 
        memoization.
        word (string): String to partition into morphemes.

    Returns:
        list: Returns a 2-D array of strings.
        For example, 메롱is partitioned into [[메롱], [메,롱]].
    """
    if len(word) <= 0:
        return []
    elif len(word) <= 1:
        return [[word]]

    # Query dict for memoization.
    key = word
    if key in cache:
        return cache[key]
    else:
        head = word[0]
        tail = word[1:]
        tail_partitions = _candidate_morpheme_seqs(cache, word[1:])
        cache[key] = tail_partitions
        partitions = []
    for partition in tail_partitions:
        # Attach head to the first char in partition.
        partitions.append(insert(partition[1:], 0, head + partition[0]))
        # Attach head as the first partition.
        partitions.append(insert(partition, 0, head))
    return partitions


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
