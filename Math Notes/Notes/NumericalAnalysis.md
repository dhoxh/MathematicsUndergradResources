---
title: Numerical Analysis
parent: Math Notes
nav_order: 5
---

# Numerical Analysis Notes

---

## 1. Introduction

**Numerical Analysis** is the science of computing solutions to mathematically posed problems in real and complex numbers, exploring both their mathematical and computational aspects.

### Computing $\sin x$ via Taylor Series

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{i=0}^{n} (-1)^{\frac{i-1}{2}} \frac{x^i}{i!}$$

A naive implementation recomputes $x^i$ and $i!$ from scratch each step — that is $O(n^2)$ flops. The improved version maintains a running term $t$ and updates it each iteration:

```matlab
function s = MySine2(x, n)
  s = x; t = x;
  for i = 3:2:n
    t = -t * x^2 / (i*(i-1));
    s = s + t;
  end
end
```

This runs in $O(n)$ time because at most 6 flops execute per iteration.

**Error analysis:** For $x \in (0,1)$ and $n$ odd:

$$\lvert\text{residual}(x,n)\rvert = \lvert\sin x - \text{MySine}(x,n)\rvert = O\!\left(\frac{x^n}{n!}\right)$$

which is very small for large enough $n$.

### Big-O and $\Theta$ Notation

$$f = O(g) \iff \lvert f(x)\rvert \leq c\,g(x) \text{ for some constant } c > 0 \text{ and all } x \in [a,b]$$

$$f = \Theta(g) \iff f = O(g) \text{ and } g = O(f)$$

$O(g)$ is an **asymptotic upper bound**; $\Theta(g)$ is **asymptotic equality**.

---

## 2. Floating Point Arithmetic

### Definition of a Floating Point Number

A number $x$ is a floating point number if

$$x = \pm d \cdot \beta^e$$

where $d \geq 0$, base $\beta \in \{2, 10\}$, integer exponent $e \in [e_{\min}, e_{\max}]$, and mantissa

$$d = d_1\beta^{-1} + d_2\beta^{-2} + \cdots + d_t\beta^{-t}$$

with each $d_i \in \{0,1\}$ when $\beta = 2$, and precision $t$.

### The Floating Point System $(\beta,\, t,\, e_{\min},\, e_{\max})$

The quadruple $(\beta, t, e_{\min}, e_{\max})$ identifies the floating point number system.

- $fl(x)$: the floating point number closest to $x \in \mathbb{R}$
- $\varepsilon_M = \beta^{-t}$: the **machine unit** — smallest difference from 1
- $\Omega = (1-\beta^{-t})\cdot\beta^{e_{\max}}$: the **largest** computer number
- $\omega = \beta^{1-t+e_{\min}}$: the **smallest** computer number

**Gradual underflow:** Keep $x$ as-is even if $d_1 = 0$.

### IEEE Standards

| Standard | $\beta$ | $t$ | $e_{\min}$ | $e_{\max}$ | $\varepsilon_M$ |
|---|---|---|---|---|---|
| Single precision | 2 | 24 | $-126$ | 128 | $\approx 5.96 \times 10^{-8}$ |
| Double precision | 2 | 53 | $-1022$ | 1024 | $\approx 1.11 \times 10^{-16}$ |

Single: $\Omega \approx 3.40 \times 10^{38}$, $\omega \approx 1.40 \times 10^{-45}$

Double: $\Omega \approx 1.80 \times 10^{308}$, $\omega \approx 4.94 \times 10^{-324}$

### Key Examples

**Example 1:** Plain Gaussian elimination on $\begin{pmatrix}10^{-17} & 1 \\ 1 & 1\end{pmatrix}$ gives $x_1 = 0$, $x_2 = 1$ — drastically wrong because $10^{-17}$ is truncated when added to 1.

**Example 2:** On $\beta = 10$, $t = 4$, $-7 \leq e \leq 7$: with $x = 0.1957 \times 10^{-7}$, $y = 0.1942 \times 10^{-7}$, $z = x - y$:

$$z = fl(x-y) = 0.015 \times 10^{-7}$$

By gradual underflow $d_1 = 0$ but $z \neq 0$.

**Example 3 (Double precision):** $f(10^{-12}) = 0$ where $f(x) = \sqrt{1+x^2} - 1$. Use the algebraically equivalent form:

$$g(x) = \frac{x^2}{\sqrt{1+x^2}+1}, \qquad g(10^{-12}) \approx \frac{10^{-24}}{2} = 0.5 \times 10^{-24}$$

**Common trick:** Avoid dividing by a small number, or subtracting quantities that nearly cancel.

---

## 3. Taylor Series

### Theorem

Assume $f(x)$ has $k+1$ derivatives on an interval containing $x_0$ and $x_0 + h$. Then:

$$f(x_0 + h) = f(x_0) + hf'(x_0) + \frac{h^2}{2}f''(x_0) + \cdots + \frac{h^k}{k!}f^{(k)}(x_0) + \frac{h^{k+1}}{(k+1)!}f^{(k+1)}(\xi)$$

where $\xi$ is some point between $x_0$ and $x_0 + h$. The three most useful cases in this course: $k = 1$, $k = 2$, and $k = \infty$.

### Function Spaces

$C[a,b]$ denotes functions continuous on $[a,b]$. $C^1[a,b]$ is continuously differentiable. $C^k[a,b]$ is $k$ times continuously differentiable.

### Examples

**Example 1:** $\sin(x+h) = \sin x + h\cos x + O(h^2)$

Since $\left\lvert\frac{1}{2}\sin(\xi)\right\rvert \leq \frac{1}{2}$, the error $-\frac{h^2}{2}\sin(\xi) = O(h^2)$. This approximates $\sin(x+h)$ to order 1 in $h$.

**Example 2:** $\ln(1+h) = h - \frac{h^2}{2} + \frac{h^3}{3} - \cdots$, applying the theorem to $f(x) = \ln x$ at $x=1$.

**Uniqueness:** If $f \in C^\infty(-1,1)$ is expressed as an infinite series, it is uniquely determined — a **smooth function** has a unique Taylor series.

### Intermediate Value Theorem

For $f \in C[a,b]$ with $f(a)f(b) < 0$, there exists $\xi \in [a,b]$ such that $f(\xi) = 0$.

### Mean Value Theorem

For $f \in C^1[a,b]$ with $a < b$, there exists $\xi \in [a,b]$ such that:

$$f'(\xi) = \frac{f(b) - f(a)}{b - a}$$

### Leibniz Formula for $\pi$

$$\pi = 4\!\left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots\right)$$

Derived by integrating $\dfrac{1}{1+t^2} = 1 - t^2 + t^4 - \cdots$ from 0 to 1, then substituting $x=1$ in $\tan^{-1} x$. Convergence is slow — error at the $n$th term is $\geq \dfrac{2}{15n^2}$.

---

## 4. Solving $f(x) = 0$

Given a continuous function $f$, find a root $x_*$ such that $f(x_*) = 0$.

### The Bisection Method

**Algorithm:**

1. Start with $[a,b]$ such that $f(a)f(b) < 0$
2. Compute midpoint $p = (a+b)/2$
3. If $b - a < h$ (tolerance), return $p$
4. If $f(a)f(p) < 0$: set $b = p$; else set $a = p$
5. Repeat

**Convergence:** After $k$ steps the interval width is $(b-a)/2^k$. To achieve accuracy $h$: need $k \geq \log_2\!\left(\frac{b-a}{h}\right)$ steps — a **linear time** algorithm.

**Example:** Root of $\sin x = 0.5$ on $[0, \pi/2]$:

| $k$ | $a$ | $b$ | $b-a$ |
|---|---|---|---|
| 0 | 0 | 1.5708 | 1.5708 |
| 1 | 0 | 0.7854 | 0.7854 |
| 2 | 0.3927 | 0.7854 | 0.3927 |
| 3 | 0.3927 | 0.5890 | 0.1963 |
| 4 | 0.4909 | 0.5890 | 0.0982 |

Final answer: $y = 0.5400$, $f(y) = 0.0141$.

---

### Newton's Method

**Algorithm:** Given initial guess $x_0$, for $k = 0, 1, 2, \ldots$:

$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$

until $\lvert x_{k+1} - x_k\rvert < h$ or $\lvert f(x_{k+1})\rvert < h$.

**Quadratic Convergence (Theorem 1):** If $f \in C^2[a,b]$ has a unique root $x_*$ with nonzero derivative everywhere, there exists $M > 0$ such that:

$$\lvert x_{k+1} - x_*\rvert \leq M\lvert x_k - x_*\rvert^2$$

*Proof sketch:* By Newton's iteration and Taylor series of order 1:

$$x_{k+1} - x_* = \frac{(x_k - x_*)^2 f''(\xi)}{2f'_k} \implies \lvert x_{k+1} - x_*\rvert \leq M\lvert x_k - x_*\rvert^2$$

where

$$M = \frac{\max_{t\in[a,b]}\lvert f''(t)\rvert}{2\min_{t\in[a,b]}\lvert f'(t)\rvert}$$

**Linear convergence:** $\lvert x_{k+1} - x_*\rvert \leq \rho\lvert x_k - x_*\rvert$ for $\rho \in (0,1)$.

**Theorem 2:** If $f \in C^2[a,b]$ with $f(a)f(b) \neq 0$, $f'(x) \neq 0$, $f''$ does not change sign, and $\left\lvert\frac{f(a)}{f'(a)}\right\rvert, \left\lvert\frac{f(b)}{f'(b)}\right\rvert < b-a$, then Newton's method converges from any $x_0 \in [a,b]$.

**Theorem 4:** For a root of multiplicity $m > 1$, the modified iteration

$$x_{k+1} = x_k - \frac{m\,f(x_k)}{f'(x_k)}$$

converges quadratically.

**Counter-example:** Newton's method diverges on

$$f(x) = -\frac{x^8}{8} + \frac{x^6}{2} - \frac{3x^4}{4} + \frac{x^2}{2}$$

near $x_0 = 1 - a$ for small $a$, since $f'(x)$ has triple roots at $x = \pm 1$.

---

### The Secant Method

Approximates $f'(x_k)$ by a finite difference:

$$f'(x_k) \approx \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}$$

**Algorithm:** Start with $x_0, x_1$; for $k = 1, 2, \ldots$:

$$x_{k+1} = x_k - \frac{f(x_k)(x_k - x_{k-1})}{f(x_k) - f(x_{k-1})}$$

**Superlinear convergence** with rate $p = \dfrac{1+\sqrt{5}}{2} \approx 1.61$. Does not require $f'(x)$ explicitly.

**Comparison for minimizing $\phi(t) = 10\cosh(t/4) - t$:**

| Method | Iterations to reach $f < 10^{-6}$ |
|---|---|
| Newton | 3 |
| Secant | 4 |
| Bisection on $[0,3]$ | 19 |

---

## 5. Linear Algebra Basics

### Vector Spaces

A **vector space** $\mathcal{V}$ is a set closed under addition ($\mathbf{a}+\mathbf{b} \in \mathcal{V}$) and scalar multiplication ($t\mathbf{a} \in \mathcal{V}$).

**Linear independence:** $k$ vectors $\mathbf{a}_1, \ldots, \mathbf{a}_k$ are linearly independent iff

$$t_1\mathbf{a}_1 + \cdots + t_k\mathbf{a}_k = \mathbf{0} \iff t_1 = \cdots = t_k = 0$$

A **basis** is a maximal linearly independent set. The **dimension** of $\mathcal{V}$ is the cardinality of any basis (always the same regardless of choice — Theorem of Basis).

**Example in $\mathbb{R}^2$:** $\mathbf{e}_1 = \begin{pmatrix}1\\0\end{pmatrix}$, $\mathbf{e}_2 = \begin{pmatrix}0\\1\end{pmatrix}$. Any $\mathbf{a} = t_1\mathbf{e}_1 + t_2\mathbf{e}_2$, and $t_1\mathbf{e}_1 + t_2\mathbf{e}_2 = \mathbf{0} \iff t_1 = t_2 = 0$. So $\{\mathbf{e}_1,\mathbf{e}_2\}$ is a basis and $\dim(\mathbb{R}^2) = 2$.

### Matrices and the Block Multiplication Rule (BMR)

$\mathbb{R}^{m \times n}$ is the set of $m \times n$ real matrices. The **BMR**: submatrix blocks can be multiplied as if they were scalars, as long as sizes are consistent.

**Transpose:** $(AB)^T = B^T A^T$. A matrix is **symmetric** if $A = A^T$.

**Dot product:** $\mathbf{x}^T\mathbf{y} = \sum_i x_i y_i$ (the inner product).

### Range and Rank

$$\text{Range}(A) = \{A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\}$$

The **rank** of $A$ is the maximum number of linearly independent columns. Row rank equals column rank for any $A$.

The **null space** is $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$, with dimension $n - \text{rank}(A)$.

### Inverse

For a square nonsingular $A$ ($\det A \neq 0$), there exists a unique $A^{-1}$ with $AA^{-1} = A^{-1}A = I$.

For $A = \begin{pmatrix}a & b \\ c & d\end{pmatrix}$:

$$A^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d & -b \\ -c & a\end{pmatrix}$$

---

## 6. Gaussian Elimination

### Elementary Row Operations

Two types:
1. **Switch** two rows — implemented by a permutation matrix $P_{ij}$
2. **Add** a scalar multiple of one row to another — implemented by a lower triangular matrix

**Theorem:** Elementary row operations do not change the null space of $A$, so they preserve the solution set of $A\mathbf{x} = \mathbf{b}$.

### Worked Example

Augmented matrix for a $3 \times 3$ system:

$$\begin{pmatrix}2 & 3 & 2 & 1 \\ 1 & \frac{1}{2} & \frac{1}{2} & 0 \\ 3 & 3 & 3 & \frac{9}{4}\end{pmatrix}$$

After $R_2 \leftarrow R_2 - \frac{1}{2}R_1$, $R_3 \leftarrow R_3 - \frac{3}{2}R_1$, $R_3 \leftarrow R_3 - \frac{3}{2}R_2$:

$$U = \begin{pmatrix}2 & 3 & 2 \\ 0 & -1 & -\frac{1}{2} \\ 0 & 0 & \frac{3}{4}\end{pmatrix}$$

Back substitution gives: $x_3 = 2$, $x_2 = -\frac{1}{2}$, $x_1 = -\frac{3}{4}$.

### Running Time

Gaussian elimination uses $\frac{2}{3}n^3 + O(n^2)$ flops. Back substitution uses $O(n^2)$. Total: $O(n^3)$.

### LU Decomposition

**Theorem:** For a nonsingular $A \in \mathbb{R}^{n \times n}$, there exist lower triangular $L$ (ones on diagonal) and upper triangular $U$ such that $A = LU$.

**Solving $A\mathbf{x} = \mathbf{b}$ via LU:**

1. Factor $A = LU$ by Gaussian elimination
2. Solve $L\mathbf{y} = \mathbf{b}$ by forward substitution
3. Solve $U\mathbf{x} = \mathbf{y}$ by back substitution

The multipliers $l_{ik} = a_{ik}/a_{kk}$ fill the lower triangle of $L$. Each elementary matrix is lower triangular, so $L$ is lower triangular.

### Gaussian Elimination with Partial Pivoting

At step $k$, find row $j$ with the largest $\lvert A^{(k)}_{j,k+1}\rvert$, then swap it to the pivot position before eliminating.

**PLU Decomposition:** For any nonsingular $A$, there exists a permutation matrix $P$ such that $PA = LU$.

On MATLAB: `[L, U, P] = lu(A)`.

Running time: $O(n^3)$ total (pivoting adds only $O(n^2)$ extra).

### Cholesky Decomposition

A matrix $A$ is **Symmetric Positive Definite (SPD)** if $A = A^T$ and $\mathbf{x}^T A\mathbf{x} > 0$ for all nonzero $\mathbf{x}$.

**Theorem:** For SPD $A$, there uniquely exists lower triangular $L$ with positive diagonal entries such that $A = LL^T$.

Benefits: $\frac{1}{3}n^3 + O(n^2)$ flops (twice as fast as GE), no pivoting needed.

On MATLAB: `L = chol(A)'`.

---

## 7. Norms and Condition Numbers

### Vector Norms

The **$p$-norm** of $\mathbf{x} \in \mathbb{R}^n$:

$$\|\mathbf{x}\|_p = \left(\sum_{i=1}^n \lvert x_i\rvert^p\right)^{1/p}, \qquad \|\mathbf{x}\|_\infty = \max_{1 \leq i \leq n}\lvert x_i\rvert$$

**Axioms of a vector norm:** For all $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$ and $\alpha \in \mathbb{R}$:

1. $\|\mathbf{x}\| \geq 0$, and $\|\mathbf{x}\| = 0 \iff \mathbf{x} = \mathbf{0}$
2. $\|\alpha\mathbf{x}\| = \lvert\alpha\rvert\,\|\mathbf{x}\|$
3. $\|\mathbf{x}+\mathbf{y}\| \leq \|\mathbf{x}\|+\|\mathbf{y}\|$ (triangle inequality)

**Norm relationships:**

$$\|\mathbf{x}\|_\infty \leq \|\mathbf{x}\|_2 \leq \|\mathbf{x}\|_1 \leq \sqrt{n}\,\|\mathbf{x}\|_2 \leq n\,\|\mathbf{x}\|_\infty$$

### Matrix Norm and Condition Number

$$\|A\| = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|} = \max_{\|\mathbf{x}\|=1}\|A\mathbf{x}\|$$

$$\kappa(A) = \|A\|\,\|A^{-1}\|$$

**Induced matrix norms** (derived from the corresponding vector norm):

$$\|A\|_\infty = \max_{1 \leq i \leq m}\sum_{j=1}^n\lvert A_{i,j}\rvert, \qquad \|A\|_1 = \max_{1 \leq j \leq n}\sum_{i=1}^m\lvert A_{i,j}\rvert$$

**Frobenius norm:**

$$\|A\|_F = \left(\sum_{i=1}^m\sum_{j=1}^n A_{i,j}^2\right)^{1/2}$$

**Axioms of a matrix norm:** $\|A\| \geq 0$; $\|A\| = 0 \iff A = 0$; $\|\alpha A\| = \lvert\alpha\rvert\|A\|$; $\|A+B\| \leq \|A\|+\|B\|$; $\|AB\| \leq \|A\|\|B\|$.

### Error Analysis via Condition Number

The computed solution $\hat{\mathbf{x}}$ of $A\mathbf{x} = \mathbf{b}$ carries residual $\hat{\mathbf{r}} = \mathbf{b} - A\hat{\mathbf{x}}$. The relative error satisfies:

$$\frac{\|\mathbf{x} - \hat{\mathbf{x}}\|}{\|\mathbf{x}\|} \leq \kappa(A)\frac{\|\hat{\mathbf{r}}\|}{\|\mathbf{b}\|}$$

A large condition number means the system is **ill-conditioned** — small residuals do not guarantee small errors.

---

## 8. Polynomial Interpolation

### The Interpolation Problem

**Given:** $n+1$ data points $\{(x_i, y_i)\}$ with distinct abscissae $x_i \in [a,b]$ and $y_i = f(x_i)$.

**Find:** coefficients $c_j$ such that $p_n(x) = \sum_{j=0}^n c_j\phi_j(x)$ satisfies $y_i = p_n(x_i)$ for all $i$.

Solve the linear system $Xc = y$ where $X_{ij} = \phi_j(x_i)$. The interpolation matrix $X$ must be nonsingular.

**Horner's rule:** Evaluate a degree-$n$ polynomial in $O(n)$ flops:

$$p_n(x) = c_0 + x\bigl(c_1 + x(c_2 + \cdots + x\,c_n)\cdots\bigr)$$

---

### Monomial (Vandermonde) Interpolation

Basis $\phi_j(x) = x^j$. The data point matrix is the **Vandermonde matrix**:

$$X = \begin{pmatrix}1 & x_0 & x_0^2 & \cdots & x_0^n \\ 1 & x_1 & x_1^2 & \cdots & x_1^n \\ \vdots & & & & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^n\end{pmatrix}$$

**Theorem:** The Vandermonde matrix is nonsingular iff the abscissae are distinct.

*Proof:* If $X$ were singular, $Xc = 0$ for some nonzero $c$, giving a degree-$n$ polynomial $p(x) = \sum c_j x^j$ with $n+1$ distinct roots — impossible by the fundamental theorem of algebra.

**Limitation:** The Vandermonde matrix can be severely ill-conditioned for large $n$.

---

### Lagrange Interpolation

Find basis satisfying $\phi_j(x_i) = 1$ if $i=j$, and $0$ if $i \neq j$.

**Lagrange polynomials:**

$$L_j(x) = \prod_{\substack{0 \leq i \leq n \\ i \neq j}} \frac{x - x_i}{x_j - x_i}$$

The interpolant:

$$p_n(x) = \sum_{j=0}^n y_j\,L_j(x)$$

**Example:** For $\{(1,1),(2,3),(4,3)\}$:

$$L_0(x) = \frac{(x-2)(x-4)}{3}$$

$$p_2(x) = \frac{(x-2)(x-4)}{3} - \frac{3(x-1)(x-4)}{2} + \frac{(x-1)(x-2)}{2}$$

Evaluation cost: $O(n)$ flops with precomputation. **Most numerically stable** of the three methods.

---

### Newton's Interpolation

Basis: $\phi_0(x) = 1$, $\phi_j(x) = \prod_{i=0}^{j-1}(x - x_i)$. The data point matrix is **lower triangular** — solve by forward substitution.

**Divided Differences:**

$$f[x_i] = f(x_i), \qquad f[x_i, x_j] = \frac{f[x_j] - f[x_i]}{x_j - x_i}$$

$$f[x_0, x_1, \ldots, x_k] = \frac{f[x_1,\ldots,x_k] - f[x_0,\ldots,x_{k-1}]}{x_k - x_0}$$

**Theorem 1:** $c_j = f[x_0, x_1, \ldots, x_j]$.

**Theorem 2 (Error):**

$$f(x) = p_n(x) + f[x_0, \ldots, x_n, x]\prod_{i=0}^n(x - x_i)$$

**Recursive advantage:** On arrival of new point $(x_n, y_n)$:

$$c_n = \frac{y_n - p_{n-1}(x_n)}{\phi_n(x_n)}$$

computed in $O(n)$ flops — **adaptive** interpolation.

### Summary of Three Methods

| Method | Basis | Construction cost | Evaluation cost | Feature |
|---|---|---|---|---|
| Monomial | $x^j$ | $\tfrac{2}{3}n^3$ | $2n$ | Simple |
| Lagrange | $L_j(x)$ | $n^2$ | $5n$ | Most stable |
| Newton | $\prod_{i < j}(x-x_i)$ | $\tfrac{1}{3}n^2$ | $2n$ | Adaptive |

---

## 9. Splines

### Motivation

A single degree-$n$ polynomial can be poorly behaved for large $n$ (Runge's phenomenon, ill-conditioning). Instead use **piecewise polynomials** on each strip $[x_i, x_{i+1}]$.

### Definition

A function $s \in C^{m-1}[a,b]$ is a **spline of degree $m$** with breakpoints $a = x_0 < x_1 < \cdots < x_n = b$ if it reduces to a polynomial of degree $\leq m$ on each $[x_i, x_{i+1}]$.

**Cubic spline:** $m = 3$, so $s \in C^2[a,b]$.

### Cubic Spline Construction

Each piece:

$$s_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3, \qquad a_i = y_i$$

Constraints from interpolation and $C^1$/$C^2$ continuity at breakpoints give $3n-2$ equations for $3n$ unknowns. Two extra boundary conditions are required.

**Three boundary options:**

1. **Natural:** $s_0''(x_0) = s_{n-1}''(x_n) = 0$
2. **Clamped:** $s_0'(x_0) = f'(x_0)$, $s_{n-1}'(x_n) = f'(x_n)$
3. **Not-a-knot:** $s_0'''(x_1) = s_1'''(x_1)$ and $s_{n-2}'''(x_{n-1}) = s_{n-1}'''(x_{n-1})$

**Algorithm:** Solve the symmetric tridiagonal system for $c_i$:

$$h_{i-1}c_{i-1} + 2(h_{i-1}+h_i)c_i + h_i c_{i+1} = 3\bigl(f[x_i, x_{i+1}] - f[x_{i-1}, x_i]\bigr)$$

with $h_i = x_{i+1} - x_i$. Then recover $d_i$ and $b_i$ from formulas (11.4a,b).

The matrix $X$ in this system is symmetric, tridiagonal, and diagonally dominant.

**Theorem 1:** A diagonally dominant square matrix is nonsingular.

**Theorem 2:** The PLU decomposition of a nonsingular tridiagonal matrix takes $O(n)$ flops.

**Example (11.4):** Natural cubic spline through $\{(0,1.1),(1,0.9),(2,2)\}$:

$$s_0(x) = 1.1 - 0.525x + 0.325x^3, \quad x < 1$$

$$s_1(x) = 0.9 + 0.45(x-1) + 0.975(x-1)^2 - 0.325(x-1)^3, \quad x \geq 1$$

---

## 10. Numerical Integration (Quadrature)

### Idea

Approximate $\int_a^b f(x)\,dx$ by integrating the interpolant $p_n(x)$ on small subintervals, then summing. When abscissae are evenly spaced, the resulting formulas are called **Newton-Cotes formulas**.

### Trapezoid Rule ($n=1$)

Integrate the linear interpolant on $[a,b]$:

$$\int_a^b p_1(x)\,dx = \frac{b-a}{2}\bigl(f(a) + f(b)\bigr)$$

**Error:** $E(f) = -\dfrac{f''(\xi)}{12}(b-a)^3$ for some $\xi \in [a,b]$.

### Simpson's Rule ($n=2$)

With $x_0=a$, $x_1=\frac{a+b}{2}$, $x_2=b$:

$$\int_a^b f(x)\,dx \approx \frac{b-a}{6}\!\left[f(a) + 4f\!\left(\frac{a+b}{2}\right) + f(b)\right]$$

**Error:** $E(f) = -\dfrac{f^{(4)}(\xi)}{90}\!\left(\dfrac{b-a}{2}\right)^5$ — accuracy order 5 per strip.

### Composite Trapezoidal Method

Divide $[a,b]$ into $n$ strips of width $h = (b-a)/n$:

$$\int_a^b f(x)\,dx \approx h\!\left[\frac{f(a)}{2} + f(x_1) + \cdots + f(x_{n-1}) + \frac{f(b)}{2}\right]$$

**Error bound:**

$$\lvert E(f)\rvert \leq \frac{h^2(b-a)}{12}\max_{a \leq \xi \leq b}\lvert f''(\xi)\rvert = O(h^2)$$

**Accuracy order 2.**

### Composite Simpson Method

Use $n$ paired strips ($m = 2n$ fine strips), $h = (b-a)/m$:

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\!\left[f(a) + 4f(t_1) + 2f(t_2) + 4f(t_3) + \cdots + 4f(t_{2n-1}) + f(b)\right]$$

**Error bound:**

$$\lvert E(f)\rvert \leq \frac{h^4(b-a)}{180}\max_{a \leq \xi \leq b}\lvert f^{(4)}(\xi)\rvert = O(h^4)$$

**Accuracy order 4.** One of the most commonly used numerical integration methods.

**Example (15.5):** Approximate $\int_0^1 e^{-x^2}\,dx$ with error $< 10^{-5}$.

Since $\lVert f^{(4)}\rVert_\infty = 12$ on $[0,1]$:

$$\lvert E(f)\rvert \leq \frac{12h^4}{180} = \frac{1}{15r^4} < 10^{-5} \implies r = 10 \text{ strips suffice}$$

$$\int_0^1 e^{-x^2}\,dx \approx 0.746824133\ldots$$

### Improper Integrals

To compute $I = \int_0^\infty e^{-x^2}\,dx$:

1. Split into $I_1 = \int_0^{2b} e^{-x^2}\,dx$ and $I_2 = \int_{2b}^\infty e^{-x^2}\,dx$
2. Bound $I_2 \leq \dfrac{e^{-4b^2}}{3b}$ — choose $b=2$ so $I_2 < 1.8756 \times 10^{-8}$
3. Apply composite Simpson to $I_1$ with the required number of strips

---

## 11. Romberg Integration

Uses **extrapolation** to eliminate low-order error terms and achieve higher accuracy without extra function evaluations.

The composite trapezoidal error expands as:

$$I - T(h) = K_2 h^2 + K_4 h^4 + K_6 h^6 + \cdots$$

for constants $K_{2j}$ independent of $h$.

**One step of extrapolation:** Compute $R_{1,1} = T(2h)$ and $R_{2,1} = T(h)$. Then:

$$I = \frac{4R_{2,1} - R_{1,1}}{3} + O(h^4)$$

This is **identical to the composite Simpson method**.

**General extrapolation formula:**

$$R_{j+1,k} = R_{j+1,k-1} + \frac{R_{j+1,k-1} - R_{j,k-1}}{4^{k-1}-1}, \quad k = 2, 3, \ldots, j+1$$

$R_{j,j}$ gives an $O(h^{2j})$-accurate approximation. The full Romberg table achieves arbitrarily high accuracy by repeating this process.

---

## 12. Initial Value Problems (IVPs)

### Formulation

**Simple IVP:** Given $f:\mathbb{R}\times\mathbb{R}\to\mathbb{R}$, find $y:[a,b]\to\mathbb{R}$ such that:

$$\frac{dy}{dt} = f(t, y(t)), \qquad y(a) = y_0$$

**Vector IVP:** Same but $\mathbf{f}:[a,b]\times\mathbb{R}^m\to\mathbb{R}^m$, finding $\mathbf{y}:[a,b]\to\mathbb{R}^m$.

**Unique Existence Theorem:** If $f$ has bounded partial derivatives and satisfies the Lipschitz condition

$$\lVert f(t,\mathbf{y}_1) - f(t,\mathbf{y}_2)\rVert \leq L\lVert\mathbf{y}_1 - \mathbf{y}_2\rVert$$

then the IVP has a unique continuous differentiable solution.

### Forward Euler Method

Let $t_i = ih$, $h = b/n$. Update rule:

$$y_{i+1} = y_i + h\,f(t_i, y_i)$$

Justified by Taylor series of order 1: $y(t_{i+1}) = y(t_i) + hy'(t_i) + O(h^2)$.

**Global error:** $O(h^2)\cdot n = O(h)$ — **accuracy order 1**.

**Example (16.1):** $y' = -y + t$, $y(0) = c$. Exact solution: $y(t) = t - 1 + (c+1)e^{-t}$.

**Spring motion (vector IVP):** $u'' + \omega^2 u = 0$. Set $\mathbf{y} = \begin{pmatrix}u \\ u'\end{pmatrix}$:

$$\mathbf{f}(t,\mathbf{y}) = \begin{pmatrix}y_2 \\ -\omega^2 y_1\end{pmatrix}$$

**Pendulum simulation (MATLAB):**

```matlab
n = 500; y = zeros(2, n+1); v = 1; g = 9.81;
y(1,1) = 0; y(2,1) = v; h = 10/n;
for i = 2:n+1
  y(:,i) = y(:,i-1) + h * [y(2,i-1); -g*sin(y(1,i-1))];
end
t = linspace(0, 10, n+1);
plot(t, y(1,:))
```

$n=500$ is too small (total energy drifts upward); $n=50000$ stabilizes.

### Accuracy Order

The **local truncation error** $d_i$ is the max one-step error from the Taylor series used. The **accuracy order** is the max $q$ such that $d_i = O(h^{q+1})$. For forward Euler: $q = 1$.

### Absolute Stability and Stiffness

Test equation: $y' = \lambda y$ with $\lambda < 0$. Euler gives $y_{i+1} = (1+h\lambda)y_i$.

Requiring $\lvert y_{i+1}\rvert \leq \lvert y_i\rvert$:

$$\lvert 1 + h\lambda\rvert \leq 1 \implies h \leq \frac{2}{\lvert\lambda\rvert}$$

An IVP requiring a step smaller than some given upper bound is called **stiff**.

---

## 13. Runge-Kutta Methods

All IVP methods approximate the integral:

$$y(t_{i+1}) = y(t_i) + \int_{t_i}^{t_{i+1}} f(t, y(t))\,dt$$

Forward Euler uses a rectangle; RK methods use higher-order quadrature.

### Explicit Trapezoidal RK (Order 2)

Approximate $y(t_{i+1})$ first by an Euler step, then apply the trapezoid rule:

$$Y = y_i + h\,f(t_i, y_i)$$

$$y_{i+1} = y_i + \frac{h}{2}\!\left[f(t_i, y_i) + f(t_{i+1}, Y)\right]$$

### Explicit Midpoint Method (Order 2)

$$Y = y_i + \frac{h}{2}f(t_i, y_i), \qquad y_{i+1} = y_i + h\,f\!\left(\tfrac{t_i+t_{i+1}}{2},\, Y\right)$$

### Classical RK Method of Order 4

Based on Simpson's rule. Four stages per step:

$$Y_1 = y_i$$

$$Y_2 = y_i + \frac{h}{2}f(t_i, Y_1)$$

$$Y_3 = y_i + \frac{h}{2}f(t_{i+1/2}, Y_2)$$

$$Y_4 = y_i + h\,f(t_{i+1/2}, Y_3)$$

$$y_{i+1} = y_i + \frac{h}{6}\!\left[f(t_i,Y_1) + 2f(t_{i+1/2},Y_2) + 2f(t_{i+1/2},Y_3) + f(t_{i+1},Y_4)\right]$$

### Comparison (for $y' = -y^2$, $y(1) = 1$)

The rate $= \log_2\!\left(\dfrac{e(2h)}{e(h)}\right)$ where $e(h) = \max_i\lvert y_i - y(t_i)\rvert$.

| $h$ | Euler | Rate | RK2 | Rate | RK4 | Rate |
|---|---|---|---|---|---|---|
| 0.1 | 2.3e-3 | 1.01 | 7.4e-5 | 2.15 | 1.4e-8 | 3.90 |
| 0.05 | 1.2e-3 | 1.01 | 1.8e-5 | 2.07 | 8.6e-10 | 3.98 |
| 0.01 | 2.3e-4 | 1.00 | 6.8e-7 | 2.01 | 1.4e-12 | 4.00 |
| 0.005 | 1.2e-4 | 1.00 | 1.7e-7 | 2.01 | 8.7e-14 | 4.00 |

Rates confirm accuracy orders 1, 2, and 4 as predicted.

---

## 14. Multi-Step Methods (Adams-Bashforth)

**Multi-step methods** approximate $\int_{t_i}^{t_{i+1}} f(t,y(t))\,dt$ by interpolating several previous values of $f$.

### Two-Step Adams-Bashforth

Interpolate $(t_i, f_i)$ and $(t_{i-1}, f_{i-1})$ by Newton's basis and integrate over $[t_i, t_{i+1}]$:

$$y_{i+1} = y_i + h\!\left(\frac{3}{2}f_i - \frac{1}{2}f_{i-1}\right)$$

**Accuracy order 2.**

### Three-Step Adams-Bashforth

Interpolate three previous values and integrate:

$$y_{i+1} = y_i + \frac{h}{12}(23f_i - 16f_{i-1} + 5f_{i-2})$$

### Four- and Five-Step Formulas

$$y_{i+1} = y_i + \frac{h}{24}(55f_i - 59f_{i-1} + 37f_{i-2} - 9f_{i-3}) \qquad \text{(order 4)}$$

$$y_{i+1} = y_i + \frac{h}{720}(1901f_i - 2774f_{i-1} + 2616f_{i-2} - 1274f_{i-3} + 251f_{i-4}) \qquad \text{(order 5)}$$

**Key property:** Once started, each new step costs only $O(1)$ extra function evaluations — the method is **adaptive**.

RK and multi-step methods are the two most traditional methodologies for solving ODEs numerically.
