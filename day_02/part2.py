from part1 import count_safe_reports as count_safe_reports_without_dampener
from part1 import parse_reports


def count_safe_reports(reports: list[list[int]]) -> int:
    """
    Count the number of reports that are considered safe.

    > So, a report only counts as safe if both of the following are true:
    > 1) The levels are either all increasing or all decreasing.
    > 2) Any two adjacent levels differ by at least one and at most three.
    > Also, if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
    """
    safe_reports = 0
    for report in reports:
        if count_safe_reports_without_dampener([report]):
            safe_reports += 1
            continue

        # verify all possible variants made using the Problem Dampener
        variants = [report[:idx_to_remove] + report[idx_to_remove + 1 :] for idx_to_remove in range(len(report))]
        if count_safe_reports_without_dampener(variants) > 0:
            # there is at least one variant that is safe
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    with open("input.txt") as f:
        reports = parse_reports(f.readlines())

    print(count_safe_reports(reports))
