# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>


def main():
    increased = -1
    prevsum = 0
    with open("input.txt") as f:
        numbers = list(map(int, f))
    for i, number in enumerate(numbers[2:], 2):
        currentsum = number + numbers[i - 1] + numbers[i - 2]
        if currentsum > prevsum:
            increased += 1
        prevsum = currentsum
    print(increased)


if __name__ == "__main__":
    main()
