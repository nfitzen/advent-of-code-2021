# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>


def main():
    with open("input.txt") as f:
        data = f.readlines()
    ones = [0] * len(data[0].strip())
    zeroes = [0] * len(data[0].strip())
    for line in data:
        for i, v in enumerate(line.strip()):
            if int(v):
                ones[i] += 1
            else:
                zeroes[i] += 1
    bitstr = ""
    for o, z in zip(ones, zeroes):
        if o > z:
            bitstr += "1"
        else:
            bitstr += "0"
    comp = bitstr.translate({ord("1"): "0", ord("0"): "1"})
    print(int(bitstr, 2) * int(comp, 2))


if __name__ == "__main__":
    main()
