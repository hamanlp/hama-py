from itertools import product


def insert(l, i, e):
    """Inserts element e into list l at index i.

    Args:
        l (list): List to insert into.
        i (int): Index to insert at.
        e (obj): Object to insert.

    Returns:
        list: Returns a new list containing the inserted element.
    """
    temp = l[:]
    temp[i:i] = [e]
    return temp


def cartesian_product(*lists):
    """Produces every possible pair of elements from input lists.

    Args:
        lists (list): Lists of variable length.

    Returns:
        list: List containing tuples of all possible combinations. 
    """
    pairs = list(product(*lists))
    return pairs


def on_bits(n):
    """Returns indices of activated bits in the 
    binary representation of integer n.
    
    Args: 
        n (int): Integer.

    Returns:
        list: List of indices where bit is 1 in 
        binary form of n.
    """
    activated = []
    index = 0
    while n:
        if n & 1:
            activated.append(index)
        n >>= 1
        index += 1
    return activated


def split_after_indices(s, indices):
    """Split string at indices
    
    Args: 
        s (str): String to segment.
        indices (list): Indices to segment at.
        indices must be sorted, and the biggest element of 
        indices must be smaller than len(s).

    Returns:
        list: String segmented at indices.
    """
    assert sorted(indices) == indices
    assert len(indices) == 0 or indices[-1] < len(s)
    start_indices = [-1] + indices
    end_indices = indices + [len(s)]
    return [s[i + 1 : j + 1] for i, j in zip(start_indices, end_indices)]
