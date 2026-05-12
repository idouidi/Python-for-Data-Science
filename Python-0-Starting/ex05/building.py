import sys


def count_and_display_char(arg: str) -> None:
    """
    Count and display the number of upper case letters, lower case letters,
    punctuation marks, spaces and digits in a given string.
    The carriage return counts as a space.

    Args:
        arg (str): The string to analyze.

    Return:
        None
    """
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    upper = sum(1 for c in arg if c.isupper())
    lower = sum(1 for c in arg if c.islower())
    digits = sum(1 for c in arg if c.isdigit())
    spaces = sum(1 for c in arg if c.isspace())
    punct = sum(1 for c in arg if c in punctuation)
    total = len(arg)

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main(argv: list[str]) -> int:
    """
    Entry point of the program. Accepts one optional argument.
    If no argument is provided, reads from stdin.
    The carriage return counts as a space, if you don't want
    to return one use ctrl + D.

    Args:
        argv (list[str]): Command line arguments.

    Returns:
        int: 0 on success, 1 on error.
    """
    try:
        if len(argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(argv) == 2:
            count_and_display_char(argv[1])

        elif len(argv) == 1:
            print("What is the text to count?")
            arg = sys.stdin.read()
            count_and_display_char(arg)

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
