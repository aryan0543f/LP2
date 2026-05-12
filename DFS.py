def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        if node in graph:
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)


def main():
    visited = set()
    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    print("DFS traversal:")
    dfs(visited, graph, 1)


if __name__ == "__main__":
    main()
# SAMPLE INPUT/OUTPUT:
# --------------------
#
# --- Input 1: Binary Tree shaped graph (7 nodes) ---
# graph = {
#     1 : [2, 3],
#     2 : [4, 5],
#     3 : [6, 7],
#     4 : [],
#     5 : [],
#     6 : [],
#     7 : []
# }
#
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
#
# DFS Output : 1 2 4 5 3 6 7   (goes deep into left branch first)
# BFS Output : 1 2 3 4 5 6 7   (visits level by level)
#
# ------------------------------------------------------------------
#
# --- Input 2: Linear chain graph (5 nodes) ---
# graph = {
#     1 : [2],
#     2 : [3],
#     3 : [4],
#     4 : [5],
#     5 : []
# }
#
#   1 → 2 → 3 → 4 → 5
#
# DFS Output : 1 2 3 4 5
# BFS Output : 1 2 3 4 5
# (Both same for linear chain — no branching)
#
# ------------------------------------------------------------------
#
# --- Input 3: Graph with multiple branches (6 nodes) ---
# graph = {
#     1 : [2, 3, 4],
#     2 : [5],
#     3 : [5],
#     4 : [],
#     5 : [6],
#     6 : []
# }
#
#       1
#     / | \
#    2  3  4
#    \  /
#     5
#     |
#     6
#
# DFS Output : 1 2 5 6 3 4
# BFS Output : 1 2 3 4 5 6
# ------------------------------------------------------------------
# THEORY:
# -------
# DFS (Depth First Search):
#   - Explores as deep as possible along each branch before backtracking.
#   - Uses a STACK data structure (here implemented via RECURSION).
#   - Visits nodes in a depth-wise manner.
# COMPLEXITY:
#   Time  Complexity : O(V + E)  -- V = Vertices, E = Edges (for both DFS & BFS)
#   Space Complexity : O(V)      -- for visited set + stack/queue# KEY DIFFERENCES:
# ┌─────────────────┬──────────────────────┬──────────────────────┐
# │ Feature         │ DFS                  │ BFS                  │
# ├─────────────────┼──────────────────────┼──────────────────────┤
# │ Data Structure  │ Stack (Recursion)    │ Queue                │
# │ Traversal       │ Deep first           │ Level by level       │
# │ Shortest Path   │ No                   │ Yes (unweighted)     │
# │ Implementation  │ Recursive            │ Iterative            │
# │ Time Complexity │ O(V + E)             │ O(V + E)             │
# │ Space Complexity│ O(V)                 │ O(V)                 │
# └─────────────────┴──────────────────────┴──────────────────────┘
# =============================================================================
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is DFS?
# A1. DFS (Depth First Search) is a graph traversal algorithm that explores
#     as far as possible along each branch before backtracking.
#     It uses a STACK (or recursion).
# Q14. What are real-world applications of DFS?
# A14. - Maze solving
#      - Topological sorting
#      - Cycle detection
#      - Finding connected components
#      - Solving puzzles (Sudoku, N-Queens) Q3. What data structure does DFS use?
# A3. Stack — in this code, recursion is used which internally uses the call stack.
