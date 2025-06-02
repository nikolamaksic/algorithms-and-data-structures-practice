class Solution:
    def checkRow(self, row):
        digits = set()
        for c in self.board[row]:
            if c in digits:
                return False
            if c!=".":
                digits.add(c)
        return True

    def checkCol(self, col):
        digits = set()
        for i in range(9):
            c = self.board[i][col]
            if c in digits:
                return False
            if c!=".":
                digits.add(c)
        return True

    def check3x3(self, startI, startJ):
        digits = set()
        for i in range(startI, startI+3):
            for j in range(startJ, startJ+3):
                c = self.board[i][j]
                if c in digits:
                    return False
                if c!=".":
                    digits.add(c)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        self.board = board
        for i in range(9):
            if not self.checkRow(i):
                return False
            if not self.checkCol(i):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.check3x3(i, j):
                    return False
                
        return True
        