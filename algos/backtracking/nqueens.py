import unittest

def nqueens(n: int) -> list[list[str]]:
    """return all possible results of n queens problem, 1 <= n <= 10"""
    rtn = []
    def backtrack(board, row):
        # finish when reaching the (last+1)th row (note: only valid board can reach this point because of the valid check)
        if row == n:
            rtn.append(board[:])
            return
        for col in range(n):
            if not is_valid(board, row, col):
                continue
            # place a queen at (row, col)
            board[row] = board[row][:col] + 'Q' + board[row][col+1:] 
            # go on to next row
            backtrack(board, row+1)
            # undo the placement of the queen
            board[row] = board[row][:col] + '.' + board[row][col+1:] 

    
    def is_valid(board, row, col):
        # check vertical
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # check upper-left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # check upper-right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True

    # initialize board to empty 
    board = ['.' * n for _ in range(n)]
    backtrack(board, 0)
    return rtn

class TestNQueens(unittest.TestCase):
    def test_nqueens(self):
        self.assertEqual(nqueens(4), [
            [".Q..",  # Solution 1
             "...Q",
             "Q...",
             "..Q."],
            ["..Q.",  # Solution 2
             "Q...",
             "...Q",
             ".Q.."]])
        self.assertEqual(nqueens(1), [['Q']])
        self.assertEqual(nqueens(2), [])
        self.assertEqual(nqueens(3), [])

if __name__ == "__main__":
    unittest.main()