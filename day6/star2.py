#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

Fishes = list[int]


def run_one_day(fish: Fishes, start_time: int = 6) -> Fishes:
    """Runs one day of lanternfish reproducing."""

    new_fish = fish.copy()

    cycled = new_fish[0]

    new_fish.append(new_fish.pop(0))

    new_fish[start_time] += cycled

    return new_fish


def main():
    with open("input.txt") as f:
        data = [int(i) for i in f.readline().split(",")]

    fish: Fishes = [0]*9
    for i in data:
        fish[i] += 1

    for _ in range(256):
        print(fish)
        fish = run_one_day(fish)

    print(sum(fish))


if __name__ == "__main__":
    main()
