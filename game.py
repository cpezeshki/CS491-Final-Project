from __future__ import annotations
from board import Board
from player import Player


class Game(object):
    player1: Player
    player2: Player
    board: Board

    def __init__(self, player1: Player, player2: Player, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def placeBet(self, player: Player, amount: float):
        if(player.wallet < amount):
            print(f"{player.name} does not have enough funds.")
            return False
        else:
            player.wallet = player.wallet - amount
            player.bet = amount
            print(f"{player.name} now has {player.wallet} avaliable")
            return True

    def handleWin(self, player: Player):
        player.setWalletWin(player.bet)
        player.bet = 0

    def handleLoss(self, player: Player):
        player.bet = 0

    def takePlayerInput(self, player: Player, playerChoice: str):
        if(playerChoice == "0" or playerChoice == "1" or playerChoice == "2" or playerChoice == "3" or playerChoice == "4"):
            if(self.board.markBoard(player, playerChoice)):
                print("Turn Successful")
                return True
        return False

    def playGame(self):
        while True:
            try:
                print(f"{player1.name} Wallet: {player1.wallet}")
                amount = float(input(
                    f"{player1.name} enter amount you would like to bet: "))
                if(game.placeBet(player1, amount)):
                    break
            except ValueError:
                continue

        while True:
            try:
                print(f"{player2.name} Wallet: {player2.wallet}")
                amount2 = float(input(
                    f"{player2.name} enter amount you would like to bet: "))
                if(game.placeBet(player2, amount2)):
                    break
            except ValueError:
                continue

        while True:
            board.printBoard()
            while True:
                playerChoice = input(
                    f"{player1.name} please select a column: ")
                if(self.takePlayerInput(player1, playerChoice)):
                    break

            if(self.board.isWin(self.player1.color)):
                print(player1.name, "Won!")
                self.handleWin(player1)
                self.handleLoss(player2)
                board.printBoard()
                break
            board.printBoard()
            while True:
                playerChoice = input(
                    f"{player2.name} please select a column: ")
                if(self.takePlayerInput(player2, playerChoice)):
                    break
            if(self.board.isWin(self.player2.color)):
                print(player2.name, "Won!")
                self.handleWin(player2)
                self.handleLoss(player1)
                board.printBoard()
                break


if __name__ == '__main__':
    print("Change")
    board = Board(6, 5)
    player1 = Player("Player 1", 500)
    player1.setColor("R")
    player2 = Player("Player 2", 500)
    player2.setColor("Y")
    game = Game(player1, player2, board)
    game.playGame()
