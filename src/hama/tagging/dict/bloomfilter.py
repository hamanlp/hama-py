from .bitarray import BitArray
import mmh3
import os


class LookupBloomFilter():
    """Class representing bloom filters.

    Bloom filters will represent morpheme 
    dictionaries and graphs.

    Attributes:
        bits: BitArray object representing the filter.
        path: Path to byte array on disk.
        size: Size of the BitArray.
        hash_count: Number of hash functions used by this filter.
    """

    def __init__(self, path, size, hash_count):
        """Initialize filter instance."""
        super().__init__()
        self.path = path
        self.size = size
        self.hash_count = hash_count

    def __getattr__(self, name):
        """Called when an called attribute does not exist."""
        return None

    def load(self):
        """Read filter files from disk."""
        if self.bits is None:
            bit_path = os.path.join(os.path.dirname(__file__), 'bits',
                                    self.path)
            self.bits = BitArray(self.size)
            self.bits.read(bit_path)

    def query(self, item):
        """Queries item from the filter.

        Args:
            item (str): String to query.
           
        Returns: 
            bool: True if contains, False if not.

        Raises:
            Exception if bit array was not initialized
            before with load()
        """

        if self.bits is None:
            raise Exception("Initialize filter before querying!")

        for i in range(self.hash_count):
            hash = mmh3.hash(item, i) % self.size
            if self.bits.at(hash) == 0:
                return False
        return True
