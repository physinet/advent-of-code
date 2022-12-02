from helpers import get_input


def calories() -> int:
    max_calories = -1
    running_total = 0
    for row in get_input(1):
        if cals := row.strip():
            running_total += int(cals)
        else:
            max_calories = max(max_calories, running_total)
            running_total = 0

    return max_calories


if __name__ == "__main__":
    print(calories())
