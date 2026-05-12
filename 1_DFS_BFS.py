
def dfs(visited, graph, node):
    # Base case: if node already visited, skip it
    if node not in visited:
        print(node, end=" ")
        visited.add(node)           # Mark node as visited
        if node in graph:           # Check if node has neighbours
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)  # Recurse for each neighbour


def bfs(visited, graph, node, queue):
    visited.add(node)       # Mark start node as visited
    queue.append(node)      # Enqueue start node

    while queue:
        s = queue.pop(0)    # Dequeue front element (FIFO)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)      # Mark as visited before enqueue
                queue.append(neighbour)     # Enqueue unvisited neighbour


def main():
    visited1 = set()  # To keep track of DFS visited nodes
    visited2 = set()  # To keep track of BFS visited nodes
    queue = []        # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1, edges + 1):
            node = int(input("Enter edge {} for node {} : ".format(j, i)))
            graph[i].append(node)

    print("The following is DFS")
    dfs(visited1, graph, 1)
    print()
    print("The following is BFS")
    bfs(visited2, graph, 1, queue)


if __name__ == "__main__":
    main()


# =============================================================================
# PROBLEM STATEMENT:
# =============================================================================
# Implement Depth First Search (DFS) and Breadth First Search (BFS) traversal
# on a given graph represented as an adjacency list. Accept the graph from the
# user (number of nodes and edges), perform both traversals starting from node 1,
# and display the order in which nodes are visited by each algorithm.
# Compare the traversal order to understand the difference between DFS
# (depth-wise, uses stack/recursion) and BFS (level-wise, uses queue).
# =============================================================================

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

# =============================================================================
# PROGRAM: Depth First Search (DFS) and Breadth First Search (BFS)
# =============================================================================
#
# THEORY:
# -------
# DFS (Depth First Search):
#   - Explores as deep as possible along each branch before backtracking.
#   - Uses a STACK data structure (here implemented via RECURSION).
#   - Visits nodes in a depth-wise manner.
#
# BFS (Breadth First Search):
#   - Explores all neighbors at the current level before going deeper.
#   - Uses a QUEUE data structure (FIFO - First In First Out).
#   - Visits nodes level by level.
#
# GRAPH REPRESENTATION:
#   - Adjacency List using Python Dictionary.
#   - Space efficient for sparse graphs: O(V + E)
#
# =============================================================================
# COMPLEXITY:
#   Time  Complexity : O(V + E)  -- V = Vertices, E = Edges (for both DFS & BFS)
#   Space Complexity : O(V)      -- for visited set + stack/queue
# =============================================================================
#
# KEY DIFFERENCES:
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
#
# EXAMPLE GRAPH:
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
#
#   DFS Output → 1 2 4 5 3 6 7   (goes deep first)
#   BFS Output → 1 2 3 4 5 6 7   (goes level by level)
#
# =============================================================================
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is DFS?
# A1. DFS (Depth First Search) is a graph traversal algorithm that explores
#     as far as possible along each branch before backtracking.
#     It uses a STACK (or recursion).
#
# Q2. What is BFS?
# A2. BFS (Breadth First Search) is a graph traversal algorithm that explores
#     all neighbors at the current depth before moving to the next level.
#     It uses a QUEUE.
#
# Q3. What data structure does DFS use?
# A3. Stack — in this code, recursion is used which internally uses the call stack.
#
# Q4. What data structure does BFS use?
# A4. Queue (FIFO) — in this code, a Python list is used with append() and pop(0).
#
# Q5. What is the role of the 'visited' set?
# A5. It tracks already-explored nodes to prevent revisiting them and
#     avoid infinite loops in cyclic graphs.
#
# Q6. Why are two separate visited sets used (visited1 and visited2)?
# A6. Because DFS and BFS run one after another on the same graph.
#     Separate sets ensure BFS starts fresh and is not affected by DFS traversal.
#
# Q7. What does queue.pop(0) do in BFS?
# A7. It removes and returns the FIRST element of the list, simulating
#     FIFO (First In First Out) queue behavior — essential for BFS.
#
# Q8. Is queue.pop(0) efficient?
# A8. No. pop(0) on a Python list is O(n) because all elements shift.
#     Better to use collections.deque with popleft() which is O(1).
#
# Q9. What is the time complexity of DFS and BFS?
# A9. Both have O(V + E) time complexity.
#     V = number of vertices, E = number of edges.
#
# Q10. Can this code handle disconnected graphs?
# A10. No. It starts only from node 1. Nodes not reachable from node 1
#      will not be visited. To handle disconnected graphs, loop over all
#      nodes and call DFS/BFS for each unvisited node.
#
# Q11. What happens if a node has no edges in DFS?
# A11. The 'if node in graph' check prevents a KeyError.
#      If the node has no entry in the graph dictionary, recursion stops there.
#
# Q12. What is the graph representation used here?
# A12. Adjacency List using a Python dictionary.
#      It is space-efficient for sparse graphs: O(V + E) space.
#
# Q13. Does BFS find the shortest path?
# A13. Yes, BFS finds the shortest path in UNWEIGHTED graphs.
#      DFS does NOT guarantee the shortest path.
#
# Q14. What are real-world applications of DFS?
# A14. - Maze solving
#      - Topological sorting
#      - Cycle detection
#      - Finding connected components
#      - Solving puzzles (Sudoku, N-Queens)
#
# Q15. What are real-world applications of BFS?
# A15. - Shortest path in GPS/maps (unweighted)
#      - Social network friend suggestions
#      - Web crawlers
#      - Level-order tree traversal
#      - Network broadcasting
#
# Q16. What is the difference between a tree and a graph?
# A16. A tree is a special case of graph with no cycles and N-1 edges for N nodes.
#      A graph can have cycles and any number of edges.
#
# Q17. What is an adjacency list vs adjacency matrix?
# A17. Adjacency List: Dictionary/list of neighbors — O(V+E) space, good for sparse graphs.
#      Adjacency Matrix: 2D array — O(V^2) space, good for dense graphs.
#
# Q18. What is backtracking in DFS?
# A18. When DFS reaches a node with no unvisited neighbors, it returns (backtracks)
#      to the previous node and explores other branches.
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   DFS uses?              → Stack / Recursion
#   BFS uses?              → Queue
#   visited set purpose?   → Avoid revisiting nodes / prevent infinite loops
#   Graph representation?  → Adjacency List (dictionary)
#   Starting node?         → Node 1 (hardcoded)
#   BFS shortest path?     → Yes, in unweighted graphs
#   DFS shortest path?     → No
#   Time complexity?       → O(V + E) for both
#   Space complexity?      → O(V) for both
# =============================================================================
