from helpers import get_input

TEST = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
TEST_COORDS = {
    (498, 4), 
    (498, 5), 
    (498, 6), 
    (497, 6), 
    (496, 6), 
    (503, 4), 
    (502, 4), 
    (502, 5),
    (502, 6),
    (502, 7),
    (502, 8),
    (502, 9),
    (501, 9),
    (500, 9),
    (499, 9),
    (498, 9),
    (497, 9),
    (496, 9),
    (495, 9),
    (494, 9),
}


Coordinate = tuple[int, int]

def parse(rows: list[str]) -> list[list[Coordinate]]:
    walls = []
    for row in rows:
        wall = []
        for coord in row.split(" -> "):
            x, y = coord.split(",")
            wall.append((int(x), int(y)))
        walls.append(wall)
    return walls

def build_walls(walls: list[list[Coordinate]]) -> set[Coordinate]:
    coords = set()
    for wall in walls:
        for (x1, y1), (x2, y2) in zip(wall[:-1], wall[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1, 1):
                    coords.add((x1, y))
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1, 1):
                    coords.add((x, y2))
    return coords

def abyss(sand: Coordinate, coords: set[Coordinate]) -> bool:
    return all(sand[1] > coord[1] for coord in coords)

def main(coords: set[Coordinate], source: Coordinate) -> int:
    blocked = set(coords)
    count = 0
    grain = source
    while not abyss(grain, coords):
        possible_positions = (
            (grain[0], grain[1] + 1), 
            (grain[0] - 1, grain[1] + 1), 
            (grain[0] + 1, grain[1] + 1)
        )
        for position in possible_positions:
            if position not in blocked:
                grain = position
                break
        else:
            blocked.add(grain)
            count += 1
            grain = source
    return count

def main2(coords: set[Coordinate], source: Coordinate) -> int:
    blocked = set(coords)
    floor = max(coord[1] for coord in coords) + 2
    count = 0
    grain = source
    while source not in blocked:
        possible_positions = (
            (grain[0], grain[1] + 1), 
            (grain[0] - 1, grain[1] + 1), 
            (grain[0] + 1, grain[1] + 1)
        )
        for position in possible_positions:
            if position[1] == floor - 1:
                break
            if position not in blocked:
                grain = position
                break
        else:
            blocked.add(grain)
            count += 1
            grain = source
    return count

SOURCE = (500, 0)

if __name__ == "__main__":
    walls = parse(TEST.split("\n"))
    coords = build_walls(walls)
    assert coords == TEST_COORDS
    assert main(coords, SOURCE) == 24
    assert main2(coords, SOURCE) == 93

    walls = parse(get_input(14))
    coords = build_walls(walls)
    print(main(coords, SOURCE))
    print(main2(coords, SOURCE))

    