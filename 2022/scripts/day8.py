from helpers import get_input
from functools import reduce

TEST = """30373
25512
65332
33549
35390"""

MAX = 9


def process_input(rows: list[str]) -> list[list[int]]:
    return [[int(c) for c in row.strip()] for row in rows]


def get_visible_map(tree_map: list[list[int]]) -> list[list[bool]]:
    n_row = len(tree_map)
    n_col = len(tree_map[0])
    vis_map = [[False for _ in range(n_col)] for _ in range(n_row)]

    for i in range(n_row):
        for iterator in (range(n_col), range(n_col - 1, -1, -1)):
            h_max = -1
            for j in iterator:
                if (h := tree_map[i][j]) > h_max:
                    vis_map[i][j] = True
                    h_max = h
                if h_max == MAX:
                    break

    for j in range(n_col):
        for iterator in (range(n_row), range(n_row - 1, -1, -1)):
            h_max = -1
            for i in iterator:
                if (h := tree_map[i][j]) > h_max:
                    vis_map[i][j] = True
                    h_max = h
                if h_max == MAX:
                    break

    return vis_map


def num_trees_visible(vis_map: list[list[bool]]) -> int:
    return sum(is_visible for row in vis_map for is_visible in row)


def max_scenic_score(tree_map: list[list[int]]) -> int:
    n_row = len(tree_map)
    n_col = len(tree_map[0])
    scores = [[[] for _ in range(n_col)] for _ in range(n_row)]
    for i, row in enumerate(tree_map):
        for j, col in enumerate(tree_map):
            h_tree = tree_map[i][j]
            four_score = []
            tot = -1
            for ii in range(i, -1, -1):
                tot += 1
                if tree_map[ii][j] >= h_tree and i != ii:
                    break
            four_score.append(tot)
            tot = -1
            for ii in range(i, n_row):
                tot += 1
                if tree_map[ii][j] >= h_tree and i != ii:
                    break
            four_score.append(tot)
            tot = -1
            for jj in range(j, -1, -1):
                tot += 1
                if tree_map[i][jj] >= h_tree and j != jj:
                    break
            four_score.append(tot)
            tot = -1
            for jj in range(j, n_col):
                tot += 1
                if tree_map[i][jj] >= h_tree and j != jj:
                    break
            four_score.append(tot)
            scores[i][j] = four_score
    total_scores = [
        reduce(lambda x, y: x * y, four_score, 1)
        for row in scores
        for four_score in row
    ]
    return max(total_scores)


if __name__ == "__main__":
    tree_map = process_input(TEST.split("\n"))
    # print(tree_map)
    vis_map = get_visible_map(tree_map)
    # print(vis_map)
    assert num_trees_visible(vis_map) == 21
    assert max_scenic_score(tree_map) == 8

    tree_map = process_input(get_input(8))
    vis_map = get_visible_map(tree_map)
    print(num_trees_visible(vis_map))
    print(max_scenic_score(tree_map))
