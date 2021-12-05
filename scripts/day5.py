from itertools import zip_longest
from math import copysign
from typing import Iterable

from helpers import get_input

Coordinate = tuple[int, int]

sign = lambda x: int(copysign(1, x))


def get_coords(rows: Iterable[str]) -> list[tuple[Coordinate, Coordinate]]:
    return [
        tuple(tuple(int(x) for x in pair.split(",")) for pair in row.split(" -> "))
        for row in rows
    ]


def main(diagonal: bool = False) -> int:
    coords = get_coords(get_input(5))
    N = 1000
    board = [[0 for _ in range(N)] for _ in range(N)]

    for start, end in coords:
        # amount to iterate in each direction
        x_iter, y_iter = (end[i] - start[i] for i in range(2))
        if diagonal or any(i == 0 for i in (x_iter, y_iter)):
            x_dir, y_dir = sign(x_iter), sign(y_iter)
            for i, j in zip_longest(
                range(start[0], end[0] + x_dir, x_dir),
                range(start[1], end[1] + y_dir, y_dir)
            ):
                i = start[0] if i is None else i
                j = start[1] if j is None else j

                board[i][j] += 1

    return sum(col > 1 for row in board  for col in row)

if __name__ == "__main__":
    print(main())
    print(main(diagonal=True))
