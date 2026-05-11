# N-Queens Problem — Backtracking
# Place N queens on N×N board so no two queens attack each other.
# Backtracking: try each column in a row, undo if it leads to no solution.

# ── Print Board ───────────────────────────────────────────────────────────────
def print_board(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

# ── Safety Check ──────────────────────────────────────────────────────────────
def is_safe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal (↖)
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal (↗)
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True   # safe to place

# ── Backtracking Solver ───────────────────────────────────────────────────────
def solve(board, row, n):
    if row == n:          # all queens placed → solution found
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1              # place queen

            if solve(board, row + 1, n):     # recurse to next row
                return True

            board[row][col] = 0              # BACKTRACK: remove queen

    return False   # no column worked in this row

# ── Main ──────────────────────────────────────────────────────────────────────
# Sample Input : 4
# Expected Output:
#   . Q . .
#   . . . Q
#   Q . . .
#   . . Q .

n     = int(input("Enter value of N: "))
board = [[0] * n for _ in range(n)]

if solve(board, 0, n):
    print_board(board, n)
else:
    print("Solution does not exist")

# =============================================================================
# THEORY:
# -------
# Backtracking:
#   - Try placing a queen in each column of the current row.
#   - If safe → place it and recurse to the next row.
#   - If recursion fails → REMOVE the queen (backtrack) and try next column.
#   - It is essentially DFS with pruning.
#
# is_safe() checks 3 things (row check not needed — one queen per row):
#   1. Same column above
#   2. Upper-left diagonal (↖)
#   3. Upper-right diagonal (↗)
#
# COMPLEXITY:
#   Time  : O(N!)  — worst case, pruned by is_safe()
#   Space : O(N²) board + O(N) recursion stack
#
# =============================================================================
# ORAL EXAM Q&A:
# =============================================================================
#
# Q1. What is the N-Queens problem?
# A1. Place N queens on an N×N board so no two queens share the same
#     row, column, or diagonal.
#
# Q2. What is Backtracking?
# A2. A recursive technique that builds a solution step by step.
#     If a step leads to a dead end, it undoes that step (backtracks)
#     and tries the next option. It is DFS with pruning.
#
# Q3. What is the backtrack step in the code?
# A3. board[row][col] = 0 — removes the queen when no solution is found
#     from that placement, so the next column can be tried.
#
# Q4. Why is there no row check in is_safe()?
# A4. Because we place exactly one queen per row (one recursive call per row),
#     so two queens can never be in the same row by design.
#
# Q5. What are the 3 checks in is_safe()?
# A5. 1. Column: scan all rows above in same column.
#     2. Upper-left diagonal (↖): move row--, col-- until out of bounds.
#     3. Upper-right diagonal (↗): move row--, col++ until out of bounds.
#
# Q6. What is the base case?
# A6. if row == n: return True — all N rows filled means all queens placed.
#
# Q7. What is the time complexity?
# A7. O(N!) worst case. Backtracking prunes many branches early via is_safe().
#
# Q8. What is the difference between Backtracking and Brute Force?
# A8. Brute Force tries all combinations without pruning.
#     Backtracking prunes invalid branches early using constraint checks,
#     making it much faster in practice.
#
# Q9. How many solutions exist for N=4 and N=8?
# A9. N=4 → 2 solutions.  N=8 → 92 solutions.
#
# Q10. Does this code find all solutions or just one?
# A10. Just the first valid solution. To find all, remove the early return
#      and collect every valid board when row == n.
#
# Q11. What is the difference between Backtracking and Branch & Bound?
# A11. Backtracking: undoes bad choices, no cost tracking.
#      Branch & Bound: uses a bounding function to prune branches that
#      cannot improve the best solution found so far. More efficient.
#      B&B uses sets for O(1) conflict checks vs Backtracking's O(N) loops.
#
# =============================================================================
# QUICK FIRE:
#   Algorithm?           → Backtracking
#   Board?               → N×N 2D list, 1=Queen, 0=Empty
#   Safety checks?       → Column, ↖ diagonal, ↗ diagonal
#   Backtrack line?      → board[row][col] = 0
#   Base case?           → row == n
#   Time complexity?     → O(N!)
#   Space complexity?    → O(N²) + O(N) stack
#   Solutions for N=8?   → 92
# =============================================================================
