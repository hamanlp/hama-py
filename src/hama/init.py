from hama.tagging.dict import Dict
from hama.tagging.hmm import TagHMM


def init(callback=None):
    Dict().load()
    TagHMM().load()

    if callback is not None:
        callback()
