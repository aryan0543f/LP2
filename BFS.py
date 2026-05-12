def bfs(visited, graph, node):
    queue = []
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


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

    print("BFS traversal:")
    bfs(visited, graph, 1)


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
# BFS (Breadth First Search):
#   - Explores all neighbors at the current level before going deeper.
#   - Uses a QUEUE data structure (FIFO - First In First Out).
#   - Visits nodes level by level.# COMPLEXITY:
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
# Q2. What is BFS?
# A2. BFS (Breadth First Search) is a graph traversal algorithm that explores
#     all neighbors at the current depth before moving to the next level.
#     It uses a QUEUE.
# Q4. What data structure does BFS use?
# A4. Queue (FIFO) — in this code, a Python list is used with append() and pop(0).
# Q15. What are real-world applications of BFS?
# A15. - Shortest path in GPS/maps (unweighted)
#      - Social network friend suggestions
#      - Web crawlers
#      - Level-order tree traversal
#      - Network broadcasting
#
