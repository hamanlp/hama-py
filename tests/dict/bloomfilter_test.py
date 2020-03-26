import pytest
from hama.dict.bloomfilter import LookupBloomFilter


def test_query():
    bf = LookupBloomFilter("", 0, 0)

    with pytest.raises(Exception):
        bf.query('')
