# N-Queens Problem — Branch and Bound
# Place N queens on N×N board so no two queens attack each other.
# Branch & Bound: use sets for O(1) conflict checks instead of O(N) loops.
# Bounding: if col/diagonal already attacked → prune that branch immediately.

# ── Print Board ───────────────────────────────────────────────────────────────
def print_board(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

# ── Branch and Bound Solver ───────────────────────────────────────────────────
# columns : set of columns already occupied
# diag1   : set of (row - col) values  → tracks \ diagonals
# diag2   : set of (row + col) values  → tracks / diagonals
def solve(board, row, n, columns, diag1, diag2):
    if row == n:          # all queens placed → solution found
        return True

    for col in range(n):
        # BOUND: skip if column or either diagonal is already under attack
        if col in columns or (row - col) in diag1 or (row + col) in diag2:
            continue      # prune this branch

        # BRANCH: place queen and mark constraints
        board[row][col] = 1
        columns.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        if solve(board, row + 1, n, columns, diag1, diag2):
            return True

        # BACKTRACK: remove queen and unmark constraints
        board[row][col] = 0
        columns.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    return False   # no column worked in this row

# ── Main ──────────────────────────────────────────────────────────────────────
# Sample Input : 4
# Expected Output:
#   . Q . .
#   . . . Q
#   Q . . .
#   . . Q .

n       = int(input("Enter value of N: "))
board   = [[0] * n for _ in range(n)]
columns = set()   # attacked columns
diag1   = set()   # attacked \ diagonals  (row - col)
diag2   = set()   # attacked / diagonals  (row + col)

if solve(board, 0, n, columns, diag1, diag2):
    print_board(board, n)
else:
    print("Solution does not exist")

# =============================================================================
# THEORY:
# -------
# Branch and Bound:
#   - BRANCH: generate child nodes (try each column for current row).
#   - BOUND:  use a bounding function to prune branches that cannot
#             lead to a valid solution — here, O(1) set lookups replace
#             O(N) loops used in plain Backtracking.
#
# Three sets track attacked positions:
#   columns : col already has a queen
#   diag1   : (row - col) is constant along a \ diagonal
#   diag2   : (row + col) is constant along a / diagonal
#
# If any of the 3 sets contains the current position → prune immediately.
#
# COMPLEXITY:
#   Time  : O(N!) worst case, but pruning is faster than plain Backtracking
#           because conflict checks are O(1) via sets instead of O(N) loops.
#   Space : O(N²) board + O(N) for sets + O(N) recursion stack
#
# =============================================================================
# ORAL EXAM Q&A:
# =============================================================================
#
# Q1. What is Branch and Bound?
# A1. An algorithm design technique that:
#     - BRANCHES: explores child nodes (possible placements).
#     - BOUNDS: uses a bounding function to prune branches that
#       cannot lead to a valid/optimal solution, saving time.
#
# Q2. What is the bounding function here?
# A2. The three sets — columns, diag1, diag2.
#     Before placing a queen, we check in O(1) if the position is already
#     under attack. If yes, we skip (prune) that entire branch.
#
# Q3. How does diag1 (row - col) track diagonals?
# A3. Along a \ diagonal, (row - col) is the same for all cells.
#     e.g., cells (0,0), (1,1), (2,2) all have row-col = 0.
#     So storing row-col in a set lets us check diagonal conflicts in O(1).
#
# Q4. How does diag2 (row + col) track diagonals?
# A4. Along a / diagonal, (row + col) is the same for all cells.
#     e.g., cells (0,2), (1,1), (2,0) all have row+col = 2.
#     So storing row+col in a set lets us check anti-diagonal conflicts in O(1).
#
# Q5. What is the key difference from Backtracking?
# A5. Backtracking's is_safe() uses O(N) loops to scan for conflicts.
#     Branch & Bound uses O(1) set lookups — faster pruning.
#     Both explore the same search tree but B&B prunes more efficiently.
#
# Q6. What is the backtrack step here?
# A6. Remove queen: board[row][col] = 0
#     Unmark constraints: columns.remove(col), diag1.remove(row-col),
#                         diag2.remove(row+col)
#
# Q7. Why do we need to remove from sets when backtracking?
# A7. Because the sets represent the current state of the board.
#     When we undo a queen placement, we must also undo its constraints
#     so they don't incorrectly block future placements.
#
# Q8. What is the base case?
# A8. if row == n: return True — all N rows filled, solution found.
#
# Q9. What is the time complexity?
# A9. O(N!) worst case, same as Backtracking theoretically.
#     But in practice B&B is faster due to O(1) conflict checks.
#
# Q10. What is the space complexity?
# A10. O(N²) for the board + O(N) for each of the 3 sets + O(N) stack.
#
# Q11. How many solutions for N=4 and N=8?
# A11. N=4 → 2 solutions.  N=8 → 92 solutions.
#
# Q12. What is the difference between Backtracking and Branch & Bound?
# A12. Backtracking: conflict check is O(N) — scans rows/diagonals with loops.
#      Branch & Bound: conflict check is O(1) — uses sets for instant lookup.
#      B&B is an optimized form of Backtracking with better bounding.
#
# Q13. Why is (row - col) used for one diagonal and (row + col) for the other?
# A13. These are mathematical properties of a chessboard:
#      \ diagonal: row - col is constant for all cells on it.
#      / diagonal: row + col is constant for all cells on it.
#      Using these as keys in a set gives O(1) diagonal conflict detection.
#
# =============================================================================
# QUICK FIRE:
#   Algorithm?               → Branch and Bound
#   Board?                   → N×N 2D list, 1=Queen, 0=Empty
#   Bounding function?       → 3 sets: columns, diag1 (row-col), diag2 (row+col)
#   Conflict check cost?     → O(1) using sets
#   Backtrack lines?         → board[row][col]=0, remove from all 3 sets
#   Base case?               → row == n
#   Time complexity?         → O(N!) worst case
#   Space complexity?        → O(N²) + O(N) sets + O(N) stack
#   Advantage over BT?       → O(1) conflict check vs O(N) in Backtracking
#   Solutions for N=8?       → 92
# =============================================================================
