from .tagging import tag


def predicates(text):
    """Extract predicates (용언) from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as predicates.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] in ["pv", "pa", "px"]]
    return filtered


def yongs(text):
    """Extract predicates (용언) from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as predicates.

    """

    return predicates(text)


def pv(text):
    """Extract 동사 from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as 동사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "pv"]
    return filtered


def pa(text):
    """Extract 형용사 from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as 형용사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "pa"]
    return filtered
