# Tic-Tac-Toe using A* Algorithm
# Computer = X (goes first) | Player = O
#
# A* Formula:  f(n) = g(n) + h(n)
#   g(n) = Minimax score   → exact cost from game-tree search
#   h(n) = Heuristic score → counts lines that are one move from winning
#   f(n) = total score     → computer picks the move with highest f(n)
#
# Board layout:
#   0 | 1 | 2
#   --+---+--
#   3 | 4 | 5
#   --+---+--
#   6 | 7 | 8

# All 8 winning lines (3 rows + 3 cols + 2 diagonals)
WIN_LINES = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

# ── Print the board ───────────────────────────────────────────────────────────
def print_board(board):
    print()
    for row in range(3):
        r = row * 3
        print(f"  {board[r]} | {board[r+1]} | {board[r+2]}")
        if row < 2:
            print("  --+---+--")
    print()

# ── Check if someone has won ──────────────────────────────────────────────────
def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]          # 'X' or 'O'
    if ' ' not in board:
        return 'Draw'
    return None                      # game still on

# ── h(n): Heuristic — how close each side is to winning ──────────────────────
def heuristic(board):
    score = 0
    for a, b, c in WIN_LINES:
        line = [board[a], board[b], board[c]]
        if line.count('X') == 2 and line.count(' ') == 1:
            score += 10   # X is one step from winning → good for computer
        if line.count('O') == 2 and line.count(' ') == 1:
            score -= 10   # O is one step from winning → bad for computer
    return score

# ── g(n): Minimax — explores full game tree to score a board state ────────────
def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == 'X':    return 10 - depth   # faster win = higher score
    if result == 'O':    return depth - 10   # faster loss = lower score
    if result == 'Draw': return 0

    if is_maximizing:          # Computer (X) wants the highest score
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '   # undo move
        return best
    else:                      # Player (O) wants the lowest score
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '   # undo move
        return best

# ── A* move selection: pick move with highest f(n) = g(n) + h(n) ─────────────
def best_move(board):
    best_f    = -1000
    best_pos  = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'                      # try the move
            g = minimax(board, 0, False)         # g(n)
            h = heuristic(board)                 # h(n)
            f = g + h                            # f(n) = A* score
            board[i] = ' '                       # undo the move

            print(f"    pos {i}: g={g:+d}, h={h:+d}, f={f:+d}")

            if f > best_f:
                best_f   = f
                best_pos = i

    return best_pos

# ── Main game ─────────────────────────────────────────────────────────────────
board = [' '] * 9

print("===== TIC-TAC-TOE WITH A* =====")
print("Computer = X  |  You = O")
print_board(board)

while True:
    # Computer's turn
    print("Computer is thinking...")
    move = best_move(board)
    board[move] = 'X'
    print(f"  → Computer plays position {move}")
    print_board(board)

    result = check_winner(board)
    if result:
        print("Computer wins!" if result == 'X' else "It's a draw!")
        break

    # Player's turn
    while True:
        try:
            move = int(input("Your move (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'O'
                break
            print("Invalid or taken. Try again.")
        except ValueError:
            print("Enter a number 0-8.")

    print_board(board)

    result = check_winner(board)
    if result:
        print("You win!" if result == 'O' else "It's a draw!")
        break
# =============================================================================
# ## Summary
# This Tic-Tac-Toe AI uses A* search (f(n) = g(n) + h(n)) to pick the best
# move. The minimax() function calculates g(n) — the true cost from exploring
# the full game tree. The heuristic() function calculates h(n) — an estimate
# of how winning the position is. Combined, they guide the computer to choose
# moves that are both strategically sound and promising.
#
# ## Deep Dive
#
# ### The Game State Representation
# The board is a simple list of 9 cells, where board[0] is top-left and
# board[8] is bottom-right:
#   0 | 1 | 2
#   --+---+--
#   3 | 4 | 5
#   --+---+--
#   6 | 7 | 8
#
# WIN_LINES defines all 8 winning combinations — think of it as the rulebook.
# Every check for a winner simply checks if any of these triplets all match.
#
# ### The Heuristic h(n) — "How Good Is This Position?"
#
#   def heuristic(board):
#       score = 0
#       for a, b, c in WIN_LINES:
#           line = [board[a], board[b], board[c]]
#           if line.count('X') == 2 and line.count(' ') == 1:
#               score += 10   # X is one step from winning
#           if line.count('O') == 2 and line.count(' ') == 1:
#               score -= 10   # O is one step from winning
#       return score
#
# This is a look-ahead estimate. If X has two in a row with one empty space,
# that's worth +10 points — X is *almost* winning. If O has the same setup,
# that's -10 — danger for the computer.
#
# Real-world analogy: Think of it like a chess player glancing at the board
# and thinking "if I move my knight here, I'm threatening their queen" —
# quick estimation without calculating every line of play.
#
# ### The Minimax g(n) — "What's The True Outcome?"
#
#   def minimax(board, depth, is_maximizing):
#       if result == 'X': return 10 - depth   # faster win = higher score
#       if result == 'O': return depth - 10   # faster loss = lower score
#       if result == 'Draw': return 0
#
# This explores the complete game tree. If X wins at depth 3, the score is
# 10 - 3 = 7. If X wins at depth 5, the score is 10 - 5 = 5. The computer
# prefers faster victories.
#   Maximizing (X): Wants the highest score — picks the best child
#   Minimizing (O): Wants the lowest score — assumes opponent plays optimally
#
# Real-world analogy: This is like playing through every possible continuation
# of a chess game to see who wins. The computer simulates: "If I play here,
# and they play optimally, what happens?"
#
# ### A* Selection — Combining Both
#
#   def best_move(board):
#       for i in range(9):
#           if board[i] == ' ':
#               board[i] = 'X'
#               g = minimax(board, 0, False)   # true cost from minimax
#               h = heuristic(board)           # estimated cost
#               f = g + h                      # A* score
#               board[i] = ' '                 # undo
#
# The key insight: g(n) is the ground truth from exhaustive search, while
# h(n) is a quick heuristic. Together:
#   f > 0  → position favors computer
#   f < 0  → position favors player
#   Higher f → better move for computer
#
# This makes the AI play strategically (it avoids positions that lead to
# guaranteed loss) while also being opportunistic (it seizes near-winning
# setups flagged by the heuristic).
#
# ### Example Trace
# Imagine the computer evaluates position 4 (center):
#   X | X | O
#   --+---+--
#   O | X |
#   --+---+--
#   O |   |
#
#   g = +8  (minimax finds winning line for X)
#   h = +10 (X has 2 in row 0, ready to win)
#   f = +18 ← Best move!
#
# The computer plays center, threatens the win, and forces the player to
# block — demonstrating how A* combines "what will happen" with "how good
# this looks right now."
# =============================================================================
# PROGRAM: Tic-Tac-Toe using A* Algorithm (with Minimax)
# =============================================================================
#
# THEORY:
# -------
# A* Algorithm:
#   - A* is an informed search algorithm that finds the optimal path.
#   - It uses the evaluation function: f(n) = g(n) + h(n)
#       g(n) = actual cost from start to current node (Minimax score here)
#       h(n) = heuristic estimate from current node to goal
#       f(n) = total estimated cost (used to pick the best move)
#   - A* always picks the node with the LOWEST f(n) (or HIGHEST in maximizing).
#
# MINIMAX Algorithm:
#   - A backtracking algorithm used in two-player games.
#   - Maximizer (X = Computer) tries to MAXIMIZE the score.
#   - Minimizer (O = Player) tries to MINIMIZE the score.
#   - Explores all possible moves recursively to find the best one.
#
# HOW A* IS APPLIED HERE:
#   - g(n) = Minimax score (exact game-tree evaluation)
#   - h(n) = Heuristic score (counts near-winning lines)
#   - f(n) = g(n) + h(n) → Computer picks move with highest f(n)
#
# BOARD POSITIONS:
#   0 | 1 | 2
#   ---------
#   3 | 4 | 5
#   ---------
#   6 | 7 | 8
#
# WINNING COMBINATIONS (8 total):
#   Rows    : [0,1,2], [3,4,5], [6,7,8]
#   Columns : [0,3,6], [1,4,7], [2,5,8]
#   Diagonals: [0,4,8], [2,4,6]
#
# =============================================================================
# COMPLEXITY:
#   Minimax Time Complexity : O(b^d) — b=branching factor(9), d=depth(9)
#   Space Complexity        : O(d)   — recursion depth
#   With A* heuristic, pruning reduces unnecessary exploration.
# =============================================================================
#
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is the A* algorithm?
# A1. A* is an informed search algorithm that finds the optimal path using:
#     f(n) = g(n) + h(n)
#     g(n) = cost from start to current node
#     h(n) = heuristic estimate to goal
#     f(n) = total estimated cost
#
# Q2. What is the difference between A* and Minimax?
# A2. Minimax explores ALL possible game states to find the best move (brute force).
#     A* uses a heuristic h(n) to guide the search more efficiently.
#     Here, A* = Minimax (g) + Heuristic (h) combined.
#
# Q3. What is the Minimax algorithm?
# A3. Minimax is a decision-making algorithm for two-player games.
#     - Maximizer (X/Computer) tries to MAXIMIZE the score.
#     - Minimizer (O/Player) tries to MINIMIZE the score.
#     It recursively evaluates all possible moves and picks the best one.
#
# Q4. What does the heuristic function calculate here?
# A4. It counts near-winning lines:
#     - If a line has 2 X's and 1 empty → score += 10 (X is close to winning)
#     - If a line has 2 O's and 1 empty → score -= 10 (O is close to winning)
#     This guides the computer to prefer positions closer to winning.
#
# Q5. What is g(n), h(n), and f(n) in this program?
# A5. g(n) = Minimax score (exact evaluation of game tree)
#     h(n) = Heuristic score (near-win line count)
#     f(n) = g(n) + h(n) → used to select the best move
#
# Q6. Why does Minimax return (10 - depth) for X winning?
# A6. Subtracting depth rewards FASTER wins.
#     A win in fewer moves gets a higher score than a win in more moves.
#     This makes the computer prefer quick victories.
#
# Q7. Why does Minimax return (depth - 10) for O winning?
# A7. Adding depth penalizes FASTER losses.
#     A loss in more moves gets a less negative score.
#     This makes the computer delay losses as long as possible.
#
# Q8. What is the role of the 'is_max' parameter in Minimax?
# A8. It determines whose turn it is:
#     is_max = True  → Computer's turn (X) → tries to MAXIMIZE score
#     is_max = False → Player's turn (O)   → tries to MINIMIZE score
#
# Q9. How does find_best_move() work?
# A9. It tries every available position:
#     1. Places X on that position
#     2. Calls minimax() to get g(n)
#     3. Calls heuristic() to get h(n)
#     4. Calculates f(n) = g + h
#     5. Picks the move with the highest f(n)
#     6. Undoes the move (board[move] = ' ')
#
# Q10. Why do we undo the move after evaluating it?
# A10. Because we are just SIMULATING the move to evaluate its score.
#      The actual move is only made after finding the best one.
#      This is called "backtracking".
#
# Q11. What does check_winner() return?
# A11. - 'X'    → if X has won
#      - 'O'    → if O has won
#      - 'Draw' → if board is full with no winner
#      - None   → game is still ongoing
#
# Q12. What are the 8 winning combinations in Tic-Tac-Toe?
# A12. 3 rows + 3 columns + 2 diagonals = 8 winning lines
#      Rows: [0,1,2], [3,4,5], [6,7,8]
#      Cols: [0,3,6], [1,4,7], [2,5,8]
#      Diag: [0,4,8], [2,4,6]
#
# Q13. What is the time complexity of Minimax?
# A13. O(b^d) where b = branching factor (max 9 moves), d = depth (max 9).
#      Worst case = 9! = 362880 states. Manageable for Tic-Tac-Toe.
#
# Q14. Is this A* implementation admissible?
# A14. The heuristic h(n) here is not strictly admissible (it can overestimate),
#      but it works well in practice for guiding the computer to better moves.
#
# Q15. What is the difference between informed and uninformed search?
# A15. Uninformed (Blind): No knowledge of goal — BFS, DFS, UCS
#      Informed: Uses heuristic to guide search — A*, Greedy, Best-First
#
# Q16. Can the computer ever lose in this implementation?
# A16. No. With perfect Minimax, the computer will always win or draw.
#      It never makes a suboptimal move.
#
# Q17. What is backtracking in this context?
# A17. After simulating a move and evaluating it, the move is undone
#      (board[move] = ' '). This allows exploring all possibilities
#      without permanently changing the board state.
#
# Q18. What is the role of 'depth' in Minimax?
# A18. Depth tracks how many moves deep we are in the game tree.
#      It is used to prefer faster wins (10 - depth) and delay losses (depth - 10).
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   A* formula?              → f(n) = g(n) + h(n)
#   g(n) here?               → Minimax score
#   h(n) here?               → Heuristic (near-win line count)
#   Computer plays as?       → X (Maximizer)
#   Player plays as?         → O (Minimizer)
#   Winning combos?          → 8 (3 rows + 3 cols + 2 diagonals)
#   Minimax time complexity? → O(b^d) = O(9^9) worst case
#   Can computer lose?       → No, Minimax is optimal
#   Backtracking used?       → Yes, board[move] = ' ' undoes the move
#   Board size?              → 3x3 = 9 positions (indexed 0-8)
# =============================================================================1
