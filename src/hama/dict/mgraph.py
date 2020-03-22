from .singleton import Singleton
import json


class MGraph(metaclass=Singleton):
    """Class responsible for managing embedded morpheme graphs."""

    def __init__(self):
        """Initialize singleton MGraph class.
        """

        super().__init__()
        self.graph = None 
        """list: Morpheme graph."""

    def load(self):
        """Loads morpheme graph into memory.
        """
        if self.graph is None:
            with open('mgraph.json') as f:
                self.graph = json.load(f)
        """list: Pre-defined morpheme graphs.
        Each row is a possible morpheme sequence. Each sequence 
        is split into pairs, similar to the output of
        hama.sequence.similarity._generate_pairs function."""

    def unload(self):
        """Unloads morpheme graph from memory.
        """
        self.graph = None

    def graphs(self):
        """Returns pre-defined morpheme graphs.
    
        Returns: 
            list: Pre-defined morpheme graph.
            Each row is a possible morpheme sequence.
            Each sequence is split into pairs, similar to
            the output of _generate_pairs function.
        """
        return []
