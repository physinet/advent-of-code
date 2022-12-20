import re
from dataclasses import dataclass
from helpers import get_input

TEST = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

Coordinate = tuple[int, int]


@dataclass
class Sensor:
    coords: Coordinate
    closest_beacon: Coordinate


def parse(rows: list[str]) -> list[Sensor]:
    sensors = []
    for row in rows:
        pattern = "Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)"
        match = re.match(pattern, row)
        sensor_coords = int(match.group(1)), int(match.group(2))
        beacon_coords = int(match.group(3)), int(match.group(4))
        sensors.append(Sensor(sensor_coords, beacon_coords))
    return sensors


def num_coords_without_beacons(sensors: list[Sensor], row_num: int) -> set[Coordinate]:
    coords = set()
    beacons = set()
    for sensor in sensors:
        beacons.add(sensor.closest_beacon)
        distance_to_beacon = abs(sensor.coords[0] - sensor.closest_beacon[0]) + abs(
            sensor.coords[1] - sensor.closest_beacon[1]
        )
        distance_to_row = abs(sensor.coords[1] - row_num)
        remaining_distance = distance_to_beacon - distance_to_row
        for y in range(remaining_distance + 1):
            coords.add((sensor.coords[0] + y, row_num))
            coords.add((sensor.coords[0] - y, row_num))

    return len(coords - beacons)


if __name__ == "__main__":
    sensors = parse(TEST.split("\n"))
    assert num_coords_without_beacons(sensors, 10) == 26

    sensors = parse(get_input(15))
    print(num_coords_without_beacons(sensors, 2_000_000))
