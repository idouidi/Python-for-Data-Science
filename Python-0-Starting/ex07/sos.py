import sys


def main(argv: list[str]) -> int:
    """
    A program that takes a string as an argument and encodes it into morse code

    Args:
        argv (list[str]): Command line arguments.

    Returns:
        int: 0 on success, 1 on error.
    """
    try:
        NESTED_MORSE = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----.",
            " ": "/",
        }

        if len(argv) != 2:
            raise AssertionError("the arguments are bad")

        text = argv[1].upper()

        for c in text:
            if c not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")

        print(" ".join(NESTED_MORSE[c] for c in text))

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
