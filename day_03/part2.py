import re

from part1 import get_multiplication_results


def get_enabled_multiplication_results(memory: list[str]) -> list[int]:
    """
    Get enabled multiplication operations results based on the provided memory.

    Args:
        memory: List representing multiplication operations within corrupted memory.

    Returns:
        Multiplication operations results
    """
    # re.DOTALL was a gamechanger cause there were \n characters in the memory...
    enabled_instructions_regex = re.compile(r"(?:^|do\(\))(.*?)(?:$|(?:don't\(\)))", flags=re.DOTALL)

    memory_concatenated = "".join(memory)
    enabled_instructions = [match[1] for match in enabled_instructions_regex.finditer(memory_concatenated)]

    return get_multiplication_results(enabled_instructions)


if __name__ == "__main__":
    with open("input.txt") as f:
        results = get_enabled_multiplication_results(f.readlines())

    print(sum(results))
