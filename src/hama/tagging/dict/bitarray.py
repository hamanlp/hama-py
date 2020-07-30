import math


class BitArray:
    """Class representing large bit arrays.

    Arrtibutes:
        BUFF_SIZE: File read buffer size, in bytes.
        ELEM_SIZE: Each int stored internally is 32 bits, or 4 bytes.

        bits: Internal bit array.
        size: Bit array size, in bits.
    """

    BUFF_SIZE = 256  # In bytes.
    ELEM_SIZE = 4  # In bytes.

    def __init__(self, size):
        """Initialize BitArray instance."""
        super().__init__()
        self.size = size
        bits_per_elem = BitArray.ELEM_SIZE * 8
        self.bits = [0] * math.ceil(self.size / bits_per_elem)

    def read(self, path):
        """Read bit array from file.

        Args:
            file (str): File path.
        """
        with open(path, "rb") as f:
            bs = BitArray.BUFF_SIZE
            es = BitArray.ELEM_SIZE

            elems_per_read = bs // es

            counter = 0
            byte = f.read(bs)
            while byte:
                for i in range(elems_per_read):
                    # Take a es-szied slice out of bs bytes.
                    start = i * es
                    end = min(start + es, len(byte))
                    byte_slice = byte[start:end]
                    if byte_slice == b"":
                        break
                    bits_index = counter + i
                    self.bits[bits_index] = int.from_bytes(byte_slice, byteorder="big")
                counter += elems_per_read
                byte = f.read(bs)

    def at(self, index):
        """Returns bit at index

        Args:
            index (int): Index of bit array to query.

        Returns:
            1 is bit is set, 0 if not.
        """
        # Location within self.bits.
        internal_index = index // 32
        # Each index of self.bits contains 4 bytes (32-bit int).
        # byte_position selects 1 ofthose 4 bytes.
        byte_position = (index // 8) % 4
        # Position from the right edge of byte.
        bit_position = 7 - (index % 8)

        int_bits = self.bits[internal_index]
        byte = int_bits.to_bytes(4, byteorder="big")[byte_position]

        bit = (byte >> bit_position) & 1
        return bit
