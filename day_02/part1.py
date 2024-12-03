def parse_reports(reports: list[str]) -> list[list[int]]:
    """
    Parse the input file representing all the reports.

    Args:
        reports: Input file representing all reports, each report per one line.

    Returns:
        Parsed reports' contents.
    """
    return [[int(number) for number in report.split(" ")] for report in reports]


def count_safe_reports(reports: list[list[int]]) -> int:
    """
    Count the number of reports that are considered safe.

    > So, a report only counts as safe if both of the following are true:
    > 1) The levels are either all increasing or all decreasing.
    > 2) Any two adjacent levels differ by at least one and at most three.
    """
    highest_possible_abs_difference = 3

    safe_reports = 0
    for report in reports:
        assert len(report) > 1, "Encountered too short report."

        differences = [second - first for first, second in zip(report[:-1], report[1:])]
        if any(diff == 0 or abs(diff) > highest_possible_abs_difference for diff in differences):
            # too much of a difference
            continue
        signums = {"+" if diff > 0 else "-" for diff in differences}
        if len(signums) > 1:
            # non-monotonous
            continue

        safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    with open("input.txt") as f:
        reports = parse_reports(f.readlines())

    print(count_safe_reports(reports))
