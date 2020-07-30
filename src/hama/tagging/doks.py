from .tagging import tag


def orthotones(text):
    """Extract orthotones (독립언) from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as orthotones.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "ii"]
    return filtered


def doks(text):
    """Extract orthotones (독립언) from text.

    args:
        text (str): text to analyze.
        
    returns:
        list: list of morphemes tagged as orthotones.

    """

    return orthotones(text)


def ii(text):
    """Extract 감탄사 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 감탄사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "ii"]
    return filtered
