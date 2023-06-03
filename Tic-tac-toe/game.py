class TicTacToe:
    def __init__(self):
        self.board = [ '' for i in range(9)]
        self.currentWinner = None
    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
       
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def printBoardNums():
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
             print(' | ' + ' | '.join(row) + ' | ')
        


