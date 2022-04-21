from __future__ import annotations


class Player(object):
    name: str
    color: str
    wallet: float
    bet: float

    def __init__(self, name: str, wallet: float):
        self.name = name
        self.wallet = wallet
        self.bet = 0

    def setColor(self, newColor: str):
        if(newColor == "R" or newColor == "Y"):
            self.color = newColor
            return True
        else:
            print("Please pick 'R' or 'Y'")
            return False

    def setWalletWin(self, settlement: float):
        self.wallet = self.wallet + (2 * settlement)
