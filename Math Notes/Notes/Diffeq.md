---
title: Differential Equations
parent: Math Notes
nav_order: 2
---

# Differential Equations Notes

---

## 1. Introduction

A **differential equation** is an equation involving an unknown function and its derivatives. The goal is to find the function $y(x)$ (or $y(t)$) satisfying the equation.

### Basic Integration Examples

**Example 1:** Solve $\dfrac{dy}{dx} = x^3 + 4x + 1$

$$
\begin{align}
\int dy &= \int(x^3 + 4x + 1)\,dx \\[6pt]
y &= \frac{x^4}{4} + 2x^2 + x + C
\end{align}
$$

**Example 2:** Solve $y'' = 2e^{5x} - \cos(3x)$

$$
\begin{align}
y' &= \frac{2}{5}e^{5x} - \frac{1}{3}\sin(3x) + C_1 \\[6pt]
y  &= \frac{2}{25}e^{5x} + \frac{1}{9}\cos(3x) + C_1 x + C_2
\end{align}
$$

### Initial Value Problems (IVP)

An IVP specifies the value of $y$ (and its derivatives) at a particular point, which pins down the constants of integration.

**Example 3:** Solve $y'' = 6 + 7\sin\!\left(\dfrac{x}{2}\right)$, $\quad y(0) = 3$, $\quad y'(0) = -1$

$$
\begin{align}
y'  &= 6x - 14\cos\!\left(\frac{x}{2}\right) + C_1 \\[6pt]
y   &= 3x^2 - 28\sin\!\left(\frac{x}{2}\right) + C_1 x + C_2
\end{align}
$$

Apply $y(0) = 3$:
$$3(0)^2 - 28\sin(0) + C_1(0) + C_2 = 3 \implies C_2 = 3$$

Apply $y'(0) = -1$:
$$6(0) - 14\cos(0) + C_1 = -1 \implies -14 + C_1 = -1 \implies C_1 = 13$$

$$\boxed{y = 3x^2 - 28\sin\!\left(\frac{x}{2}\right) + 13x + 3}$$

---

## 2. Classifying Differential Equations

### Order
The **order** of a differential equation is the highest derivative that appears.

| Equation | Order |
|---|---|
| $y'' - y' = 0$ | 2 |
| $xy^{(6)} - 4y^2 y'' + 9y = 7x + 3$ | 6 |
| $\cos(y+3) - 7\sin(x^3)(y'')^4 - 2y^3 y' = 2$ | 2 |
| $\ln(y^{(3)}) - e^{x+y} - 4\sin x = y' \cdot y''$ | 3 |

### Linearity

A differential equation is **linear** if it can be written as:
$$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \cdots + a_1(x)y' + a_0(x)y = f(x)$$

where the $a_i(x)$ are functions of $x$ only. This means:
- No powers of $y$ or its derivatives: no $y^a$, $(y^{(n)})^a$
- No products of $y$ terms: no $y \cdot y'$
- No nonlinear functions of $y$: no $\sin(y)$, $e^y$

| Equation | Linear? |
|---|---|
| $y'' - y' = 0$ | ✓ |
| $8xy' + 4y = x^3 + e^x$ | ✓ |
| $\cos(x)y^{(3)} + 7y'' + (1-x)y' = 5x+1$ | ✓ |
| $9x^2 y'' + 3(1-x)y' = 4y^2$ | ✗ (has $y^2$) |

---

## 3. Direction Fields and Autonomous Equations

### Direction Fields

A **direction field** assigns a short line segment at each point $(x, y)$ with slope $\dfrac{dy}{dx}$ evaluated there. Tracing along these segments sketches solution curves without solving explicitly.

### Autonomous Differential Equations

An ODE is **autonomous** if it has the form $\dfrac{dy}{dx} = f(y)$ — the right-hand side depends only on $y$, not on $x$.

**Equilibrium solutions** occur where $f(y) = 0$: the derivative is zero, so $y$ is constant.

**Example:** $\dfrac{dy}{dx} = y^2 - 1 = (y-1)(y+1)$

- Equilibria: $y = 1$ and $y = -1$
- Between $-1$ and $1$: $f(y) < 0$ (decreasing)
- Outside that interval: $f(y) > 0$ (increasing)

**Example:** $\dfrac{dy}{dx} = y(y-2)^2(y+1)$
- Equilibria: $y = 0,\; y = 2,\; y = -1$

### Phase Portrait and Stability

A **phase portrait** shows the sign of $\dfrac{dy}{dx}$ on the $y$-axis to classify equilibria.

**Example:** $\dfrac{dy}{dx} = y^2(y+2)(y-1)$

Equilibria: $y = -2,\; y = 0,\; y = 1$

| Equilibrium | Behavior | Stability |
|---|---|---|
| $y = -2$ | Solutions pushed toward it from both sides | **Stable** |
| $y = 0$ | Pushed toward from one side, away from other | **Semi-stable** |
| $y = 1$ | Solutions pushed away from both sides | **Unstable** |

> **Limit trick:** If $y(-1) = 1$ (i.e. the solution passes through $(-1, 1)$), since it lies between the unstable equilibrium $y = 1$ and the stable one $y = -2$, the solution decreases toward $y = -2$:
> $$\lim_{x \to \infty} y(x) = -2$$

---

## 4. Separable Differential Equations

A **separable ODE** can be written as $\dfrac{dy}{dx} = g(x)\,h(y)$. We separate variables and integrate each side independently.

**Steps:**
1. Separate: get all $y$ and $dy$ on one side, all $x$ and $dx$ on the other
2. Integrate both sides
3. Solve for $y$ if possible
4. Apply initial conditions if given
5. Be careful absorbing constants — multiple $C$'s combine into one

**Example 1:** $(x^2+1)\dfrac{dy}{dx} = xy$

$$
\begin{align}
\frac{1}{y}\,dy &= \frac{x}{x^2+1}\,dx \\[6pt]
\ln|y| &= \frac{1}{2}\ln(x^2+1) + C \\[6pt]
y &= C_1\sqrt{x^2+1}
\end{align}
$$

**Example 2:** $e^{4y-3x}\dfrac{dy}{dx} = x$

$$
\begin{align}
e^{4y}\,dy &= x\,e^{3x}\,dx \\[6pt]
\frac{1}{4}e^{4y} &= \frac{x}{3}e^{3x} - \frac{1}{9}e^{3x} + C \\[6pt]
y &= \frac{1}{4}\ln\!\left(\frac{4x}{3}e^{3x} - \frac{4}{9}e^{3x} + C\right)
\end{align}
$$

**Example 3:** $x\dfrac{dy}{dx} = 6y$

$$
\begin{align}
\frac{dy}{y} &= \frac{6}{x}\,dx \\[6pt]
\ln|y| &= 6\ln|x| + C \\[6pt]
y &= Cx^6
\end{align}
$$

---

## 5. First-Order Linear Differential Equations

**Standard form:**
$$y' + P(x)y = Q(x)$$

**Integrating factor:**
$$\mu(x) = e^{\int P(x)\,dx}$$

Multiplying both sides by $\mu$ makes the left side a perfect derivative:
$$\frac{d}{dx}\bigl[\mu(x)\,y\bigr] = \mu(x)\,Q(x)$$

Integrate both sides and solve for $y$.

**Steps:**
1. Write in standard form (divide by leading coefficient)
2. Compute $\mu = e^{\int P(x)\,dx}$
3. Multiply through by $\mu$
4. Recognize the left side as $\dfrac{d}{dx}[\mu y]$
5. Integrate both sides
6. Solve for $y$

**Example:** $x^2y' + x(x+2)y = e^x$

Divide by $x^2$:
$$y' + \frac{x+2}{x}y = \frac{e^x}{x^2}$$

$$\mu = e^{\int\frac{x+2}{x}\,dx} = e^{\int\left(1 + \frac{2}{x}\right)dx} = e^{x+2\ln x} = x^2 e^x$$

$$\frac{d}{dx}\bigl[x^2 e^x y\bigr] = e^{2x}$$

$$x^2 e^x y = \frac{1}{2}e^{2x} + C$$

$$\boxed{y = \frac{1}{2}x^{-2}e^x + Cx^{-2}e^{-x}}$$

> **Transient term:** A term that $\to 0$ as $x \to \infty$ (e.g. $Cx^{-2}e^{-x}$ above).

---

## 6. Word Problems and Applications

### Exponential Growth / Decay

The model $\dfrac{dP}{dt} = kP$ arises whenever the rate of change is proportional to the current amount.

**Solution:** $P(t) = P_0\,e^{kt}$, where $P_0 = P(0)$.

**Example — Fox Population:**

Initial population $P(0) = 50$. After 3 years the population is 60 (20% growth). Find $P(10)$.

$$
\begin{align}
P(t) &= 50\,e^{kt} \\[6pt]
P(3) = 60 &\implies e^{3k} = 1.2 \implies k = \frac{\ln 1.2}{3} \\[8pt]
P(10) &= 50\,e^{\frac{10}{3}\ln 1.2} \approx \boxed{92 \text{ foxes}}
\end{align}
$$

**Example — Bacterial Growth:**

A culture starts with $P_0$ bacteria. At $t = 1$ hour there are $\frac{3}{2}P_0$. How long until the population triples?

$$
\begin{align}
P(t) &= P_0\,e^{kt} \\[6pt]
P(1) = \tfrac{3}{2}P_0 &\implies k = \ln\tfrac{3}{2} \\[8pt]
3P_0 &= P_0\,e^{(\ln\frac{3}{2})t}
\implies t = \frac{\ln 3}{\ln\frac{3}{2}} \approx \boxed{2.71 \text{ hours}}
\end{align}
$$

### Mixing Problems

For a tank of volume $V$, pumping a solution in and out:

$$A'(t) = C_{\text{in}} \cdot R_{\text{in}} - C_{\text{out}} \cdot R_{\text{out}}$$

where $C_{\text{out}} = \dfrac{A(t)}{V}$ when the volume stays constant.

**Example:** A 1000 L tank initially has 50 g of dye. A solution of 4 g/L flows in at 2 L/hr; the tank drains at the same rate. Find $A(1)$.

$$
\begin{align}
A'(t) &= 4(2) - \frac{A}{1000}(2) = 8 - \frac{A}{500} \\[8pt]
A' + \frac{1}{500}A &= 8
\quad\text{(first-order linear ODE)}\\[6pt]
\mu &= e^{t/500} \\[6pt]
\frac{d}{dt}\bigl[e^{t/500}A\bigr] &= 8e^{t/500} \\[6pt]
A(t) &= 4000 + Ce^{-t/500}
\end{align}
$$

Apply $A(0) = 50$: $\;C = 50 - 4000 = -3950$

$$\boxed{A(t) = 4000 - 3950\,e^{-t/500}}$$

$$A(1) = 4000 - 3950\,e^{-1/500} \approx 57.9 \text{ g}$$

---

## 7. Higher-Order Linear ODEs and the Wronskian

### General Form

$$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \cdots + a_1(x)y' + a_0(x)y = f(x)$$

### Existence and Uniqueness Theorem

If $a_0, \ldots, a_n$ and $f$ are continuous on an interval $I$, and $a_n(x) \neq 0$ on $I$, then the IVP has a **unique** solution on $I$.

### Linear Independence and the Wronskian

For $n$ solutions $y_1, y_2, \ldots, y_n$, form the **Wronskian**:

$$W(y_1, \ldots, y_n) = \det\begin{pmatrix} y_1 & y_2 & \cdots & y_n \\ y_1' & y_2' & \cdots & y_n' \\ \vdots & & & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \cdots & y_n^{(n-1)} \end{pmatrix}$$

- $W \neq 0$ on $I$ $\implies$ $y_1, \ldots, y_n$ are **linearly independent** (form a fundamental set)
- $W = 0$ everywhere $\implies$ linearly dependent

**Example:** $y'' - 25y = 0$, $\quad y_1 = e^{5x}$, $\quad y_2 = e^{-5x}$

$$W(e^{5x}, e^{-5x}) = \det\begin{pmatrix} e^{5x} & e^{-5x} \\ 5e^{5x} & -5e^{-5x} \end{pmatrix} = -5 - 5 = -10 \neq 0$$

Linearly independent. General solution: $y = C_1 e^{5x} + C_2 e^{-5x}$.

**IVP Example:** $y''' - 6y'' = 0$, $\quad y(0)=3,\; y'(0)=2,\; y''(0)=5$

The solutions $y_1 = 1$, $y_2 = x$, $y_3 = e^{6x}$ give general solution:
$$y = C_1 + C_2 x + C_3 e^{6x}$$

Applying initial conditions:
$$C_3 = \frac{5}{36}, \quad C_2 = \frac{7}{6}, \quad C_1 = \frac{103}{36}$$

---

## 8. Homogeneous ODEs with Constant Coefficients

For the equation $a_n y^{(n)} + \cdots + a_1 y' + a_0 y = 0$, substitute $y = e^{mx}$ to get the **auxiliary (characteristic) equation**:

$$a_n m^n + a_{n-1}m^{n-1} + \cdots + a_1 m + a_0 = 0$$

### Three Cases

**Case 1: Distinct real roots** $m_1 \neq m_2$

$$y = C_1 e^{m_1 x} + C_2 e^{m_2 x}$$

**Case 2: Repeated real root** $m$ of multiplicity $k$

$$y = (C_1 + C_2 x + C_3 x^2 + \cdots + C_k x^{k-1})\,e^{mx}$$

**Case 3: Complex conjugate roots** $m = \alpha \pm \beta i$

$$y = e^{\alpha x}\bigl(C_1 \cos\beta x + C_2 \sin\beta x\bigr)$$

### Examples

**Example 1:** $y'' - 3y' + 2y = 0$

$$m^2 - 3m + 2 = (m-1)(m-2) = 0 \implies m = 1, 2$$

$$y = C_1 e^x + C_2 e^{2x}$$

**Example 2:** $y''' - 7y'' - 8y' = 0$

$$m^3 - 7m^2 - 8m = m(m-8)(m+1) = 0 \implies m = 0, 8, -1$$

$$y = C_1 + C_2 e^{8x} + C_3 e^{-x}$$

**Example 3 (Complex roots):** $y'' - 6y' + 25y = 0$

$$m = \frac{6 \pm \sqrt{36 - 100}}{2} = \frac{6 \pm 8i}{2} = 3 \pm 4i$$

$$y = e^{3x}\bigl(C_1 \cos 4x + C_2 \sin 4x\bigr)$$

**IVP Example:** $y''' - 7y'' - 8y' = 0$, $\quad y(0)=3,\; y'(0)=0,\; y''(0)=4$

General solution: $y = C_1 + C_2 e^{8x} + C_3 e^{-x}$

$$
\begin{align}
y(0)  &= C_1 + C_2 + C_3 = 3 \\
y'(0) &= 8C_2 - C_3 = 0 \\
y''(0)&= 64C_2 + C_3 = 4
\end{align}
$$

Solving: $C_2 = \tfrac{1}{18}$, $C_3 = \tfrac{4}{9}$, $C_1 = \tfrac{5}{2}$

$$\boxed{y = \frac{5}{2} + \frac{1}{18}e^{8x} + \frac{4}{9}e^{-x}}$$

---

## 9. Non-Homogeneous ODEs — Method of Undetermined Coefficients

For $a_n y^{(n)} + \cdots + a_0 y = f(x)$, the **general solution** is:
$$y = y_c + y_p$$

- $y_c$: **complementary solution** — solves the homogeneous version (set right side to 0)
- $y_p$: **particular solution** — any single solution to the full equation

### Choosing the Ansatz for $y_p$

| Form of $f(x)$ | Ansatz for $y_p$ |
|---|---|
| Polynomial degree $n$ | $A_n x^n + \cdots + A_1 x + A_0$ |
| $e^{ax}$ | $Ae^{ax}$ |
| $\sin(bx)$ or $\cos(bx)$ | $A\cos(bx) + B\sin(bx)$ |
| $e^{ax}\sin(bx)$ | $e^{ax}(A\cos(bx)+B\sin(bx))$ |
| Product of above | Product of corresponding ansatzes |

> **Exception (modification rule):** If the ansatz duplicates a term in $y_c$, multiply it by $x$ (or $x^2$, etc.) until it no longer overlaps.

### Examples

**Example 1:** $y'' - 5y' + 6y = 4x + 1$

Complementary: $m^2 - 5m + 6 = (m-2)(m-3) = 0$, so $y_c = C_1 e^{2x} + C_2 e^{3x}$

Particular (try $y_p = Ax + B$):
$$0 - 5A + 6Ax + 6B = 4x + 1$$
$$6A = 4 \implies A = \tfrac{2}{3}, \quad 6B - 5A = 1 \implies B = \tfrac{13}{18}$$

$$\boxed{y = C_1 e^{2x} + C_2 e^{3x} + \frac{2}{3}x + \frac{13}{18}}$$

**Example 2:** $y'' + 4y' = 8e^{2x}$

Complementary: $m(m+4) = 0 \implies y_c = C_1 + C_2 e^{-4x}$

Particular (try $y_p = Ae^{2x}$):
$$4Ae^{2x} + 8Ae^{2x} = 12Ae^{2x} = 8e^{2x} \implies A = \tfrac{2}{3}$$

$$\boxed{y = C_1 + C_2 e^{-4x} + \frac{2}{3}e^{2x}}$$

**Example 3 (Trig forcing):** $y'' + 4y' = 2\cos(3x)$

Complementary: $y_c = C_1 + C_2 e^{-4x}$

Particular (try $y_p = A\cos(3x) + B\sin(3x)$):
$$y_p'' + 4y_p' = (-9A + 12B)\cos(3x) + (-9B - 12A)\sin(3x) = 2\cos(3x)$$

$$-9A + 12B = 2, \quad -9B - 12A = 0 \implies A = -\tfrac{2}{25},\; B = \tfrac{8}{75}$$

$$\boxed{y = C_1 + C_2 e^{-4x} - \frac{2}{25}\cos(3x) + \frac{8}{75}\sin(3x)}$$

---

## 10. Reduction of Order

If one solution $y_1$ to a second-order homogeneous ODE is known, a second linearly independent solution is:

$$y_2 = y_1 \int \frac{e^{-\int P(x)\,dx}}{y_1^2}\,dx$$

where $P(x)$ is the coefficient of $y'$ after putting the equation in standard form.

**Examples:**

**(a)** $y'' - 4y' + 4y = 0$, $\quad y_1 = e^{2x}$

$$y_2 = e^{2x}\int \frac{e^{4x}}{e^{4x}}\,dx = e^{2x}\int 1\,dx = xe^{2x}$$

**(b)** $y'' + 16y = 0$, $\quad y_1 = \cos(4x)$

$$y_2 = \cos(4x)\int \sec^2(4x)\,dx = \cos(4x)\cdot\frac{1}{4}\tan(4x) = \frac{1}{4}\sin(4x)$$

**(c)** $9y'' - 12y' + 4y = 0$, $\quad y_1 = e^{2x/3}$ $\implies P = -\tfrac{4}{3}$

$$y_2 = e^{2x/3}\int 1\,dx = xe^{2x/3}$$

**(d)** $x^2y'' - 7xy' + 16y = 0$, $\quad y_1 = x^4$ $\implies P = -\tfrac{7}{x}$

$$y_2 = x^4\int \frac{x^7}{x^8}\,dx = x^4\int x^{-1}\,dx = x^4 \ln x$$

**(e)** $xy'' + y' = 0$, $\quad y_1 = \ln x$ $\implies P = \tfrac{1}{x}$

$$y_2 = \ln x \int \frac{x^{-1}}{(\ln x)^2}\,dx = 1$$

---

## 11. Mass-Spring Systems

The motion of a mass-spring-damper system satisfies:
$$mu'' + \gamma u' + ku = F(t)$$

| Parameter | Meaning |
|---|---|
| $m$ | mass (kg) |
| $\gamma$ | damping coefficient (Ns/m) |
| $k$ | spring constant (N/m) |
| $F(t)$ | external forcing |

### Classification

| Condition | Type |
|---|---|
| $F(t) = 0$ | Free (unforced) |
| $\gamma = 0$ | Undamped |
| $\gamma^2 - 4mk < 0$ | **Underdamped** (oscillates, decays) |
| $\gamma^2 - 4mk = 0$ | **Critically damped** (fastest decay, no oscillation) |
| $\gamma^2 - 4mk > 0$ | **Overdamped** (decays without oscillation) |

**Example:** $m = 1$, $\gamma = 14$, $k = 98$, $u(0)=2$, $u'(0)=-3.5$

$$u'' + 14u' + 98u = 0$$
$$r = \frac{-14 \pm \sqrt{196 - 392}}{2} = -7 \pm 7i$$

Check: $\gamma^2 = 196 < 4(1)(98) = 392$ → **underdamped**

$$u(t) = e^{-7t}(C_1\cos 7t + C_2\sin 7t)$$

Apply ICs: $C_1 = 2$, $\;-7C_1 + 7C_2 = -3.5 \implies C_2 = 1.5$

$$\boxed{u(t) = e^{-7t}(2\cos 7t + 1.5\sin 7t)}$$

---

## 12. Laplace Transforms

The **Laplace transform** converts a differential equation in $t$ into an algebraic equation in $s$:

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t)\,dt$$

### Derivations of Common Transforms

$$
\mathcal{L}\{1\} = \frac{1}{s}, \qquad
\mathcal{L}\{t\} = \frac{1}{s^2}, \qquad
\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}
$$

$$
\mathcal{L}\{e^{at}\} = \frac{1}{s-a}, \qquad
\mathcal{L}\{f'(t)\} = sF(s) - f(0), \qquad
\mathcal{L}\{f''(t)\} = s^2F(s) - sf(0) - f'(0)
$$

### Laplace Transform Table

| $f(t)$ | $F(s) = \mathcal{L}\{f(t)\}$ |
|---|---|
| $1$ | $\dfrac{1}{s}$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ |
| $\sin(at)$ | $\dfrac{a}{s^2+a^2}$ |
| $\cos(at)$ | $\dfrac{s}{s^2+a^2}$ |
| $e^{ct}\sin(at)$ | $\dfrac{a}{(s-c)^2+a^2}$ |
| $e^{ct}\cos(at)$ | $\dfrac{s-c}{(s-c)^2+a^2}$ |
| $t^n e^{ct}$ | $\dfrac{n!}{(s-c)^{n+1}}$ |
| $f'(t)$ | $sF(s) - f(0)$ |
| $f''(t)$ | $s^2F(s) - sf(0) - f'(0)$ |
| $U(t-c)$ | $\dfrac{e^{-cs}}{s}$ |
| $f(t-c)\,U(t-c)$ | $e^{-cs}F(s)$ |
| $g(t)\,U(t-c)$ | $e^{-cs}\,\mathcal{L}\{g(t+c)\}$ |
| $\delta(t-a)$ | $e^{-as}$ |
| $t^n f(t)$ | $(-1)^n F^{(n)}(s)$ |

### Inverse Laplace — Partial Fractions

Break $F(s)$ into recognizable pieces using partial fraction decomposition, then read off $f(t)$ from the table.

**Example 1:**

$$F(s) = \frac{11}{s+2} - \frac{7}{s^3} + \frac{2s+5}{s^2+36}$$

$$f(t) = 11e^{-2t} - \frac{7}{2}t^2 + 2\cos(6t) + \frac{5}{6}\sin(6t)$$

**Example 2:**

$$F(s) = \frac{9s^2+3s+16}{s(s^2+4)} = \frac{4}{s} + \frac{5s+3}{s^2+4}$$

$$f(t) = 4 + 5\cos(2t) + \frac{3}{2}\sin(2t)$$

### Solving IVPs with Laplace Transforms

**Steps:**
1. Take $\mathcal{L}$ of both sides (use derivative rules with ICs)
2. Solve algebraically for $Y(s)$
3. Partial fraction decompose $Y(s)$
4. Take $\mathcal{L}^{-1}$ to recover $y(t)$

**Example:** $3y' + 8y = 2$, $\quad y(0) = 1$

$$
\begin{align}
3(sY - 1) + 8Y &= \frac{2}{s} \\[6pt]
Y(s) &= \frac{3s+2}{s(3s+8)} = \frac{1/4}{s} + \frac{3/4}{s + 8/3} \\[8pt]
y(t) &= \frac{1}{4} + \frac{3}{4}e^{-8t/3}
\end{align}
$$

---

## 13. Unit Step Function and Piecewise Forcing

The **Heaviside unit step function** is:
$$U(t-c) = \begin{cases} 0 & t < c \\ 1 & t \geq c \end{cases}$$

$$\mathcal{L}\{U(t-c)\} = \frac{e^{-cs}}{s}$$

**Key formula for shifting:** To take $\mathcal{L}\{g(t)\,U(t-c)\}$, substitute $t \to t+c$:
$$\mathcal{L}\{g(t)\,U(t-c)\} = e^{-cs}\,\mathcal{L}\{g(t+c)\}$$

**Examples:**

**1.** $\mathcal{L}\{t\,U(t-2)\}$: write $t = (t-2) + 2$, so $g(u) = u + 2$

$$= e^{-2s}\!\left(\frac{1}{s^2} + \frac{2}{s}\right)$$

**2.** $\mathcal{L}\{\cos(2t)\,U(t-\pi)\}$: $\cos(2(u+\pi)) = \cos(2u)$

$$= e^{-\pi s}\cdot\frac{s}{s^2+4}$$

**3.** $\mathcal{L}\{t^2\,U(t-1)\}$: $(u+1)^2 = u^2 + 2u + 1$

$$= e^{-s}\!\left(\frac{2}{s^3} + \frac{2}{s^2} + \frac{1}{s}\right)$$

**4.** $\mathcal{L}\{\sin t\,(1 - U(t-2\pi))\}$: $\sin(u + 2\pi) = \sin u$

$$= \frac{1-e^{-2\pi s}}{s^2+1}$$

### Inverse Unit Step Examples

**1.** $\mathcal{L}^{-1}\!\left\{\dfrac{e^{-\pi s}}{s^2+1}\right\} = \sin(t-\pi)\,U(t-\pi)$

**2.** $\mathcal{L}^{-1}\!\left\{\dfrac{e^{-s}}{s(s+1)}\right\}$: partial fractions give $\tfrac{1}{s} - \tfrac{1}{s+1}$

$$= \bigl(1 - e^{-(t-1)}\bigr)\,U(t-1)$$

---

## 14. Systems of Differential Equations

A **system** of first-order linear ODEs can be written as $\mathbf{x}' = A\mathbf{x}$, where $A$ is a constant matrix. The solution structure mirrors the characteristic equation approach.

**General method:**
1. Find eigenvalues $\lambda$ of $A$ via $\det(A - \lambda I) = 0$
2. For each $\lambda$, find eigenvector $\mathbf{v}$ from $(A-\lambda I)\mathbf{v} = 0$
3. Assemble the general solution

### Case 1: Distinct Real Eigenvalues

$$\mathbf{x}(t) = C_1\,\mathbf{v}^{(1)}e^{\lambda_1 t} + C_2\,\mathbf{v}^{(2)}e^{\lambda_2 t}$$

**Example:** $A = \begin{pmatrix}10 & -5 \\ 8 & -12\end{pmatrix}$

$$\det(A - \lambda I) = \lambda^2 + 2\lambda - 80 = 0 \implies \lambda_1 = 8,\; \lambda_2 = -10$$

Eigenvectors: $\mathbf{v}^{(1)} = \begin{pmatrix}5\\2\end{pmatrix}$ for $\lambda = 8$, $\quad \mathbf{v}^{(2)} = \begin{pmatrix}5\\20\end{pmatrix}$ for $\lambda = -10$

$$\mathbf{x}(t) = C_1\begin{pmatrix}5\\2\end{pmatrix}e^{8t} + C_2\begin{pmatrix}5\\20\end{pmatrix}e^{-10t}$$

### Case 2: Repeated Eigenvalue

If $\lambda$ has multiplicity 2 but only one eigenvector $\mathbf{v}$, find a **generalized eigenvector** $\mathbf{w}$ from $(A - \lambda I)\mathbf{w} = \mathbf{v}$:

$$\mathbf{x}(t) = \bigl[C_1\,\mathbf{v} + C_2(t\,\mathbf{v} + \mathbf{w})\bigr]e^{\lambda t}$$

**Example:** $A = \begin{pmatrix}-1 & 3 \\ -3 & 5\end{pmatrix}$, $\quad \lambda = 2$ (repeated)

$\mathbf{v} = \begin{pmatrix}1\\1\end{pmatrix}$, $\quad \mathbf{w} = \begin{pmatrix}0\\1\end{pmatrix}$

$$\mathbf{x}(t) = \left[C_1\begin{pmatrix}1\\1\end{pmatrix} + C_2\!\left(t\begin{pmatrix}1\\1\end{pmatrix}+\begin{pmatrix}0\\1\end{pmatrix}\right)\right]e^{2t}$$

### Case 3: Complex Eigenvalues $\lambda = \alpha \pm \beta i$

Find the eigenvector $\mathbf{k} = \text{Re}(\mathbf{k}) + i\,\text{Im}(\mathbf{k})$ for $\lambda = \alpha + \beta i$. Then:

$$\mathbf{x}(t) = e^{\alpha t}\!\left[C_1\bigl(\text{Re}(\mathbf{k})\cos\beta t - \text{Im}(\mathbf{k})\sin\beta t\bigr) + C_2\bigl(\text{Re}(\mathbf{k})\sin\beta t + \text{Im}(\mathbf{k})\cos\beta t\bigr)\right]$$

**Example:** $A = \begin{pmatrix}5 & 1 \\ -2 & 3\end{pmatrix}$

$$\lambda^2 - 8\lambda + 17 = 0 \implies \lambda = 4 \pm i$$

Eigenvector for $\lambda = 4+i$: $\;\mathbf{k} = \begin{pmatrix}-1\\1-i\end{pmatrix}$, $\quad \text{Re}(\mathbf{k}) = \begin{pmatrix}-1\\1\end{pmatrix}$, $\;\text{Im}(\mathbf{k}) = \begin{pmatrix}0\\-1\end{pmatrix}$

$$\mathbf{x}(t) = e^{4t}\!\left[C_1\!\left(\begin{pmatrix}-1\\1\end{pmatrix}\cos t + \begin{pmatrix}0\\1\end{pmatrix}\sin t\right) + C_2\!\left(\begin{pmatrix}-1\\1\end{pmatrix}\sin t - \begin{pmatrix}0\\1\end{pmatrix}\cos t\right)\right]$$
