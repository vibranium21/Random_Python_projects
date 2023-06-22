import random
class Player():
    def __init__(self):
        self.letter = letter
    def Move(self):
        pass
class RandomComputerPlayer(Player):
    def RandomMove(self, Legal_MovesX, Legal_MovesO):
        if self.letter == 'O':
            return random.choice(Legal_MovesO)
        if self.letter == 'X':
            return random.choice(Legal_MovesX)
class HumanPlayer(Player):
    def HumanMove():
        move = input("What Is your move? Answer with 0 for top left and 8 for the bottom right corner.")
        return move
