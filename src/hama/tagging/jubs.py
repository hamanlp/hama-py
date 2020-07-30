from .tagging import tag


def affixes(text):
    """Extract affixes (접사) from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as affixes.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] in ["xp", "xs"]]
    return filtered


def jubs(text):
    """Extract affixes (접사) from text.

    args:
        text (str): text to analyze.
        
    returns:
        list: list of morphemes tagged as affixes.

    """

    return affixes(text)


def xp(text):
    """Extract 접두사 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 접두사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "xp"]
    return filtered


def xs(text):
    """Extract 접미사 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 접미사.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "xs"]
    return filtered
