import sys


from ft_filter import ft_filter


def main(argv: list[str]) -> int:
    """
    Accept a string and an integer, then return the words in the string
    whose length is greater than the given integer.

    Args:
        argv (list[str]): Command line arguments.

    Returns:
        int: 0 on success, 1 on error.
    """
    try:
        if len(argv) != 2 or not argv[1].replace(" ", "").isalpha() or \
             not argv[2].isdigit():
            raise AssertionError("the arguments are bad")

        sentence = sys.argv[1].split()
        length = int(sys.argv[2])

        print([x for x in ft_filter((lambda i: len(i) > length), sentence)])

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
