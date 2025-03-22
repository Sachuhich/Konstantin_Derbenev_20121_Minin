class Solution:
    def solveSudoku(self, board): self.solve(board)
    def solve(self, board):

        for row in range(9): # Осуществляет переход
            for col in range(9):
                if board[row][col] == '.':
                    for num in [str(i) for i in range(1, 10)]:
                        f = True

                        if f: # Проверка строки
                            for i in range(9):
                                if board[row][i] == num:
                                    f=False
                                    break
                        if f: # Проверка столбца
                            for i in range(9):
                                if board[i][col] == num:
                                    f=False
                                    break
                        if f: # Проверка подсетки 3x3
                            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
                            for i in range(start_row, start_row + 3):
                                for j in range(start_col, start_col + 3):
                                    if board[i][j] == num:
                                        f=False
                                        break
                        if f:
                            board[row][col] = num
                            if sum(r.count('.') for r in board) == 0: return True

                            if self.solve(board): return True

                            else: board[row][col] = '.'
                    return False

if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    res_board = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                 ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                 ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                 ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                 ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                 ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                 ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                 ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                 ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    Solution().solveSudoku(board)
    assert res_board == board
    print("Passed")