import unittest
from board import Board
from player import Player
from game import Game


class TestGame(unittest.TestCase):

    # Player Unittests

    def test_setColorPlayer(self):
        player = Player("Test", 500)
        self.assertEqual(player.setColor("R"), True)

    def test_setColorPlayerFail(self):
        player = Player("Test", 500)
        self.assertEqual(player.setColor("G"), False)

    def test_setWalletWinPlayer(self):
        player = Player("Test", 500)
        player.setWalletWin(50)
        self.assertEqual(player.wallet, 600)

    # Board Unittests

    def test_isBackwardDiaganalWin(self):
        board = Board(6, 5)
        coords = [
            [0, 4, "R"],
            [1, 3, "R"],
            [2, 2, "R"],
            [3, 1, "R"],
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isBackwardDiaganalWin("R", 0, 1), True)

    def test_isBackwardDiaganalWinFail(self):
        board = Board(6, 5)
        coords = [
            [0, 4, "R"],
            [1, 3, "R"],
            [2, 2, "R"],
            [3, 1, "Y"],
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isBackwardDiaganalWin("R", 0, 1), False)

    def test_isForwardDiaganalWin(self):
        board = Board(6, 5)
        coords = [
            [0, 0, "R"],
            [1, 1, "R"],
            [2, 2, "R"],
            [3, 3, "R"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isForwardDiaganalWin("R", 0, 0), True)

    def test_isForwardDiaganalWinFail(self):
        board = Board(6, 5)
        coords = [
            [0, 0, "R"],
            [1, 1, "R"],
            [2, 2, "R"],
            [3, 3, "Y"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isForwardDiaganalWin("R", 0, 0), False)

    def test_isHorizontalWin(self):
        board = Board(6, 5)
        coords = [
            [4, 0, "R"],
            [4, 1, "R"],
            [4, 2, "R"],
            [4, 3, "R"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isHorizontalWin("R", 4, 0), True)

    def test_isHorizontalDiaganalWinFail(self):
        board = Board(6, 5)
        coords = [
            [4, 0, "R"],
            [4, 1, "R"],
            [4, 2, "R"],
            [4, 3, "Y"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isHorizontalWin("R", 4, 0), False)

    def test_isVerticalWin(self):
        board = Board(6, 5)
        coords = [
            [0, 4, "R"],
            [1, 4, "R"],
            [2, 4, "R"],
            [3, 4, "R"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isVerticalWin("R", 0, 4), True)

    def test_isVerticalWinFail(self):
        board = Board(6, 5)
        coords = [
            [0, 4, "R"],
            [1, 4, "R"],
            [2, 4, "R"],
            [3, 4, "Y"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isVerticalWin("R", 0, 4), False)

    def test_isWin(self):
        board = Board(6, 5)
        coords = [
            [0, 4, "R"],
            [1, 4, "R"],
            [2, 4, "R"],
            [3, 4, "R"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isWin("R"), True)

    def test_isWinFail(self):
        board = Board(6, 5)
        coords = [
            [0, 4, "R"],
            [1, 4, "R"],
            [2, 4, "R"],
            [3, 4, "Y"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color
        self.assertEqual(board.isWin("R"), False)

    # Board Player Integration Tests

    def test_markBoard(self):
        player = Player("Test", 500)
        board = Board(6, 5)

        player.setColor("R")

        self.assertEqual(board.markBoard(player, 0), True)
        self.assertEqual(board.board[0][0], "R")

    def test_markBoardFail(self):
        player = Player("Test", 500)
        board = Board(6, 5)

        player.setColor("R")
        coords = [
            [0, 4, "R"],
            [1, 4, "R"],
            [2, 4, "R"],
            [3, 4, "Y"],
            [4, 4, "Y"]
        ]

        for [row, col, color] in coords:
            board.board[row][col] = color

        self.assertEqual(board.markBoard(player, 4), False)

    # Game Player Board Integration Tests

    def test_placeBet(self):
        player1 = Player("Player 1", 500)
        player2 = Player("Player 2", 500)
        board = Board(6, 5)
        game = Game(player1, player2, board)
        self.assertAlmostEqual(game.placeBet(player1, 30), True)
        self.assertAlmostEqual(player1.wallet, 470)
        self.assertAlmostEqual(player1.bet, 30)
        pass

    def test_placeBetFail(self):
        player1 = Player("Player 1", 500)
        player2 = Player("Player 2", 500)
        board = Board(6, 5)
        game = Game(player1, player2, board)
        self.assertAlmostEqual(game.placeBet(player1, 550), False)
        self.assertAlmostEqual(player1.wallet, 500)
        self.assertAlmostEqual(player1.bet, 0)
        pass

    def test_handleWin(self):
        player1 = Player("Player 1", 500)
        player2 = Player("Player 2", 500)
        board = Board(6, 5)
        game = Game(player1, player2, board)
        game.placeBet(game.player1, 50)
        game.handleWin(game.player1)
        self.assertEqual(game.player1.wallet, 550)

    def test_handleLoss(self):
        player1 = Player("Player 1", 500)
        player2 = Player("Player 2", 500)
        board = Board(6, 5)
        game = Game(player1, player2, board)
        game.placeBet(player1, 50)
        game.handleLoss(player1)
        self.assertAlmostEqual(player1.wallet, 450)

    def test_takePlayerInput(self):
        player1 = Player("Player 1", 500)
        player2 = Player("Player 2", 500)
        board = Board(6, 5)
        player1.setColor("R")
        game = Game(player1, player2, board)
        game.takePlayerInput(player1, "0")
        self.assertEqual(game.takePlayerInput(player1, "0"), True)

    def test_takePlayerInputFail(self):
        player1 = Player("Player 1", 500)
        player2 = Player("Player 2", 500)
        board = Board(6, 5)
        player1.setColor("R")
        game = Game(player1, player2, board)
        coords = [
            [0, 4, "R"],
            [1, 4, "R"],
            [2, 4, "R"],
            [3, 4, "Y"],
            [4, 4, "Y"]
        ]

        for [row, col, color] in coords:
            game.board.board[row][col] = color

        self.assertEqual(game.takePlayerInput(player1, "4"), False)


if __name__ == "__main__":
    unittest.main()
