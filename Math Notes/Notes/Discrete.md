---
title: Discrete
parent: Math Notes
nav_order: 1
---
# Discrete Mathematics Notes

---

## 1. Sets

### What is a Set?
A **set** is a well-defined collection of distinct objects called **elements**.

**Examples:**
- $\{1, 2, 3\}$
- $\{2, 4, 6, 8, 10\}$
- $\{\text{dogs}\}$

**Set Equality:** Order does not matter.
$$\{1, 2, 3\} = \{3, 2, 1\}$$

### Membership

| Notation | Meaning |
|---|---|
| $x \in A$ | $x$ is an element of $A$ |
| $x \notin A$ | $x$ is not an element of $A$ |

**Examples:**
- $8 \in \{2,4,6,8,10\}$
- $5 \notin \{2,4,6,8,10\}$
- $\{2\} \notin \{1,2,3\}$ — because $\{2\} \neq 2$; a set is not the same as its element
- $\{2\} \in \{\{1\},\{2\}\}$ — here $\{2\}$ is itself an element

> **Key Rule:** $n \neq \{n\}$. A set containing one element is not the same as that element.

---

### Set Builder Notation

$$\{x \mid x \text{ satisfies some property}\}$$

**Common Number Sets:**

| Symbol | Set |
|---|---|
| $\mathbb{Z}$ | Integers $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ |
| $\mathbb{R}$ | Real Numbers |
| $\mathbb{Q}$ | Rational Numbers |
| $\mathbb{N}$ | Natural Numbers $\{0, 1, 2, \ldots\}$ |
| $\mathbb{C}$ | Complex Numbers |
| $\mathbb{Z}^+$ | Positive Integers |

**Examples:**
- $\{n \in \mathbb{Z} \mid n > 0\} = \mathbb{Z}^+$
- $A = \{x \in \mathbb{R} \mid 2 < x \leq 5\} = (2, 5]$
- $B = \{x \in \mathbb{Z} \mid 2 < x \leq 5\} = \{3, 4, 5\}$

---

### Subsets

$$A \subseteq B \iff \forall x,\; x \in A \Rightarrow x \in B$$

- Every set is a subset of itself: $A \subseteq A$
- $A \not\subseteq B \iff \exists\, x \in A$ such that $x \notin B$
- **Proper subset** $A \subsetneq B$: $A \subseteq B$ and $A \neq B$

**Example:** With $A = (2,5]$ and $B = \{3,4,5\}$:
- $B \subseteq A$ since every integer in $B$ lies in $(2,5]$
- $A \not\subseteq B$ since $2.5 \in A$ but $2.5 \notin B$

**Proof that $C \subseteq D$ when $C$ = even integers and $D = \{n \in \mathbb{Z} \mid \exists\, k \in \mathbb{Z},\; n = 2k\}$:**

Let $n \in C$. Then $n$ is even, so by definition $n = 2k$ for some $k \in \mathbb{Z}$. Thus $n \in D$. Similarly, if $n \in D$ then $n = 2k$, making $n$ even, so $n \in C$. Therefore $C = D$.

---

### The Empty Set

$$\emptyset = \{\} \quad \text{(no elements)}$$

- $\emptyset \subseteq A$ for every set $A$ — vacuously true, since there is no $x \in \emptyset$ to violate the condition.

---

### Power Set

$$\mathcal{P}(X) = \{\text{all subsets of } X\}$$

If $|X| = n$ then $|\mathcal{P}(X)| = 2^n$.

**Examples:**
- $X = \{a, b\}$: $\mathcal{P}(X) = \{\emptyset,\, \{a\},\, \{b\},\, \{a,b\}\}$
- $Y = \{a, b, c\}$: $\mathcal{P}(Y) = \{\emptyset,\, \{a\},\, \{b\},\, \{c\},\, \{a,b\},\, \{a,c\},\, \{b,c\},\, \{a,b,c\}\}$

---

### Set Operations

| Operation | Definition | Meaning |
|---|---|---|
| $A \cup B$ | $\{x \mid x \in A \text{ or } x \in B\}$ | Union |
| $A \cap B$ | $\{x \mid x \in A \text{ and } x \in B\}$ | Intersection |
| $A - B$ | $\{x \in A \mid x \notin B\}$ | Difference |
| $A^c$ | $\{x \in U \mid x \notin A\}$ | Complement |

**Example:** Let $U = \{-5,\ldots,5\}$, $A = \{1,2,3,4,5\}$, $B = \{-1,2,-3,4,-5\}$

- $A \cup B = \{-5,-3,-1,1,2,3,4,5\}$
- $A \cap B = \{2,4\}$
- $A - B = \{1,3,5\}$
- $A^c = \{-5,-4,-3,-2,-1,0\}$

---

### Set Identities

| Law | Identity |
|---|---|
| Commutative | $A \cup B = B \cup A$ |
| Associative | $A \cup (B \cup C) = (A \cup B) \cup C$ |
| Distributive | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| De Morgan's | $(A \cup B)^c = A^c \cap B^c$ |
| De Morgan's | $(A \cap B)^c = A^c \cup B^c$ |
| Identity | $A \cup \emptyset = A$, $\quad A \cap U = A$ |
| Complement | $A \cup A^c = U$, $\quad A \cap A^c = \emptyset$ |

**Proof (Element Argument):** $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

*Part 1:* Let $x \in A \cap (B \cup C)$. Then $x \in A$ and ($x \in B$ or $x \in C$).
- If $x \in B$: then $x \in A \cap B \subseteq (A \cap B) \cup (A \cap C)$.
- If $x \in C$: then $x \in A \cap C \subseteq (A \cap B) \cup (A \cap C)$.

*Part 2:* Let $x \in (A \cap B) \cup (A \cap C)$. Then $x \in A \cap B$ or $x \in A \cap C$.
- Either way, $x \in A$ and $x \in B \cup C$, so $x \in A \cap (B \cup C)$. $\blacksquare$

**Algebraic Proof:** $(A \cup B) - C = (A - C) \cup (B - C)$

$$
\begin{aligned}
(A \cup B) - C &= (A \cup B) \cap C^c & \text{(set difference law)} \\
&= C^c \cap (A \cup B) & \text{(commutative)} \\
&= (C^c \cap A) \cup (C^c \cap B) & \text{(distributive)} \\
&= (A - C) \cup (B - C) & \text{(set difference law)}
\end{aligned}
$$

---

### Partitions

A **partition** of a set $X$ is a collection of nonempty, pairwise disjoint sets $A_1, A_2, \ldots, A_n$ such that:
$$A_1 \cup A_2 \cup \cdots \cup A_n = X \quad \text{and} \quad A_i \cap A_j = \emptyset \text{ for } i \neq j$$

**Example:** $A = \{1,2\}$, $B = \{3,4\}$, $C = \{5,6\}$ is a partition of $X = \{1,2,3,4,5,6\}$.

---

## 2. Logic

### Statements and Predicates

A **statement (proposition)** is a sentence that is definitively **True** or **False** — never both, never neither.

| Example | Statement? | Truth Value |
|---|---|---|
| "It is raining outside" | Yes | T or F |
| "$x > 7$" | No (depends on $x$) | — |
| "$9 > 7$" | Yes | T |
| "$9 < 7$" | Yes | F |

A **predicate** is a sentence with free variables that becomes a statement once those variables are specified.

- $P(x)$: "$x > 7$" with domain $\mathbb{R}$ — truth set: $\{x \in \mathbb{R} \mid x > 7\} = (7, \infty)$
- $P(x)$: "$x^2 = 4$" — truth set: $\{-2, 2\}$

---

### Compound Statements

| Connective | Symbol | Meaning |
|---|---|---|
| Conjunction | $p \land q$ | $p$ and $q$ |
| Disjunction | $p \lor q$ | $p$ or $q$ |
| Negation | $\neg p$ | not $p$ |
| Conditional | $p \to q$ | if $p$ then $q$ |
| Biconditional | $p \leftrightarrow q$ | $p$ if and only if $q$ |

**Truth Tables:**

**Negation $\neg p$:**

| $p$ | $\neg p$ |
|---|---|
| T | F |
| F | T |

**Conjunction $p \land q$:**

| $p$ | $q$ | $p \land q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Disjunction $p \lor q$:**

| $p$ | $q$ | $p \lor q$ |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

---

### Logical Equivalences and Laws

Two statement forms are **logically equivalent** ($\equiv$) if they have identical truth values in every row of their truth table.

**De Morgan's Laws:**
$$\neg(p \land q) \equiv \neg p \lor \neg q$$
$$\neg(p \lor q) \equiv \neg p \land \neg q$$

**Distributive Laws:**
$$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$
$$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$

**Double Negation:** $\neg(\neg p) \equiv p$

**Absorption:** $p \land (p \lor q) \equiv p$

**Negation Laws:** $p \lor \neg p \equiv \mathbf{t}$ (tautology), $\quad p \land \neg p \equiv \mathbf{c}$ (contradiction)

**Tautology ($\mathbf{t}$):** Always true. Example: $p \lor \neg p$.

**Contradiction ($\mathbf{c}$):** Always false. Example: $p \land \neg p$.

**Example using equivalence laws** — Show $\neg(\neg p \land q) \land (p \lor q) \equiv p$:
$$
\begin{aligned}
\neg(\neg p \land q) \land (p \lor q)
&\equiv (\neg\neg p \lor \neg q) \land (p \lor q) & \text{(De Morgan)} \\
&\equiv (p \lor \neg q) \land (p \lor q) & \text{(Double Negation)} \\
&\equiv p \lor (\neg q \land q) & \text{(Distributive)} \\
&\equiv p \lor \mathbf{c} & \text{(Negation Law)} \\
&\equiv p & \text{(Identity Law)}
\end{aligned}
$$

---

### Conditional Statements

$$p \to q \quad \text{"If } p \text{ then } q\text{"}$$

**Truth Table:**

| $p$ | $q$ | $p \to q$ |
|---|---|---|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

> The conditional is **only false** when the hypothesis is true and the conclusion is false.

**Key Equivalence:**
$$p \to q \equiv \neg p \lor q$$
$$\neg(p \to q) \equiv p \land \neg q$$

**Variants of $p \to q$:**

| Name | Form | Equivalent to $p \to q$? |
|---|---|---|
| Converse | $q \to p$ | ✗ |
| Contrapositive | $\neg q \to \neg p$ | ✓ |
| Inverse | $\neg p \to \neg q$ | ✗ (equivalent to converse) |

**Biconditional:** $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$ — true exactly when $p$ and $q$ have the same truth value.

---

### Valid Arguments

An argument is **valid** if: whenever all premises are true, the conclusion must be true.

**Modus Ponens:**
$$\frac{p \to q \qquad p}{\therefore\; q}$$

**Modus Tollens:**
$$\frac{p \to q \qquad \neg q}{\therefore\; \neg p}$$

**Elimination:**
$$\frac{p \lor q \qquad \neg q}{\therefore\; p}$$

**Transitivity (Hypothetical Syllogism):**
$$\frac{p \to q \qquad q \to r}{\therefore\; p \to r}$$

**Generalization:**
$$\frac{p}{\therefore\; p \lor q} \qquad \frac{q}{\therefore\; p \lor q}$$

**Contradiction Rule:**
$$\frac{\neg p \to \mathbf{c}}{\therefore\; p}$$

**Example — Checking Validity with a Truth Table:**

Is the following valid?
$$p \to q \lor \neg r, \quad q \to p \land r \quad \therefore\; p \to r$$

| $p$ | $q$ | $r$ | $p \to q \lor \neg r$ | $q \to p \land r$ | $p \to r$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | T | F | T | F | — |
| T | F | T | F | T | — |
| **T** | **F** | **F** | **T** | **T** | **F** |
| F | T | T | T | F | — |
| F | F | F | T | T | T |

Row 4 has both premises true but conclusion false → **not valid**.

**Common Fallacies:**

- *Converse Error:* Assuming $q \to p$ from $p \to q$ — invalid.
- *Inverse Error:* Assuming $\neg p \to \neg q$ from $p \to q$ — invalid.

---

### Quantifiers

**Universal Quantifier $\forall$:** "For all"
$$\forall x \in \mathbb{R},\; x^2 \geq 0$$

**Existential Quantifier $\exists$:** "There exists"
$$\exists x \in \mathbb{R} \text{ such that } 5x = 0 \quad \text{(true: take } x = 0\text{)}$$

**Negating Quantifiers:**
$$\neg\bigl(\forall x \in D,\; P(x)\bigr) \equiv \exists x \in D \text{ such that } \neg P(x)$$
$$\neg\bigl(\exists x \in D \text{ s.t. } P(x)\bigr) \equiv \forall x \in D,\; \neg P(x)$$

**Negating Conditional Statements:**
$$\neg\bigl(\forall x,\; P(x) \to Q(x)\bigr) \equiv \exists x \text{ s.t. } P(x) \land \neg Q(x)$$

**Example:** Negate "$\forall x \in \mathbb{Z}$, if 4 divides $x$ then 2 divides $x$":
$$\exists x \in \mathbb{Z} \text{ such that } 4 \mid x \text{ and } 2 \nmid x$$
This is false — if 4 divides $x$ evenly, $x$ must be even, so 2 always divides it.

**Nested Quantifiers — Order Matters:**

| Statement | Truth Value |
|---|---|
| $\forall x \in \mathbb{R},\; \exists y \in \mathbb{R}$ s.t. $xy = 0$ | **True** — pick $y = 0$ for any $x$ |
| $\exists x \in \mathbb{R}$ s.t. $\forall y \in \mathbb{R},\; xy = 0$ | **True** — pick $x = 0$; then $xy = 0$ for all $y$ |
| $\forall x \in \mathbb{R},\; \exists y \in \mathbb{R}$ s.t. $5x = y$ | **True** — pick $y = 5x$ |
| $\exists x \in \mathbb{R}$ s.t. $\forall y \in \mathbb{R},\; 5x = y$ | **False** — no single $x$ satisfies this for all $y$ |

> Swapping quantifiers of different types generally changes the truth value.

**Vacuously True:** A statement $\forall x \in D,\; P(x) \to Q(x)$ is vacuously true when $D$ is empty or $P(x)$ is never true — the hypothesis is never satisfied, so the conditional is never falsified.

---

## 3. Elementary Number Theory and Proofs

### Ground Rules
- Integers are closed under addition, subtraction, and multiplication.
- Rationals are closed under addition, subtraction, multiplication, and division (by nonzero).
- Standard algebraic rules (factoring, distribution) apply.

---

### Even and Odd

$$n \text{ is even} \iff \exists\, k \in \mathbb{Z},\; n = 2k$$
$$n \text{ is odd} \iff \exists\, k \in \mathbb{Z},\; n = 2k + 1$$

**Proof:** If $a$ is odd and $b$ is even, then $5a + 4b$ is odd.

Let $a = 2k+1$ and $b = 2l$ for some $k, l \in \mathbb{Z}$. Then:
$$5a + 4b = 5(2k+1) + 4(2l) = 10k + 5 + 8l = 2(5k + 4l + 2) + 1$$
This is of the form $2t + 1$, so $5a + 4b$ is odd. $\blacksquare$

---

### Divisibility

$$d \mid n \iff \exists\, k \in \mathbb{Z},\; n = dk \quad (d \neq 0)$$

Equivalent language: $n$ is divisible by $d$ / $d$ is a factor of $n$ / $n$ is a multiple of $d$.

**Proof:** $\forall\, a,b,c \in \mathbb{Z}$: if $a \mid b$ and $a \mid c$ then $a \mid (b+c)$.

Let $b = ak$ and $c = al$ for some $k,l \in \mathbb{Z}$. Then $b + c = ak + al = a(k+l)$. Since $k+l \in \mathbb{Z}$, we have $a \mid (b+c)$. $\blacksquare$

**Proof:** $\forall\, a,b,c \in \mathbb{Z}$: $(a \mid b) \land (a \mid c) \Rightarrow a^2 \mid (bc)$.

Let $b = ka$ and $c = la$. Then $bc = (ka)(la) = (kl)a^2$, so $a^2 \mid bc$. $\blacksquare$

---

### Prime Numbers

$$p > 1 \text{ is prime} \iff \forall\, r,s \in \mathbb{Z}^+,\; p = rs \Rightarrow (r = 1 \land s = p) \text{ or } (r = p \land s = 1)$$

$$p \text{ is composite} \iff \exists\, r,s \in \mathbb{Z}^+,\; p = rs,\; 1 < r < p,\; 1 < s < p$$

**Theorem (Existence of a Prime Divisor):** Every integer $n > 1$ is divisible by a prime.

*Proof.* If $n$ is prime, done. Otherwise write $n = r_0 s_0$ with $1 < r_0 < n$. If $r_0$ is prime, done. Otherwise write $r_0 = r_1 s_1$ with $1 < r_1 < r_0$. Continue to get:
$$n > r_0 > r_1 > r_2 > \cdots > 1$$
Since these are positive integers this chain must terminate at some $r_k$ which must be prime (otherwise we could factor further). Then $r_k \mid r_{k-1} \mid \cdots \mid n$. $\blacksquare$

---

### Fundamental Theorem of Arithmetic

Every integer $n > 1$ has a **unique** factorization (up to order):
$$n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}, \quad p_1 < p_2 < \cdots < p_k,\; e_i \geq 1$$

**Example:** $3300 = 2^2 \cdot 3 \cdot 5^2 \cdot 11$

**Example:** Given $8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot m = 17 \cdot 16 \cdot 15 \cdot 14 \cdot 13 \cdot 12 \cdot 11 \cdot 10$, does $17 \mid m$?

By unique factorization, $17$ appears exactly once on the right and zero times in $8!$, so $17 \mid m$. Solving: $m = 17 \cdot 13 \cdot 11 \cdot 2$.

---

### Quotient–Remainder Theorem

For any $n \in \mathbb{Z}$ and $d \in \mathbb{Z}^+$, there exist **unique** $q, r \in \mathbb{Z}$ such that:
$$n = dq + r, \quad 0 \leq r < d$$

$q$ is the **quotient**, $r$ is the **remainder**.

**Examples:**
- $621 = 4 \cdot 155 + 1 \Rightarrow q = 155,\; r = 1$
- $-76 = 3 \cdot (-26) + 2 \Rightarrow q = -26,\; r = 2$

**Consequence for $d = 2$:** Every integer is either even ($r=0$) or odd ($r=1$).

**Consequence for $d = 8$:** Every odd integer $n = 2k+1$ satisfies:
$$n^2 = (2k+1)^2 = 4k(k+1) + 1 = 8m + 1$$
since $k(k+1)$ is always even. So **the square of any odd integer is $\equiv 1 \pmod{8}$**.

---

## 4. Proof Techniques

### Direct Proof
Assume the hypothesis, apply definitions and known facts, derive the conclusion.

### Proof by Contrapositive
To prove $p \to q$, instead prove $\neg q \to \neg p$.

**Example:** Prove $n^3$ odd $\Rightarrow$ $n$ odd.

*Contrapositive:* If $n$ is even then $n^3$ is even. Let $n = 2k$. Then $n^3 = 8k^3 = 2(4k^3)$, which is even. $\blacksquare$

### Proof by Contradiction
Assume the statement is false, derive a logical contradiction.

**Example:** Prove the product of a rational and an irrational is irrational.

Suppose $x \in \mathbb{Q}$, $y \notin \mathbb{Q}$, but $xy \in \mathbb{Q}$. Write $x = a/b$ and $xy = c/d$. Then:
$$y = \frac{xy}{x} = \frac{c/d}{a/b} = \frac{cb}{da} \in \mathbb{Q}$$
This contradicts $y \notin \mathbb{Q}$. $\blacksquare$

### Proof by Induction

To prove $P(n)$ for all $n \geq n_0$:
1. **Base case:** Verify $P(n_0)$.
2. **Inductive step:** Assume $P(k)$ (inductive hypothesis). Prove $P(k+1)$.

**Example:** Prove $\displaystyle\sum_{i=1}^{n} \frac{1}{i(i+1)} = \frac{n}{n+1}$ for all $n \geq 1$.

*Base case* $n=1$: $\dfrac{1}{1 \cdot 2} = \dfrac{1}{2} = \dfrac{1}{1+1}$. ✓

*Inductive step:* Assume $\displaystyle\sum_{i=1}^{k} \frac{1}{i(i+1)} = \frac{k}{k+1}$. Then:
$$\sum_{i=1}^{k+1} \frac{1}{i(i+1)} = \frac{k}{k+1} + \frac{1}{(k+1)(k+2)} = \frac{k(k+2)+1}{(k+1)(k+2)} = \frac{(k+1)^2}{(k+1)(k+2)} = \frac{k+1}{k+2}$$
This matches the formula with $n = k+1$. $\blacksquare$

### Disproving Universal Statements (Counterexample)

$$\neg\bigl(\forall x \in D,\; P(x) \to Q(x)\bigr) \equiv \exists x \in D \text{ s.t. } P(x) \land \neg Q(x)$$

**Example:** Disprove $\forall\, a,b \in \mathbb{R},\; a^2 = b^2 \Rightarrow a = b$.

Counterexample: $a = 2$, $b = -2$. Then $a^2 = b^2 = 4$ but $a \neq b$. $\blacksquare$

### Existential Proofs
To prove $\exists x$ with some property, exhibit one concrete example.

- *There exists a prime that is even:* $p = 2$. ✓
- *There exists $n$ expressible as a sum of two primes in two ways:* $10 = 5+5 = 7+3$. ✓
