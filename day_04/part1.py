import re
from collections.abc import Iterable

import numpy as np


def count_horizontal(lines: Iterable[np.ndarray], reversed: bool = False) -> int:
    """Count horizontal occurrences of XMAS word."""
    pattern = re.compile("XMAS")
    return sum(len(pattern.findall("".join(line if not reversed else line[::-1]))) for line in lines)


def count_vertical(txt: np.ndarray, reversed: bool = False) -> int:
    """Count vertical occurrences of XMAS word."""
    return count_horizontal(txt.T, reversed=reversed)


def count_diagonal(txt: np.ndarray, reversed: bool = False) -> int:
    """Count diagonal occurrences of XMAS word."""
    rows, columns = txt.shape
    diagonals = [np.diag(txt, k=k) for k in range(-rows, columns + 1)]
    return count_horizontal(diagonals, reversed=reversed)


def count_all(txt: np.ndarray) -> int:
    """Count all occurrences of XMAS word."""
    counts = [
        count_horizontal(txt),
        count_horizontal(txt, reversed=True),
        count_vertical(txt),
        count_vertical(txt, reversed=True),
        count_diagonal(txt),
        count_diagonal(txt, reversed=True),
        count_diagonal(np.flip(txt, axis=0)),
        count_diagonal(np.flip(txt, axis=0), reversed=True),
    ]
    print(counts)
    return sum(counts)


if __name__ == "__main__":
    with open("input.txt") as f:
        word_search_input = np.array([[char for char in line.strip()] for line in f])

    print(count_all(word_search_input))
