import sys
from collections import defaultdict
from enum import Enum, auto
from itertools import groupby


class SubSequenceType(Enum):
    CANDIDATE = auto()
    INVALID = auto()


def count_subsequences(
    sum_target: int, max_target: int, sequence: list[int], mode: SubSequenceType
) -> int:
    subarrays = []
    total = 0

    if mode == SubSequenceType.CANDIDATE:
        subarrays = [
            list(group)
            for is_passing, group in groupby(sequence, lambda x: x <= max_target)
            if is_passing
        ]
    elif mode == SubSequenceType.INVALID:
        subarrays = [
            list(group)
            for is_passing, group in groupby(sequence, lambda x: x < max_target)
            if is_passing
        ]

    for subarray in subarrays:
        prefix_sum_total = 0
        seen_prefix_sums = defaultdict(int)
        seen_prefix_sums[0] = 1
        for x in subarray:
            prefix_sum_total += x
            required_prefix = prefix_sum_total - sum_target

            total += seen_prefix_sums[required_prefix]

            seen_prefix_sums[prefix_sum_total] += 1

    return total


def solve_testcase(params: str, data: str) -> str:
    _, sum_target, max_target = map(int, params.split())
    full_sequence = [int(x) for x in data.split()]

    if max_target not in set(full_sequence):
        return str(0)

    candidate_subsequences: int = count_subsequences(
        sum_target, max_target, full_sequence, SubSequenceType.CANDIDATE
    )
    invalid_subsequences: int = count_subsequences(
        sum_target, max_target, full_sequence, SubSequenceType.INVALID
    )

    return str(candidate_subsequences - invalid_subsequences)


def solve():
    sysin = sys.stdin.readline
    number_of_testcases = int(sysin())

    for _ in range(number_of_testcases):
        params = sysin()
        data = sysin()
        sys.stdout.write(solve_testcase(params, data) + "\n")


if __name__ == "__main__":
    solve()
