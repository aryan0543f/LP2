# Kruskal's Algorithm — Minimum Spanning Tree (MST)
# Greedy approach: always pick the smallest edge that doesn't form a cycle

# ── 1. Find root of a vertex (with path compression) ─────────────────────────
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])   # path compression: flatten tree
    return parent[i]

# ── 2. Union: merge two components ───────────────────────────────────────────
def union(parent, x, y):
    parent[x] = y   # make root of x point to root of y

# ── 3. Kruskal's MST ──────────────────────────────────────────────────────────
def kruskal(v, edges):
    # Step 1: Sort all edges by weight (Greedy choice)
    edges.sort(key=lambda x: x[2])

    # Step 2: Initialize each vertex as its own parent
    # Use max vertex index + 1 to safely handle any vertex numbering
    max_vertex = max(max(src, dst) for src, dst, _ in edges) if edges else v - 1
    parent = list(range(max(v, max_vertex + 1)))

    result = []
    cost   = 0

    for src, dst, w in edges:
        root_u = find(parent, src)
        root_v = find(parent, dst)

        # Step 3: Add edge only if it doesn't form a cycle
        if root_u != root_v:
            result.append((src, dst, w))
            cost += w
            union(parent, root_u, root_v)

    print("\nEdges in Minimum Spanning Tree:")
    for u, v, w in result:
        print(f"  {u} -- {v}  ==  {w}")
    print(f"Minimum Cost = {cost}")

vertices = int(input("Enter number of vertices: "))
e        = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

kruskal(vertices, edges)
# =============================================================================
# PROBLEM STATEMENT:
# Given a connected, undirected, weighted graph with V vertices and E edges,
# find the Minimum Spanning Tree (MST) using Kruskal's algorithm and display
# the selected edges along with the minimum total cost.
# =============================================================================

# ── Input ─────────────────────────────────────────────────────────────────────
#
# --- Input 1: 4 vertices, 5 edges ---
#
#       10
#   0 ────── 1
#   |  \     |
#  6|   5\   |15
#   |     \  |
#   2 ────── 3
#       4
#
#   Enter number of vertices: 4
#   Enter number of edges: 5
#   Enter edges (u v weight):
#   0 1 10
#   0 2 6
#   0 3 5
#   1 3 15
#   2 3 4
#
#   Edges in Minimum Spanning Tree:
#     2 -- 3  ==  4
#     0 -- 3  ==  5
#     0 -- 1  ==  10
#   Minimum Cost = 19
#
# ------------------------------------------------------------------
#
# --- Input 2: 5 vertices, 7 edges ---
#
#       2       3
#   0 ────── 1 ────── 2
#   |      / |        |
#  6|    4/  |5      1|
#   |  /     |        |
#   3 ────── 4 ────── 2 (back to 2)
#       3
#
#   Enter number of vertices: 5
#   Enter number of edges: 7
#   Enter edges (u v weight):
#   0 1 2
#   0 3 6
#   1 2 3
#   1 3 4
#   1 4 5
#   2 4 1
#   3 4 3
#
#   Edges in Minimum Spanning Tree:
#     2 -- 4  ==  1
#     0 -- 1  ==  2
#     3 -- 4  ==  3
#     1 -- 2  ==  3
#   Minimum Cost = 9
#
# ------------------------------------------------------------------
#
# --- Input 3: 6 vertices, 8 edges ---
#
#       4       2
#   0 ────── 1 ────── 2
#   |        |      / |
#  3|       8|    5/  |6
#   |        |  /     |
#   3 ────── 4 ────── 5
#       7        9
#
#   Enter number of vertices: 6
#   Enter number of edges: 8
#   Enter edges (u v weight):
#   0 1 4
#   0 3 3
#   1 2 2
#   1 4 8
#   2 4 5
#   2 5 6
#   3 4 7
#   4 5 9
#
#   Edges in Minimum Spanning Tree:
#     1 -- 2  ==  2
#     0 -- 3  ==  3
#     0 -- 1  ==  4
#     2 -- 4  ==  5
#     2 -- 5  ==  6
#   Minimum Cost = 20
# ------------------------------------------------------------------
#
# --- Input 4: 7 vertices, 12 edges (a=0, b=1, c=2, d=3, e=4, f=5, g=6) ---
#
#   Graph from image:
#       d(3) ──2── e(4)
#      / |  \        \
#     4  1   \        10
#    /   |    \        \
#  a(0)──2──b(1)──7──c(2)
#    \       |  \       |
#     5      8   4      6
#      \     |    \     |
#      f(5)──1──g(6)────┘
#
#   Enter number of vertices: 7
#   Enter number of edges: 12
#   Enter edges (u v weight):
#   0 3 4
#   0 1 2
#   0 5 5
#   3 4 2
#   3 1 1
#   4 1 3
#   4 2 10
#   1 2 7
#   1 5 8
#   1 6 4
#   5 6 1
#   6 2 6
#
#   Edges in Minimum Spanning Tree:
#     5 -- 6  ==  1
#     3 -- 1  ==  1
#     3 -- 4  ==  2
#     0 -- 1  ==  2
#     4 -- 1  ==  3
#     1 -- 6  ==  4
#   Minimum Cost = 13
# ------------------------------------------------------------------

# =============================================================================
# THEORY:
# -------
# Minimum Spanning Tree (MST):
#   - A spanning tree of a graph that connects ALL vertices with MINIMUM total
#     edge weight and NO cycles.
#   - For a graph with V vertices, MST has exactly V-1 edges.
#
# Kruskal's Algorithm:
#   - A GREEDY algorithm that builds MST by always picking the smallest
#     available edge that does NOT form a cycle.
#   - Uses DISJOINT SET (Union-Find) data structure to detect cycles.
#
# STEPS:
#   1. Sort ALL edges by weight in ascending order.
#   2. Pick the smallest edge.
#   3. Check if adding it forms a cycle (using Union-Find).
#   4. If NO cycle → add edge to MST.
#   5. If cycle → skip the edge.
#   6. Repeat until MST has V-1 edges.
#
# DISJOINT SET (Union-Find):
#   - Data structure that tracks which vertices are in the same component.
#   - find(i)    → returns the ROOT of i's component.
#   - union(x,y) → merges two components.
#   - Path Compression → makes find() faster by flattening the tree.
#     Code: parent[i] = find(parent, parent[i])
#
# =============================================================================
# COMPLEXITY:
#   Sorting edges   : O(E log E)
#   Union-Find ops  : O(E α(V))  ← α = inverse Ackermann ≈ O(1) practically
#   Overall         : O(E log E)
#   Space           : O(V + E)
#
#   E = number of edges, V = number of vertices
# =============================================================================
#
# KRUSKAL'S vs PRIM'S:
# ┌─────────────────┬──────────────────────┬──────────────────────┐
# │ Feature         │ Kruskal's            │ Prim's               │
# ├─────────────────┼──────────────────────┼──────────────────────┤
# │ Approach        │ Edge-based (Greedy)  │ Vertex-based (Greedy)│
# │ Data Structure  │ Disjoint Set         │ Priority Queue       │
# │ Works on        │ Edge list            │ Adjacency Matrix/List│
# │ Best for        │ Sparse graphs        │ Dense graphs         │
# │ Time Complexity │ O(E log E)           │ O(V²) or O(E log V)  │
# │ Cycle Detection │ Union-Find           │ Visited array        │
# └─────────────────┴──────────────────────┴──────────────────────┘
#
# =============================================================================
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is a Minimum Spanning Tree (MST)?
# A1. A spanning tree that connects all vertices of a graph with the minimum
#     possible total edge weight and contains no cycles.
#     For V vertices, MST always has exactly V-1 edges.
#
# Q2. What is Kruskal's Algorithm?
# A2. A greedy algorithm that builds MST by:
#     1. Sorting all edges by weight (ascending).
#     2. Picking the smallest edge that does NOT form a cycle.
#     3. Repeating until V-1 edges are selected.
#
# Q3. Why is Kruskal's called a Greedy algorithm?
# A3. Because at each step it makes the locally optimal choice —
#     always picking the minimum weight edge available —
#     without reconsidering previous choices.
#
# Q4. What data structure does Kruskal's use for cycle detection?
# A4. Disjoint Set (Union-Find) data structure.
#     It efficiently checks if two vertices belong to the same component.
#     If yes → adding the edge would form a cycle → skip it.
#
# Q5. What is a Disjoint Set (Union-Find)?
# A5. A data structure that maintains a collection of disjoint sets.
#     - find(i)    → returns the root/representative of i's set.
#     - union(x,y) → merges the sets containing x and y.
#     Used to detect cycles in Kruskal's algorithm.
#
# Q6. What is Path Compression in Union-Find?
# A6. An optimization in find() that makes every node on the path
#     point directly to the root, flattening the tree.
#     This speeds up future find() calls to nearly O(1).
#     Code: parent[i] = find(parent, parent[i])
#
# Q7. How does cycle detection work?
# A7. find(u) and find(v) return the roots of u and v.
#     If root_u == root_v → same component → adding edge forms a cycle → skip.
#     If root_u != root_v → different components → safe to add → call union().
#
# Q8. What is the time complexity of Kruskal's algorithm?
# A8. O(E log E) — dominated by the edge sorting step.
#     Union-Find operations are nearly O(1) with path compression.
#
# Q9. How many edges does an MST have?
# A9. Always V-1 edges, where V is the number of vertices.
#
# Q10. What is the difference between a spanning tree and MST?
# A10. A spanning tree connects all vertices with V-1 edges (no cycles).
#      An MST is a spanning tree with the MINIMUM total edge weight.
#
# Q11. When does Kruskal's algorithm stop?
# A11. When the MST contains V-1 edges, or all edges are processed.
#
# Q12. Can Kruskal's work on disconnected graphs?
# A12. Yes. It produces a Minimum Spanning FOREST —
#      one MST per connected component.
#
# Q13. What is the difference between Kruskal's and Prim's?
# A13. Kruskal's: Edge-based, sorts all edges, uses Disjoint Set,
#                 better for SPARSE graphs. O(E log E)
#      Prim's:    Vertex-based, grows from one vertex, uses Priority Queue,
#                 better for DENSE graphs. O(V²) or O(E log V)
#
# Q14. Does Kruskal's work on directed graphs?
# A14. No. Kruskal's is designed for UNDIRECTED weighted graphs.
#
# Q15. What is the initial state of the parent array?
# A15. parent = [0, 1, 2, ..., n-1]
#      Every vertex starts as its own parent (separate component).
#
# Q16. What are real-world applications of MST / Kruskal's?
# A16. - Network design (minimum cable to connect all computers)
#      - Road/railway construction (minimum cost to connect cities)
#      - Electrical grid design
#      - Cluster analysis in machine learning
#
# Q17. What is the space complexity of Kruskal's?
# A17. O(V + E) — O(V) for the parent array, O(E) for edges and MST.
#
# Q18. What happens if two edges have the same weight?
# A18. Either can be picked — both are valid. The MST weight is always
#      unique even if the structure differs.
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   Algorithm type?          → Greedy
#   Data structure used?     → Disjoint Set (Union-Find)
#   First step?              → Sort all edges by weight (ascending)
#   Cycle detection?         → if find(u) == find(v) → cycle → skip
#   MST edges count?         → V - 1
#   Time complexity?         → O(E log E)
#   Space complexity?        → O(V + E)
#   Path compression?        → parent[i] = find(parent, parent[i])
#   Best for?                → Sparse graphs
#   Works on directed graph? → No, only undirected graphs
# =============================================================================
