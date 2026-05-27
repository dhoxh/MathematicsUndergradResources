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

A naive implementation recomputes $x^i$ and $i!$ from scratch each step — that's $O(n^2)$ flops. The improved version (MySine2) maintains a running term $t$ and updates it:

```matlab
function s = MySine2(x, n)
  s = x; t = x;
  for i = 3:2:n
    t = -t * x^2 / (i*(i-1));
    s = s + t;
  end
end
```

This runs in $O(n)$ time because at most 6 flops are executed per iteration.

**Error analysis:** For $x \in (0,1)$ and $n$ odd:

$$|{residual}(x,n)| = |\sin x - MySine(x,n)| = O\!\left(\frac{x^n}{n!}\right)$$

which is very small for large enough $n$.

### Big-O and $\Theta$ Notation

$$f = O(g) \iff |f(x)| \leq c\,g(x) \text{ for some constant } c > 0 \text{ and all } x \in [a,b]$$

$$f = \Theta(g) \iff f = O(g) \text{ and } g = O(f)$$

$O(g)$ is an **asymptotic upper bound**; $\Theta(g)$ is **asymptotic equality**.

---

## 2. Floating Point Arithmetic

### Definition of a Floating Point Number

A number $x$ is a floating point number if

$$x = \pm d \cdot \beta^e$$

where $d \geq 0$, base $\beta \in \{2, 10\}$, integer exponent $e \in [e_{\min}, e_{\max}]$, and mantissa

$$d = d_1\beta^{-1} + d_2\beta^{-2} + \cdots + d_t\beta^{-t}$$

with each $d_i \in \{0,1\}$ (when $\beta = 2$) and precision $t$.

### The Floating Point System $(\beta,\, t,\, e_{\min},\, e_{\max})$

| Quantity | Definition | Meaning |
|---|---|---|
| $fl(x)$ | closest floating point number to $x$ | rounding function |
| $\varepsilon_M = \beta^{-t}$ | machine unit | smallest difference from 1 |
| $\Omega = (1-\beta^{-t})\cdot\beta^{e_{\max}}$ | largest computer number | overflow boundary |
| $\omega = \beta^{1-t+e_{\min}}$ | smallest computer number | underflow boundary |

**Gradual underflow:** Keep $x$ as-is even if $d_1 = 0$.

### IEEE Standards

| Standard | $\beta$ | $t$ | $e_{\min}$ | $e_{\max}$ | $\varepsilon_M$ | $\Omega$ |
|---|---|---|---|---|---|---|
| Single precision | 2 | 24 | $-126$ | 128 | $\approx 5.96 \times 10^{-8}$ | $\approx 3.40 \times 10^{38}$ |
| Double precision | 2 | 53 | $-1022$ | 1024 | $\approx 1.11 \times 10^{-16}$ | $\approx 1.80 \times 10^{308}$ |

### Key Examples

**Example 1:** Plain Gaussian elimination on

$$\begin{pmatrix}10^{-17} & 1 \\ 1 & 1\end{pmatrix}$$

gives $x_1 = 0$, $x_2 = 1$ — drastically wrong because $10^{-17}$ is truncated when added to 1.

**Example 2:** On $\beta = 10$, $t = 4$, $-7 \leq e \leq 7$:

$x = 0.1957 \times 10^{-7}$, $y = 0.1942 \times 10^{-7}$, $z = x - y$:

$$z = fl(x-y) = 0.015 \times 10^{-7}$$

By gradual underflow $d_1 = 0$ but $z \neq 0$.

**Example 3 (Double precision):** $f(10^{-12}) = 0$ where $f(x) = \sqrt{1+x^2} - 1$.

Use the equivalent form:

$$g(x) = \frac{x^2}{\sqrt{1+x^2}+1}$$

$$g(10^{-12}) \approx \frac{10^{-24}}{\sqrt{1+10^{-24}}+1} \approx \frac{10^{-24}}{2} = 0.5 \times 10^{-24}$$

**Common trick:** Avoid dividing by a small number, or subtracting expressions that produce a small result.

---

## 3. Taylor Series

### Theorem (Taylor Series)

Assume $f(x)$ has $k+1$ derivatives on an interval containing $x_0$ and $x_0 + h$. Then:

$$f(x_0 + h) = f(x_0) + hf'(x_0) + \frac{h^2}{2}f''(x_0) + \cdots + \frac{h^k}{k!}f^{(k)}(x_0) + \frac{h^{k+1}}{(k+1)!}f^{(k+1)}(\xi)$$

where $\xi$ is some point between $x_0$ and $x_0 + h$.

The three most useful cases: $k = 1$, $k = 2$, and $k = \infty$.

### Function Spaces

| Space | Meaning |
|---|---|
| $C[a,b]$ | Functions continuous on $[a,b]$ |
| $C^1[a,b]$ | Continuously differentiable on $[a,b]$ |
| $C^k[a,b]$ | $k$ times continuously differentiable |

### Examples

**Example 1:** $\sin(x+h) = \sin x + h\cos x + O(h^2)$

By the theorem with $k=1$: since $\left|\frac{1}{2}\sin(\xi)\right| \leq \frac{1}{2}$, the error term $-\frac{h^2}{2}\sin(\xi) = O(h^2)$.

**Example 2:** $\ln(1+h) = h - \frac{h^2}{2} + \frac{h^3}{3} - \cdots$ (applying the theorem to $f(x) = \ln x$ at $x=1$).

**Uniqueness of Taylor series:** If $f \in C^\infty(-1,1)$ is expressed as an infinite series, it is uniquely determined — a **smooth function** has a unique Taylor series.

### Intermediate Value Theorem

For $f \in C[a,b]$ with $f(a)f(b) < 0$, there exists $\xi \in [a,b]$ such that $f(\xi) = 0$.

### Mean Value Theorem

For $f \in C^1[a,b]$ with $a < b$, there exists $\xi \in [a,b]$ such that:

$$f'(\xi) = \frac{f(b) - f(a)}{b - a}$$

### Leibniz Formula for $\pi$

$$\pi = 4\!\left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots\right)$$

Derived by integrating $\dfrac{1}{1+t^2} = 1 - t^2 + t^4 - \cdots$ from 0 to 1, then substituting $x=1$ in $\tan^{-1} x$.

Convergence is slow — the error at the $n$th term is $\geq \dfrac{2}{15n^2}$, much larger than $O(h^n)$.

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

**Convergence:** After $k$ steps, the interval width is $(b-a)/2^k$. To achieve accuracy $h$: need $k \geq \log_2\!\left(\frac{b-a}{h}\right)$ steps — a linear time algorithm.

**Example:** Finding the root of $\sin x = 0.5$ on $[0, \pi/2]$:

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

until $|x_{k+1} - x_k| < h$ or $|f(x_{k+1})| < h$.

**Quadratic Convergence (Theorem 1):** If $f \in C^2[a,b]$ has a unique root $x_*$ with nonzero derivative everywhere, there exists $M > 0$ such that:

$$|x_{k+1} - x_*| \leq M|x_k - x_*|^2$$

*Proof sketch:* By Newton's iteration and Taylor series of order 1:

$$x_{k+1} - x_* = \frac{(x_k - x_*)^2 f''(\xi)}{2f'_k} \implies |x_{k+1} - x_*| \leq M|x_k - x_*|^2$$

where $M = \dfrac{\max_{t\in[a,b]}|f''(t)|}{2\min_{t\in[a,b]}|f'(t)|}$.

**Linear convergence:** $|x_{k+1} - x_*| \leq \rho|x_k - x_*|$ for $\rho \in (0,1)$.

**Convergence theorems:**

*Theorem 2:* If $f \in C^2[a,b]$ with $f(a)f(b) \neq 0$, $f'(x) \neq 0$, $f''$ does not change sign, and $\left|\frac{f(a)}{f'(a)}\right|, \left|\frac{f(b)}{f'(b)}\right| < b-a$, then Newton's method converges from any $x_0 \in [a,b]$.

*Theorem 4:* For a root of multiplicity $m > 1$, the modified iteration

$$x_{k+1} = x_k - \frac{m\,f(x_k)}{f'(x_k)}$$

converges quadratically.

**Counter-example:** Newton's method diverges on $f(x) = -\dfrac{x^8}{8} + \dfrac{x^6}{2} - \dfrac{3x^4}{4} + \dfrac{x^2}{2}$ near $x_0 = 1 - a$ for small $a$, since $f'(x)$ has triple roots at $x = \pm 1$.

---

### The Secant Method

Approximates $f'(x_k)$ by a finite difference:

$$f'(x_k) \approx \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}$$

**Algorithm:** Start with $x_0, x_1$; for $k = 1, 2, \ldots$:

$$x_{k+1} = x_k - \frac{f(x_k)(x_k - x_{k-1})}{f(x_k) - f(x_{k-1})}$$

**Superlinear convergence** with rate $p = \dfrac{1+\sqrt{5}}{2} \approx 1.61$.

Does **not** require $f'(x)$ explicitly.

**Comparison for minimizing $\phi(t) = 10\cosh(t/4) - t$:**

| Method | Iterations to $f < 10^{-6}$ |
|---|---|
| Newton | 3 |
| Secant | 4 |
| Bisection on $[0,3]$ | 19 |

---

## 5. Linear Algebra Basics

### Vector Spaces

A **vector space** $\mathcal{V}$ is a set closed under addition ($\mathbf{a}+\mathbf{b} \in \mathcal{V}$) and scalar multiplication ($t\mathbf{a} \in \mathcal{V}$).

**Linear independence:** $k$ vectors $\mathbf{a}_1, \ldots, \mathbf{a}_k \in \mathcal{V}$ are linearly independent iff

$$t_1\mathbf{a}_1 + \cdots + t_k\mathbf{a}_k = \mathbf{0} \iff t_1 = \cdots = t_k = 0$$

A **basis** is a maximal linearly independent set. The **dimension** of $\mathcal{V}$ is the cardinality of any basis (the Theorem of Basis guarantees this is unique).

**Example in $\mathbb{R}^2$:** $\mathbf{e}_1 = \begin{pmatrix}1\\0\end{pmatrix}$, $\mathbf{e}_2 = \begin{pmatrix}0\\1\end{pmatrix}$ form the standard basis. Any $\mathbf{a} = t_1\mathbf{e}_1 + t_2\mathbf{e}_2$.

### Matrices and the Block Multiplication Rule (BMR)

$\mathbb{R}^{m \times n}$ is the set of $m \times n$ real matrices. The **BMR** says: submatrix blocks can be multiplied as if they were scalars, as long as their sizes are consistent.

**Transpose:** $(AB)^T = B^T A^T$. A matrix is **symmetric** if $A = A^T$.

**Dot product:** $\mathbf{x}^T\mathbf{y} = \sum_i x_i y_i$ (inner product).

### Range and Rank

$$\text{Range}(A) = \{A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\}$$

The **rank** of $A$ is the maximum number of linearly independent columns. **Theorem:** row rank = column rank for any $A$.

**Null space:** $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$ — has dimension $n - \text{rank}(A)$.

### Inverse

For a square nonsingular $A$ ($\det A \neq 0$), there exists a unique $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$.

If $A = \begin{pmatrix}a & b \\ c & d\end{pmatrix}$ then $A^{-1} = \dfrac{1}{ad-bc}\begin{pmatrix}d & -b \\ -c & a\end{pmatrix}$.

---

## 6. Gaussian Elimination

### Elementary Row Operations

Two types:
1. **Switch** two rows (implemented by a permutation matrix $P_{ij}$)
2. **Add** a scalar multiple of one row to another (implemented by a lower triangular matrix)

**Theorem:** Elementary row operations do not change the null space of $A$, so they preserve the solution set of $A\mathbf{x} = \mathbf{b}$.

### Worked Example

Solve the $3 \times 3$ system with augmented matrix:

$$\begin{pmatrix}2 & 3 & 2 & 1 \\ 1 & \frac{1}{2} & \frac{1}{2} & 0 \\ 3 & 3 & 3 & \frac{9}{4}\end{pmatrix}$$

After $R_2 \leftarrow R_2 - \frac{1}{2}R_1$, $R_3 \leftarrow R_3 - \frac{3}{2}R_1$, $R_3 \leftarrow R_3 - \frac{3}{2}R_2$:

$$U = \begin{pmatrix}2 & 3 & 2 \\ 0 & -1 & -\frac{1}{2} \\ 0 & 0 & \frac{3}{4}\end{pmatrix}$$

Back substitution gives: $x_3 = 2$, $x_2 = -\frac{1}{2}$, $x_1 = -\frac{3}{4}$.

### Running Time

| Step | Flops |
|---|---|
| Gaussian Elimination | $\frac{2}{3}n^3 + O(n^2)$ |
| Back substitution | $O(n^2)$ |
| Total | $O(n^3)$ |

### LU Decomposition

**Theorem:** For a nonsingular $A \in \mathbb{R}^{n \times n}$, there exist lower triangular $L$ (with ones on the diagonal) and upper triangular $U$ such that $A = LU$.

**Solving $A\mathbf{x} = \mathbf{b}$ via LU:**

1. Factor $A = LU$ (by Gaussian elimination)
2. Solve $L\mathbf{y} = \mathbf{b}$ by forward substitution
3. Solve $U\mathbf{x} = \mathbf{y}$ by backward substitution

**Finding $L$:** The multipliers $l_{ik} = a_{ik}/a_{kk}$ used in the elimination fill the lower triangle of $L$. Each elementary matrix for operation ii) is lower triangular, so their product $L$ is lower triangular.

### Gaussian Elimination with Partial Pivoting

At step $k$, before processing column $k$, find row $j$ such that $|A^{(k)}_{j,k+1}|$ is maximum, then swap rows $j$ and $k+1$.

**PLU Decomposition:** For any nonsingular $A$, there exists a permutation matrix $P$ such that $PA = LU$.

On MATLAB: `[L, U, P] = lu(A)`.

**Running time:** $O(n^3)$ for the LU plus $O(n^2)$ extra for pivoting — total still $O(n^3)$.

### Cholesky Decomposition (SPD Matrices)

A matrix $A$ is **Symmetric Positive Definite (SPD)** if $A = A^T$ and $\mathbf{x}^T A\mathbf{x} > 0$ for all nonzero $\mathbf{x}$.

**Theorem:** For an SPD $A$, there uniquely exists lower triangular $L$ with positive diagonal entries such that $A = LL^T$.

**Benefits:**
- Takes $\frac{1}{3}n^3 + O(n^2)$ flops — twice as fast as GE
- No pivoting needed (good stability)

On MATLAB: `L = chol(A)'`.

---

## 7. Norms and Condition Numbers

### Vector Norms

The **$p$-norm** of $\mathbf{x} \in \mathbb{R}^n$:

$$\|\mathbf{x}\|_p = \left(\sum_{i=1}^n |x_i|^p\right)^{1/p}, \quad \|\mathbf{x}\|_\infty = \max_{1 \leq i \leq n}|x_i|$$

**Axioms:** $\|\mathbf{x}\| \geq 0$; $\|\mathbf{x}\| = 0 \iff \mathbf{x} = \mathbf{0}$; $\|\alpha\mathbf{x}\| = |\alpha|\|\mathbf{x}\|$; $\|\mathbf{x}+\mathbf{y}\| \leq \|\mathbf{x}\|+\|\mathbf{y}\|$.

**Relationships:**

$$\|\mathbf{x}\|_\infty \leq \|\mathbf{x}\|_2 \leq \|\mathbf{x}\|_1 \leq \sqrt{n}\,\|\mathbf{x}\|_2 \leq n\,\|\mathbf{x}\|_\infty$$

### Matrix Norm and Condition Number

$$\|A\| = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|} = \max_{\|\mathbf{x}\|=1}\|A\mathbf{x}\|$$

$$\kappa(A) = \|A\|\,\|A^{-1}\|$$

**Frobenius norm:** $\|A\|_F = \left(\sum_{i=1}^m\sum_{j=1}^n A_{i,j}^2\right)^{1/2}$

Induced matrix norms:

$$\|A\|_\infty = \max_{1 \leq i \leq m}\sum_{j=1}^n|A_{i,j}|, \qquad \|A\|_1 = \max_{1 \leq j \leq n}\sum_{i=1}^m|A_{i,j}|$$

### Error Analysis via Condition Number

The computed solution $\hat{\mathbf{x}}$ of $A\mathbf{x} = \mathbf{b}$ has residual $\hat{\mathbf{r}} = \mathbf{b} - A\hat{\mathbf{x}}$. The relative error satisfies:

$$\frac{\|\mathbf{x} - \hat{\mathbf{x}}\|}{\|\mathbf{x}\|} \leq \kappa(A)\frac{\|\hat{\mathbf{r}}\|}{\|\mathbf{b}\|}$$

A large condition number means the system is **ill-conditioned** — small residuals do not guarantee small errors.

---

## 8. Polynomial Interpolation

### The Interpolation Problem

**Given:** $n+1$ data points $\{(x_i, y_i) : x_i \in [a,b],\, y_i = f(x_i),\, 0 \leq i \leq n\}$ with distinct abscissae $x_i$.

**Find:** $n+1$ coefficients $c_j$ such that $p_n(x) = \sum_{j=0}^n c_j\phi_j(x)$ satisfies $y_i = p_n(x_i)$ for all $i$.

**General process:** Solve the linear system $Xc = y$ where $X_{ij} = \phi_j(x_i)$. The interpolation matrix $X$ must be nonsingular.

**Horner's rule:** Evaluate a degree-$n$ polynomial in $O(n)$ flops by rewriting

$$p_n(x) = c_0 + x(c_1 + x(c_2 + \cdots + x\,c_n)\cdots)$$

---

### Monomial (Vandermonde) Interpolation

Basis: $\phi_j(x) = x^j$. The data point matrix is the **Vandermonde matrix**:

$$X = \begin{pmatrix}1 & x_0 & x_0^2 & \cdots & x_0^n \\ 1 & x_1 & x_1^2 & \cdots & x_1^n \\ \vdots & & & & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^n\end{pmatrix}$$

**Theorem:** The Vandermonde matrix is nonsingular iff the $n+1$ abscissae are distinct.

**Corollary:** For any $n+1$ data points with distinct abscissae, there exists a unique polynomial of degree $\leq n$ interpolating them.

*Proof:* If $X$ were singular, then $Xc = 0$ for some nonzero $c$, making $p(x) = \sum c_j x^j$ a degree-$n$ polynomial with $n+1$ distinct roots — impossible by the fundamental theorem of algebra.

**Limitation:** The Vandermonde matrix can be ill-conditioned for large $n$.

---

### Lagrange Interpolation

Find basis $\phi_j$ satisfying $\phi_j(x_i) = \begin{cases}1 & i=j \\ 0 & i \neq j\end{cases}$.

**Lagrange polynomials:**

$$\Phi_j(x) = \prod_{\substack{0 \leq i \leq n \\ i \neq j}} \frac{x - x_i}{x_j - x_i}$$

The interpolant is then:

$$p_n(x) = \sum_{j=0}^n y_j\,\Phi_j(x)$$

**Example:** For $\{(1,1),(2,3),(4,3)\}$:

$$\Phi_0(x) = \frac{(x-2)(x-4)}{(1-2)(1-4)} = \frac{(x-2)(x-4)}{3}$$

$$p_2(x) = \frac{(x-2)(x-4)}{3} - \frac{3(x-1)(x-4)}{2} + \frac{(x-1)(x-2)}{2}$$

**Evaluation cost:** $O(n)$ flops with precomputation of $\prod(x - x_i)$.

**Most stable** of the three interpolation methods.

---

### Newton's Interpolation

Basis: $\phi_0(x) = 1$, $\phi_j(x) = \prod_{i=0}^{j-1}(x - x_i)$.

The data point matrix $X$ is **lower triangular** → solve by forward substitution.

**Divided Differences:**

$$f[x_i] = f(x_i), \qquad f[x_i, x_j] = \frac{f[x_j] - f[x_i]}{x_j - x_i}$$

$$f[x_0, x_1, \ldots, x_k] = \frac{f[x_1,\ldots,x_k] - f[x_0,\ldots,x_{k-1}]}{x_k - x_0}$$

**Theorem 1:** $c_j = f[x_0, x_1, \ldots, x_j]$ for $0 \leq j \leq n$.

**Theorem 2 (Error formula):** If $f$ is interpolated at $x_0, \ldots, x_n$:

$$f(x) = p_n(x) + f[x_0, x_1, \ldots, x_n, x]\prod_{i=0}^n(x - x_i)$$

**Adaptive/Recursive Advantage:** Upon the arrival of a new point $(x_n, y_n)$:

$$c_n = f[x_0, x_1, \ldots, x_n] = \frac{y_n - p_{n-1}(x_n)}{\phi_n(x_n)}$$

computed in $O(n)$ flops instead of $O(n^2)$.

### Summary of Three Methods

| Method | Basis $\phi_j(x)$ | Construction | Evaluation | Feature |
|---|---|---|---|---|
| Monomial | $x^j$ | $\frac{2}{3}n^3$ | $2n$ | Simple |
| Lagrange | $L_j(x)$ | $n^2$ | $5n$ | Most stable |
| Newton | $\prod_{i=0}^{j-1}(x-x_i)$ | $\frac{1}{3}n^2$ | $2n$ | Adaptive |

---

## 9. Splines

### Motivation

A single polynomial of degree $n$ can be poorly behaved (Runge's phenomenon, ill-conditioning) for large $n$. Instead, use **piecewise polynomials** on partitioned intervals $[x_i, x_{i+1}]$.

### Definition

A function $s \in C^{m-1}[a,b]$ is a **spline of degree $m$** with breakpoints $x_0 < x_1 < \cdots < x_n$ if it reduces to a polynomial of degree $\leq m$ on each $[x_i, x_{i+1}]$.

**Cubic spline:** $m = 3$, in $C^2[a,b]$.

### Cubic Spline Construction

Each piece is $s_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3$ with $a_i = y_i$.

**Constraints (11.1a–d):**

$$s_i(x_{i+1}) = f(x_{i+1}), \quad s_i'(x_{i+1}) = s_{i+1}'(x_{i+1}), \quad s_i''(x_{i+1}) = s_{i+1}''(x_{i+1})$$

These give $3n-2$ conditions for $3n$ unknowns ($b_i, c_i, d_i$). Need 2 more.

**Three boundary options:**

1. **Natural (free boundary):** $s_0''(x_0) = s_{n-1}''(x_n) = 0$
2. **Clamped:** $s_0'(x_0) = f'(x_0)$, $s_{n-1}'(x_n) = f'(x_n)$
3. **Not-a-knot:** $s_0'''(x_1) = s_1'''(x_1)$ and $s_{n-2}'''(x_{n-1}) = s_{n-1}'''(x_{n-1})$

**Algorithm:** The coefficients $c_i$ solve the symmetric tridiagonal system $Xc = \psi$ where

$$h_{i-1}c_{i-1} + 2(h_{i-1}+h_i)c_i + h_i c_{i+1} = 3(f[x_i, x_{i+1}] - f[x_{i-1}, x_i])$$

with $h_i = x_{i+1} - x_i$. Then $d_i$ and $b_i$ follow from (11.4a,b).

**Theorem 1:** A diagonally dominant square matrix is nonsingular.

**Theorem 2:** The PLU decomposition of a nonsingular tridiagonal $n \times n$ matrix takes $O(n)$ flops.

**Example (Example 11.4):** Natural cubic spline through $\{(0,1.1),(1,0.9),(2,2)\}$:

$$s_0(x) = 1.1 - 0.525x + 0.325x^3, \quad x < 1$$

$$s_1(x) = 0.9 + 0.45(x-1) + 0.975(x-1)^2 - 0.325(x-1)^3, \quad x \geq 1$$

---

## 10. Numerical Integration (Quadrature)

### Idea

Approximate $\int_a^b f(x)\,dx$ by integrating the interpolant $p_n(x)$ on small subintervals $[x, x+h]$, then sum.

### Trapezoid Rule ($n=1$)

Integrate the linear interpolant on $[a,b]$:

$$\int_a^b p_1(x)\,dx = \frac{b-a}{2}\bigl(f(a) + f(b)\bigr)$$

**Error:** $E(f) = -\frac{f''(\xi)}{12}(b-a)^3$ for some $\xi \in [a,b]$.

### Simpson's Rule ($n=2$)

Use $x_0 = a$, $x_1 = \frac{a+b}{2}$, $x_2 = b$:

$$\int_a^b f(x)\,dx \approx \frac{b-a}{6}\!\left[f(a) + 4f\!\left(\frac{a+b}{2}\right) + f(b)\right]$$

**Error:** $E(f) = -\dfrac{f^{(4)}(\xi)}{90}\!\left(\dfrac{b-a}{2}\right)^5$ — achieves accuracy order 5.

### Composite Trapezoidal Method

Divide $[a,b]$ into $n$ strips of width $h = (b-a)/n$:

$$\int_a^b f(x)\,dx \approx h\!\left[\frac{f(a)}{2} + f(x_1) + f(x_2) + \cdots + f(x_{n-1}) + \frac{f(b)}{2}\right]$$

**Error bound:**

$$|E(f)| \leq \frac{h^2(b-a)}{12}\max_{a \leq \xi \leq b}|f''(\xi)| = O(h^2)$$

**Accuracy order 2.**

### Composite Simpson Method

Use $n$ paired strips (so $m = 2n$ fine strips), step $h = (b-a)/m$:

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\!\left[f(a) + 4f(t_1) + 2f(t_2) + 4f(t_3) + \cdots + 2f(t_{2n-2}) + 4f(t_{2n-1}) + f(b)\right]$$

**Error bound:**

$$|E(f)| \leq \frac{h^4(b-a)}{180}\max_{a \leq \xi \leq b}|f^{(4)}(\xi)| = O(h^4)$$

**Accuracy order 4.** One of the most commonly used general numerical integration methods.

**Example (15.5):** Approximate $\int_0^1 e^{-x^2}dx$ with error $< 10^{-5}$:

Since $\|f^{(4)}\|_\infty = 12$ on $[0,1]$:

$$|E(f)| \leq \frac{12h^4}{180} = \frac{1}{15r^4} < 10^{-5} \implies r = 10 \text{ strips suffices}$$

$$\int_0^1 e^{-x^2}dx \approx 0.7468249\ldots \approx 0.746824133$$

### Improper Integrals

To compute $I = \int_0^\infty e^{-x^2}dx$:

1. Split: $I = I_1 + I_2$ where $I_1 = \int_0^{2b} e^{-x^2}dx$, $I_2 = \int_{2b}^\infty e^{-x^2}dx$
2. Bound $I_2 \leq \frac{e^{-4b^2}}{3b}$ — choose $b=2$ so $I_2 < 1.8756 \times 10^{-8}$
3. Apply composite Simpson to $I_1$

---

## 11. Romberg Integration

Uses **extrapolation** to eliminate low-order error terms and achieve higher accuracy.

The composite trapezoidal error has the expansion:

$$I - T(h) = K_2 h^2 + K_4 h^4 + K_6 h^6 + \cdots$$

for constants $K_{2j}$ independent of $h$.

**Step 1:** Compute $R_{1,1} = T(2h)$ and $R_{2,1} = T(h)$.

**Step 2:** Eliminate the $h^2$ term:

$$I = \frac{4R_{2,1} - R_{1,1}}{3} + O(h^4)$$

This is **identical to the composite Simpson method**.

**Step 3:** Continue extrapolating:

$$R_{j+1,k} = R_{j+1,k-1} + \frac{R_{j+1,k-1} - R_{j,k-1}}{4^{k-1}-1}, \quad k = 2, 3, \ldots, j+1$$

$R_{j,j}$ provides an $O(h^{2j})$-accurate approximation.

**Algorithm (from p.471):**

1. Evaluate starting trapezoidal formula $R_{1,1} = \frac{h}{2}[f(a)+f(b)+2\sum_{k=1}^{r-1}f(a+kh)]$
2. For $j=1,\ldots,s-1$: refine $R_{j+1,1}$ and compute $R_{j+1,k}$ by the extrapolation formula

---

## 12. Initial Value Problems (IVPs)

### Formulation

**Simple IVP:** Given $f:\mathbb{R}\times\mathbb{R}\to\mathbb{R}$, find $y:[a,b]\to\mathbb{R}$ satisfying

$$\frac{dy}{dt} = f(t, y(t)), \qquad y(a) = y_0$$

**Vector IVP:** Same but $\mathbf{f}:[a,b]\times\mathbb{R}^m\to\mathbb{R}^m$ and $\mathbf{y}:[a,b]\to\mathbb{R}^m$.

**Unique Existence Theorem:** If $f$ has bounded partial derivatives and is Lipschitz continuous:

$$\|f(t,\mathbf{y}_1) - f(t,\mathbf{y}_2)\| \leq L\|\mathbf{y}_1 - \mathbf{y}_2\|$$

then the IVP has a unique continuous differentiable solution.

### Forward Euler Method

Let $t_i = ih$, $h = b/n$. Update:

$$y_{i+1} = y_i + h\,f(t_i, y_i)$$

Justified by Taylor series of order 1: $y(t_{i+1}) = y(t_i) + hy'(t_i) + O(h^2)$.

**Global error:** $O(h^2)\cdot n = O(h^2)\cdot\frac{b-a}{h} = O(h)$ — **accuracy order 1**.

**Example 16.1:** $y' = -y + t$, $y(0) = c$. Exact solution: $y(t) = t - 1 + (c+1)e^{-t}$.

**Spring motion (vector IVP):**

$$u'' + \omega^2 u = 0, \quad u(0) = u_0, \quad u'(0) = v_0$$

Reformulate with $\mathbf{y} = \begin{pmatrix}u \\ u'\end{pmatrix}$, $\mathbf{f}(t,\mathbf{y}) = \begin{pmatrix}y_2 \\ -\omega^2 y_1\end{pmatrix}$.

**Pendulum simulation (MATLAB):**

```matlab
n=500; y=zeros(2,n+1); v=1; g=9.81;
y(1,1)=0; y(2,1)=v; h=10/n;
for i=2:n+1
  y(:,i) = y(:,i-1) + h*[y(2,i-1); -g*sin(y(1,i-1))];
end
t = linspace(0,10,n+1);
plot(t, y(1,:))
```

Note: $n=500$ shows energy increase (instability); $n=50000$ stabilizes.

### Accuracy Order

The **local truncation error** $d_i$ for a method is the max one-step error from Taylor series. The **accuracy order** is the max $q$ such that $d_i = O(h^{q+1})$. For forward Euler: $q = 1$.

### Absolute Stability and Stiffness

Test equation: $y' = \lambda y$ with $\lambda < 0$. Exact solution $y(t) = e^{\lambda t}y(0)$ decays. Euler gives $y_{i+1} = (1+h\lambda)y_i$.

Requiring $|y_{i+1}| \leq |y_i|$:

$$|1 + h\lambda| \leq 1 \implies h \leq \frac{2}{|\lambda|}$$

An IVP requiring a smaller step than some given upper bound is **stiff**.

---

## 13. Runge-Kutta Methods

All IVP solvers approximate:

$$y(t_{i+1}) = y(t_i) + \int_{t_i}^{t_{i+1}} f(t, y(t))\,dt$$

The forward Euler method approximates the integral by a rectangle of width $h$. RK methods use higher-order quadrature.

### Explicit Trapezoidal RK (Order 2)

Apply the trapezoid rule to the integral. Since $f(t_{i+1}, y(t_{i+1}))$ is unknown, approximate $y(t_{i+1})$ by one Euler step:

$$Y = y_i + h\,f(t_i, y_i)$$

$$y_{i+1} = y_i + \frac{h}{2}\!\left[f(t_i, y_i) + f(t_{i+1}, Y)\right]$$

**Accuracy order 2.**

### Explicit Midpoint Method (Order 2)

$$Y = y_i + \frac{h}{2}f(t_i, y_i), \qquad y_{i+1} = y_i + h\,f\!\left(\frac{t_i+t_{i+1}}{2}, Y\right)$$

### Classical RK Method (Order 4)

Based on Simpson's rule. Four stages per step:

$$Y_1 = y_i$$

$$Y_2 = y_i + \frac{h}{2}f(t_i, Y_1)$$

$$Y_3 = y_i + \frac{h}{2}f(t_{i+1/2}, Y_2)$$

$$Y_4 = y_i + h\,f(t_{i+1/2}, Y_3)$$

$$y_{i+1} = y_i + \frac{h}{6}\!\left[f(t_i,Y_1) + 2f(t_{i+1/2},Y_2) + 2f(t_{i+1/2},Y_3) + f(t_{i+1},Y_4)\right]$$

**Accuracy order 4.**

### Comparison Table (for $y'=-y^2$, $y(1)=1$)

| $h$ | Euler | Rate | RK2 | Rate | RK4 | Rate |
|---|---|---|---|---|---|---|
| 0.1 | 2.3e-3 | 1.01 | 7.4e-5 | 2.15 | 1.4e-8 | 3.90 |
| 0.05 | 1.2e-3 | 1.01 | 1.8e-5 | 2.07 | 8.6e-10 | 3.98 |
| 0.01 | 2.3e-4 | 1.00 | 6.8e-7 | 2.01 | 1.4e-12 | 4.00 |
| 0.005 | 1.2e-4 | 1.00 | 1.7e-7 | 2.01 | 8.7e-14 | 4.00 |

The rate $= \log_2\!\left(\frac{e(2h)}{e(h)}\right)$ confirms accuracy orders 1, 2, and 4.

---

## 14. Multi-Step Methods (Adams-Bashforth)

Instead of approximating $f(t,y(t))$ at a single point, **multi-step methods** interpolate using several previous values.

### Two-Step Adams-Bashforth

Interpolate the two data points $(t_i, f_i)$ and $(t_{i-1}, f_{i-1})$ by Newton's basis:

$$p_1(t) = f_i + f[t_{i-1}, t_i](t - t_i) = f_i + \frac{f_i - f_{i-1}}{h}(t - t_i)$$

Integrate over $[t_i, t_{i+1}]$:

$$y_{i+1} = y_i + h\!\left(\frac{3}{2}f_i - \frac{1}{2}f_{i-1}\right)$$

**Accuracy order 2.**

### Three-Step Adams-Bashforth

Derived by interpolating $(t_i, f_i)$, $(t_{i-1}, f_{i-1})$, $(t_{i-2}, f_{i-2})$ and integrating:

$$y_{i+1} = y_i + \frac{h}{12}(23f_i - 16f_{i-1} + 5f_{i-2})$$

### Four- and Five-Step Formulas (from p.502)

$$y_{i+1} = y_i + \frac{h}{24}(55f_i - 59f_{i-1} + 37f_{i-2} - 9f_{i-3}) \quad \text{(order 4)}$$

$$y_{i+1} = y_i + \frac{h}{720}(1901f_i - 2774f_{i-1} + 2616f_{i-2} - 1274f_{i-3} + 251f_{i-4}) \quad \text{(order 5)}$$

**Key property:** Multi-step methods are **adaptive** — each new step costs only $O(1)$ extra function evaluations.
