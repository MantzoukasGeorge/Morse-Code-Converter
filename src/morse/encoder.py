
MORSE_CODE_DICT: dict[str, str] = {
    # Letters
    "A": ".-",     "B": "-...",   "C": "-.-.",   "D": "-..",
    "E": ".",      "F": "..-.",   "G": "--.",    "H": "....",
    "I": "..",     "J": ".---",   "K": "-.-",    "L": ".-..",
    "M": "--",     "N": "-.",     "O": "---",    "P": ".--.",
    "Q": "--.-",   "R": ".-.",    "S": "...",    "T": "-",
    "U": "..-",    "V": "...-",   "W": ".--",    "X": "-..-",
    "Y": "-.--",   "Z": "--..",

    # Numbers
    "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--",
    "4": "....-",  "5": ".....",  "6": "-....",  "7": "--...",
    "8": "---..",  "9": "----.",

    # Punctuation (most common)
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.",  "(": "-.--.",  ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-.",

    # Word separator – a single space in the input becomes "   "
    " ": "/",
}

def encode(text: str) -> str:
    if not text:
        return ""
    morse_parts: list[str] = []
    for ch in text:
        upper = ch.upper()
        morse = MORSE_CODE_DICT.get(upper)
        if morse is not None:
            morse_parts.append(morse)
        else:
            raise print("Invalid morse code")
    return " ".join(morse_parts)

if __name__ == "__main__":
    test_cases = [
        ("SOS", "... --- ..."),
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("123", ".---- ..--- ...--"),
        ("A.B.", ".- .-.-.- -... .-.-.-"),
    ]
    for inp, expected in test_cases:
        out = encode(inp)
        print(f'"{inp}" → "{out}"', "OK" if out == expected else "FAIL")