from .assemble_machine import Assembler
from .constants import (
    chosung_set,
    chosungs,
    jongsung_set,
    jongsungs,
    joongsung_set,
    joongsungs,
)


def disassemble(text, out=list):
    """
    Deconstruct input text into Korean consonants and vowels.

    Args:
        text (str): Input string to deconstruct.
        out (type): [Optional, default: list] Output type. 
                    One of list and str.

    Returns:
        list: List of consonants and vowels. Symbols and foreign 
              languages are returned as-is.
        list: List that maps each index of disassembled component to 
              its original character index.
    """
    out_list, recovery_map = list(), list()

    for i, c in enumerate(text):

        if c.isspace():
            continue

        code = ord(c)

        # Unicode hangul range.
        if 0xAC00 <= code <= 0xD7A3:

            chosung_code = chosungs[(code - 0xAC00) // (28 * 21)]
            joongsung_code = joongsungs[(code - 0xAC00) % (28 * 21) // 28]
            jongsung_code = jongsungs[(code - 0xAC00) % (28 * 21) % 28]

            disassembled = [chosung_code, joongsung_code]
            if jongsung_code:
                disassembled.append(jongsung_code)

        else:
            disassembled = [c]

        for item in disassembled:
            out_list.append(item)
            recovery_map.append(i)

    if out == list:
        return out_list, recovery_map
    else:
        return "".join(out_list), recovery_map


def assemble(jamo_list):
    """
    Reassemble Korean consonants and vowels into text.

    Args:
        jamo_list (list): Input jamo list to reassemble.

    Returns:
         str: Reconstructed string.
        list: List that maps each index of original deconstructed text 
              to its constructed string index.
    """

    assembler = Assembler()
    return "".join(assembler.assemble(jamo_list))
