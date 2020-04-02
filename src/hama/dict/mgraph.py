import os
import configparser
from hama.langutils import Singleton
from .bloomfilter import LookupBloomFilter


class MGraph(metaclass=Singleton):
    """Class responsible for managing embedded morpheme graphs.
    
    Attributes:
        graph (LookupBloomFilter): Pre-defined morpheme graph.
    """

    def __init__(self):
        """Initialize singleton MGraph class."""

        super().__init__()
        self.graph = None

    def __getattr__(self, name):
        """Called when an called attribute does not exist."""
        return None

    def load(self):
        """Loads morpheme graph into memory."""
        if self.graph is None:

            config_path = os.path.join(os.path.dirname(__file__),
                                       'meta/source.ini')
            config = configparser.ConfigParser()
            config.read(config_path)

            fp = config['FILTER_PATH']['g']
            hc = config['HASH_COUNT']['g']
            sz = config['FILTER_SIZE']['g']

            filter = LookupBloomFilter(path=fp,
                                       size=int(sz),
                                       hash_count=int(hc))
            filter.load()

            self.graph = filter

    def unload(self):
        """Unloads morpheme graph from memory."""
        self.graph = None

    def query(self, seq):
        """See if seq is in morpheme graph.

        Args:
            seq (str): Morpheme graph string.
    
        Returns: 
            bool: True if found, False if not.

         Raises:
            Exception if graph was not initialized
            before with load().
        """

        if self.graph is None:
            raise Exception("Initialize graph before querying!")

        return self.graph.query(seq)
