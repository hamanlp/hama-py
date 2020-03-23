def adjacent_char_cmp(s1, s2):
    """
    Splits list into char pairs and see how many pairs overlap.
    s1 = [F,R,A,N,C,E] -> [FR, RA, AN, NC, CE]
    s2 = [F,R,E,N,C,H] -> [FR, RE, EN, NC, CH]
    similarity(s1, s2) 
        = 2 * intersection(s1 splits, s2 splits) / 
            (len(s1 splits) + len(s2 splits))
        = 0.4
    Adopted from 
    http://www.catalysoft.com/articles/StrikeAMatch.html

    Args:
        s1 (list): First sequence to compare.
        s2 (list): Pair-dissected (see _generate_pairs function)
        pre-defined morpheme graph.

    Returns:
        float: Similarity score between two sequences, between
        0 and 1.
    """
    s1_pairs = _generate_pairs(s1)
    s1_set = set(s1_pairs)
    s2_set = set(s2)
    intersection = s1_set.intersection(s2_set)
    score = 2 * len(intersection) / (len(s1_set) + len(s2_set))
    return score


def _generate_pairs(s):
    """
    Helper for adjacent_char_cmp.
    For example, [F,R,A,N,C,E] -> [FR, RA, AN, NC, CE]

    Args:
        s (list): Sequence to split.

    Returns:
        list: List split into pairs.
    """

    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s[0]]
    pairs = []
    for i in range(len(s)):
        if i >= len(s) - 1:
            break
        pairs.append(s[i] + s[i + 1])
    return pairs
