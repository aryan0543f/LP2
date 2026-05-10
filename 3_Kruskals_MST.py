
class DisjointSet:
    def __init__(self, n):
        # Initially each vertex is its own parent (n separate components)
        self.parent = list(range(n))

    def find(self, x):
        # Find root of x's component with PATH COMPRESSION
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Flatten tree
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)    # Find root of x
        yroot = self.find(y)    # Find root of y
        if xroot == yroot:
            return False        # Same component → adding edge forms a CYCLE
        self.parent[yroot] = xroot  # Merge: make xroot the parent of yroot
        return True             # Successfully merged (no cycle)


def kruskal_mst(edges, n):
    # Step 1: Sort all edges by weight in ascending order (Greedy choice)
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(n)     # Initialize Disjoint Set for n vertices
    mst = []                # Stores MST edges
    total_weight = 0

    for u, v, weight in edges:
        # Step 2: Try to add edge (u, v) — union() returns False if cycle
        if ds.union(u, v):
            mst.append((u, v, weight))  # Add edge to MST
            total_weight += weight
            # Stop early if MST is complete (V-1 edges)
            if len(mst) == n - 1:
                break

    return mst, total_weight


# =============================================================================
# GRAPH DEFINITION
# =============================================================================
# Define edges as (u, v, weight) — undirected graph
edges = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 3, 7),
    (2, 8, 2),
    (2, 5, 4),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (6, 8, 6),
    (7, 8, 7),
]

n = 9   # Number of vertices (0 to 8)

mst, total_weight = kruskal_mst(edges, n)

print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")

print(f"Total weight of MST: {total_weight}")

# EXPECTED OUTPUT:
# Edges in MST:
# 6 - 7: 1
# 2 - 8: 2
# 5 - 6: 2
# 0 - 1: 4
# 2 - 5: 4
# 2 - 3: 7
# 0 - 7: 8
# Total weight of MST: 37

# =============================================================================
# PROGRAM: Kruskal's Algorithm — Minimum Spanning Tree (MST)
# =============================================================================
#
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
#   - find(x)  → returns the ROOT/representative of x's component.
#   - union(x,y) → merges two components; returns False if already same (cycle).
#   - Path Compression → makes find() faster by flattening the tree.
#
# =============================================================================
# COMPLEXITY:
#   Sorting edges      : O(E log E)
#   Union-Find ops     : O(E α(V))  ← α = inverse Ackermann ≈ O(1) practically
#   Overall            : O(E log E)
#   Space Complexity   : O(V + E)
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
# EXAMPLE GRAPH (9 vertices, 14 edges):
#   Vertices: 0 to 8
#   MST edges selected (sorted by weight):
#     6-7: 1, 2-8: 2, 5-6: 2, 0-1: 4, 2-5: 4, 2-3: 7, 0-7: 8
#   Total MST weight = 37
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
#     - find(x)   → returns the root/representative of x's set.
#     - union(x,y) → merges the sets containing x and y.
#     Used to detect cycles in Kruskal's algorithm.
#
# Q6. What is Path Compression in Union-Find?
# A6. An optimization in find() that makes every node on the path
#     point directly to the root, flattening the tree.
#     This speeds up future find() calls to nearly O(1).
#     Code: self.parent[x] = self.find(self.parent[x])
#
# Q7. How does union() detect a cycle?
# A7. If find(x) == find(y), both vertices have the SAME root,
#     meaning they are already in the same component.
#     Adding an edge between them would form a cycle → return False.
#
# Q8. What is the time complexity of Kruskal's algorithm?
# A8. O(E log E) — dominated by the edge sorting step.
#     Union-Find operations are nearly O(1) with path compression.
#     E = number of edges.
#
# Q9. How many edges does an MST have?
# A9. Always V-1 edges, where V is the number of vertices.
#     This is because a spanning tree of V nodes has exactly V-1 edges.
#
# Q10. What is the difference between a spanning tree and MST?
# A10. A spanning tree connects all vertices with V-1 edges (no cycles).
#      An MST is a spanning tree with the MINIMUM total edge weight.
#      Multiple spanning trees can exist; MST has the minimum weight.
#
# Q11. When does Kruskal's algorithm stop?
# A11. When the MST contains V-1 edges (all vertices are connected),
#      or when all edges have been processed.
#
# Q12. Can Kruskal's work on disconnected graphs?
# A12. Yes. If the graph is disconnected, Kruskal's produces a
#      Minimum Spanning FOREST — one MST for each connected component.
#
# Q13. What is the difference between Kruskal's and Prim's?
# A13. Kruskal's: Edge-based, sorts all edges, uses Disjoint Set,
#                 better for SPARSE graphs. O(E log E)
#      Prim's:    Vertex-based, grows from one vertex, uses Priority Queue,
#                 better for DENSE graphs. O(V²) or O(E log V)
#
# Q14. Does Kruskal's work on directed graphs?
# A14. No. Kruskal's is designed for UNDIRECTED weighted graphs.
#      For directed graphs, we use algorithms like Edmonds' algorithm.
#
# Q15. What is the initial state of the Disjoint Set?
# A15. Each vertex is its own parent: parent = [0, 1, 2, ..., n-1]
#      Every vertex starts as its own separate component.
#
# Q16. What are real-world applications of MST / Kruskal's?
# A16. - Network design (minimum cable to connect all computers)
#      - Road/railway construction (minimum cost to connect cities)
#      - Electrical grid design
#      - Cluster analysis in machine learning
#      - Approximation algorithms for TSP (Travelling Salesman Problem)
#
# Q17. What is the space complexity of Kruskal's?
# A17. O(V + E) — O(V) for the Disjoint Set parent array,
#      O(E) for storing edges and MST.
#
# Q18. What happens if two edges have the same weight in Kruskal's?
# A18. Either can be picked first — both are valid choices.
#      The resulting MST may differ in structure but will have the same
#      total weight (MST weight is unique even if MST structure is not).
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   Algorithm type?          → Greedy
#   Data structure used?     → Disjoint Set (Union-Find)
#   First step?              → Sort all edges by weight (ascending)
#   Cycle detection?         → Union-Find: if find(x) == find(y) → cycle
#   MST edges count?         → V - 1
#   Time complexity?         → O(E log E)
#   Space complexity?        → O(V + E)
#   Path compression?        → Optimization in find() — flattens tree
#   Best for?                → Sparse graphs
#   Works on directed graph? → No, only undirected graphs
# =============================================================================