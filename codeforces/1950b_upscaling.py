import sys


def solve() -> None:
    input: list[str] = sys.stdin.read().split()
    output: list[str] = []

    if not input:
        return

    number_of_tests: int = int(input[0])

    for i in range(1, number_of_tests + 1):
        checkerboard_rows: list[str] = build_checkerboard(int(input[i]))
        output.extend(checkerboard_rows)

    sys.stdout.write("\n".join(output) + "\n")


def build_checkerboard(n: int) -> list[str]:
    row_type_a: str = ("##.." * n)[: 2 * n]
    row_type_b: str = ("..##" * n)[: 2 * n]

    board: list[str] = []

    for rows in range(2 * n):
        if (rows // 2) % 2 == 0:
            board.append(row_type_a)
        else:
            board.append(row_type_b)

    return board


if __name__ == "__main__":
    solve()
