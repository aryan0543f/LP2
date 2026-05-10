
def print_board(board):
    # Prints the 3x3 Tic-Tac-Toe board
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")


def check_winner(board):
    # All 8 possible winning combinations
    wins = [[0,1,2], [3,4,5], [6,7,8],   # rows
            [0,3,6], [1,4,7], [2,5,8],   # columns
            [0,4,8], [2,4,6]]             # diagonals

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != ' ':
            return board[w[0]]  # Return winner ('X' or 'O')

    if ' ' not in board:
        return 'Draw'   # Board full, no winner
    return None         # Game still ongoing


def heuristic(board):
    # h(n): counts near-winning lines to estimate board advantage
    score = 0
    wins = [[0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]

    for w in wins:
        line = [board[w[0]], board[w[1]], board[w[2]]]
        if line.count('X') == 2 and line.count(' ') == 1:
            score += 10     # X is one move away from winning
        elif line.count('O') == 2 and line.count(' ') == 1:
            score -= 10     # O is one move away from winning
    return score


def get_moves(board):
    # Returns list of all empty positions on the board
    return [i for i in range(9) if board[i] == ' ']


def minimax(board, depth, is_max):
    # Base cases: check if game is over
    winner = check_winner(board)

    if winner == 'X':
        return 10 - depth   # X wins: prefer faster wins
    elif winner == 'O':
        return depth - 10   # O wins: prefer slower losses
    elif winner == 'Draw':
        return 0            # Draw: neutral score

    if is_max:
        # Computer's turn (X) — maximize score
        best = -1000
        for move in get_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False)
            board[move] = ' '   # Undo move (backtrack)
            best = max(best, score)
        return best
    else:
        # Player's turn (O) — minimize score
        best = 1000
        for move in get_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True)
            board[move] = ' '   # Undo move (backtrack)
            best = min(best, score)
        return best


def find_best_move(board):
    # A* move selection: f(n) = g(n) + h(n)
    best_score = -1000
    best_move = None

    for move in get_moves(board):
        board[move] = 'X'
        score = minimax(board, 0, False)    # g(n) = minimax score
        h = heuristic(board)                # h(n) = heuristic score
        f = score + h                       # f(n) = g(n) + h(n)  ← A* formula
        board[move] = ' '                   # Undo move (backtrack)

        print(f"Position {move}: g={score}, h={h}, f={f}")

        if f > best_score:
            best_score = f
            best_move = move

    return best_move


# =============================================================================
# MAIN GAME LOOP
# =============================================================================
board = [' '] * 9   # Empty 3x3 board
print("Tic-Tac-Toe with A* Algorithm")
print("Positions: 0-8 (left to right, top to bottom)")
print_board(board)

while True:
    winner = check_winner(board)
    if winner:
        print(f"Result: {winner}")
        break

    # Computer's turn (X) — uses A* to find best move
    print("Computer's turn (X):")
    move = find_best_move(board)
    board[move] = 'X'
    print(f"Computer chose position {move}")
    print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"Result: {winner}")
        break

    # Player's turn (O) — manual input
    while True:
        try:
            move = int(input("Your turn (O), enter position (0-8): "))
            if board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("Position taken!")
        except:
            print("Invalid input!")

    print_board(board)
    

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
