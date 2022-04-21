from __future__ import annotations
from player import Player


class Board(object):
    columns: int
    rows: int
    board: list[list[str]]

    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        self.board = [[" " for x in range(self.columns)]
                      for y in range(self.rows)]

    def isBackwardDiaganalWin(self, color: str, row: int, col: int):
        for i in range(4):
            if self.board[row + 3 - i][col + i] is not color:
                return False
        return True

    def isForwardDiaganalWin(self, color: str, row: int, col: int):
        for i in range(4):
            if self.board[row + i][col + i] is not color:
                return False
        return True

    def isHorizontalWin(self, color: str, row: int, col: int):
        for i in range(4):
            if self.board[row][col + i] is not color:
                return False
        return True

    def isVerticalWin(self, color: str, row: int, col: int):
        for i in range(4):
            if self.board[row + i][col] is not color:
                return False
        return True

    def isWin(self, color: str):
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                # print(f"{row}, {col}")
                if self.isForwardDiaganalWin(color, row, col) or self.isBackwardDiaganalWin(color, row, col):
                    return True

        for row in range(self.rows):
            for col in range(self.columns - 3):
                # print(f"{row}, {col}")
                if self.isHorizontalWin(color, row, col):
                    return True

        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.isVerticalWin(color, row, col):
                    return True

        return False

    def markBoard(self, player: Player, columnChoice: int):
        columnChoice = int(columnChoice)
        for i in range(self.rows):
            if(self.board[i][columnChoice] == " "):
                self.board[i][columnChoice] = player.color
                return True
        print("Column is Full!!")
        return False

    def printBoard(self):
        print("  -- Connect 4 ----")
        for row in range(self.rows):
            print(f"{self.rows -row-1} |", end="")
            for col in range(self.columns-1):
                print(f"{self.board[self.rows - row -1][col]}|", end="")
            print()
        print("  -----------------")
        print("   ", end="")
        for col in range(self.columns-1):
            print(f"{col} ", end="")
        pass
