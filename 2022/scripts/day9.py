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


def sign(x):
    return x // abs(x) if x != 0 else 0


def _correction_vector(leader, follower):
    x_delta, y_delta = (leader[i] - follower[i] for i in range(2))
    if abs(x_delta) > 1 or abs(y_delta) > 1:
        return sign(x_delta), sign(y_delta)


def _draw(positions, N=6):
    s = ""
    for i in range(N - 1, -1, -1):
        for j in range(N):
            for k, position in enumerate(positions):
                if position == (j, i):
                    s += "H" if k == 0 else str(k)
                    break
            else:
                s += "."
        s += "\n"
    print(s)


def _move(positions, move):
    # Head
    positions[0] = positions[0][0] + move[0], positions[0][1] + move[1]
    for i, follower in enumerate(positions[1:]):
        leader = positions[i]
        if correction_vector := _correction_vector(leader, follower):
            positions[i + 1] = (
                follower[0] + correction_vector[0],
                follower[1] + correction_vector[1],
            )
    return positions


def main(rows, N=2, draw=False):
    positions = [(0, 0) for _ in range(N)]
    tail_visited = set()
    for row in rows:
        direction, distance = row.strip().split()
        move = MOVES[direction]
        for _ in range(int(distance)):
            if draw:
                _draw(positions)
            positions = _move(positions, move)
            tail_visited.add(positions[-1])
    return len(tail_visited)


if __name__ == "__main__":
    print(main(TEST.split("\n"), draw=True))
    print(main(get_input(9), draw=False))
    print(main(TEST.split("\n"), N=10, draw=True))
    print(main(get_input(9), N=10, draw=False))
