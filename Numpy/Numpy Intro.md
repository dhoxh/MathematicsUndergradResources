
## What Is NumPy?

NumPy is a Python library for numerical computation. It gives you a fast, efficient array type and a large collection of mathematical functions that operate on those arrays. It is the foundation that almost every other scientific Python library sits on top of, including Matplotlib, SciPy, and pandas.

For math majors, NumPy fills the role of a programmable calculator that actually handles the scale of problems you will encounter. NumPy handles all of that without the friction you would run into trying to do it by hand or even with basic Python lists.

This guide covers arrays, indexing, arithmetic, broadcasting, linear algebra, and random number generation. By the end you will have enough to use NumPy practically for coursework in linear algebra, analysis, and applied math.

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Creating Arrays](#2-creating-arrays)
3. [Array Attributes](#3-array-attributes)
4. [Indexing and Slicing](#4-indexing-and-slicing)
5. [Array Arithmetic](#5-array-arithmetic)
6. [Broadcasting](#6-broadcasting)
7. [Math Functions](#7-math-functions)
8. [Linear Algebra](#8-linear-algebra)
9. [Random Numbers](#9-random-numbers)
10. [Reshaping and Stacking](#10-reshaping-and-stacking)
11. [Useful Workflows for Math Majors](#11-useful-workflows-for-math-majors)
12. [Quick Reference](#12-quick-reference)

---

## 1. Getting Started

If you installed Python through Anaconda, NumPy is already there. Confirm it:

```bash
python -c "import numpy; print(numpy.__version__)"
```

A version number should print. If it does not, install NumPy with:

```bash
pip install numpy
```

Or with conda:

```bash
conda install numpy
```

In every script and notebook you will import NumPy at the top. The convention is to alias it as `np`:

```python
import numpy as np
```

Everything in this guide assumes that import is at the top of your file.

---

## 2. Creating Arrays

The core data structure in NumPy is the `ndarray`, short for n-dimensional array. You will create arrays in a few different ways depending on what you need.

**From a Python list:**

```python
v = np.array([1, 2, 3, 4, 5])
A = np.array([[1, 2, 3], [4, 5, 6]])   # 2D array (matrix)
```

**Sequences:**

```python
np.arange(10)              # [0 1 2 3 4 5 6 7 8 9]
np.arange(0, 1, 0.25)     # [0.   0.25 0.5  0.75]
np.linspace(0, 1, 5)      # [0.   0.25 0.5  0.75 1. ] -- includes endpoint
```

`linspace` is the one you will reach for constantly. It gives you `n` evenly spaced points between two values, endpoints included. Perfect for plotting and numerical integration.

**Arrays filled with constants:**

```python
np.zeros(5)               # [0. 0. 0. 0. 0.]
np.ones((3, 3))           # 3x3 matrix of ones
np.zeros((2, 4))          # 2x4 matrix of zeros
np.full((3, 3), 7)        # 3x3 matrix filled with 7
```

**Identity matrix:**

```python
np.eye(4)                 # 4x4 identity matrix
```

**Diagonal matrix:**

```python
np.diag([1, 2, 3])        # 3x3 diagonal matrix with 1, 2, 3 on the diagonal
```

---

## 3. Array Attributes

Once you have an array, these are the properties you check most often:

```python
A = np.array([[1, 2, 3], [4, 5, 6]])

A.shape       # (2, 3) -- 2 rows, 3 columns
A.ndim        # 2 -- number of dimensions
A.size        # 6 -- total number of elements
A.dtype       # dtype('int64') -- data type of elements
```

**Data types matter.** By default, arrays of integers get `int64` and arrays with any decimal get `float64`. You can specify a type explicitly:

```python
np.array([1, 2, 3], dtype=float)      # forces float: [1. 2. 3.]
np.zeros(5, dtype=int)                 # integer zeros: [0 0 0 0 0]
```

For most math work, `float64` is what you want. If you are ever getting unexpected integer division behavior, check the dtype.

---

## 4. Indexing and Slicing

**1D arrays:**

NumPy uses zero-based indexing. The first element is at index 0.

```python
v = np.array([10, 20, 30, 40, 50])

v[0]          # 10
v[-1]         # 50  (last element)
v[1:4]        # [20 30 40]  (slice: index 1 up to but not including 4)
v[::2]        # [10 30 50]  (every other element)
v[::-1]       # [50 40 30 20 10]  (reversed)
```

**2D arrays:**

```python
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

A[0, 0]       # 1  (row 0, column 0)
A[1, 2]       # 6  (row 1, column 2)
A[0, :]       # [1 2 3]  (entire first row)
A[:, 1]       # [2 5 8]  (entire second column)
A[0:2, 0:2]   # top-left 2x2 submatrix
```

**Boolean indexing:**

```python
v = np.array([3, 7, 1, 9, 4])

v[v > 4]                  # [7 9]  -- elements greater than 4
v[v % 2 == 0]             # [4]    -- even elements
```

This is useful for filtering values in a dataset or applying a condition across a vector without writing a loop.

---

## 5. Array Arithmetic

All standard arithmetic operations on NumPy arrays happen element-wise:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b         # [5 7 9]
a - b         # [-3 -3 -3]
a * b         # [4 10 18]
a / b         # [0.25 0.4  0.5]
a ** 2        # [1 4 9]
```

Operations between an array and a scalar apply the scalar to every element:

```python
a + 10        # [11 12 13]
a * 3         # [3 6 9]
2 ** a        # [2 4 8]
```

**Matrix multiplication:**

Element-wise multiplication and matrix multiplication are different things. Use `@` for matrix multiplication:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A * B         # element-wise: [[5 12] [21 32]]
A @ B         # matrix multiply: [[19 22] [43 50]]
```

You can also use `np.dot(A, B)` for matrix multiplication, but `@` is cleaner and easier to read.

---

## 6. Broadcasting

Broadcasting is how NumPy handles arithmetic between arrays of different shapes without making you manually resize anything.

The clearest example: adding a row vector to every row of a matrix.

```python
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

v = np.array([10, 20, 30])

A + v
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]
```

NumPy stretched `v` across all three rows automatically. No loop needed.

The rule is: dimensions are compared from the right. Two dimensions are compatible if they are equal or one of them is 1. If the dimensions do not align at all, NumPy raises an error.

Broadcasting comes up constantly in practice. Once you get used to it, you will stop writing a lot of loops.

---

## 7. Math Functions

NumPy includes a full set of mathematical functions that operate on arrays element-wise. These are called universal functions (ufuncs).

**Basic math:**

```python
x = np.array([1.0, 4.0, 9.0, 16.0])

np.sqrt(x)          # [1. 2. 3. 4.]
np.abs(x)           # absolute value
np.log(x)           # natural log
np.log10(x)         # log base 10
np.log2(x)          # log base 2
np.exp(x)           # e^x
```

**Trigonometry (arguments in radians):**

```python
x = np.linspace(0, 2 * np.pi, 5)

np.sin(x)
np.cos(x)
np.tan(x)
np.arcsin(x)
np.arccos(x)
np.arctan(x)
np.arctan2(y, x)    # angle for point (x, y), handles quadrants correctly
```

**Constants:**

```python
np.pi       # 3.141592653589793
np.e        # 2.718281828459045
np.inf      # infinity
np.nan      # not a number
```

**Rounding:**

```python
np.round(3.14159, 2)    # 3.14
np.floor(3.9)           # 3.0
np.ceil(3.1)            # 4.0
```

**Aggregations:**

```python
x = np.array([3, 1, 4, 1, 5, 9, 2, 6])

np.sum(x)           # 31
np.prod(x)          # product of all elements
np.min(x)           # 1
np.max(x)           # 9
np.mean(x)          # 3.875
np.median(x)        # 3.5
np.std(x)           # standard deviation
np.var(x)           # variance
np.cumsum(x)        # running sum
np.cumprod(x)       # running product
```

For 2D arrays, you can aggregate along an axis:

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(A, axis=0)   # [5 7 9]  -- sum down each column
np.sum(A, axis=1)   # [6 15]   -- sum across each row
```

---

## 8. Linear Algebra

NumPy's linear algebra tools live in `np.linalg`. This is where NumPy really earns its place for math majors.

**Matrix operations:**

```python
A = np.array([[1, 2], [3, 4]], dtype=float)

np.linalg.det(A)         # determinant: -2.0
np.linalg.inv(A)         # inverse
A.T                      # transpose
np.trace(A)              # trace (sum of diagonal)
np.linalg.matrix_rank(A) # rank
```

**Solving a linear system:**

To solve Ax = b:

```python
A = np.array([[2, 1], [5, 7]], dtype=float)
b = np.array([11, 13], dtype=float)

x = np.linalg.solve(A, b)
# x = [7.11... -3.22...]

# Verify:
A @ x    # should equal b
```

`np.linalg.solve` is more numerically stable than computing `inv(A) @ b`, so always prefer it when solving systems.

**Eigenvalues and eigenvectors:**

```python
A = np.array([[4, -2], [1, 1]], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)

eigenvalues            # array of eigenvalues
eigenvectors           # columns are the corresponding eigenvectors
```

Note that the eigenvectors are in the columns, not the rows. `eigenvectors[:, 0]` is the eigenvector for `eigenvalues[0]`.

**Norms:**

```python
v = np.array([3.0, 4.0])

np.linalg.norm(v)          # Euclidean norm: 5.0
np.linalg.norm(v, ord=1)   # 1-norm (sum of abs values): 7.0
np.linalg.norm(v, ord=np.inf)  # infinity norm (max abs value): 4.0
```

**Singular Value Decomposition:**

```python
A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)

U, S, Vt = np.linalg.svd(A)
# A = U @ np.diag(S) @ Vt
```

**QR decomposition:**

```python
Q, R = np.linalg.qr(A)
```

**Least squares:**

For overdetermined systems where no exact solution exists, use the least squares solver:

```python
A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
b = np.array([1.0, 2.0, 2.0])

coeffs, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=None)
```

---

## 9. Random Numbers

Random number generation lives in `np.random`. You will use this a lot for simulations, Monte Carlo methods, and testing code.

**Set a seed for reproducibility:**

```python
rng = np.random.default_rng(seed=42)
```

Using `default_rng` is the current recommended approach. It gives you a random number generator object that you call methods on, which is cleaner than the older `np.random.seed()` style.

**Generating random values:**

```python
rng = np.random.default_rng(42)

rng.random(5)                   # 5 uniform random floats in [0, 1)
rng.integers(0, 10, size=5)     # 5 random integers in [0, 10)
rng.normal(0, 1, size=100)      # 100 samples from N(0, 1)
rng.normal(mu, sigma, size=n)   # samples from N(mu, sigma^2)
rng.uniform(a, b, size=n)       # uniform on [a, b]
rng.choice([1, 2, 3, 4], size=10, replace=True)  # sampling with replacement
```

**Shuffling:**

```python
arr = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr)                # shuffles in place
shuffled = rng.permutation(arr) # returns a shuffled copy, original unchanged
```

**Common distributions:**

```python
rng.binomial(n=10, p=0.5, size=1000)
rng.poisson(lam=3, size=1000)
rng.exponential(scale=2, size=1000)
rng.chisquare(df=5, size=1000)
```

---

## 10. Reshaping and Stacking

**Reshape:**

```python
a = np.arange(12)         # [0 1 2 3 4 5 6 7 8 9 10 11]

a.reshape(3, 4)           # 3x4 matrix
a.reshape(2, 6)           # 2x6 matrix
a.reshape(2, 2, 3)        # 3D: 2 blocks of 2x3

a.reshape(3, -1)          # -1 means "figure out this dimension automatically"
```

Reshape does not copy data. It just gives you a different view of the same underlying array.

**Flatten:**

```python
A = np.array([[1, 2, 3], [4, 5, 6]])

A.flatten()               # [1 2 3 4 5 6] -- returns a copy
A.ravel()                 # same thing but returns a view if possible
```

**Stacking arrays:**

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.hstack([a, b])         # [1 2 3 4 5 6]  -- horizontal stack (side by side)
np.vstack([a, b])         # [[1 2 3]        -- vertical stack (row on row)
                          #  [4 5 6]]

np.concatenate([a, b])    # [1 2 3 4 5 6]  -- general version, specify axis
```

---

## 11. Useful Workflows for Math Majors

**Numerically integrating a function:**

NumPy does not have a built-in integrator (that is in SciPy), but you can approximate integrals with the trapezoidal rule:

```python
import numpy as np

a, b, n = 0, np.pi, 1000
x = np.linspace(a, b, n)
y = np.sin(x)

integral = np.trapz(y, x)
# 2.0 -- exact answer for integral of sin from 0 to pi
```

`np.trapz` uses the trapezoidal rule across however many points you give it. More points means a better approximation.

**Computing a Riemann sum manually:**

```python
n = 10000
x = np.linspace(0, 1, n, endpoint=False)
dx = 1 / n
y = x ** 2

riemann_sum = np.sum(y * dx)
# about 0.3333 -- exact answer is 1/3
```

**Applying a function to a grid of points:**

```python
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)     # creates 2D grids

Z = np.sin(X) * np.cos(Y)    # evaluate f(x, y) = sin(x)cos(y) at every point
```

`meshgrid` paired with a function gives you the z-values for a surface plot. You will use this pattern every time you plot in 2D or 3D with Matplotlib.

**Checking numerical linear algebra results:**

```python
A = np.array([[2.0, 1.0], [5.0, 7.0]])
b = np.array([11.0, 13.0])

x = np.linalg.solve(A, b)

residual = np.linalg.norm(A @ x - b)
print(f"Residual: {residual:.2e}")   # should be very close to 0
```

Always verify your linear system solutions. `np.linalg.norm(A @ x - b)` should be on the order of machine epsilon (around 1e-14 or smaller for well-conditioned systems).

**Monte Carlo estimation of pi:**

```python
rng = np.random.default_rng(0)
n = 1_000_000

x = rng.uniform(-1, 1, n)
y = rng.uniform(-1, 1, n)

inside = (x**2 + y**2) <= 1
pi_estimate = 4 * np.sum(inside) / n

print(f"pi estimate: {pi_estimate:.4f}")   # about 3.1416
```

This is a clean example of vectorized Monte Carlo. No explicit loop, no conditional inside a loop. The whole simulation runs in a few lines.

---

## 12. Quick Reference

**Creating arrays:**

|Task|Command|
|---|---|
|From list|`np.array([1, 2, 3])`|
|Integer range|`np.arange(n)`|
|Evenly spaced|`np.linspace(a, b, n)`|
|Zeros|`np.zeros((m, n))`|
|Ones|`np.ones((m, n))`|
|Identity|`np.eye(n)`|
|Diagonal|`np.diag([a, b, c])`|
|Constant fill|`np.full((m, n), val)`|

**Array info:**

|Task|Command|
|---|---|
|Shape|`A.shape`|
|Dimensions|`A.ndim`|
|Total elements|`A.size`|
|Data type|`A.dtype`|

**Math functions:**

|Task|Command|
|---|---|
|Square root|`np.sqrt(x)`|
|Absolute value|`np.abs(x)`|
|Natural log|`np.log(x)`|
|Log base 10|`np.log10(x)`|
|Exponential|`np.exp(x)`|
|Sine / Cosine|`np.sin(x)` / `np.cos(x)`|
|Sum|`np.sum(x)`|
|Mean|`np.mean(x)`|
|Std deviation|`np.std(x)`|
|Cumulative sum|`np.cumsum(x)`|
|Minimum / Maximum|`np.min(x)` / `np.max(x)`|

**Linear algebra:**

|Task|Command|
|---|---|
|Matrix multiply|`A @ B`|
|Transpose|`A.T`|
|Determinant|`np.linalg.det(A)`|
|Inverse|`np.linalg.inv(A)`|
|Solve Ax = b|`np.linalg.solve(A, b)`|
|Eigenvalues|`np.linalg.eig(A)`|
|Norm|`np.linalg.norm(v)`|
|Rank|`np.linalg.matrix_rank(A)`|
|SVD|`np.linalg.svd(A)`|
|QR|`np.linalg.qr(A)`|
|Least squares|`np.linalg.lstsq(A, b, rcond=None)`|

**Reshaping:**

|Task|Command|
|---|---|
|Reshape|`A.reshape(m, n)`|
|Flatten|`A.flatten()`|
|Horizontal stack|`np.hstack([a, b])`|
|Vertical stack|`np.vstack([a, b])`|
|Meshgrid|`np.meshgrid(x, y)`|
|Concatenate|`np.concatenate([a, b], axis=0)`|

**Random (with `rng = np.random.default_rng(seed)`):**

|Task|Command|
|---|---|
|Uniform [0, 1)|`rng.random(n)`|
|Random integers|`rng.integers(low, high, size=n)`|
|Normal|`rng.normal(mu, sigma, size=n)`|
|Shuffle (in place)|`rng.shuffle(arr)`|
|Permutation (copy)|`rng.permutation(arr)`|
