import math


class BitArray():
    """Class representing large bit arrays.

    Arrtibutes:
        bits: Internal bit array.
        size: Bit array size, in bits.
    """

    def __init__(self, size):
        """Initialize BitArray instance."""
        super().__init__()
        self.size = size
        self.bits = [0] * math.ceil((self.size / 32))

    def read(self, path):
        """Read bit array from file.

        Args:
            file (str): File path.
        """
        with open(path, "rb") as f:
            counter = 0
            byte = f.read(4)
            while byte:
                self.bits[counter] = int.from_bytes(byte, byteorder='big')
                counter += 1
                byte = f.read(4)

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
        byte = int_bits.to_bytes(4, byteorder='big')[byte_position]

        bit = (byte >> bit_position) & 1
        return bit
