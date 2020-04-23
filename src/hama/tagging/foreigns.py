from .tagging import tag


def foreigns():
    """Extract foreign words from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as foreign words.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == 'f']
    return filtered
