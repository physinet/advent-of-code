from helpers import get_input
from collections import defaultdict, deque

TEST = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def elevation(char):
    if char == "S":
        return ord("a")
    if char == "E":
        return ord("z")
    return ord(char)


def neighbors(i, j, width, height):
    _neighbors = set()
    if i != 0:
        _neighbors.add((i - 1, j))
    if j != 0:
        _neighbors.add((i, j - 1))
    if i != width - 1:
        _neighbors.add((i + 1, j))
    if j != height - 1:
        _neighbors.add((i, j + 1))
    return _neighbors


def build_graph(rows):
    height = len(rows)
    width = len(rows[0].strip())

    starts = []
    ends = []
    graph = defaultdict(set)
    for i in range(width):
        for j in range(height):
            current_elevation = elevation(rows[j][i])
            for x, y in neighbors(i, j, width, height):
                if elevation(rows[y][x]) - current_elevation <= 1:
                    graph[(i, j)].add((x, y))
            match rows[j][i]:
                case "S":
                    start = (i, j)
                case "a":
                    starts.append((i, j))
                case "E":
                    end = (i, j)

    return graph, start, end, starts


def main(graph, start, end):
    visited = {start}
    queue = deque([(0, start)])

    while queue:
        depth, node = queue.popleft()
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append((depth + 1, child))
            if child == end:
                return depth + 1
    return 1e100


if __name__ == "__main__":
    assert elevation("S") == 97
    assert elevation("a") == 97
    assert elevation("b") == 98

    assert neighbors(0, 0, 10, 10) == {(0, 1), (1, 0)}
    assert neighbors(9, 5, 10, 10) == {(8, 5), (9, 6), (9, 4)}
    assert neighbors(5, 5, 10, 10) == {(4, 5), (6, 5), (5, 4), (5, 6)}
    graph, start, end, starts = build_graph(TEST.split("\n"))
    print(main(graph, start, end))
    print(min(main(graph, s, end) for s in starts))

    graph, start, end, starts = build_graph(get_input(12))
    print(main(graph, start, end))
    print(min(main(graph, s, end) for s in starts))
