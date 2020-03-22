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
