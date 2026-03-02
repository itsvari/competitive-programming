import sys


def solve():
    sysin = sys.stdin.readline
    number_of_testcases = int(sysin())

    for _ in range(number_of_testcases):
        sysin()
        distinct_numbers = set(sysin().split())
        print(str(len(distinct_numbers) * 2 - 1))


if __name__ == "__main__":
    solve()
