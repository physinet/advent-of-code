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
    coords = {}
    for wall in walls:
        for (x1, y1), (x2, y2) in zip(wall[:-1], wall[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1, 1):
                    coords.add((x1, y))
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1, 1):
                    coords.add((x, y2))
    return coords

def main(coords: set[Coordinate], source: Coordinate) -> None:
    ...

if __name__ == "__main__":
    walls = parse(TEST.split("\n"))
    print(walls)
    coords = build_walls(walls)
    print(coords)
    assert coords == TEST_COORDS