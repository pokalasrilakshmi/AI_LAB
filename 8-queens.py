def solve_queens(n): 
    board = [-1] * n 

    def safe(row, col): 
        for i in range(row): 
            if board[i] == col or abs(board[i] - col) == row - i: 
                return False 
        return True 

    def backtrack(row): 
        if row == n: 
            print("Solution:", board) 
            return True 

        for col in range(n): 
            if safe(row, col): 
                board[row] = col 
                if backtrack(row + 1): 
                    return True 
        return False 

    backtrack(0) 


solve_queens(8)