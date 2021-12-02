import pathlib

def part1() -> int:
    input_file = pathlib.Path(__file__).resolve().parent.parent / "input/day1"
    with open(input_file, "r") as f:
        depths = [int(row) for row in f.readlines()]
    num_increases = sum(
        depth2 > depth1 for depth1, depth2 in zip(depths, depths[1:])
    )
    return num_increases

if __name__ == "__main__":
    print(part1())

