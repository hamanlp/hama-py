from hama.sequence import (insert, cartesian_product, 
        adjacent_char_cmp)
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
    words = text.split()
    for word in words:
        w_morphemes, w_tags = tag_word(word)
        morphemes.extend(w_morphemes)
        tags.extend(w_tags)
    if zipped:
        return list(zip(morphemes,tags))
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
    assert(len(best_ms) == len(best_ts))
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

    partitions = []
    if len(word) <= 0:
        return []
    elif len(word) <= 1:
        return [[word]]
    head = word[0]
    tail_partitions = candidate_morpheme_seqs(word[1:])
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
    max_score = 0
    for g in MGraph().graph:
        s = adjacent_char_cmp(ts, g)
        if s > max_score:
            max_score = s
    return max_score / len(ts)


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
        m_tags = query_dict(m)
        if len(m_tags) > 0:
            tags.append(m_tags)
        else:
            tags.append(['u'])
    assert (len(ms) == len(tags))
    return tags


def query_dict(morpheme):
    """Queries embedded dictionary for morpheme.

    Args:
        morpheme (str): Morpheme to search for.

    Returns:
        list: List containing all found tags in the 
        embedded dictionary. Empty if not found.
    """
    return Dict().query(morpheme)

