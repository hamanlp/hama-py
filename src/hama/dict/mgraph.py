from .singleton import Singleton
import pandas as pd


class MGraph(metaclass=Singleton):
    """Class responsible for managing embedded morpheme graphs.
    
    Attributes:
        graph (obj): Morpheme graph.
    """

    def __init__(self):
        """Initialize singleton MGraph class."""

        super().__init__()
        self.graph = None 

    def load(self):
        """Loads morpheme graph into memory."""
        if self.graph is None:
            self.graph = pd.read_csv('mgraph.csv')
        """list: Pre-defined morpheme graphs.
        Each row is a possible morpheme sequence. Each sequence 
        is split into pairs, similar to the output of
        hama.sequence.similarity._generate_pairs function."""

    def unload(self):
        """Unloads morpheme graph from memory."""
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

    def query(self, seq):
        """See is seq is in morpheme graph.
    
        Returns: 
            bool: True if found, False if not.
        """
        entries = self.graph.loc[
                self.graph.graph.isin([seq])]
        return len(entries) > 0




