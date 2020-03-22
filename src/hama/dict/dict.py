from .singleton import Singleton
import pandas as pd


class Dict(metaclass=Singleton):
    """Class responsible for managing embedded morpheme dictionary.
    """
    
    def __init__(self):
        """Initialize singleton dictionary class.
        """

        super().__init__()
        self.dict = None 
        """obj: Morpheme dictionary."""

    def load(self):
        """Loads morpheme dictionary into memory.
        """
        if self.dict is None:
            self.dict = pd.read_csv('morphemes.csv')

    def unload(self):
        """Unloads morpheme dictionary from memory.
        """
        self.dict = None

    def query(self, m):
        """Query morpheme from dictionary.
    
        Args:
            m (str): Morpheme to query from dict.
    
        Returns:
            list: list containing tags of morpheme.
        """
        tags = []
        # Change when using bloom filters.
        entries = self.dict.loc[self.dict.term.isin([m])]
        if len(entries) > 0:
            for row in entries.itertuples():
                tags.append(row.pos22)
        ########################################
        return tags 


