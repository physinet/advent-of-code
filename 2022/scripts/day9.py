from helpers import get_input

TEST = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

MOVES = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def _tail_too_far(head_position, tail_position):
    return any(abs(head_position[i] - tail_position[i]) > 1 for i in range(2))


def _draw(head_position, tail_position, N=5):
    s = ""
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if head_position == (j, i):
                s += "H"
            elif tail_position == (j, i):
                s += "T"
            else:
                s += "."
        s += "\n"
    print(s)


def _move(head_position, tail_position, move):
    head_position = head_position[0] + move[0], head_position[1] + move[1]
    if _tail_too_far(head_position, tail_position):
        tail_position = head_position[0] - move[0], head_position[1] - move[1]
    return head_position, tail_position


def main(rows, draw=False):
    head_position = (0, 0)
    tail_position = (0, 0)
    tail_visited = set()
    for row in rows:
        direction, distance = row.strip().split()
        move = MOVES[direction]
        for _ in range(int(distance)):
            if draw:
                _draw(head_position, tail_position)
            head_position, tail_position = _move(head_position, tail_position, move)
            tail_visited.add(tuple(tail_position))
    return len(tail_visited)


if __name__ == "__main__":
    print(main(TEST.split("\n"), draw=True))
    print(main(get_input(9), draw=False))
