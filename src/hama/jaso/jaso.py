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


def assemble(text):
    """

    """
    pass
