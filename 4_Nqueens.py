
def issafe(arr, x, y, n):
    # Check 1: Column attack — scan all rows above in same column
    for row in range(x):
        if arr[row][y] == 1:
            return False    # Queen found in same column → not safe

    # Check 2: Upper-left diagonal attack (↖)
    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False    # Queen found on upper-left diagonal → not safe
        row -= 1
        col -= 1

    # Check 3: Upper-right diagonal attack (↗)
    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False    # Queen found on upper-right diagonal → not safe
        row -= 1
        col += 1

    return True     # No attacks found → position is safe


def nQueen(arr, x, n):
    # Base case: all N queens placed successfully (one per row)
    if x >= n:
        return True

    # Try placing queen in each column of current row x
    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 1             # Place queen at (x, col)
            if nQueen(arr, x + 1, n):   # Recurse for next row
                return True
            arr[x][col] = 0             # BACKTRACK: remove queen, try next col

    return False    # No valid column found in this row → backtrack


def main():
    n = int(input("Enter number of Queens : "))
    arr = [[0] * n for i in range(n)]   # Initialize N×N board with 0s

    if nQueen(arr, 0, n):
        # Print the board: 1 = Queen, 0 = Empty
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
            print()
    else:
        print("No solution exists for N =", n)


if __name__ == '__main__':
    main()


# SAMPLE OUTPUT (N=4):
# --------------------
# Enter number of Queens : 4
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0
#
# Board visualization:
#   . Q . .
#   . . . Q
#   Q . . .
#   . . Q .
#
# Explanation:
#   Row 0: Queen at column 1
#   Row 1: Queen at column 3
#   Row 2: Queen at column 0
#   Row 3: Queen at column 2
#   → No two queens share a row, column, or diagonal ✓
# =============================================================================
# PROGRAM: N-Queens Problem using Backtracking
# =============================================================================
#
# THEORY:
# -------
# N-Queens Problem:
#   - Place N queens on an N×N chessboard such that NO two queens attack each other.
#   - A queen can attack in 3 directions: same ROW, same COLUMN, same DIAGONAL.
#   - Goal: Find a valid arrangement where all N queens are safe.
#
# Backtracking:
#   - A general algorithm for finding solutions by trying partial solutions
#     and abandoning them ("backtracking") if they cannot lead to a valid solution.
#   - It is essentially DFS with pruning.
#   - Steps:
#       1. Place a queen in a row, column by column.
#       2. Check if placement is safe (issafe).
#       3. If safe → move to next row (recurse).
#       4. If not safe OR no solution found → remove queen (backtrack).
#       5. Try next column in the same row.
#
# SAFETY CHECKS (issafe function):
#   1. Column Check    : No queen in the same column above current row.
#   2. Diagonal Check  : No queen on the upper-left diagonal (↖).
#   3. Anti-Diagonal   : No queen on the upper-right diagonal (↗).
#   NOTE: Row check is NOT needed because we place exactly ONE queen per row.
#
# BOARD REPRESENTATION:
#   - 2D list (n×n) initialized with 0s.
#   - 1 = Queen placed, 0 = Empty cell.
#   - Example for 4-Queens solution:
#       0 1 0 0
#       0 0 0 1
#       1 0 0 0
#       0 0 1 0
#
# =============================================================================
# COMPLEXITY:
#   Time Complexity  : O(N!)  — worst case tries N × (N-1) × (N-2) × ... × 1
#   Space Complexity : O(N²)  — for the N×N board
#                    + O(N)   — recursion stack depth (one call per row)
# =============================================================================
#
# NUMBER OF SOLUTIONS:
#   N=1 → 1 solution
#   N=2 → 0 solutions
#   N=3 → 0 solutions
#   N=4 → 2 solutions
#   N=5 → 10 solutions
#   N=8 → 92 solutions  (classic 8-Queens problem)
#
# =============================================================================
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is the N-Queens problem?
# A1. Place N queens on an N×N chessboard such that no two queens attack
#     each other — no two queens share the same row, column, or diagonal.
#
# Q2. What algorithm is used to solve N-Queens here?
# A2. Backtracking — a recursive algorithm that tries placing queens row by row,
#     backtracks when a conflict is found, and tries the next valid position.
#
# Q3. What is Backtracking?
# A3. Backtracking is a problem-solving technique that builds solutions
#     incrementally and abandons a path as soon as it determines the path
#     cannot lead to a valid solution. It is DFS with pruning.
#
# Q4. Why is row check not needed in issafe()?
# A4. Because we place exactly ONE queen per row (one recursive call per row).
#     So two queens can never be in the same row by design.
#
# Q5. What three checks does issafe() perform?
# A5. 1. Column Check     : No queen in the same column in rows above.
#     2. Diagonal (↖)     : No queen on upper-left diagonal.
#     3. Anti-Diagonal (↗): No queen on upper-right diagonal.
#
# Q6. How does the diagonal check work?
# A6. Starting from (x, y), move up-left: row--, col--
#     If any cell has a queen (arr[row][col] == 1) → not safe.
#     This checks the upper-left diagonal (↖ direction).
#
# Q7. How does the anti-diagonal check work?
# A7. Starting from (x, y), move up-right: row--, col++
#     If any cell has a queen (arr[row][col] == 1) → not safe.
#     This checks the upper-right diagonal (↗ direction).
#
# Q8. What does arr[x][col] = 0 do in nQueen()?
# A8. It REMOVES the queen from position (x, col) — this is the BACKTRACKING step.
#     When no solution is found from the current placement, we undo it and
#     try the next column.
#
# Q9. What is the base case of the nQueen() recursion?
# A9. if x >= n: return True
#     When x equals n, all N queens have been successfully placed
#     (one in each row 0 to n-1), so a solution is found.
#
# Q10. What is the time complexity of N-Queens?
# A10. O(N!) in the worst case — for each row we try up to N columns,
#      but with backtracking many branches are pruned early.
#
# Q11. What is the space complexity?
# A11. O(N²) for the board + O(N) for the recursion stack (depth = N rows).
#
# Q12. How many solutions exist for 8-Queens?
# A12. 92 distinct solutions exist for the classic 8-Queens problem.
#
# Q13. What is the difference between Backtracking and Brute Force?
# A13. Brute Force tries ALL possible combinations without any pruning.
#      Backtracking prunes invalid branches early using constraint checks
#      (issafe), making it much more efficient.
#
# Q14. What is the difference between Backtracking and Dynamic Programming?
# A14. Backtracking: Explores all possibilities, backtracks on failure.
#                    Used for constraint satisfaction problems.
#      Dynamic Programming: Stores subproblem results to avoid recomputation.
#                           Used for optimization problems.
#
# Q15. Can this code find ALL solutions or just one?
# A15. This code finds only the FIRST valid solution and returns True.
#      To find all solutions, remove the early return and collect all valid boards.
#
# Q16. What are real-world applications of N-Queens / Backtracking?
# A16. - Constraint satisfaction problems (scheduling, timetabling)
#      - Sudoku solver
#      - Graph coloring
#      - Crossword puzzle generation
#      - Resource allocation problems
#
# Q17. Why do we only check rows ABOVE the current row in issafe()?
# A17. Because queens are placed row by row from top to bottom.
#      Rows below the current row are still empty, so no conflict is possible there.
#
# Q18. What happens when nQueen() returns False?
# A18. It means no valid column exists in the current row for any placement.
#      The function returns False, triggering backtracking in the previous row —
#      the queen placed there is removed and the next column is tried.
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   Algorithm used?          → Backtracking
#   Board representation?    → 2D list (N×N), 1=Queen, 0=Empty
#   Safety checks?           → Column, Diagonal (↖), Anti-Diagonal (↗)
#   Why no row check?        → One queen placed per row by design
#   Base case?               → x >= n (all rows filled)
#   Backtrack step?          → arr[x][col] = 0 (remove queen)
#   Time complexity?         → O(N!)
#   Space complexity?        → O(N²) board + O(N) stack
#   Solutions for N=8?       → 92
#   Solutions for N=4?       → 2
#   Finds all solutions?     → No, only the first one
# =============================================================================