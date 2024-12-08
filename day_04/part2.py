from collections.abc import Iterator

import numpy as np


def slide_3x3_window(txt: np.ndarray) -> Iterator[np.ndarray]:
    """Slide a window over given text and get all 3x3 squares."""
    yield from iter(np.lib.stride_tricks.sliding_window_view(txt, window_shape=(3, 3)))


def is_xmas(txt: np.ndarray) -> bool:
    """Verify if provided 2D text contain an X-MAS that can be read from left to right."""
    assert txt.shape == (3, 3), txt.shape
    unparsed_line_tl_br = np.diag(txt)  # diagonal from top-left to bottom-right
    unparsed_line_bl_tr = np.diag(np.flip(txt, axis=0))  # diagonal from bottom-left to top-right

    line_tl_br = "".join(unparsed_line_tl_br)
    line_bl_tr = "".join(unparsed_line_bl_tr)
    return line_tl_br == line_bl_tr == "MAS"


def count_all_xmas(txt: np.ndarray) -> int:
    """Count all occurrences of 2D X-MAS word."""
    all_occurrences = 0
    for windows in slide_3x3_window(word_search_input):
        for window in windows:
            rotated_window = window
            for _ in range(4):
                rotated_window = np.rot90(rotated_window)
                if not is_xmas(rotated_window):
                    continue

                all_occurrences += 1
                break

    return all_occurrences


if __name__ == "__main__":
    with open("input.txt") as f:
        word_search_input = np.array([[char for char in line.strip()] for line in f])

    print(count_all_xmas(word_search_input))
