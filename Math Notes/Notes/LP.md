---
title: Linear Programming
parent: Math Notes
nav_order: 7
---

# Linear Programming Notes

> Comprehensive notes covering the full LP sequence: geometry of LPs, basic feasible solutions, simplex, revised simplex, duality, complementary slackness, and dual simplex.

---

# 1. Introduction to Linear Programming

A linear program (LP) has the form

$$
\min c^T x
$$

or

$$
\max c^T x
$$

subject to linear constraints.

Standard form:

$$
\min c^T x
$$

subject to

$$
Ax=b,
\qquad
x\ge 0.
$$

where

- $A\in\mathbb R^{m\times n}$
- $b\in\mathbb R^m$
- $c\in\mathbb R^n$

---

# 2. Geometry of Linear Programs

## Feasible Region

The feasible region is

$$
P=\{x:Ax=b,\;x\ge0\}.
$$

A feasible region is a convex polyhedron.

## Convex Sets

A set $S$ is convex if

$$
x,y\in S
$$

implies

$$
\lambda x+(1-\lambda)y\in S
$$

for all

$$
0\le \lambda \le 1.
$$

Interpretation:

Every line segment connecting two feasible points remains feasible.

---

# 3. Convexity

## Convex Combination

A convex combination is

$$
\sum_{i=1}^{k}\lambda_i x_i
$$

where

$$
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1.
$$

## Why Convexity Matters

Linear objectives satisfy

$$
c^T(\lambda x+(1-\lambda)y)
=
\lambda c^Tx+(1-\lambda)c^Ty.
$$

Therefore local optimality implies global optimality.

---

# 4. Extreme Points

## Definition

A point $x$ is an extreme point if it cannot be written as

$$
x=\lambda y+(1-\lambda)z
$$

for distinct feasible points $y,z$.

## Geometric Interpretation

Extreme points are the "corners" of the feasible region.

---

## Fundamental Theorem

If an LP has an optimal solution and the feasible region contains an extreme point, then there exists an optimal solution that is an extreme point.

This theorem justifies searching only corner points.

---

# 5. Linear Algebra Review

A matrix

$$
A=[A_1,\dots,A_n]
$$

has columns

$$
A_j.
$$

A collection of columns is linearly independent if

$$
\alpha_1A_{i_1}+\cdots+\alpha_kA_{i_k}=0
$$

implies

$$
\alpha_1=\cdots=\alpha_k=0.
$$

---

# 6. Basic Solutions

Choose $m$ linearly independent columns of $A$.

Call their indices

$$
B(1),\dots,B(m).
$$

Construct

$$
B=[A_{B(1)},\dots,A_{B(m)}].
$$

Because the columns are independent,

$$
B^{-1}
$$

exists.

Solve

$$
x_B=B^{-1}b.
$$

Set all remaining variables equal to zero.

The resulting vector is a basic solution.

---

# 7. Basic Feasible Solutions

A basic solution is feasible if

$$
B^{-1}b\ge0.
$$

Such solutions are called Basic Feasible Solutions (BFS).

## Important Theorem

Basic feasible solutions correspond exactly to extreme points of the feasible region.

This connects algebra with geometry.

---

# 8. Degeneracy

A BFS is degenerate if at least one basic variable equals zero.

Example:

$$
x_B=(5,0,2).
$$

Even though a variable is basic, its value is zero.

Degeneracy creates difficulties for simplex.

---

# 9. Optimality Conditions

For basis $B$ define

$$
c_B
$$

to be the costs of basic variables.

Define reduced costs

$$
\bar c_j
=
c_j-c_B^TB^{-1}A_j.
$$

---

## Optimality Theorem

For minimization:

$$
\bar c_j\ge0
$$

for every nonbasic variable.

Then the current BFS is optimal.

If any

$$
\bar c_j<0,
$$

the objective can be improved.

---

# 10. The Simplex Idea

Start at a BFS.

Move to an adjacent BFS with a better objective value.

Repeat until optimality conditions hold.

Because only finitely many bases exist, simplex searches among corner points.

---

# 11. Search Direction

Suppose variable $x_j$ enters the basis.

Define

$$
u=B^{-1}A_j.
$$

Then movement occurs along

$$
d
=
\begin{bmatrix}
-u\\
1
\end{bmatrix}.
$$

This direction preserves feasibility of equality constraints.

---

# 12. Ratio Test

Current basic variables:

$$
x_B=B^{-1}b.
$$

After moving:

$$
x_B-\theta u.
$$

Need

$$
x_B-\theta u\ge0.
$$

Therefore

$$
\theta
\le
\frac{(x_B)_i}{u_i}
$$

for all

$$
u_i>0.
$$

Maximum feasible step:

$$
\theta^*
=
\min_{u_i>0}
\frac{(x_B)_i}{u_i}.
$$

The minimizing variable leaves the basis.

---

# 13. Abstract Simplex Method

1. Start with BFS.
2. Compute reduced costs.
3. Choose entering variable.
4. Compute direction.
5. Apply ratio test.
6. Pivot.
7. Repeat.

Termination occurs when all reduced costs are nonnegative.

---

# 14. Full Tableau Method

The tableau stores

$$
B^{-1}A
$$

and

$$
B^{-1}b.
$$

Also stores reduced costs.

Advantages:

- Easy computations by hand.
- Useful for classroom examples.

Disadvantages:

- Large memory usage.
- Expensive updates.

---

# 15. Updating the Inverse

After a pivot, only one column changes.

Instead of recomputing

$$
B^{-1},
$$

update it efficiently.

This observation leads directly to the revised simplex method.

---

# 16. Revised Simplex Method

Store only

$$
B^{-1}
$$

rather than the entire tableau.

Key computations:

$$
x_B=B^{-1}b
$$

and

$$
\bar c_j
=
c_j-c_B^TB^{-1}A_j.
$$

Benefits:

- Lower memory requirements.
- Faster on large LPs.
- Used in practical solvers.

---

# 17. Cycling

Without degeneracy, simplex always improves the objective.

With degeneracy:

- Objective may not improve.
- Same basis may reappear.
- Algorithm can cycle.

---

# 18. Bland's Rule

Anti-cycling strategy:

Choose:

- Smallest indexed entering variable.
- Smallest indexed leaving variable.

Theorem:

Bland's Rule guarantees termination.

---

# 19. Feasibility

Many LPs do not provide an obvious starting BFS.

Need a method for finding one.

This motivates artificial variables.

---

# 20. Two-Phase Simplex

Introduce artificial variables

$$
y_1,\dots,y_m.
$$

Construct

$$
Ax+y=b.
$$

---

## Phase I

Solve

$$
\min \sum_i y_i.
$$

If optimum value is positive:

Original LP is infeasible.

If optimum value equals zero:

A feasible basis has been found.

---

## Phase II

Remove artificial variables.

Optimize the original objective function.

---

# 21. Motivation for Duality

Primal question:

> How small can the objective become?

Dual question:

> What lower bound can we prove using the constraints?

The dual transforms constraints into variables.

---

# 22. Constructing the Dual

Primal:

$$
\min c^Tx
$$

subject to

$$
Ax\ge b,
\qquad
x\ge0.
$$

Dual:

$$
\max p^Tb
$$

subject to

$$
p\ge0,
$$

$$
p^TA\le c^T.
$$

---

# 23. Sign Rules

Constraint type determines dual-variable sign.

| Primal Constraint | Dual Variable |
|---|---|
| $\ge$ | $p_i\ge0$ |
| $\le$ | $p_i\le0$ |
| $=$ | free |

---

Variable sign determines dual constraint.

| Primal Variable | Dual Constraint |
|---|---|
| $x_j\ge0$ | $\le$ |
| $x_j\le0$ | $\ge$ |
| free | $=$ |

---

# 24. Weak Duality

For every primal feasible $x$ and dual feasible $p$,

$$
p^Tb\le c^Tx.
$$

Consequences:

- Dual gives lower bounds.
- Primal gives upper bounds.

If bounds meet, optimality is proven.

---

# 25. Strong Duality

If optimal solutions exist:

$$
c^Tx^*=p^{*T}b.
$$

Primal optimum equals dual optimum.

This is one of the most important theorems in optimization.

---

# 26. Complementary Slackness

Let $x$ and $p$ be feasible.

They are optimal iff

$$
p_i(a_i^Tx-b_i)=0
$$

for every row.

And

$$
(c_j-p^TA_j)x_j=0
$$

for every column.

---

## Interpretation

Either:

Constraint slack exists:

$$
a_i^Tx>b_i
$$

and

$$
p_i=0,
$$

or constraint is tight.

Likewise:

Either

$$
x_j=0
$$

or

$$
c_j-p^TA_j=0.
$$

---

# 27. Physical Interpretation of Duality

Imagine a puck moving through the feasible region.

Objective force:

$$
-c.
$$

pushes the puck.

Active constraints exert balancing forces.

At optimum:

Net force equals zero.

Dual variables measure the strengths of these balancing forces.

This interpretation explains why

$$
p^TA=c^T
$$

appears naturally at optimality.

---

# 28. Dual Simplex Method

Primal simplex:

- Maintain primal feasibility.
- Improve optimality.

Dual simplex:

- Maintain dual feasibility.
- Repair primal infeasibility.

Useful after adding or modifying constraints.

---

# 29. Important Theorems Summary

### Extreme Point Theorem

Optimal solutions occur at extreme points.

### BFS Theorem

Extreme points correspond to BFSs.

### Optimality Theorem

$$
\bar c_j\ge0
$$

implies optimality.

### Weak Duality

$$
p^Tb\le c^Tx.
$$

### Strong Duality

$$
p^{*T}b=c^Tx^*.
$$

### Complementary Slackness

$$
p_i(a_i^Tx-b_i)=0
$$

$$
(c_j-p^TA_j)x_j=0.
$$

---

# 30. Formula Sheet

### Basic Variables

$$
x_B=B^{-1}b
$$

### Reduced Cost

$$
\bar c_j=c_j-c_B^TB^{-1}A_j
$$

### Direction

$$
u=B^{-1}A_j
$$

### Ratio Test

$$
\theta^*
=
\min_{u_i>0}
\frac{(B^{-1}b)_i}{u_i}
$$

### Weak Duality

$$
p^Tb\le c^Tx
$$

### Strong Duality

$$
p^{*T}b=c^Tx^*
$$

### Complementary Slackness

$$
p_i(a_i^Tx-b_i)=0
$$

$$
(c_j-p^TA_j)x_j=0
$$
