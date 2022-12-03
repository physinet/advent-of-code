from helpers import get_input

SCORES = {
    ("A", "X"): 3 + 1,
    ("A", "Y"): 6 + 2,
    ("A", "Z"): 0 + 3,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 6 + 1,
    ("C", "Y"): 0 + 2,
    ("C", "Z"): 3 + 3,
}


SCORES2 = {
    ("A", "X"): 0 + 3,
    ("A", "Y"): 3 + 1,
    ("A", "Z"): 6 + 2,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 0 + 2,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 6 + 1,
}


def rps(rows, scores) -> int:
    score = 0
    for row in rows:
        score += scores[tuple(row.split())]
    return score


if __name__ == "__main__":
    print(rps(["A Y", "B X", "C Z"], SCORES))
    print(rps(get_input(2), SCORES))
    print(rps(["A Y", "B X", "C Z"], SCORES2))
    print(rps(get_input(2), SCORES2))
