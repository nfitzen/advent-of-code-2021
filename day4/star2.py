# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

import itertools
import math
from typing import Iterable, Optional, Union

Board = list[list[int]]


def main():
    with open("input.txt") as f:
        data = f.readlines()

    nums_called = [int(i) for i in data[0].strip().split(",")]
    board_data = data[2:]

    boards = [[]]
    for line in board_data:
        if line == "\n":
            boards.append([])
            continue
        boards[-1].append([int(l) for l in line.split()])

    # pick a winner

    worst_game = (0, 0, []) # this is kinda stupid
    for board in boards:
        current_game = play_bingo(board, nums_called)
        if current_game[0] > worst_game[0]:
            worst_game = current_game

    print(worst_game)

    total = 0
    for row in worst_game[2]:
        total += sum(i for i in row if i is not None)
    print(total * worst_game[1])




def play_bingo(board: Board, numbers: Iterable[int]) -> tuple[int, int, Board]:
    """Returns the number required to win Bingo."""

    current_board = board.copy() # type: ignore

    for index, num in enumerate(numbers):
        # Mark number on board
        for i, row in enumerate(board):
            for j, entry in enumerate(row):
                if entry == num:
                    current_board[i][j] = None # type: ignore
                    break

        # Check if a row or column is 5 in a row
        for units in (current_board, zip(*current_board)):
            for row in units:
                if all(e is None for e in row):
                    return (index, num, current_board)

    raise Exception("wtf")


if __name__ == "__main__":
    main()
