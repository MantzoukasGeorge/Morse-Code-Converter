from encoder import MORSE_CODE_DICT

REVERSE_MORSE_DICT: dict[str, str] = {v: k for k, v in MORSE_CODE_DICT.items()}

def decode(morse: str) -> str:
    if not morse.strip():
        return ""

    tokens = morse.strip().split()
    decoded_chars: list[str] = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        char = REVERSE_MORSE_DICT.get(token)
        if char:
            decoded_chars.append(char)
        i += 1
    return "".join(decoded_chars)

if __name__ == "__main__":
    test_cases = [
        ("... --- ...", "SOS"),
        (".... . .-.. .-.. --- / .-- --- .-. .-.. -..", "HELLO WORLD"),
        (".---- ..--- ...--", "123"),
        (".- / -... .-.-.-", "A B."),
        (".... . .-.. .-.. --- /// .-- --- .-. .-.. -..", "HELLO WORLD"),  # triple space
    ]
    for inp, expected in test_cases:
        out = decode(inp)
        status = "OK" if out == expected else "FAIL"
        print(f'"{inp}" → "{out}" [{status}]')