from typing import Iterable
from helpers import get_input

Coordinate = tuple[int, int]


def get_coords(rows: Iterable[str]) -> list[tuple[Coordinate, Coordinate]]:
    return [
        tuple(tuple(int(x) for x in pair.split(",")) for pair in row.split(" -> "))
        for row in rows
    ]


def sign(x: bool) -> int:
    """Returns -1 if x is False, 1 if x is True"""
    return 2 * x - 1


def main() -> int:
    coords = get_coords(get_input(5))
    N = 1000
    board = [[0 for _ in range(N)] for _ in range(N)]
    for start, end in coords:
        if (x := start[0]) == end[0]:
            direction =  sign(end[1] > start[1])
            for j in range(start[1], end[1] + direction, direction):
                board[x][j] += 1
        elif (y := start[1]) == end[1]:
            direction =  sign(end[0] > start[0])
            for i in range(start[0], end[0] + direction, direction):
                board[i][y] += 1

    count_overlap = 0
    for row in board:
        for col in row:
            if col > 1:
                count_overlap += 1
    return count_overlap


if __name__ == "__main__":
    print(main())
