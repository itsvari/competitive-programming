import sys


def solve():
    sysin = sys.stdin.readline

    t = int(sysin())

    for _ in range(t):
        array_size = int(sysin())
        values = list(map(int, sysin().split()))
        result = array_size * max(values)
        print(result)


if __name__ == "__main__":
    solve()
