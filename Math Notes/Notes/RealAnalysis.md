---
title: Real Analysis
parent: Math Notes
nav_order: 6
---

# Real Analysis Notes

> MATH 312 — Main themes: algebraic foundations, order and completeness, sequences, series, continuity, limits of functions, power series, derivatives, and Darboux integration.

---

## 1. Algebraic Numbers and the Rational Zeros Theorem

### Algebraic Numbers

A number $\alpha$ is **algebraic** if it satisfies a nonzero polynomial with integer coefficients:

$$c_n x^n + c_{n-1}x^{n-1} + \cdots + c_1 x + c_0 = 0, \quad c_i \in \mathbb{Z},\; c_n \neq 0$$

Every rational number is algebraic: $r = \frac{m}{n}$ satisfies $nx - m = 0$. So $\mathbb{Q} \subseteq \{\text{algebraic numbers}\}$.

### Divisibility

An integer $k$ is a **factor** of $m$ if $\frac{m}{k} \in \mathbb{Z}$, written $k \mid m$.

### Rational Zeros Theorem

If $r = \frac{c}{d}$ (in lowest terms) is a root of $c_nx^n + \cdots + c_0 = 0$ with integer coefficients, then $c \mid c_0$ and $d \mid c_n$.

**Practical use:** the only possible rational roots are $\pm\frac{\text{factor of } c_0}{\text{factor of } c_n}$.

---

## 2. Fields and Ordered Fields

### Field Axioms

A **field** is a set with addition and multiplication satisfying:

**Addition:** associativity, commutativity, identity $a+0=a$, and inverses $a + (-a) = 0$.

**Multiplication:** associativity, commutativity, identity $a \cdot 1 = a$, and inverses $aa^{-1} = 1$ for $a \neq 0$.

**Distributive Law:** $a(b+c) = ab + ac$.

**Basic consequences:** $a \cdot 0 = 0$; $(-a)b = -(ab)$; $(-a)(-b) = ab$; $ab = 0 \implies a = 0$ or $b = 0$.

### Ordered Field

An **ordered field** has an order relation $\leq$ satisfying:

1. Totality: $a \leq b$ or $b \leq a$
2. Antisymmetry: $a \leq b$ and $b \leq a \implies a = b$
3. Transitivity: $a \leq b$ and $b \leq c \implies a \leq c$
4. $a \leq b \implies a + c \leq b + c$
5. $a \leq b$ and $c > 0 \implies ac \leq bc$

$\mathbb{R}$ is an ordered field.

---

## 3. Bounds, Supremum, and Infimum

### Maximum and Minimum

For nonempty $S \subseteq \mathbb{R}$, $s_0 \in S$ is the **maximum** if $s \leq s_0$ for all $s \in S$. Similarly $s_1 \in S$ is the **minimum** if $s_1 \leq s$ for all $s \in S$.

| Set | Min | Max |
|---|---|---|
| $\{1,2,3\}$ | 1 | 3 |
| $(a,b)$ | DNE | DNE |
| $[a,b]$ | $a$ | $b$ |

### Upper and Lower Bounds

$M$ is an **upper bound** of $S$ if $s \leq M$ for all $s \in S$.

$m$ is a **lower bound** of $S$ if $m \leq s$ for all $s \in S$.

$S$ is **bounded** if $S \subseteq [m, M]$ for some $m, M \in \mathbb{R}$.

### Supremum and Infimum

$$\sup S = \text{least upper bound of } S, \qquad \inf S = \text{greatest lower bound of } S$$

If $\max S$ exists then $\sup S = \max S$. But $\sup S$ can exist even when $\max S$ does not.

**Example:** $S = (0,1)$. Then $\inf S = 0$, $\sup S = 1$, but $\min S$ and $\max S$ do not exist.

### Extended Reals

$+\infty$ and $-\infty$ are order symbols, **not real numbers** — do not apply ordinary algebra to them.

If $S$ is unbounded above: $\sup S = +\infty$. If unbounded below: $\inf S = -\infty$.

$$\sup \mathbb{N} = +\infty, \quad \inf \mathbb{N} = 1, \quad \sup \mathbb{R} = +\infty, \quad \inf \mathbb{R} = -\infty$$

---

## 4. Sequences

### Definition

A **sequence** is a function with domain $\mathbb{N}$ (or $\{n \in \mathbb{Z} : n \geq m\}$), written $(s_n)$ or $(s_n)_{n=m}^\infty$. Do not confuse the sequence with its set of values $\{s_n : n \geq m\}$.

### Standard Examples

| Sequence | Formula | Limit |
|---|---|---|
| Reciprocal square | $s_n = \frac{1}{n^2}$ | $0$ |
| Alternating | $a_n = (-1)^n$ | diverges |
| Constant | $s_n = 5$ | $5$ |
| $n$th root | $a_n = n^{1/n}$ | $1$ |
| Euler's number | $b_n = \left(1+\frac{1}{n}\right)^n$ | $e$ |

---

## 5. Limits of Sequences

### Definition

$(s_n)$ **converges to** $s \in \mathbb{R}$ if for every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that

$$n > N \implies \lvert s_n - s \rvert < \varepsilon$$

Written $\lim_{n\to\infty} s_n = s$.

### Proof Template

To prove $\lim_{n\to\infty} s_n = s$:

1. Let $\varepsilon > 0$ be arbitrary
2. Study $\lvert s_n - s \rvert$
3. Force it below $\varepsilon$ by choosing $n$ large enough
4. State a valid $N$
5. Conclude: $n > N \implies \lvert s_n - s \rvert < \varepsilon$

### Example: Prove $\frac{1}{n^2} \to 0$

We need $\frac{1}{n^2} < \varepsilon$, which holds when $n > \frac{1}{\sqrt{\varepsilon}}$. Choose $N = \frac{1}{\sqrt{\varepsilon}}$.

Then $n > N \implies \frac{1}{n^2} < \varepsilon$. $\blacksquare$

### Example: Rational Sequence

For $s_n = \frac{3n+1}{7n-4}$, the limit is $\frac{3}{7}$. We compute:

$$\left\lvert\frac{3n+1}{7n-4} - \frac{3}{7}\right\rvert = \frac{19}{7(7n-4)}$$

Choose $N > \frac{19}{49\varepsilon} + \frac{4}{7}$. Then for $n > N$ the expression is less than $\varepsilon$. $\blacksquare$

### Estimation Method

For $\left\lvert\frac{4n^3+3n}{n^3-6} - 4\right\rvert = \left\lvert\frac{3n+24}{n^3-6}\right\rvert$, estimate $3n+24 < 27n$ and $n^3-6 > \frac{n^3}{2}$:

$$\left\lvert\frac{3n+24}{n^3-6}\right\rvert < \frac{27n}{n^3/2} = \frac{54}{n^2}$$

Choose $N > \sqrt{\frac{54}{\varepsilon}}$. $\blacksquare$

---

## 6. Bounded and Monotone Sequences

### Bounded Sequences

$(s_n)$ is **bounded** if there exists $M > 0$ such that $\lvert s_n \rvert \leq M$ for all $n$.

**Theorem:** Every convergent sequence is bounded.

*Proof idea:* If $s_n \to s$, take $\varepsilon = 1$. Eventually $\lvert s_n \rvert \leq \lvert s \rvert + 1$. The finitely many early terms are also bounded, so set $M = \max\{\lvert s\rvert + 1, \lvert s_1 \rvert, \ldots, \lvert s_N \rvert\}$.

### Monotone Sequences

$(s_n)$ is **increasing** if $s_n \leq s_{n+1}$ for all $n$, **decreasing** if $s_n \geq s_{n+1}$. A sequence is **monotone** if either holds.

### Monotone Convergence Theorem

If $(s_n)$ is increasing and bounded above:

$$\lim_{n\to\infty} s_n = \sup\{s_n : n \in \mathbb{N}\}$$

If $(s_n)$ is decreasing and bounded below:

$$\lim_{n\to\infty} s_n = \inf\{s_n : n \in \mathbb{N}\}$$

If monotone but unbounded, the limit is $\pm\infty$ accordingly.

### Algebra of Limits

If $s_n \to s$ and $t_n \to t$:

$$\lim(s_n + t_n) = s + t, \quad \lim(s_n t_n) = st, \quad \lim\frac{t_n}{s_n} = \frac{t}{s}\; (s \neq 0)$$

**Standard limits:** For $p > 0$: $\dfrac{1}{n^p} \to 0$. For $\lvert a \rvert < 1$: $a^n \to 0$. For $a > 0$: $a^{1/n} \to 1$. Also $n^{1/n} \to 1$.

---

## 7. Subsequences

### Definition

A **subsequence** of $(s_n)$ is $(s_{n_k})_{k \in \mathbb{N}}$ where $n_1 < n_2 < n_3 < \cdots$. It preserves the original order.

Formally: if $\sigma : \mathbb{N} \to \mathbb{N}$ is increasing, the subsequence is $s \circ \sigma$, i.e. $t_k = s_{\sigma(k)}$.

**Theorem:** If $s_n \to s$, then every subsequence also converges to $s$.

### Bolzano-Weierstrass Theorem

Every bounded sequence in $\mathbb{R}$ has a convergent subsequence.

### Monotone Subsequence Theorem

Every sequence has a monotone subsequence. Combined with boundedness, this yields Bolzano-Weierstrass.

---

## 8. Limsup and Liminf

Define the tail supremum and infimum:

$$v_N = \sup\{s_n : n > N\}, \qquad u_N = \inf\{s_n : n > N\}$$

As $N$ increases, $u_N$ is increasing and $v_N$ is decreasing. Then:

$$\liminf_{n\to\infty} s_n = \lim_{N\to\infty} u_N, \qquad \limsup_{n\to\infty} s_n = \lim_{N\to\infty} v_N$$

Always: $\liminf s_n \leq \limsup s_n$.

If $(s_n)$ converges: $\liminf s_n = \limsup s_n = \lim s_n$.

---

## 9. Infinite Series

### Definition

The series $\sum_{n=m}^\infty a_n$ **converges** if the partial sums $s_N = \sum_{n=m}^N a_n$ converge to a real number $s$. Otherwise it **diverges**.

**Absolute convergence:** $\sum a_n$ is absolutely convergent if $\sum \lvert a_n \rvert$ converges. Absolute convergence implies convergence.

### Geometric Series

$$\sum_{n=0}^\infty ar^n = \frac{a}{1-r}, \quad \lvert r \rvert < 1$$

Diverges for $\lvert r \rvert \geq 1$ (unless $a = 0$).

### $p$-Series

$$\sum_{n=1}^\infty \frac{1}{n^p} \text{ converges} \iff p > 1$$

The harmonic series ($p=1$) diverges. Proof by comparison with $\int_1^n \frac{1}{x}\,dx = \ln(n+1) \to +\infty$.

For $p > 1$: $\sum_{k=1}^n \frac{1}{k^p} \leq 1 + \int_1^n x^{-p}\,dx = 1 + \frac{n^{1-p}-1}{1-p}$, which stays bounded.

---

## 10. Continuity

### Sequential Definition

$f$ is **continuous at** $x_0 \in D_f$ if for every sequence $(x_n)$ in $D_f$ with $x_n \to x_0$:

$$f(x_n) \to f(x_0)$$

### $\varepsilon$-$\delta$ Definition

$f$ is continuous at $x_0$ iff for every $\varepsilon > 0$, there exists $\delta > 0$ such that:

$$x \in D_f,\; \lvert x - x_0 \rvert < \delta \implies \lvert f(x) - f(x_0) \rvert < \varepsilon$$

**Algebra:** If $f$ and $g$ are continuous at $x_0$, so are $f+g$, $fg$, and $f/g$ (when $g(x_0) \neq 0$).

**Composition:** If $f$ is continuous at $x_0$ and $g$ is continuous at $f(x_0)$, then $g \circ f$ is continuous at $x_0$.

---

## 11. Extreme Value and Intermediate Value Theorems

### Extreme Value Theorem (EVT)

If $f$ is continuous on $[a,b]$, then $f$ is bounded and attains its maximum and minimum — there exist $x_0, y_0 \in [a,b]$ such that $f(x_0) \leq f(x) \leq f(y_0)$ for all $x \in [a,b]$.

> **Hypotheses matter:** EVT fails on open intervals, unbounded intervals, or for discontinuous functions.

### Intermediate Value Theorem (IVT)

If $f$ is continuous on an interval $I$ and $a, b \in I$ with $a < b$, then for any $y$ strictly between $f(a)$ and $f(b)$, there exists $c \in (a,b)$ with $f(c) = y$.

**Practical use:** If $f(a) < 0 < f(b)$, then $\exists\, c \in (a,b)$ with $f(c) = 0$.

---

## 12. Uniform Continuity

### Definition

$f$ is **uniformly continuous** on $S$ if for every $\varepsilon > 0$ there exists $\delta > 0$ (depending only on $\varepsilon$) such that:

$$x, y \in S,\; \lvert x - y \rvert < \delta \implies \lvert f(x) - f(y) \rvert < \varepsilon$$

The key difference from ordinary continuity: $\delta = \delta(\varepsilon)$ only, not $\delta(\varepsilon, x_0)$.

Uniform continuity $\implies$ continuity at every point.

### Heine-Cantor Theorem

If $f$ is continuous on a closed interval $[a,b]$, then $f$ is uniformly continuous on $[a,b]$.

### Examples

**$f(x) = \frac{1}{x^2}$ on $[a, +\infty)$, $a > 0$:**

$$\left\lvert\frac{1}{x^2} - \frac{1}{y^2}\right\rvert = \frac{\lvert x-y\rvert \lvert x+y\rvert}{x^2 y^2} \leq \frac{2}{a^3}\lvert x - y\rvert$$

Choose $\delta = \frac{\varepsilon a^3}{2}$. $\blacksquare$

**$f(x) = x^2$ on $[-7, 7]$:**

$$\lvert x^2 - y^2 \rvert = \lvert x-y\rvert\lvert x+y\rvert \leq 14\lvert x-y\rvert$$

Choose $\delta = \frac{\varepsilon}{14}$. $\blacksquare$

---

## 13. Limits of Functions

### Sequential Definition

Let $a$ be a limit point of $S$. Then $\lim_{x \to a} f(x) = L$ if for every sequence $(x_n)$ in $S$ with $x_n \to a$ and $x_n \neq a$:

$$f(x_n) \to L$$

$f$ is continuous at $a$ iff $\lim_{x \to a} f(x) = f(a)$.

### One-Sided Limits

$\lim_{x\to a^+} f(x) = L$ (from the right), $\lim_{x\to a^-} f(x) = L$ (from the left).

The two-sided limit exists iff both one-sided limits exist and are equal.

**Examples:**

$$\lim_{x\to 0^+}\frac{1}{x} = +\infty, \quad \lim_{x\to 0^-}\frac{1}{x} = -\infty, \quad \text{so } \lim_{x\to 0}\frac{1}{x} \text{ DNE}$$

### Limit Laws

If $\lim_{x\to a} f(x) = L_1$ and $\lim_{x\to a} g(x) = L_2$:

$$\lim(f+g) = L_1 + L_2, \quad \lim(fg) = L_1 L_2, \quad \lim\frac{f}{g} = \frac{L_1}{L_2}\; (L_2 \neq 0)$$

If $h$ is continuous at $L_1$: $\lim_{x\to a} h(f(x)) = h(L_1)$.

---

## 14. Power Series

### Definition

A power series centered at $0$:

$$\sum_{n=0}^\infty a_n x^n$$

Always converges at $x = 0$. Convergence elsewhere depends on the coefficients.

### Radius of Convergence

Let $\beta = \limsup_{n\to\infty} \lvert a_n \rvert^{1/n}$ and $R = \frac{1}{\beta}$ (with $R = +\infty$ if $\beta = 0$, and $R = 0$ if $\beta = +\infty$).

$$\lvert x \rvert < R \implies \sum a_n x^n \text{ converges}, \qquad \lvert x \rvert > R \implies \sum a_n x^n \text{ diverges}$$

At $x = \pm R$: **must test separately**.

**Ratio test shortcut:** If $\lim_{n\to\infty}\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = L$, then $R = \frac{1}{L}$.

A power series converges on one of: all of $\mathbb{R}$, just $\{0\}$, or a bounded interval centered at $0$ (open, closed, or half-open).

---

## 15. Derivatives and Extrema

### Derivative

$$f'(x_0) = \lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$

### Interior Extrema Theorem

If $f$ is defined on an open interval, attains an extremum at $x_0$, and is differentiable there, then $f'(x_0) = 0$.

**For closed intervals $[a,b]$**, extremum candidates are: endpoints $a,b$; points where $f'=0$; points where $f'$ does not exist.

### Rolle's Theorem

If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $f(a) = f(b)$, then there exists $c \in (a,b)$ with $f'(c) = 0$.

### Mean Value Theorem (MVT)

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists $c \in (a,b)$ with:

$$f'(c) = \frac{f(b)-f(a)}{b-a}$$

Rolle's theorem is the special case $f(a) = f(b)$.

### Consequences of MVT

- $f'(x) = 0$ on an interval $\implies$ $f$ is constant
- $f'(x) > 0$ $\implies$ $f$ is increasing; $f'(x) < 0$ $\implies$ $f$ is decreasing
- $\lvert f'(x)\rvert \leq M$ $\implies$ $\lvert f(x)-f(y)\rvert \leq M\lvert x-y\rvert$ (Lipschitz, implies uniform continuity)

---

## 16. Darboux Integration

### Partitions and Darboux Sums

A **partition** of $[a,b]$ is $P = \{a = t_0 < t_1 < \cdots < t_n = b\}$.

For bounded $f$ on $[a,b]$, define on each subinterval $[t_{k-1}, t_k]$:

$$M_k = \sup\{f(x) : x \in [t_{k-1},t_k]\}, \qquad m_k = \inf\{f(x) : x \in [t_{k-1},t_k]\}$$

**Upper Darboux sum:**

$$U(f,P) = \sum_{k=1}^n M_k(t_k - t_{k-1})$$

**Lower Darboux sum:**

$$L(f,P) = \sum_{k=1}^n m_k(t_k - t_{k-1})$$

**Basic inequality:** For every partition $P$:

$$m(f,[a,b])(b-a) \leq L(f,P) \leq U(f,P) \leq M(f,[a,b])(b-a)$$

**Refinement:** If $P \subseteq Q$ (i.e. $Q$ refines $P$):

$$L(f,P) \leq L(f,Q) \leq U(f,Q) \leq U(f,P)$$

### Upper and Lower Integrals

$$L(f) = \sup_P L(f,P), \qquad U(f) = \inf_P U(f,P), \qquad L(f) \leq U(f)$$

### Darboux Integrability

$f$ is **integrable** on $[a,b]$ if $L(f) = U(f)$. In that case:

$$\int_a^b f(x)\,dx = L(f) = U(f)$$

This is equivalent to: for every $\varepsilon > 0$, there exists a partition $P$ with $U(f,P) - L(f,P) < \varepsilon$.

### Examples

**$f(x) = x^2$ on $[0,b]$:** Using equal partitions $t_k = \frac{kb}{n}$ gives $\int_0^b x^2\,dx = \frac{b^3}{3}$.

**Dirichlet-type function:** $f(x) = 1$ on $\mathbb{Q}$, $f(x) = 0$ otherwise. On every subinterval, both rationals and irrationals appear, so $U(f,P) = b-a$ and $L(f,P) = 0$ for every $P$. Thus $U(f) \neq L(f)$ and $f$ is **not integrable**.

---

## 17. Proof Templates

### Sequence Convergence

Let $\varepsilon > 0$. Study $\lvert s_n - s\rvert$, simplify or estimate, choose $N$ so that $n > N$ forces it below $\varepsilon$. Conclude $\lim s_n = s$.

### Continuity at $x_0$

Let $\varepsilon > 0$. Simplify $\lvert f(x) - f(x_0)\rvert$, factor out $\lvert x - x_0\rvert$, bound the remaining factor near $x_0$, choose $\delta$.

### Uniform Continuity on $S$

Let $\varepsilon > 0$. Find one $\delta > 0$ (independent of $x$ and $y$) such that $\lvert x-y\rvert < \delta$ implies $\lvert f(x)-f(y)\rvert < \varepsilon$.

### Darboux Integrability

For every $\varepsilon > 0$, exhibit a partition $P$ with $U(f,P) - L(f,P) < \varepsilon$.

---

## 18. Common Mistakes

**$\sup$ vs $\max$:** A maximum must be in the set. $\sup (0,1) = 1$ but $\max(0,1)$ DNE.

**$\infty$ is not a number:** Do not apply real-number algebra to $\pm\infty$.

**Power series endpoints:** The radius $R$ only settles convergence for $\lvert x\rvert < R$ and $\lvert x\rvert > R$. Test $x = \pm R$ separately.

**Continuity $\neq$ uniform continuity:** Continuous at every point of $S$ does not imply uniformly continuous on $S$ in general — but it does on closed bounded intervals (Heine-Cantor).

**EVT needs a closed bounded interval:** Open intervals are not enough.

**Rolle's theorem needs $f(a) = f(b)$:** Do not apply it without checking.

**Integrability needs $L(f) = U(f)$:** It is not about one partition — it is about the best lower and upper sums agreeing.

---

## 19. Formula Summary

$$\text{Rational root: } r = \frac{c}{d} \text{ (lowest terms)} \implies c \mid c_0,\; d \mid c_n$$

$$s_n \to s \iff \forall\,\varepsilon>0\;\exists N : n > N \implies \lvert s_n - s\rvert < \varepsilon$$

$$\text{Increasing + bounded above} \implies s_n \to \sup\{s_n\}$$

$$\liminf s_n \leq \limsup s_n; \quad \text{convergent} \implies \liminf = \limsup = \lim$$

$$\sum_{n=0}^\infty ar^n = \frac{a}{1-r}\; (\lvert r\rvert < 1), \qquad \sum_{n=1}^\infty \frac{1}{n^p} \text{ converges} \iff p > 1$$

$$f \text{ continuous at } x_0 \iff \forall\varepsilon>0\;\exists\delta>0: \lvert x-x_0\rvert<\delta \implies \lvert f(x)-f(x_0)\rvert<\varepsilon$$

$$f \text{ uniformly continuous on } S \iff \forall\varepsilon>0\;\exists\delta>0: \lvert x-y\rvert<\delta \implies \lvert f(x)-f(y)\rvert<\varepsilon$$

$$\lim_{x\to a}f(x)=L \iff x_n\to a,\;x_n\neq a \implies f(x_n)\to L$$

$$R = \frac{1}{\limsup\lvert a_n\rvert^{1/n}}, \quad \lvert x\rvert < R \implies \sum a_n x^n \text{ converges}, \quad \lvert x\rvert > R \implies \text{diverges}$$

$$f'(x_0) = \lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$

$$\text{Rolle: } f(a)=f(b) \implies \exists\,c\in(a,b): f'(c)=0$$

$$\text{MVT: } \exists\,c\in(a,b): f'(c)=\frac{f(b)-f(a)}{b-a}$$

$$U(f,P)=\sum_{k=1}^n M_k(t_k-t_{k-1}), \quad L(f,P)=\sum_{k=1}^n m_k(t_k-t_{k-1})$$

$$f \text{ integrable} \iff L(f)=U(f) \iff \forall\varepsilon>0\;\exists P: U(f,P)-L(f,P)<\varepsilon$$
