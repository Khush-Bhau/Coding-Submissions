class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        # Sets to keep track of occupied constraints
        col_set = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        def backtrack(r):
            # Base Case: If we've placed queens in all rows (0 to n-1)
            if r == n:
                # Convert the board list of lists to list of strings
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try every column in the current row 'r'
            for c in range(n):
                # Check if the current position is under attack
                if c in col_set or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place Queen
                col_set.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # Recurse to next row
                backtrack(r + 1)

                # Backtrack (Remove Queen to explore other possibilities)
                col_set.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res