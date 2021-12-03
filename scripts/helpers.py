import pathlib

def get_input(day: int) -> list:
    input_file = pathlib.Path(__file__).resolve().parent.parent / f"input/day{day}"
    with open(input_file, "r") as f:
        return f.readlines()
