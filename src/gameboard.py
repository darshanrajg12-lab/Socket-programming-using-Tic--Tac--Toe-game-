class Board:

    def __init__(self,player2):
        self.board = [" "]*9
        self.lastMove = player2
        self.numGames = 0
        self.wins = {"X":0,"O":0}
        self.loss = {"X":0,"O":0}
        self.ties = 0

    def playMoveOnBoard(self,pos,player):

        if player == "player1":
            self.board[pos] = "O"
        else:
            self.board[pos] = "X"


    def isGameFinished(self):

        combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
        ]

        for a,b,c in combos:
            if self.board[a]==self.board[b]==self.board[c] and self.board[a]!=" ":
                return True,self.board[a]

        if " " not in self.board:
            return True,"Tie"

        return False,None


    def resetGameBoard(self):
        self.board = [" "]*9


    def recordGamePlayed(self):
        self.numGames +=1


    def computeStats(self):

        return {
        "numGames":self.numGames,
        "wins":self.wins,
        "loss":self.loss,
        "ties":self.ties
        }