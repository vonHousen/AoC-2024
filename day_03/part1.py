import re


def get_multiplication_results(memory: list[str]) -> list[int]:
    """
    Get all multiplication operations results based on the provided memory.

    Args:
        memory: List representing multiplication operations within corrupted memory.

    Returns:
        Multiplication operations results
    """
    multiplication_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return [int(match[1]) * int(match[2]) for line in memory for match in multiplication_regex.finditer(line) if match]


if __name__ == "__main__":
    with open("input.txt") as f:
        results = get_multiplication_results(f.readlines())

    print(sum(results))
