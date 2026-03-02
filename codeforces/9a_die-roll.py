import math
import sys


def solve():
    y, w = map(int, sys.stdin.read().split())
    max_roll: int = max(y, w)
    TOTAL_OUTCOMES = 6
    win_outcomes = TOTAL_OUTCOMES - max_roll + 1
    common_divisor = math.gcd(TOTAL_OUTCOMES, win_outcomes)

    numerator = win_outcomes // common_divisor
    denominator = TOTAL_OUTCOMES // common_divisor

    print(f"{numerator}/{denominator}")


if __name__ == "__main__":
    solve()
