from collections import Counter
from helpers import get_input


def main(last: bool) -> int:
    rows = get_input(4)
    boards = {}
    board = {}
    row_num = 0
    board_num = 0
    for row in rows[2:]:
        if row.strip():
            row_coords = {int(num): (row_num, j) for j, num in enumerate(row.split())}
            board.update(row_coords)
            row_num += 1
        else:
            boards[board_num] = board
            board_num += 1
            board = {}
            row_num = 0

    draws = set()
    winner = None

    for draw in [int(num) for num in rows[0].split(",")]:
        draws.add(draw)
        for board_num, board in list(boards.items()):
            row_counts = Counter((board.get(draw, (-1, -1))[0] for draw in draws))
            col_counts = Counter((board.get(draw, (-1, -1))[1] for draw in draws))
            if any(
                value == 5
                for counts in (row_counts, col_counts)
                for key, value in counts.items()
                if key != -1
            ):
                winner = boards.pop(board_num)
            if winner and not last:
                break

        if (not boards) or (not last and winner):
            break

    return (
        sum(board.keys()) - sum(draw for draw in draws if board.get(draw) is not None)
    ) * draw


if __name__ == "__main__":
    print(main(last=False))
    print(main(last=True))
