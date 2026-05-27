---
title: Probability Theory
parent: Math Notes
nav_order: 3
has_toc: true
---

# Intro to Probability Lecture Notes

# Module 1 — Probability & Counting

---

##### Lecture 1 — Basic Counting Rule

### Core Idea
Counting = breaking a problem into stages.

### Basic Counting Rule (Multiplication Rule)
If an experiment has$r$stages and each stage has$n_i$outcomes:

$$
\text{Total outcomes} = n_1 \cdot n_2 \cdots n_r
$$

### Key Insight
- Multiply choices across stages  
- Order of stages matters  

---

##### Lecture 2 — Permutations & Combinations

### Permutations (Order Matters)
$$
P(n,r) = \frac{n!}{(n-r)!}
$$

- Used when order matters (rankings, assignments)

---

### Combinations (Order Does NOT Matter)
$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

- Used when order does not matter (groups, committees)

---

### Key Idea
- Permutations → order matters  
- Combinations → order does not matter  

---

##### Lecture 3 — Multinomial Coefficient

### Multinomial Coefficient
$$
\binom{n}{n_1,n_2,\dots,n_k} = \frac{n!}{n_1!n_2!\cdots n_k!}
$$

### Use Case
- Dividing items into groups of fixed sizes  

### Key Idea
- Generalization of combinations  

---

##### Lecture 4 — Sample Space & Events

### Definitions
- Sample space$S$: all possible outcomes  
- Event$A \subseteq S$: subset of outcomes  

---

### Event Operations

Union:
$$
A \cup B
$$

Intersection:
$$
A \cap B
$$

Complement:
$$
A^c
$$

---

### DeMorgan’s Laws
$$
(A \cup B)^c = A^c \cap B^c
$$
$$
(A \cap B)^c = A^c \cup B^c
$$

---

### Probability (Equally Likely Outcomes)
$$
P(A) = \frac{|A|}{|S|}
$$

---

##### Lecture 5 — Axioms of Probability

### Axioms
1.
$$
0 \leq P(A) \leq 1
$$

2.
$$
P(S) = 1
$$

3.
$$
P\left(\bigcup A_i\right) = \sum P(A_i)
$$

---

### Key Formulas

Complement:
$$
P(A^c) = 1 - P(A)
$$

Union:
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

---

##### Lecture 6 — Practice Concepts

### Core Idea
Combine counting + probability

---

### Common Patterns

At least one:
$$
P(\text{at least one}) = 1 - P(\text{none})
$$

---

Birthday-type problems:
- Use complement  
- Multiply sequential probabilities  

---

### Key Takeaways
- Break into stages  
- Check if order matters  
- Use complement when easier  

---

# Module 2 — Conditional Probability

---

##### Lecture 1 — Conditional Probability

### Core Idea
Update probability with new information.

### Definition
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

- Prior:$P(A)$
- Posterior:$P(A|B)$

---

### Key Insight
- Restrict to event$B$
- Compute probability within that space  

---

##### Lecture 2 — Multiplication Rule & Total Probability

### Multiplication Rule
$$
P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)
$$

---

### General Form
$$
P(A_1 \cap \cdots \cap A_n)
= P(A_1)P(A_2|A_1)\cdots
$$

---

### Law of Total Probability
$$
P(B) = \sum_{i=1}^{n} P(B|A_i)P(A_i)
$$

---

### Key Insight
- Break into cases  
- Use trees  

---

##### Lecture 3 — Bayes’ Theorem

### Bayes’ Rule
$$
P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)}
$$

---

### Key Idea
- Reverse conditioning  

---

##### Lecture 4 — Independence

### Definition
$$
P(A \cap B) = P(A)P(B)
$$

Equivalent:
$$
P(A|B) = P(A)
$$

---

### Key Differences
- Independent → no effect  
- Disjoint → cannot happen together  

---

### Conditional Independence
$$
P(A \cap B | E) = P(A|E)P(B|E)
$$

---

### Key Takeaways
- Update probabilities with info  
- Multiply for joint events  
- Use total probability for cases  
- Bayes reverses conditioning  
- Independence = no influence
  
# Module 3 — Discrete Random Variables

---

##### Lecture 1 — Random Variables & PMF

### Random Variable
A random variable is a function:
$$
X : S \to \mathbb{R}
$$

- Maps outcomes → numbers  
- Events look like:$X = x$

---

### Discrete Random Variable
- Takes finite or countable values  
- Support = values where$P(X = x) > 0$

---

### PMF (Probability Mass Function)
$$
p_X(x) = P(X = x)
$$

### Valid PMF Conditions
-$p_X(x) \ge 0$
-$\sum_x p_X(x) = 1$

---

##### Lecture 2 — CDF & Functions of RVs

### CDF
$$
F_X(x) = P(X \le x)
$$

---

### Key Relationship
- PMF → point probabilities  
- CDF → accumulated probabilities  

---

### Function of Random Variable
If $Y = g(X)$:

$$
P(Y = y) = \sum_{x: g(x)=y} P(X = x)
$$

---

### Key Insight
- Transform values, then recompute probabilities

---

##### Lecture 3 — Expectation & Variance

### Expectation
$$
E(X) = \sum_x x \, p_X(x)
$$

- Weighted average

---

### Function Expectation
$$
E[g(X)] = \sum_x g(x)p_X(x)
$$

---

### Linearity
$$
E(aX + b) = aE(X) + b
$$

---

### Variance
$$
\text{Var}(X) = E[(X - E(X))^2]
$$

Alternative:
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Standard Deviation
$$
SD(X) = \sqrt{\text{Var}(X)}
$$

---

##### Lecture 4 — Independence, Bernoulli, Binomial

### Independence (Random Variables)
$$
P(X=x, Y=y) = P(X=x)P(Y=y)
$$

---

### Bernoulli Distribution
$$
P(X=1)=p,\quad P(X=0)=1-p
$$

- One trial (success/failure)

---

### Properties
$$
E(X)=p, \quad \text{Var}(X)=p(1-p)
$$

---

### Binomial Distribution
$$
P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}
$$

-$n$trials  
- Independent  
- Same probability$p$

---

##### Lecture 5 — Binomial (Applications)

### Conditions
- Fixed$n$
- Independent trials  
- Same$p$
- Two outcomes  

---

### Properties
$$
E(X)=np, \quad \text{Var}(X)=np(1-p)
$$

---

### Key Trick
Use complement for “at least”:
$$
P(X \ge k) = 1 - P(X < k)
$$

---

##### Lecture 6 — Poisson & Negative Binomial

### Poisson Distribution
$$
P(X=x) = \frac{e^{-\lambda}\lambda^x}{x!}
$$

- Counts events in interval  
- Models rare events  

---

### Properties
$$
E(X)=\lambda, \quad \text{Var}(X)=\lambda
$$

---

### Approximation
$$
\text{Bin}(n,p) \approx \text{Pois}(\lambda = np)
$$

---

### Negative Binomial
$$
P(X=n) = \binom{n-1}{r-1} p^r (1-p)^{n-r}
$$

- Number of trials until$r$successes  

---

##### Lecture 7 — Geometric & Hypergeometric

### Geometric Distribution
$$
P(X=x) = (1-p)^{x-1}p
$$

- Trials until first success  

---

### Properties
$$
E(X)=\frac{1}{p}, \quad \text{Var}(X)=\frac{1-p}{p^2}
$$

---

### Hypergeometric Distribution
$$
P(X=x) = \frac{\binom{m}{x}\binom{N-m}{n-x}}{\binom{N}{n}}
$$

- Sampling without replacement  

---

### Key Difference
- Binomial → independent trials  
- Hypergeometric → dependent (no replacement)  

---

##### Lecture 8 — Distribution Summary

### When to Use

- Bernoulli → one trial  
- Binomial → fixed number of trials  
- Poisson → count over time/space  
- Negative Binomial → until$r$successes  
- Geometric → until first success  
- Hypergeometric → sampling without replacement  

---

### Key Relationships
- Bernoulli = Binomial with$n=1$
- Geometric = Negative Binomial with$r=1$
- Binomial → Poisson (large$n$, small$p$)  

---

### Core Takeaways
- Random variables map outcomes to numbers  
- PMF describes probabilities  
- Expectation = average  
- Variance = spread  
- Choose distribution based on setup

# Module 4 — Continuous Random Variables

---

##### Lecture 1 — Continuous RV, PDF & CDF

### Continuous Random Variable
- Takes values over intervals  
- Examples: height, time, distance  

---

### CDF
$$
F_X(x) = P(X \le x)
$$

---

### PDF
$$
f(x) = \frac{d}{dx}F_X(x)
$$

---

### Probability via PDF
$$
P(a \le X \le b) = \int_a^b f(x)\,dx
$$

---

### Key Properties
-$f(x) \ge 0$
-$\int_{-\infty}^{\infty} f(x)\,dx = 1$
-$P(X = a) = 0$

---

##### Lecture 2 — Transformations & Expectation

### Transformation
If $Y = g(X)$(monotonic):

$$
f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|
$$

---

### Expectation (Continuous)
$$
E(X) = \int_{-\infty}^{\infty} x f(x)\,dx
$$

---

### Function Expectation
$$
E[g(X)] = \int g(x)f(x)\,dx
$$

---

### Key Idea
- Replace sums → integrals  

---

##### Lecture 3 — Variance (Continuous)

### Variance
$$
\text{Var}(X) = E[(X - E(X))^2]
$$

Alternative:
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Key Insight
- Same formulas as discrete, but integrals  

---

##### Lecture 4 — Uniform & Exponential

### Uniform Distribution
$$
f(x) = \frac{1}{b-a}, \quad a < x < b
$$

- All values equally likely  

---

### Properties
$$
E(X) = \frac{a+b}{2}, \quad \text{Var}(X) = \frac{(b-a)^2}{12}
$$

---

### Exponential Distribution
$$
f(x) = \lambda e^{-\lambda x}, \quad x > 0
$$

---

### Properties
$$
E(X) = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}
$$

---

### Memoryless Property
$$
P(X \ge s+t \mid X \ge s) = P(X \ge t)
$$

---

##### Lecture 5 — Normal Distribution

### PDF
$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

---

### Properties
- Mean:$\mu$
- Variance:$\sigma^2$
- Symmetric, bell-shaped  

---

### Standardization
$$
Z = \frac{X - \mu}{\sigma}
$$

---

##### Lecture 6 — Empirical Rule & Chi-Square

### Empirical Rule
-$P(|Z| < 1) \approx 0.68$
-$P(|Z| < 2) \approx 0.95$
-$P(|Z| < 3) \approx 0.997$

---

### Chi-Squared Distribution
$$
Q = Z_1^2 + \cdots + Z_k^2 \sim \chi^2_k
$$

---

### Key Idea
- Sum of squared standard normals  

---

##### Lecture 7 — Gamma & Beta

### Gamma Distribution
$$
f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}
$$

- Models waiting time  

---

### Key Relationship
$\text{Gamma}(1,\lambda) = \text{Exponential}$

---

### Beta Distribution
$$
f(x) = \frac{1}{B(\alpha,\beta)} x^{\alpha-1}(1-x)^{\beta-1}, \quad 0<x<1
$$

- Models proportions  

---

##### Lecture 8 — Weibull & Log-Normal

### Weibull Distribution
$$
f(x) = \gamma \lambda x^{\gamma-1} e^{-\lambda x^\gamma}
$$

- Flexible lifetime model  

---

### Log-Normal Distribution
$$
f(x) = \frac{1}{x\sigma \sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}
$$

---

### Key Idea
- If $\ln X \sim N(\mu,\sigma^2)$, then$X$is log-normal  

---

##### Lecture 9 — Summary & Relationships

### When to Use

- Uniform → equal likelihood  
- Normal → symmetric data  
- Exponential → waiting time  
- Gamma → sum of waiting times  
- Beta → proportions  
- Chi-square → sum of squares  
- Weibull → lifetime modeling  
- Log-normal → positive, skewed data  

---

### Key Relationships
- Exponential ↔ Poisson (waiting vs count)  
- Gamma → sum of exponentials  
- Beta from Gamma ratios  
- Normal → basis for many distributions  

---

### Core Takeaways
- Continuous → use integrals  
- PDF gives density, not point probability  
- CDF accumulates probability  
- Choose distribution based on context

# Module 5 — Moment Generating Functions

---

##### Lecture 1 — Moments & MGF

### Moments
- k-th moment:
$$
E(X^k)
$$

- k-th central moment:
$$
E[(X - \mu)^k]
$$

---

### Skewness
$$
\text{Skew}(X) = E\left[\left(\frac{X-\mu}{\sigma}\right)^3\right]
$$

---

### Kurtosis
$$
\text{Kurt}(X) = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] - 3
$$

---

### Moment Generating Function (MGF)
$$
M_X(t) = E(e^{tX})
$$

---

### Key Properties
-$M(0) = 1$
- Encodes all moments  
- Must be finite near$t = 0$

---

##### Lecture 2 — Using MGF

### Moments from MGF
- Take derivatives:
$$
E(X^k) = M_X^{(k)}(0)
$$

---

### First Two Moments
$$
E(X) = M'_X(0)
$$
$$
E(X^2) = M''_X(0)
$$

---

### Variance
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Transformation Property
If $Y = a + bX$:
$$
M_Y(t) = e^{at} M_X(bt)
$$

---

### Key Idea
- MGF turns calculus → moments  

---

##### Lecture 3 — Sums of Random Variables

### Sum of Independent RVs
If $U = X_1 + \cdots + X_n$:

$$
M_U(t) = M_{X_1}(t)\cdots M_{X_n}(t)
$$

---

### Key Insight
- MGFs multiply for independent sums  

---

### Important Results
- Sum of normals → normal  
- Sum of Poissons → Poisson  

---

### Example Pattern
If $X_i \sim \text{Bern}(p)$, then:
$$
\sum X_i \sim \text{Binomial}(n,p)
$$

---

### Core Takeaways
- MGF uniquely determines distribution  
- Derivatives give moments  
- Products handle sums  
- Useful for proving distribution resultsheory

# Module 1 — Probability & Counting

---

##### Lecture 1 — Basic Counting Rule

### Core Idea
Counting = breaking a problem into stages.

### Basic Counting Rule (Multiplication Rule)
If an experiment has$r$stages and each stage has$n_i$outcomes:

$$
\text{Total outcomes} = n_1 \cdot n_2 \cdots n_r
$$

### Key Insight
- Multiply choices across stages  
- Order of stages matters  

---

##### Lecture 2 — Permutations & Combinations

### Permutations (Order Matters)
$$
P(n,r) = \frac{n!}{(n-r)!}
$$

- Used when order matters (rankings, assignments)

---

### Combinations (Order Does NOT Matter)
$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

- Used when order does not matter (groups, committees)

---

### Key Idea
- Permutations → order matters  
- Combinations → order does not matter  

---

##### Lecture 3 — Multinomial Coefficient

### Multinomial Coefficient
$$
\binom{n}{n_1,n_2,\dots,n_k} = \frac{n!}{n_1!n_2!\cdots n_k!}
$$

### Use Case
- Dividing items into groups of fixed sizes  

### Key Idea
- Generalization of combinations  

---

##### Lecture 4 — Sample Space & Events

### Definitions
- Sample space$S$: all possible outcomes  
- Event$A \subseteq S$: subset of outcomes  

---

### Event Operations

Union:
$$
A \cup B
$$

Intersection:
$$
A \cap B
$$

Complement:
$$
A^c
$$

---

### DeMorgan’s Laws
$$
(A \cup B)^c = A^c \cap B^c
$$
$$
(A \cap B)^c = A^c \cup B^c
$$

---

### Probability (Equally Likely Outcomes)
$$
P(A) = \frac{|A|}{|S|}
$$

---

##### Lecture 5 — Axioms of Probability

### Axioms
1.
$$
0 \leq P(A) \leq 1
$$

2.
$$
P(S) = 1
$$

3.
$$
P\left(\bigcup A_i\right) = \sum P(A_i)
$$

---

### Key Formulas

Complement:
$$
P(A^c) = 1 - P(A)
$$

Union:
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

---

##### Lecture 6 — Practice Concepts

### Core Idea
Combine counting + probability

---

### Common Patterns

At least one:
$$
P(\text{at least one}) = 1 - P(\text{none})
$$

---

Birthday-type problems:
- Use complement  
- Multiply sequential probabilities  

---

### Key Takeaways
- Break into stages  
- Check if order matters  
- Use complement when easier  

---

# Module 2 — Conditional Probability

---

##### Lecture 1 — Conditional Probability

### Core Idea
Update probability with new information.

### Definition
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

- Prior:$P(A)$
- Posterior:$P(A|B)$

---

### Key Insight
- Restrict to event$B$
- Compute probability within that space  

---

##### Lecture 2 — Multiplication Rule & Total Probability

### Multiplication Rule
$$
P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)
$$

---

### General Form
$$
P(A_1 \cap \cdots \cap A_n)
= P(A_1)P(A_2|A_1)\cdots
$$

---

### Law of Total Probability
$$
P(B) = \sum_{i=1}^{n} P(B|A_i)P(A_i)
$$

---

### Key Insight
- Break into cases  
- Use trees  

---

##### Lecture 3 — Bayes’ Theorem

### Bayes’ Rule
$$
P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)}
$$

---

### Key Idea
- Reverse conditioning  

---

##### Lecture 4 — Independence

### Definition
$$
P(A \cap B) = P(A)P(B)
$$

Equivalent:
$$
P(A|B) = P(A)
$$

---

### Key Differences
- Independent → no effect  
- Disjoint → cannot happen together  

---

### Conditional Independence
$$
P(A \cap B | E) = P(A|E)P(B|E)
$$

---

### Key Takeaways
- Update probabilities with info  
- Multiply for joint events  
- Use total probability for cases  
- Bayes reverses conditioning  
- Independence = no influence
  
# Module 3 — Discrete Random Variables

---

##### Lecture 1 — Random Variables & PMF

### Random Variable
A random variable is a function:
$$
X : S \to \mathbb{R}
$$

- Maps outcomes → numbers  
- Events look like:$X = x$

---

### Discrete Random Variable
- Takes finite or countable values  
- Support = values where$P(X = x) > 0$

---

### PMF (Probability Mass Function)
$$
p_X(x) = P(X = x)
$$

### Valid PMF Conditions
-$p_X(x) \ge 0$
-$\sum_x p_X(x) = 1$

---

##### Lecture 2 — CDF & Functions of RVs

### CDF
$$
F_X(x) = P(X \le x)
$$

---

### Key Relationship
- PMF → point probabilities  
- CDF → accumulated probabilities  

---

### Function of Random Variable
If $Y = g(X)$:

$$
P(Y = y) = \sum_{x: g(x)=y} P(X = x)
$$

---

### Key Insight
- Transform values, then recompute probabilities

---

##### Lecture 3 — Expectation & Variance

### Expectation
$$
E(X) = \sum_x x \, p_X(x)
$$

- Weighted average

---

### Function Expectation
$$
E[g(X)] = \sum_x g(x)p_X(x)
$$

---

### Linearity
$$
E(aX + b) = aE(X) + b
$$

---

### Variance
$$
\text{Var}(X) = E[(X - E(X))^2]
$$

Alternative:
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Standard Deviation
$$
SD(X) = \sqrt{\text{Var}(X)}
$$

---

##### Lecture 4 — Independence, Bernoulli, Binomial

### Independence (Random Variables)
$$
P(X=x, Y=y) = P(X=x)P(Y=y)
$$

---

### Bernoulli Distribution
$$
P(X=1)=p,\quad P(X=0)=1-p
$$

- One trial (success/failure)

---

### Properties
$$
E(X)=p, \quad \text{Var}(X)=p(1-p)
$$

---

### Binomial Distribution
$$
P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}
$$

-$n$trials  
- Independent  
- Same probability$p$

---

##### Lecture 5 — Binomial (Applications)

### Conditions
- Fixed$n$
- Independent trials  
- Same$p$
- Two outcomes  

---

### Properties
$$
E(X)=np, \quad \text{Var}(X)=np(1-p)
$$

---

### Key Trick
Use complement for “at least”:
$$
P(X \ge k) = 1 - P(X < k)
$$

---

##### Lecture 6 — Poisson & Negative Binomial

### Poisson Distribution
$$
P(X=x) = \frac{e^{-\lambda}\lambda^x}{x!}
$$

- Counts events in interval  
- Models rare events  

---

### Properties
$$
E(X)=\lambda, \quad \text{Var}(X)=\lambda
$$

---

### Approximation
$$
\text{Bin}(n,p) \approx \text{Pois}(\lambda = np)
$$

---

### Negative Binomial
$$
P(X=n) = \binom{n-1}{r-1} p^r (1-p)^{n-r}
$$

- Number of trials until$r$successes  

---

##### Lecture 7 — Geometric & Hypergeometric

### Geometric Distribution
$$
P(X=x) = (1-p)^{x-1}p
$$

- Trials until first success  

---

### Properties
$$
E(X)=\frac{1}{p}, \quad \text{Var}(X)=\frac{1-p}{p^2}
$$

---

### Hypergeometric Distribution
$$
P(X=x) = \frac{\binom{m}{x}\binom{N-m}{n-x}}{\binom{N}{n}}
$$

- Sampling without replacement  

---

### Key Difference
- Binomial → independent trials  
- Hypergeometric → dependent (no replacement)  

---

##### Lecture 8 — Distribution Summary

### When to Use

- Bernoulli → one trial  
- Binomial → fixed number of trials  
- Poisson → count over time/space  
- Negative Binomial → until$r$successes  
- Geometric → until first success  
- Hypergeometric → sampling without replacement  

---

### Key Relationships
- Bernoulli = Binomial with$n=1$
- Geometric = Negative Binomial with$r=1$
- Binomial → Poisson (large$n$, small$p$)  

---

### Core Takeaways
- Random variables map outcomes to numbers  
- PMF describes probabilities  
- Expectation = average  
- Variance = spread  
- Choose distribution based on setup

# Module 4 — Continuous Random Variables

---

##### Lecture 1 — Continuous RV, PDF & CDF

### Continuous Random Variable
- Takes values over intervals  
- Examples: height, time, distance  

---

### CDF
$$
F_X(x) = P(X \le x)
$$

---

### PDF
$$
f(x) = \frac{d}{dx}F_X(x)
$$

---

### Probability via PDF
$$
P(a \le X \le b) = \int_a^b f(x)\,dx
$$

---

### Key Properties
-$f(x) \ge 0$
-$\int_{-\infty}^{\infty} f(x)\,dx = 1$
-$P(X = a) = 0$

---

##### Lecture 2 — Transformations & Expectation

### Transformation
If $Y = g(X)$(monotonic):

$$
f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|
$$

---

### Expectation (Continuous)
$$
E(X) = \int_{-\infty}^{\infty} x f(x)\,dx
$$

---

### Function Expectation
$$
E[g(X)] = \int g(x)f(x)\,dx
$$

---

### Key Idea
- Replace sums → integrals  

---

##### Lecture 3 — Variance (Continuous)

### Variance
$$
\text{Var}(X) = E[(X - E(X))^2]
$$

Alternative:
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Key Insight
- Same formulas as discrete, but integrals  

---

##### Lecture 4 — Uniform & Exponential

### Uniform Distribution
$$
f(x) = \frac{1}{b-a}, \quad a < x < b
$$

- All values equally likely  

---

### Properties
$$
E(X) = \frac{a+b}{2}, \quad \text{Var}(X) = \frac{(b-a)^2}{12}
$$

---

### Exponential Distribution
$$
f(x) = \lambda e^{-\lambda x}, \quad x > 0
$$

---

### Properties
$$
E(X) = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}
$$

---

### Memoryless Property
$$
P(X \ge s+t \mid X \ge s) = P(X \ge t)
$$

---

##### Lecture 5 — Normal Distribution

### PDF
$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

---

### Properties
- Mean:$\mu$
- Variance:$\sigma^2$
- Symmetric, bell-shaped  

---

### Standardization
$$
Z = \frac{X - \mu}{\sigma}
$$

---

##### Lecture 6 — Empirical Rule & Chi-Square

### Empirical Rule
-$P(|Z| < 1) \approx 0.68$
-$P(|Z| < 2) \approx 0.95$
-$P(|Z| < 3) \approx 0.997$

---

### Chi-Squared Distribution
$$
Q = Z_1^2 + \cdots + Z_k^2 \sim \chi^2_k
$$

---

### Key Idea
- Sum of squared standard normals  

---

##### Lecture 7 — Gamma & Beta

### Gamma Distribution
$$
f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}
$$

- Models waiting time  

---

### Key Relationship
$\text{Gamma}(1,\lambda) = \text{Exponential}$

---

### Beta Distribution
$$
f(x) = \frac{1}{B(\alpha,\beta)} x^{\alpha-1}(1-x)^{\beta-1}, \quad 0<x<1
$$

- Models proportions  

---

##### Lecture 8 — Weibull & Log-Normal

### Weibull Distribution
$$
f(x) = \gamma \lambda x^{\gamma-1} e^{-\lambda x^\gamma}
$$

- Flexible lifetime model  

---

### Log-Normal Distribution
$$
f(x) = \frac{1}{x\sigma \sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}
$$

---

### Key Idea
- If $\ln X \sim N(\mu,\sigma^2)$, then$X$is log-normal  

---

##### Lecture 9 — Summary & Relationships

### When to Use

- Uniform → equal likelihood  
- Normal → symmetric data  
- Exponential → waiting time  
- Gamma → sum of waiting times  
- Beta → proportions  
- Chi-square → sum of squares  
- Weibull → lifetime modeling  
- Log-normal → positive, skewed data  

---

### Key Relationships
- Exponential ↔ Poisson (waiting vs count)  
- Gamma → sum of exponentials  
- Beta from Gamma ratios  
- Normal → basis for many distributions  

---

### Core Takeaways
- Continuous → use integrals  
- PDF gives density, not point probability  
- CDF accumulates probability  
- Choose distribution based on context

# Module 5 — Moment Generating Functions

---

##### Lecture 1 — Moments & MGF

### Moments
- k-th moment:
$$
E(X^k)
$$

- k-th central moment:
$$
E[(X - \mu)^k]
$$

---

### Skewness
$$
\text{Skew}(X) = E\left[\left(\frac{X-\mu}{\sigma}\right)^3\right]
$$

---

### Kurtosis
$$
\text{Kurt}(X) = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] - 3
$$

---

### Moment Generating Function (MGF)
$$
M_X(t) = E(e^{tX})
$$

---

### Key Properties
-$M(0) = 1$
- Encodes all moments  
- Must be finite near$t = 0$

---

##### Lecture 2 — Using MGF

### Moments from MGF
- Take derivatives:
$$
E(X^k) = M_X^{(k)}(0)
$$

---

### First Two Moments
$$
E(X) = M'_X(0)
$$
$$
E(X^2) = M''_X(0)
$$

---

### Variance
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Transformation Property
If $Y = a + bX$:
$$
M_Y(t) = e^{at} M_X(bt)
$$

---

### Key Idea
- MGF turns calculus → moments  

---

##### Lecture 3 — Sums of Random Variables

### Sum of Independent RVs
If $U = X_1 + \cdots + X_n$:

$$
M_U(t) = M_{X_1}(t)\cdots M_{X_n}(t)
$$

---

### Key Insight
- MGFs multiply for independent sums  

---

### Important Results
- Sum of normals → normal  
- Sum of Poissons → Poisson  

---

### Example Pattern
If $X_i \sim \text{Bern}(p)$, then:
$$
\sum X_i \sim \text{Binomial}(n,p)
$$

---

### Core Takeaways
- MGF uniquely determines distribution  
- Derivatives give moments  
- Products handle sums  
- Useful for proving distribution results

# Module 5 — Moment Generating Functions

---

##### Lecture 1 — Moments & MGF

### Moments
- k-th moment:
$$
E(X^k)
$$

- k-th central moment:
$$
E[(X - \mu)^k]
$$

---

### Skewness
$$
\text{Skew}(X) = E\left[\left(\frac{X-\mu}{\sigma}\right)^3\right]
$$

---

### Kurtosis
$$
\text{Kurt}(X) = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] - 3
$$

---

### Moment Generating Function (MGF)
$$
M_X(t) = E(e^{tX})
$$

---

### Key Properties
- $M(0) = 1$  
- Encodes all moments  
- Must be finite near $t = 0$  

---

##### Lecture 2 — Using MGF

### Moments from MGF
Take derivatives:
$$
E(X^k) = M_X^{(k)}(0)
$$

---

### First Two Moments
$$
E(X) = M'_X(0)
$$

$$
E(X^2) = M''_X(0)
$$

---

### Variance
$$
\text{Var}(X) = E(X^2) - (E(X))^2
$$

---

### Transformation Property
If $Y = a + bX$:
$$
M_Y(t) = e^{at} M_X(bt)
$$

---

### Key Idea
- MGF turns calculus into moments  

---

##### Lecture 3 — Sums of Random Variables

### Sum of Independent RVs
If $U = X_1 + \cdots + X_n$:
$$
M_U(t) = M_{X_1}(t)\cdots M_{X_n}(t)
$$

---

### Key Insight
- MGFs multiply for independent sums  

---

### Important Results
- Sum of normals $\rightarrow$ normal  
- Sum of Poissons $\rightarrow$ Poisson  

---

### Example Pattern
If $X_i \sim \text{Bern}(p)$, then:
$$
\sum X_i \sim \text{Binomial}(n,p)
$$

---

### Core Takeaways
- MGF uniquely determines distribution  
- Derivatives give moments  
- Products handle sums  
- Useful for proving distribution results

# Module 7 — Limit Theorems

---

##### Lecture 1 — Inequalities & LLN

### Jensen’s Inequality
If $g$ is convex:
$$
E[g(X)] \geq g(E[X])
$$

If $g$ is concave:
$$
E[g(X)] \leq g(E[X])
$$

Examples:
- $E\left(\frac{1}{X}\right) \geq \frac{1}{E(X)}$ for $X > 0$  
- $E[\log X] \leq \log(E[X])$  

---

### Markov’s Inequality
For $X > 0$, $a > 0$:
$$
P(X \geq a) \leq \frac{E(X)}{a}
$$

---

### Chebyshev’s Inequality
If $E(X) = \mu$, $\text{Var}(X) = \sigma^2$:
$$
P(|X - \mu| \geq a) \leq \frac{\sigma^2}{a^2}
$$

---

### Chernoff Inequality
$$
P(X \geq a) \leq \frac{E(e^{tX})}{e^{ta}}, \quad t > 0
$$

---

### Law of Large Numbers (LLN)

Sample mean:
$$
\bar{X}_n = \frac{X_1 + \cdots + X_n}{n}
$$

---

#### Strong LLN
$$
P(\bar{X}_n \to \mu) = 1
$$

- Converges with probability 1  

---

#### Weak LLN
For all $\epsilon > 0$:
$$
P(|\bar{X}_n - \mu| > \epsilon) \to 0
$$

- Probability of large error $\to 0$  

---

### Key Idea
- More data $\rightarrow$ sample mean $\approx$ true mean  

---

##### Lecture 2 — CLT

### Standardization
$$
Z_n = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
$$

---

### Central Limit Theorem
If $X_i$ are iid with mean $\mu$, variance $\sigma^2$:
$$
Z_n \xrightarrow{d} N(0,1)
$$

---

### Key Insight
- Regardless of original distribution  
- Sample mean becomes approximately normal  

---

### Important Approximation
If $Y \sim \text{Bin}(n,p)$ and $n$ large:
$$
Y \approx N(np, np(1-p))
$$

---

### Takeaway
- CLT = why normal shows up everywhere  

---

##### Lecture 3 — Normal Approximation & t Distribution

### Normal Approximation
Use CLT for probabilities when exact is hard

---

### When CLT Works
- Large $n$  
- Finite mean and variance  

---

### Warning
- Does NOT work for distributions like Cauchy  
(no mean or variance)

---

### Sample Variance
$$
S_n^2 = \frac{1}{n-1} \sum (X_i - \bar{X}_n)^2
$$

---

### Chi-Squared Result
$$
\frac{(n-1)S_n^2}{\sigma^2} \sim \chi^2_{n-1}
$$

---

### t Distribution
If:
- $Z \sim N(0,1)$  
- $V \sim \chi^2_n$  
- independent  

Then:
$$
T = \frac{Z}{\sqrt{V/n}} \sim t_n
$$

---

### Key Properties
- Heavy tails  
- Used when $\sigma$ unknown  
- As $n \to \infty$, $t_n \to N(0,1)$  

---

### Big Picture
- LLN → convergence  
- CLT → shape becomes normal  
- t-dist → small sample inference  
