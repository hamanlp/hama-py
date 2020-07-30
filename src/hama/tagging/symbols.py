from .tagging import tag


def symbols(text):
    """Extract symbols from text.

    Args:
        text (str): Text to analyze.
        
    Returns:
        list: List of morphemes tagged as symbols.

    """
    tags = tag(text, zipped=True)
    filtered = [t[0] for t in tags if t[1] == "s"]
    return filtered
