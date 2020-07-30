from .tagging import tag


def nouns(text):
    """Extract nouns (체언) from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as nouns.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] in ["nc", "nq", "nb", "np", "nn"]]
    return filtered


def ches(text):
    """Extract nouns (체언) from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as nouns.

    """

    return nouns(text)


def nc(text):
    """Extract 보통명사, 고유명사 from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as 보통명사/고유명사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "nc"]
    return filtered


def nb(text):
    """Extract 의존명사 from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as 의존명사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "nb"]
    return filtered


def np(text):
    """Extract 대명사 from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as 대명사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "np"]
    return filtered


def nn(text):
    """Extract 수사 from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as 수사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "nn"]
    return filtered
