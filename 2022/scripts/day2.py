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


def rps() -> int:
    score = 0
    for row in get_input(2):
        opponent, you = row.split()
        score += SCORES[opponent, you]
    return score


if __name__ == "__main__":
    print(rps())
