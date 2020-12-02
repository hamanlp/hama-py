chosungs = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]
joongsungs = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]
jongsungs = [
    None,
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

chosung_set = set(chosungs)
joongsung_set = set(joongsungs)
jongsung_set = set(jongsungs)


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

        code = ord(c)

        # Unicode hangul range.
        if 0xAC00 <= code <= 0xD7A3:

            chosung_code = chosungs[(code - 0xAC00) // (28 * 21)]
            joongsung_code = joongsungs[(code - 0xAC00) % (28 * 21) // 28]
            jongsung_code = jongsungs[(code - 0xAC00) % (28 * 21) % 28]

            disassembled = [chosung_code, joongsung_code, jongsung_code]
            disassembled = [e for e in disassembled if e]

        else:
            disassembled = [c]

        for item in disassembled:
            out_list.append(item)
            recovery_map.append(i)

    if out == list:
        return out_list, recovery_map
    else:
        return "".join(out_list), recovery_map


def assemble(jaso_list):
    """
    Reassemble Korean consonants and vowels into text.

    Args:
        jaso_list (list): Input jaso list to reassemble.

    Returns:
         str: Reconstructed string.
        list: List that maps each index of original deconstructed text 
              to its constructed string index.
    """

    def valid_combination(jasos):
        jasos_len = len(jasos)
        valid_chosung = jasos_len > 0 and jasos[0] in chosung_set
        valid_joongsung = jasos_len < 1 or jasos[1] in joongsung_set
        valid_jongsung = jasos_len < 2 or jasos[2] in jongsung_set
        return valid_chosung and valid_joongsung and valid_jongsung

    out, recovery_map = "", list()

    collected, corresponding_jamos, character_complete = list(), list(), False

    chunk_start = 0

    while chunk_start < len(jaso_list):

        code = ord(jaso_list[chunk_start])

        # Compatability jamo range.
        if not (0x3130 <= code <= 0x318E):
            out += c
            recovery_map.append(i)
            continue

        chunk_end = min(chunk_start + 3, len(jaso_list))

        while chunk_end > 0:

            chunk = jaso_list[chunk_start:chunk_end]

            if valid_combination(chunk):

                chunk_length = len(chunk)
                chosung = chosungs.index(chunk[0]) * 21 * 28 if chunk_length > 0 else 0
                joongsung = joongsungs.index(chunk[1]) * 28 if chunk_length > 1 else 0
                jongsung = jongsungs.index(chunk[2]) if chunk_length > 2 else 0

                assembled_code = chosung + joongsung + jongsung + 0xAC00
                return chr(assembled_code)

            chunk_end -= 1
    return None
