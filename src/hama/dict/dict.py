import os
import configparser
from hama.langutils import Singleton
from .bloomfilter import LookupBloomFilter


class Dict(metaclass=Singleton):
    """Class responsible for managing embedded morpheme dictionary.

    Attributes:
        dict (dic): Morpheme dictionaries.
        Keys include KAIST POS22 tags.
    """

    def __init__(self):
        """Initialize singleton dictionary class."""

        super().__init__()
        self.dict = None

    def __getattr__(self, name):
        """Called when an called attribute does not exist."""
        return None

    def load(self):
        """Loads morpheme dictionary into memory."""
        if self.dict is None:

            config_path = os.path.join(os.path.dirname(__file__),
                                       'meta/source.ini')
            config = configparser.ConfigParser()
            config.read(config_path)

            fp = config['FILTER_PATH']
            hc = config['HASH_COUNT']
            sz = config['FILTER_SIZE']

            self.dict = {}
            for name, path in fp.items():
                if name[0] == 'd':
                    filter = LookupBloomFilter(path=path,
                                               size=int(sz[name]),
                                               hash_count=int(hc[name]))
                    filter.load()

                    tag = name[2:]
                    self.dict[tag] = filter

    def unload(self):
        """Unloads morpheme dictionary from memory."""
        self.dict = None

    def query(self, m):
        """Query morpheme from dictionary.
    
        Args:
            m (str): Morpheme to query from dict.
    
        Returns:
            list: list containing tags of morpheme.

        Raises:
            Exception if dictionary was not initialized
            before with load().
        """

        if self.dict is None:
            raise Exception("Initialize dict before querying!")

        tags = []
        for tag, dict in self.dict.items():
            if dict.query(m):
                tags.append(tag)
        return tags
