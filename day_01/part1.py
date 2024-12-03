def parse_lists(location_ids_lists: list[str]) -> tuple[list[int], list[int]]:
    """
    Parse the input file representing two lists side-by-side.

    Args:
        location_ids_lists: Input file representing two lists side-by-side, one row per line.

    Returns:
        Tuple of two lists each containing location IDs.
    """
    first: list[int] = []
    second: list[int] = []
    for line in location_ids_lists:
        first_location_id, seconds_location_id, *_ = line.split("   ")
        first.append(int(first_location_id))
        second.append(int(seconds_location_id))

    return first, second


def calculate_distances(first_location_ids: list[int], second_location_ids: list[int]) -> list[int]:
    """
    Calculate distances between two lists' location IDs.

    > To find out, pair up the numbers and measure how far apart they are.
    > Pair up the smallest number in the left list with the smallest number in the right list,
    > then the second-smallest left number with the second-smallest right number, and so on.

    > Within each pair, figure out how far apart the two numbers are;

    Args:
        first_location_ids: First list of location IDs.
        second_location_ids: Second list of location IDs.

    Returns:
        Distances between corresponding location IDs.
    """
    assert len(first_location_ids) == len(second_location_ids), "List' lengths mismatch!"
    return [
        abs(first_location_id - second_location_id)
        for first_location_id, second_location_id in zip(sorted(first_location_ids), sorted(second_location_ids))
    ]


if __name__ == "__main__":
    with open("input.txt") as f:
        first_location_ids, second_location_ids = parse_lists(f.readlines())

    print(sum(calculate_distances(first_location_ids, second_location_ids)))
