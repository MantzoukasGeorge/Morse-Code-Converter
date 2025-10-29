# src/cli.py
import argparse
from morse.encoder import encode
from morse import decode

def main():
    parser = argparse.ArgumentParser(
        prog="morse",
        description="Encode text to Morse code or decode Morse to text"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Text → Morse")
    encode_parser.add_argument("text", nargs="?", help="Text to encode")

    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Morse → Text")
    decode_parser.add_argument("morse", nargs="?", help="Morse code to decode")

    args = parser.parse_args()

    # Read from stdin if no argument
    if args.command == "encode":
        text = args.text or input()
        print(encode(text))
    elif args.command == "decode":
        morse = args.morse or input().strip()
        print(decode(morse))

if __name__ == "__main__":
    main()