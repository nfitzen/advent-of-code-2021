#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>


def run_one_day(fish: list[int], start_time: int = 6, new_time: int = 8):
    """Runs one day of lanternfish reproducing."""
    fishes = fish.copy()

    for i, f in enumerate(fish):
        if f == 0:
            fishes[i] = start_time
            fishes.append(new_time)
        else:
            fishes[i] = f - 1

    return fishes


def main():
    with open("input.txt") as f:
        fish = [int(i) for i in f.readline().strip().split(",")]

    for _ in range(80):
        fish = run_one_day(fish)

    print(len(fish))


if __name__ == "__main__":
    main()
