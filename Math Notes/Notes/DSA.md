---
title: Data Structures and Algorithms
parent: Math Notes
nav_order: 3
has_toc: true
---

# Lecture 1 — Introduction to Algorithm Analysis

## Motivation and Goals
Algorithm analysis focuses on three fundamental questions:
1. **Correctness** — Does the algorithm always produce the correct output?
2. **Efficiency** — How much time and space does the algorithm use?
3. **Optimality** — Can we design an algorithm that is asymptotically better?

In this course, we primarily care about *scalability*: how performance changes as the input size grows.

---

## Measuring Running Time

### Dependence on Input Size
Running time typically depends on input size $n$. We define:

- **Worst-case time**  
  $$T(n) = \max \{ \text{time on any input of size } n \}$$  
  This is the default notion used in CMPSC 465.

- **Average-case time**  
  Expected time over all inputs of size $n$ (requires a probability distribution).

- **Amortized time**  
  Average time per operation over a sequence of operations.

> Best-case analysis is usually not meaningful, since it can hide poor performance on most inputs.

---

## Example: Linear Search

### Problem
Input: array $A$ of size $n$, key $k$  
Output: index of $k$ if found, otherwise $-1$

### Pseudocode
```
linear-search(A, k):
  i = n - 1
  while i >= 0:
    if A[i] == k:
      return i
    i = i - 1
  return -1
```

### Worst-Case Analysis
Worst case occurs when $k$ is not in the array. The loop executes $n$ times.

Let the cost of each elementary operation be constant. Then:
$$
T(n) = an + b
$$
which implies **linear time**, written as $O(n)$.

---

## Abstract Machine Model
To compare algorithms fairly, we assume:
- A single processor
- Sequential execution
- Each elementary operation takes constant time

This abstracts away hardware and implementation details.

---

## Scalability Examples
If input size increases from $n$ to $10n$:
- $O(1)$ → same time
- $O(n)$ → 10× slower
- $O(n^2)$ → 100× slower
- $O(2^n)$ → infeasible

This motivates asymptotic analysis.

---

# Lecture 2 — Asymptotic Notation

## Big-O Notation

### Definition
For functions $f(n)$ and $g(n)$:
$$
f(n) = O(g(n))
$$
if there exist constants $c > 0$ and $n_0$ such that:
$$
f(n) \le c \cdot g(n) \quad \forall n \ge n_0.
$$

Interpretation:
- $f(n)$ grows no faster than $g(n)$ asymptotically.
- $g(n)$ is an upper bound on $f(n)$.

---

## Examples
- $10n + 7 = O(n)$
- $0.01n^2 \not= O(n)$

Even small constants cannot save a higher-degree polynomial.

---

## Why We Choose Tight Bounds
Linear search takes $an + b$ steps.
Valid upper bounds include $O(n)$, $O(n^2)$, $O(2^n)$.
We always choose the **tightest** bound: $O(n)$.

---

## Useful Properties of Big-O
- Constants don’t matter: $a f(n) = O(f(n))$
- Lower-degree polynomials are dominated by higher-degree ones
- Polynomials dominate logarithms
- Exponentials dominate polynomials
- Transitivity: if $f=O(g)$ and $g=O(h)$, then $f=O(h)$

---

# Lecture 3 — Sorting Algorithms

## The Sorting Problem
Input: $n$ numbers $a_1, a_2, \dots, a_n$  
Output: a permutation such that:
$$
a'_1 \le a'_2 \le \cdots \le a'_n
$$

---

## Insertion Sort

### Idea
Build a sorted prefix by inserting one element at a time into its correct position.

### Pseudocode
```
InsertionSort(A[1..n]):
  for i = 1 to n:
    key = A[i]
    j = i - 1
    while j > 0 and A[j] > key:
      A[j+1] = A[j]
      j = j - 1
    A[j+1] = key
```

### Correctness (Loop Invariant)
After the $k$-th iteration, $A[1..k]$ is sorted.
- Base case: $A[1]$ is sorted.
- Inductive step: inserting $A[k]$ preserves sortedness.

---

### Time Complexity
Worst case (reverse order):
$$
1 + 2 + \cdots + (n-1) = \Theta(n^2)
$$

### Space Complexity
Uses $O(1)$ extra space.

---

## Merge Sort

### Idea (Divide and Conquer)
1. Split array into halves
2. Recursively sort each half
3. Merge the sorted halves

### Recurrence
$$
T(n) = 2T(n/2) + \Theta(n)
$$

---

# Lecture 4 — Solving Recurrences

## Substitution Method
Guess a solution (e.g., $T(n)=O(n\log n)$) and prove by induction.

Applied to MergeSort:
$$
T(n) = 2T(n/2) + \Theta(n) = \Theta(n\log n)
$$

---

## Unrolling Method
Expand the recurrence repeatedly:
$$
T(n) = 2^k T(n/2^k) + k \Theta(n)
$$
Stop when $n/2^k = 1$ → $k = \log n$.

Result:
$$
T(n) = O(n\log n)
$$

---

# Lecture 5 — Information-Theoretic Lower Bounds & QuickSort

## Decision Tree Model
Comparison-based sorting algorithms can be modeled as binary decision trees:
- Internal nodes: comparisons
- Leaves: possible sorted outputs

For $n$ distinct elements, there are $n!$ possible outputs.

---

## Lower Bound on Sorting
A binary tree of height $h$ has at most $2^h$ leaves.
Thus:
$$
2^h \ge n! \Rightarrow h \ge \log(n!) = \Omega(n\log n)
$$

### Theorem
Any comparison-based sorting algorithm requires:
$$
\Omega(n\log n)
$$
comparisons in the worst case.

MergeSort is asymptotically optimal.

---

## Notes
- Non-comparison sorts (Counting Sort, Radix Sort) can run in $O(n)$ under constraints.
- Information-theoretic lower bounds apply only to comparison-based models.

---
# Lecture 6 — QuickSort and Selection

## QuickSort Overview
QuickSort is a **divide-and-conquer** sorting algorithm.

Steps:
1. Choose a **pivot** element.
2. Partition the array so that:
   - elements `< pivot` are on the left
   - elements `≥ pivot` are on the right
3. Recursively sort the two subarrays.

---

## In-Place Partition Algorithm

We choose the **last element** as pivot.

### Pseudocode
```
Partition(A, st, ed):
  pivot = A[ed]
  bd = st - 1
  for cur = st to ed - 1:
    if A[cur] < pivot:
      bd = bd + 1
      swap A[bd], A[cur]
  swap A[bd + 1], A[ed]
  return bd + 1
```

### Key Invariant
- Indices `st..bd` contain elements `< pivot`
- Indices `bd+1..cur-1` contain elements `≥ pivot`

### Complexity
- Time: Θ(n)
- Extra space: Θ(1)

---

## QuickSort Recurrence

Worst case (extremely unbalanced partitions):
$$
T(n) = T(n-1) + \Theta(n) = O(n^2)
$$

Best case (perfect split):
$$
T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)
$$

### Why QuickSort Is Still Fast
- Expected running time is $O(n \log n)$
- Even 90–10 splits still give logarithmic depth
- Very small constants
- In-place (no extra memory)

---

## Selection Problem
Given an array of $n$ numbers, find the $k$-th smallest element.

### Naive Method
- Sort the array
- Return element at index $k$
- Cost: $O(n \log n)$

---

## Randomized Selection
Similar to QuickSort but recurse into **only one side**.

Expected running time:
$$
O(n)
$$

Worst case:
$$
O(n^2)
$$

---

# Lecture 7 — Median of Medians & Divide-and-Conquer

## Deterministic Linear-Time Selection

### Median of Medians Algorithm
1. Divide array into groups of 5
2. Find median of each group
3. Recursively find median of medians
4. Use it as pivot
5. Recurse on one side

---

## Why Groups of 5 Work

We can guarantee:
- At least $3n/10$ elements ≤ pivot
- At least $3n/10$ elements ≥ pivot

This leads to recurrence:
$$
T(n) = T(n/5) + T(7n/10) + \Theta(n)
$$

Which solves to:
$$
T(n) = O(n)
$$

---

## Notes
- Group size 3 → not enough elimination
- Group size 7 → works but larger constants
- 5 is the smallest size that guarantees linear time

---

## Matrix Multiplication

### Naive Algorithm
For two $n \times n$ matrices:
$$
C[i][j] = \sum_{k=1}^{n} A[i][k] \cdot B[k][j]
$$

Time complexity:
$$
O(n^3)
$$

Lower bound:
$$
\Omega(n^2)
$$

---

# Lecture 8 — Binary Heaps & Priority Queues

## Priority Queue ADT

Operations:
- GetMax
- Insert
- DeleteMax
- ChangePriority

Goal: Support all operations efficiently.

---

## Why Binary Heaps?
Binary heaps support:
- GetMax: $O(1)$
- Insert: $O(\log n)$
- DeleteMax: $O(\log n)$

---

## Complete Binary Tree

A binary tree is **complete** if:
- All levels are full except possibly the last
- Last level filled left-to-right

Stored efficiently in an array.

### Index Relations
- parent(i) = ⌊i/2⌋
- left(i) = 2i
- right(i) = 2i + 1

---

## Max-Heap Property
For all $i > 1$:
$$
H[i] \le H[parent(i)]
$$

Duplicates allowed.

---

# Lecture 9 — Heap Operations & HeapSort

## Heap Height
A heap with $n$ elements has height:
$$
h = O(\log n)
$$

---

## Insertion (Heapify-Up)

Steps:
1. Insert new key at end
2. Swap upward while violating heap property

### Time Complexity
$$
O(\log n)
$$

---

## Deletion (Heapify-Down)

Steps:
1. Replace deleted element with last element
2. Swap downward until heap property restored

### Time Complexity
$$
O(\log n)
$$

---

## HeapSort

Algorithm:
1. Build max-heap
2. Repeatedly swap max with last element
3. Reduce heap size
4. Heapify-down

### Complexity
- Time: $O(n \log n)$
- Space: $O(1)$ (in-place)
- Not stable

---

# Lecture 10 — Graphs and Representations

## Graph Definition
A graph is a pair:
$$
G = (V, E)
$$

Where:
- $V$ is the set of vertices
- $E$ is the set of edges

---

## Directed vs Undirected Graphs

- Undirected edge: $\{u, v\}$
- Directed edge: $(u, v)$

Directed graphs model asymmetric relationships.

---

## Graph Representations

### Adjacency Matrix
- $|V| \times |V|$ matrix
- Space: $O(|V|^2)$
- Fast edge lookup

---

### Adjacency List
- Store neighbors for each vertex
- Space: $O(|V| + |E|)$
- Preferred for sparse graphs
# Lecture 11 — Depth First Search (DFS) on Undirected Graphs

## Connected Components

A **connected component** of an undirected graph is a **maximal set of vertices** such that every pair of vertices in the set is connected by a path.

Key motivation:
- Answer reachability questions: *“Is node v connected to node w?”*
- Partition the graph into independent subproblems

The core idea: **explore the graph** starting from an unvisited vertex.

---

## DFS Intuition

DFS is analogous to **exploring a maze**:
- Vertices are intersections
- Edges are corridors
- Chalk marks visited intersections
- A stack (explicit or implicit via recursion) is used to backtrack

DFS goes **as deep as possible** before backtracking.

---

## DFS-Explore Algorithm

**Input:** Graph $G=(V,E)$, start vertex $s$, color  
**Output:** All vertices reachable from $s$ marked with the given color

```
Explore(G, s, color):
  visited[s] = color
  for each edge {s, v} in E:
    if visited[v] == 0:
      Explore(G, v, color)
```

This marks exactly the vertices in the connected component containing $s$.

---

## DFS for Connected Components

To find **all** connected components:
1. Initialize all vertices as unvisited
2. For each vertex $v$:
   - If unvisited, call `Explore(G, v, new_color)`
3. Each DFS call discovers one connected component

---

## Correctness (DFS)

**Claim:** `Explore(G, s)` visits exactly the vertices reachable from $s$.

*Proof sketch*:
- Any visited vertex has a path from $s$ (by recursion)
- Any vertex reachable from $s$ will eventually be explored
- DFS never leaves the connected component

---

## Time Complexity

Using adjacency lists:
- Each vertex visited once
- Each edge explored at most twice

$$
O(|V| + |E|)
$$

---

# Lecture 12 — DFS on Directed Graphs

## DFS Still Works

DFS works unchanged on directed graphs, but reveals **more structure**.

In directed graphs:
- Reachability is asymmetric
- Paths may exist in one direction but not the other

---

## DFS Forest

Running DFS on all vertices produces a **DFS forest**:
- Each tree corresponds to a DFS call
- Together they cover the entire graph

---

## Edge Classification

During DFS on directed graphs, edges are classified as:

1. **Tree edges** — part of the DFS tree
2. **Back edges** — point to an ancestor (indicates a cycle)
3. **Forward edges** — point to a descendant
4. **Cross edges** — connect different subtrees

These are determined using discovery times.

---

## Pre- and Post-Visit Times

We maintain a global clock:

```
Explore(G, s):
  pre[s] = clock++
  for each (s, v):
    if not visited[v]:
      Explore(G, v)
  post[s] = clock++
```

Properties:
- $pre[v] < post[v]$
- Ancestor intervals strictly contain descendant intervals

---

## Applications

- Cycle detection
- Topological sorting (DAGs)
- Graph structure analysis

---

# Lecture 13 — Strongly Connected Components (SCC)

## Connectivity in Directed Graphs

In a directed graph, vertices $u$ and $v$ are **strongly connected** if:
- There is a path from $u$ to $v$
- There is a path from $v$ to $u$

This defines an equivalence relation.

---

## Strongly Connected Components

A **strongly connected component (SCC)** is a maximal set of vertices that are mutually reachable.

Every directed graph can be decomposed uniquely into SCCs.

---

## Why SCCs Matter

- Collapse SCCs → DAG (condensation graph)
- Used in:
  - Program analysis
  - Dependency resolution
  - Circuit analysis

---

## Kosaraju’s Algorithm (High Level)

1. Run DFS on $G$, record post times
2. Reverse all edges to get $G^R$
3. Run DFS on $G^R$ in decreasing post order
4. Each DFS tree gives one SCC

---

## Complexity

Each DFS is linear:
$$
O(|V| + |E|)
$$

Total time remains linear.

---

# Lecture 14 — Breadth First Search (BFS)

## BFS Intuition

BFS explores the graph **layer by layer**:
- First all vertices at distance 1
- Then distance 2
- And so on

Uses a **queue** instead of recursion.

---

## BFS-Explore Algorithm

```
BFS-Explore(G, s, color):
  enqueue(s)
  visited[s] = color
  while queue not empty:
    v = dequeue()
    for each edge {v, w}:
      if visited[w] == 0:
        enqueue(w)
        visited[w] = color
```

---

## BFS Properties

- Visits vertices in order of increasing distance from $s$
- Computes shortest paths in **unweighted graphs**
- Discovers connected components (like DFS)

---

## Time Complexity

Each vertex enqueued once, each edge examined twice:
$$
O(|V| + |E|)
$$

---

# Lecture 15 — Dijkstra’s Algorithm

## Shortest Paths with Weights

BFS fails when edges have weights.

Goal:
- Compute shortest paths from a source $s$
- Edge weights are **non-negative**

---

## Key Idea

Maintain tentative distances:
- Initialize $dist[s]=0$, others $=\infty$
- Repeatedly select unvisited vertex with smallest distance
- Relax outgoing edges

---

## Relaxation

For edge $(u,v)$ with weight $w(u,v)$:
$$
dist[v] = \min(dist[v], dist[u] + w(u,v))
$$

---

## Algorithm Outline

1. Initialize distances
2. Use a priority queue keyed by distance
3. Extract-min repeatedly
4. Relax edges

---

## Correctness (Greedy Choice)

Once a vertex is extracted:
- Its shortest path is finalized
- No shorter path exists through unvisited vertices

Requires **non-negative weights**.

---

## Time Complexity

Using binary heap:
$$
O((|V| + |E|) \log |V|)
$$

---
## Lecture 16 — Revisiting Dijkstra’s Algorithm

### Motivation and High-Level View
Dijkstra’s algorithm can be viewed as **BFS generalized to weighted graphs with nonnegative edge weights**.  
In BFS, nodes are explored in increasing number of edges from the source.  
In Dijkstra, nodes are explored in increasing **distance value** from the source.

The key invariant:
> Once a node is extracted from the priority queue, its shortest-path distance from the source is finalized.

This invariant **only holds when all edge weights are nonnegative**.

---

### Algorithm (Priority Queue Version)

We maintain:
- `dist[v]`: current best-known distance from source `s` to `v`
- `prev[v]`: predecessor of `v` on the shortest path
- A min-priority queue `Q` keyed by `dist`

```text
Initialize dist[v] = ∞ for all v ∈ V
dist[s] = 0
Insert (0, s) into priority queue Q

while Q is not empty:
    v = ExtractMin(Q)
    for each edge (v, w):
        if dist[w] > dist[v] + ℓ(v, w):
            dist[w] = dist[v] + ℓ(v, w)
            prev[w] = v
            Update w’s key in Q
```

---

### Correctness Intuition
At each step, we choose the unvisited node with the smallest tentative distance.  
Because **all edges are nonnegative**, any alternative path to this node must be **at least as long**, so the distance is final.

This is analogous to BFS layers:
- BFS: layers by number of edges
- Dijkstra: layers by total path weight

---

### Time Complexity
Using a binary heap:
- Insert/DeleteMin: `O(log |V|)`
- DecreaseKey: `O(log |V|)`

Total complexity:
$$
O\big((|V| + |E|)\log |V|\big)
$$

---

### Worked Example
Given a graph with nodes `{S, B, C, D, ...}` and weighted edges, Dijkstra repeatedly:
1. Extracts the node with smallest `dist`
2. Relaxes all outgoing edges
3. Updates the priority queue

The table of queue states demonstrates how distances monotonically increase.

---

## Lecture 17 — Shortest Paths with Negative Weights (Bellman–Ford)

### Why Dijkstra Fails
Dijkstra assumes:
$$
\text{Once a node is chosen, no shorter path can exist later}
$$

This fails when **negative edges** exist:
- A later path may reduce a previously “finalized” distance

In undirected graphs:
- Any negative edge implies a negative cycle

---

### Update (Relaxation) Operation
For an edge $(v, w)$:
$$
\text{if } dist[w] > dist[v] + \ell(v,w) \text{ then update}
$$

Key observation:
> A shortest path can always be found by a sequence of correct relaxations — even with negative edges.

---

### Bellman–Ford Algorithm

Idea:
- Repeatedly relax **all edges**
- Repeat exactly $|V| - 1$ times

Why?
- Any simple shortest path has at most $|V| - 1$ edges

```text
Initialize dist[s] = 0, dist[v] = ∞ for v ≠ s

Repeat |V| − 1 times:
    for each edge (u, v):
        relax(u, v)
```

---

### Negative Cycle Detection
After $|V| - 1$ iterations:
- Perform one more full relaxation pass
- If **any distance improves**, a negative cycle exists

This is crucial:
> With a negative cycle reachable from `s`, shortest paths are undefined.

---

### Time Complexity
$$
O(|V| \cdot |E|)
$$

Slower than Dijkstra, but handles **negative edges safely**.

---

## Lecture 18 — All-Pairs Shortest Paths (Floyd–Warshall)

### Problem Statement
Compute shortest-path distances between **all pairs** $(i, j)$ in a graph.

---

### Dynamic Programming Formulation

Let:
$$
dist_k[i][j] = \text{shortest path from } i \text{ to } j \text{ using only nodes } \{1,\dots,k\}
$$

Base case:
$$
dist_0[i][j] =
\begin{cases}
0 & i=j \\
\ell(i,j) & (i,j)\in E \\
\infty & \text{otherwise}
\end{cases}
$$

---

### Recurrence (Core Idea)
Either:
- Do not use node $k$ as an intermediate
- Or use $k$ somewhere in the path

$$
dist_k[i][j] = \min\big(dist_{k-1}[i][j],\ dist_{k-1}[i][k] + dist_{k-1}[k][j]\big)
$$

---

### Algorithm (Floyd–Warshall)

```text
for k = 1 to n:
    for i = 1 to n:
        for j = 1 to n:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

---

### Properties
- Handles negative edges
- Detects negative cycles if `dist[i][i] < 0`
- Extremely simple conceptually

---

### Time and Space Complexity
$$
O(|V|^3) \text{ time}, \quad O(|V|^2) \text{ space}
$$

Used when graphs are dense or $|V|$ is small.

---

## Lecture 19 — Maximum Flow Problem

### Flow Network Definition
A **flow network** is a directed graph $G=(V,E)$ with:
- Capacity $c(e) \ge 0$ on each edge
- Source $s$
- Sink $t$

A flow $f$ satisfies:
1. **Capacity constraint:** $0 \le f(e) \le c(e)$
2. **Flow conservation:**  
   $$
   \sum f(\text{in edges}) = \sum f(\text{out edges})
   $$
   for all $v \ne s,t$

---

### Flow Value
$$
|f| = \sum_{(s,v)\in E} f(s,v)
$$

This equals total flow into $t$.

---

### Augmenting Path Idea
Start with zero flow:
1. Find a path from $s$ to $t$
2. Push as much flow as possible
3. Update remaining capacities
4. Repeat

But naïvely choosing paths may fail — we need structure.

---

## Lecture 20 — Ford–Fulkerson & Max-Flow Min-Cut

### Residual Graph
Given a flow $f$, define residual capacity:
$$
c_f(u,v) = c(u,v) - f(u,v)
$$

Residual graph includes:
- Forward edges (remaining capacity)
- Backward edges (undo flow)

---

### Ford–Fulkerson Algorithm

```text
Initialize f(e) = 0 for all edges

while there exists an s–t path P in residual graph:
    b = bottleneck capacity of P
    augment flow along P by b
    update residual graph
```

---

### Correctness Intuition
Each augmentation strictly increases flow value.  
Algorithm stops **iff no augmenting path exists**.

---

### Max-Flow Min-Cut Theorem
**The maximum value of an s–t flow equals the minimum capacity of an s–t cut.**

Key consequences:
- If no augmenting path exists, current flow is optimal
- Cuts certify optimality

---

### Complexity Notes
- Ford–Fulkerson may not terminate with irrational capacities
- With integer capacities, it terminates
- Edmonds–Karp (BFS-based) guarantees:
$$
O(|V|\cdot |E|^2)
$$

---
## Lecture 21 — Greedy Algorithms: Foundations and Pitfalls

### What Is a Greedy Algorithm?
A **greedy algorithm** solves an optimization problem by making a **locally optimal choice at each step**, with the hope that these local choices lead to a global optimum.

Greedy algorithms:
- Build solutions incrementally
- Never revise previous decisions
- Are usually fast, but not always correct

---

### Example: 0–1 Knapsack

**Goal:** maximize value without exceeding capacity.

Greedy choice: always pick the most valuable item that fits.

Counterexample shows greedy gives \$46, while optimal gives \$50.

**Lesson:** greedy is not always optimal.

---

### When Greedy Works
Greedy algorithms are optimal when:
1. **Greedy-choice property** holds
2. **Optimal substructure** exists

---

## Lecture 22 — Minimum Spanning Trees (MST)

### Definition
Given a connected weighted graph $G=(V,E)$, an MST is a spanning tree minimizing total edge weight.

Properties:
- Exactly $|V|-1$ edges
- No cycles

---

### Applications
- Network design
- Clustering
- Taxonomy
- Graph algorithms

---

## Lecture 23 — Kruskal’s Algorithm

### Algorithm
1. Sort edges by weight
2. Add smallest edge that doesn’t create a cycle
3. Stop when $|V|-1$ edges chosen

---

### Correctness
- **Cut property**
- **Cycle property**

---

### Complexity
$$
O(|E| \log |E|)
$$

---

## Lecture 24 — Disjoint Sets (Union-Find)

### Operations
- **Find:** determine component
- **Union:** merge components

Optimizations:
- Weighted union
- Path compression

Amortized time: $O(\alpha(n))$

---

## Lecture 25 — Huffman Coding

### Goal
Create a prefix-free binary encoding minimizing total length.

### Greedy Strategy
Repeatedly merge two least frequent symbols.

---

### Properties
- Prefix-free
- Optimal
- $O(n \log n)$ time
## Lecture 26 — Greedy Algorithms: Set Cover

### Problem Definition (Set Cover)
Let:
- $B$ be a universe of elements
- $S_1, S_2, \dots, S_m \subseteq B$ be subsets

**Goal:**  
Find a minimum-size collection of subsets whose union equals $B$.

$$
\bigcup_{j \in J} S_j = B
$$

This is an **NP-hard** optimization problem.

---

### Motivating Example: Post Offices
- Each post office serves towns within 30 miles.
- Towns = elements of $B$
- For each town $t$, define $S(t)$ = towns reachable from $t$

**Observation:**  
Choosing towns where to build post offices is equivalent to choosing subsets $S(t)$ that cover all towns.

---

### Greedy Algorithm for Set Cover
**Heuristic:**
Repeatedly pick the subset that covers the largest number of *currently uncovered* elements.

**Algorithm:**
1. Initialize $C = \emptyset$
2. While uncovered elements remain:
   - Choose $S_i$ maximizing uncovered elements
   - Add $S_i$ to $C$
3. Return $C$

---

### Properties
- Not optimal in general
- Approximation guarantee:
$$
|C_{\text{greedy}}| \le O(\log n) \cdot |C_{\text{optimal}}|
$$

---

## Lecture 27 — Greedy vs Dynamic Programming

### Comparison

| Property | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Optimal substructure | ✔ | ✔ |
| Greedy-choice property | ✔ | ✘ |
| Guarantees optimal | ✘ (usually) | ✔ |

**Key insight:**  
Greedy makes *locally optimal* choices; DP explores all relevant subproblems.

---

## Lecture 28 — Longest Increasing Subsequence (LIS)

### Problem
Given sequence $a_1, a_2, \dots, a_n$, find the longest subsequence:
$$
i_1 < i_2 < \dots < i_k \quad \text{and} \quad a_{i_1} < a_{i_2} < \dots < a_{i_k}
$$

---

### Greedy Attempt (Fails)
Algorithm:
- Start with empty LIS
- Append $a_i$ if larger than last element

**Counterexample:**  
Fails because early large choices block future optimal solutions.

---

### DP Formulation (DAG View)
Define:
$$
L(j) = \text{length of LIS ending at } a_j
$$

Recurrence:
$$
L(j) = 1 + \max_{i < j, a_i < a_j} L(i)
$$

Base case:
$$
L(j) = 1 \quad \text{if no smaller predecessor}
$$

**Answer:**
$$
\max_j L(j)
$$

**Time complexity:** $O(n^2)$

---

## Lecture 29 — Edit Distance

### Definition
Edit distance between strings $x$ and $y$ is the minimum number of:
- Insertions
- Deletions
- Substitutions

to transform $x$ into $y$.

---

### DP Definition
Let:
- $x = x_1 \dots x_m$
- $y = y_1 \dots y_n$

Define:
$$
E(i,j) = \text{edit distance between } x_1\dots x_i \text{ and } y_1\dots y_j
$$

---

### Recurrence
$$
E(i,j) = \min \begin{cases}
1 + E(i-1,j) & \text{(deletion)} \\
1 + E(i,j-1) & \text{(insertion)} \\
\text{diff}(i,j) + E(i-1,j-1) & \text{(match/mismatch)}
\end{cases}
$$

Where:
$$
\text{diff}(i,j) =
\begin{cases}
0 & x_i = y_j \\
1 & x_i \ne y_j
\end{cases}
$$

---

### Base Cases
$$
E(0,j) = j, \quad E(i,0) = i
$$

---

### Complexity
- Time: $O(mn)$
- Space: $O(mn)$

---

## Lecture 30 — Sequence Alignment & APSP

### From Edit Distance to Alignment Score
Allow:
- Match = reward $R > 0$
- Mismatch = penalty $P_1 < 0$
- Gap = penalty $P_2 < 0$

DP Recurrence:
$$
Score(i,j) = \max \begin{cases}
P_2 + Score(i-1,j) \\
P_2 + Score(i,j-1) \\
\text{diff}(i,j) + Score(i-1,j-1)
\end{cases}
$$

---

### Global vs Local Alignment
- **Global:** align entire strings
- **Local:** allow restarting at 0
$$
Score(i,j) = \max(\dots, 0)
$$

Used in bioinformatics (DNA matching).

---

## All-Pairs Shortest Paths (APSP)

### Problem
Given weighted directed graph $G=(V,E)$, find shortest paths between all pairs $(u,v)$.

---

### DP Subproblem
$$
dist(u,v,k) = \text{shortest path from } u \text{ to } v \text{ using vertices } \{1,\dots,k\}
$$

---

### Recurrence (Floyd–Warshall)
$$
dist(u,v,k) = \min\big(dist(u,v,k-1),\; dist(u,k,k-1) + dist(k,v,k-1)\big)
$$

---

### Algorithm
Triple nested loop over:
- $k$
- $u$
- $v$

**Time complexity:** $O(|V|^3)$

---

### Key Takeaways
- DP systematically explores all subproblems
- Greedy is faster but less reliable
- Many classical problems reduce to DP recurrences
## Lecture 31 — Dense Subsequences (Dynamic Programming)

### Problem Definition
Given a sequence of real numbers
$$
A = \{a_1, a_2, \dots, a_n\},
$$
a subsequence $A^*$ is **dense** if for every pair of consecutive elements in $A$, at least one of them is included in $A^*$.

**Goal:** Find a dense subsequence with **maximum sum**.

### DP State
We define two DP states at index $i$:
- $DP(i,\text{added})$: maximum sum if $a_i$ is included
- $DP(i,\text{skipped})$: maximum sum if $a_i$ is excluded

### Recurrence
$$
\begin{aligned}
DP(i,\text{added}) &= \max(DP(i-1,\text{added}), DP(i-1,\text{skipped})) + a_i \\
DP(i,\text{skipped}) &= DP(i-1,\text{added})
\end{aligned}
$$

### Base Case
$$
DP(1,\text{added}) = a_1, \quad DP(1,\text{skipped}) = 0
$$

### Final Answer
$$
\max(DP(n,\text{added}), DP(n,\text{skipped}))
$$

### Backtracking
Store parent decisions to reconstruct the dense subsequence by tracing backward from the maximum value in the last column.

---

## Lecture 32 — Linear Programming Basics

### Linear Programming (LP)
An LP problem optimizes a linear objective subject to linear constraints:
$$
\max \ c^T x \quad \text{s.t. } Ax \le b,\ x \ge 0
$$

### Feasible Region
- Convex polytope
- Optimal solutions occur at **vertices**
- Infinite solutions possible, but optimal is always at a vertex

### Standard Form
- All constraints are equalities
- Introduce **slack variables** for $\le$ constraints

---

## Lecture 33 — Simplex Method: Setup

### Slack Variables
Convert:
$$
x \le 3 \Rightarrow x + a_1 = 3, \ a_1 \ge 0
$$

### Tableau Structure
- Rows: constraints + objective
- Columns: variables + RHS ($b$)
- Basic variables form an identity matrix

### Initial BFS
- Nonbasic variables = 0
- Basic variables = RHS values

---

## Lecture 34 — Simplex Method: Iterations

### Pivot Selection
1. **Pivot column:** most negative coefficient in $z$-row
2. **Pivot row:** smallest nonnegative ratio $\frac{b_i}{a_{ij}}$
3. **Pivot element:** intersection

### Gaussian Elimination
Transform pivot column into a unit vector.

### Termination
Stop when all coefficients in $z$-row are nonnegative.

### Interpretation
Each iteration moves along an edge of the feasible region to a better vertex.

---

## Lecture 35 — Advanced Simplex & Two-Phase Method

### Why Two-Phase Simplex?
Needed when:
- Surplus variables ($\ge$ constraints)
- No obvious initial BFS

### Phase I
- Introduce artificial variables
- Minimize sum of artificial variables
- If minimum $>0$: infeasible LP

### Phase II
- Remove artificial variables
- Optimize original objective

### Key Insight
Feasibility first, optimality second.

---

## Complexity & Notes
- Simplex is exponential in worst case
- Extremely fast in practice
- Foundation for real-world optimization

## Lecture 36 — Duality in Linear Programming

### Primal vs Dual LP
Every linear program (LP) has an associated **dual** LP.

**Primal (maximization form):**
$$
\max \; c_1x_1 + \cdots + c_n x_n
$$
subject to
$$
\sum_{j=1}^n a_{ij} x_j \le b_i \quad (i=1,\dots,m), \qquad x_j \ge 0
$$

**Dual (minimization form):**
$$
\min \; b_1y_1 + \cdots + b_m y_m
$$
subject to
$$
\sum_{i=1}^m a_{ij} y_i \ge c_j \quad (j=1,\dots,n), \qquad y_i \ge 0
$$

Each **primal constraint ↔ dual variable**  
Each **primal variable ↔ dual constraint**

---

### Weak and Strong Duality

**Weak Duality Theorem**  
For any feasible primal solution $x$ and feasible dual solution $y$:
$$
c^T x \le b^T y
$$

Interpretation:
- Any feasible dual solution gives an **upper bound** on the primal optimum.

**Strong Duality Theorem**  
If both LPs are feasible:
$$
\max(\text{primal}) = \min(\text{dual})
$$

This explains *why simplex stops when reduced costs are nonnegative*.

---

### Degenerate Cases
- Primal unbounded ⇒ Dual infeasible
- Dual unbounded ⇒ Primal infeasible
- Both infeasible possible

---

### Economic Interpretation
- Primal variables: activity levels
- Dual variables: **shadow prices**
- $y_i$ = marginal value of one extra unit of resource $i$

Sensitivity analysis:
- Changing RHS of primal constraints affects dual objective
- Original dual solution may remain feasible

---

## Lecture 37 — Polynomial-Time Reductions & Hardness

### Motivation
Some problems:
- Best known algorithm is exponential
- We suspect *no polynomial-time algorithm exists*

Instead of proving impossibility directly, we:
- **Compare problems to each other**
- Classify relative difficulty

---

### Polynomial-Time Reduction

**Definition**
A problem $Y$ is polynomial-time reducible to $X$ (written $Y \le_p X$) if:
- Any instance of $Y$ can be transformed into an instance of $X$
- Transformation takes polynomial time
- Solving $X$ gives a solution to $Y$

---

### Consequences

If $Y \le_p X$:
- $X$ is *at least as hard* as $Y$
- If $X$ is easy ⇒ $Y$ is easy
- If $Y$ is hard ⇒ $X$ is hard

Reductions preserve hardness.

---

## Lecture 38 — NP, NP-Completeness, and SAT

### Decision Problems
A **decision problem** asks a yes/no question.

Input size measured in bits.

---

### Class P
$$
\mathbf{P} = \{ \text{problems solvable in polynomial time} \}
$$

Examples:
- Shortest path
- MST
- Sorting

---

### Checking vs Solving

A problem is in **NP** if:
- Given a candidate solution (certificate)
- We can verify correctness in polynomial time

Verification ≠ finding the solution.

---

### Class NP
$$
\mathbf{NP} = \{ \text{problems verifiable in polynomial time} \}
$$

Open question:
$$
\mathbf{P} \stackrel{?}{=} \mathbf{NP}
$$

---

### SAT and k-SAT

**SAT (Satisfiability):**
Given a Boolean formula in CNF, is there an assignment that satisfies it?

**k-SAT:**
Each clause has exactly $k$ literals.

- 2-SAT ∈ P
- 3-SAT is NP-complete

---

### Independent Set

**Definition**
A set of vertices with no edges between them.

**Decision version**
Given $G$ and $k$, does $G$ have an independent set of size $k$?

---

### 3-SAT ≤ Independent Set

Construction:
- One triangle per clause
- Vertices = literals
- Conflict edges between $x$ and $\bar{x}$

Key idea:
- Pick one literal per clause
- No conflicts ⇒ satisfying assignment

Thus:
$$
\text{3-SAT is satisfiable} \iff \text{Independent Set of size } k \text{ exists}
$$

---

### NP-Completeness

A problem is **NP-complete** if:
1. It is in NP
2. Every problem in NP reduces to it

Classic NP-complete problems:
- 3-SAT
- Independent Set
- Vertex Cover
- Hamiltonian Cycle
- Traveling Salesman (decision version)

---

## Key Takeaways
- LP duality explains optimality and bounds
- Reductions compare problem difficulty
- NP-complete problems are the hardest in NP
- A poly-time solution to one NP-complete problem solves all of them

---
