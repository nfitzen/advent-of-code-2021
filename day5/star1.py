# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

# for historical preservation

from cmath import phase
from math import pi


Line = tuple[complex, complex]


def is_straight(line: Line) -> bool:
    return line[1].real == 0 or line[1].imag == 0


def main():
    parsed: list[Line] = []
    with open("input.txt") as f:
        for line in f:
            # quaternions would *obviously* help here
            coords = line.split(" -> ")
            coords1 = tuple(map(int, coords[0].split(",")))
            coords1 = coords1[0] + coords1[1] * 1j
            coords2 = tuple(map(int, coords[1].split(",")))
            coords2 = coords2[0] + coords2[1] * 1j

            parsed.append((coords1, coords2 - coords1))

    lines = parsed

    non_diagonal = [line for line in lines if is_straight(line)]

    counts = {}
    for line in non_diagonal:
        arg = phase(line[1])
        if 0 <= arg < pi/2: # to the right
            tmp = set(line[0]+i for i in range(abs(int(line[1].real)) + 1))
        elif pi/2 <= arg < pi: # upwards
            tmp = set(line[0]+i*1j for i in range(abs(int(line[1].imag)) + 1))
        elif arg == pi or arg < -pi/2:  # to the left
            tmp = set(line[0]+i*(-1) for i in range(abs(int(line[1].real)) + 1))
        elif -pi/2 <= arg < 0: # downwards
            tmp = set(line[0]+i*(-1j) for i in range(abs(int(line[1].imag)) + 1))
        else:
            raise Exception('wtf')

        for i in tmp:
            counts[i] = counts.get(i, 0) + 1

    count = 0
    for i in counts.values():
        if i > 1:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
