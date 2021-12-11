#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

from statistics import median


def sum_range(n: int) -> int:
    return n * (n + 1) // 2


def main():
    with open("input.txt") as f:
        data = sorted(int(i) for i in f.readline().split(","))

    best = 0
    best_fuel = float("inf")
    for i in range(max(data)):
        cur_fuel = sum(sum_range(abs(j - i)) for j in data)
        if cur_fuel < best_fuel:
            best = i
            best_fuel = cur_fuel

    print(best_fuel)


if __name__ == "__main__":
    main()
