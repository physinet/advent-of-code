import pathlib

def number_of_measurement_increases(window=1) -> int:
    input_file = pathlib.Path(__file__).resolve().parent.parent / "input/day1"
    with open(input_file, "r") as f:
        depths = [int(row) for row in f.readlines()]

    num_increases = sum(
        sum(depths[i+1:i+window+1]) > sum(depths[i:i+window]) 
        for i in range(len(depths)-window)
    )
    return num_increases

if __name__ == "__main__":
    print(number_of_measurement_increases(1))
    print(number_of_measurement_increases(3))

