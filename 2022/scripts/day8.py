from helpers import get_input

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


if __name__ == "__main__":
    tree_map = process_input(TEST.split("\n"))
    # print(tree_map)
    vis_map = get_visible_map(tree_map)
    # print(vis_map)
    assert num_trees_visible(vis_map) == 21

    tree_map = process_input(get_input(8))
    vis_map = get_visible_map(tree_map)
    print(num_trees_visible(vis_map))
