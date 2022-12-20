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

def parse(rows):
    sensors = []
    for row in rows:
        pattern = "Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)"
        match = re.match(pattern, row)
        sensor_coords = int(match.group(1)), int(match.group(2))
        beacon_coords = int(match.group(3)), int(match.group(4))
        sensors.append(Sensor(sensor_coords, beacon_coords))
    return sensors

if __name__ == "__main__":
    sensors = parse(TEST.split("\n"))
    print(sensors)
    