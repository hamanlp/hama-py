from ..tagging import tag


def suffixes(text):
    """Extract suffixes (어미) from text.

    args:
        text (str): text to analyze.
        
    returns:
        list: list of morphemes tagged as suffixes.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] in ['ep', 'ec', 'et', 'ef']]
    return filtered


def eoms(text):
    """Extract suffixes (어미) from text.

    args:
        text (str): text to analyze.
        
    returns:
        list: list of morphemes tagged as suffixes.

    """
    return suffixes(text)


def ep(text):
    """Extract 선어말어미 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 선어말어미.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == 'ep']
    return filtered


def ec(text):
    """Extract 연결어미 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 연결어미.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == 'ec']
    return filtered


def et(text):
    """Extract 전성어미 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 전성어미.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == 'et']
    return filtered


def ef(text):
    """Extract 종결어미 from text.

    args:
        text (str): Text to analyze.
        
    returns:
        list: List of morphemes tagged as 종결어미.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == 'ef']
    return filtered
