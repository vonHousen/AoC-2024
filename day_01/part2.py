from collections import Counter

from part1 import parse_lists


def calculate_similarity_score(first_location_ids: list[int], second_location_ids: list[int]) -> int:
    """
    Calculate similarity score between two lists of location IDs.

    > figure out exactly how often each number from the left list appears in the right list.
    > Calculate a total similarity score by adding up each number in the left list
    > after multiplying it by the number of times that number appears in the right list.
    """
    second_location_ids_counts = Counter(second_location_ids)
    return sum(location_id * second_location_ids_counts.get(location_id, 0) for location_id in first_location_ids)


if __name__ == "__main__":
    with open("input.txt") as f:
        first_location_ids, second_location_ids = parse_lists(f.readlines())

    print(calculate_similarity_score(first_location_ids, second_location_ids))
