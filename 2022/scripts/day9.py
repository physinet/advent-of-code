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


def _follower_too_far(leader, follower):
    return any(abs(leader[i] - follower[i]) > 1 for i in range(2))


def _draw(positions, N=5):
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
    for i, (leader, follower) in enumerate(zip(positions[:-1], positions[1:])):
        if _follower_too_far(leader, follower):
            # follower position moves to follow the leader in the opposite direction the leader moved
            positions[i + 1] = leader[0] - move[0], leader[1] - move[1]
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
