import numpy as np

print("=" * 50)
print("         NUMPY SHOWCASE")
print("=" * 50)

# -----------------------------------------------
# 1. Array Basics
# -----------------------------------------------
print("\n--- 1. Array Basics ---")

a = np.array([1, 2, 3, 4, 5])
b = np.arange(0, 10, 2)
c = np.linspace(0, 1, 5)

print(f"Array:        {a}")
print(f"Arange:       {b}")
print(f"Linspace:     {c}")
print(f"a * 2:        {a * 2}")
print(f"a ** 2:       {a ** 2}")
print(f"sqrt(a):      {np.round(np.sqrt(a), 3)}")

# -----------------------------------------------
# 2. Matrix Operations
# -----------------------------------------------
print("\n--- 2. Matrix Operations ---")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"A @ B (matrix multiply):\n{A @ B}")
print(f"Transpose of A:\n{A.T}")
print(f"Determinant of A: {np.linalg.det(A):.2f}")
print(f"Inverse of A:\n{np.round(np.linalg.inv(A), 3)}")

# -----------------------------------------------
# 3. Eigenvalues and Eigenvectors
# -----------------------------------------------
print("\n--- 3. Eigenvalues & Eigenvectors ---")

values, vectors = np.linalg.eig(A)
print(f"Eigenvalues:  {np.round(values, 4)}")
print(f"Eigenvectors:\n{np.round(vectors, 4)}")

# -----------------------------------------------
# 4. Solving a Linear System
# -----------------------------------------------
print("\n--- 4. Solving Linear System Ax = b ---")

A_sys = np.array([[2,  1, -1],
                  [-3, -1,  2],
                  [-2,  1,  2]])

b_sys = np.array([8, -11, -3])

x = np.linalg.solve(A_sys, b_sys)
print(f"A:\n{A_sys}")
print(f"b: {b_sys}")
print(f"Solution x: {x}")
print(f"Verified (A @ x == b): {np.allclose(A_sys @ x, b_sys)}")

# -----------------------------------------------
# 5. Statistics
# -----------------------------------------------
print("\n--- 5. Statistics ---")

np.random.seed(42)
data = np.random.normal(loc=70, scale=10, size=1000)

print(f"Sample size:  {len(data)}")
print(f"Mean:         {np.mean(data):.4f}")
print(f"Std Dev:      {np.std(data):.4f}")
print(f"Median:       {np.median(data):.4f}")
print(f"Min:          {np.min(data):.4f}")
print(f"Max:          {np.max(data):.4f}")
print(f"Percentiles (25, 50, 75): {np.round(np.percentile(data, [25, 50, 75]), 3)}")

# -----------------------------------------------
# 6. Correlation
# -----------------------------------------------
print("\n--- 6. Correlation Matrix ---")

x = np.random.randn(100)
y = 2 * x + np.random.randn(100)
matrix = np.corrcoef(x, y)
print(f"Correlation matrix:\n{np.round(matrix, 4)}")

# -----------------------------------------------
# 7. Array Operations
# -----------------------------------------------
print("\n--- 7. Array Operations ---")

a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Original:     {a}")
print(f"Sorted:       {np.sort(a)}")
print(f"Unique:       {np.unique(a)}")
print(f"Where > 4:    {a[a > 4]}")
print(f"Cumsum:       {np.cumsum(a)}")
print(f"Argsort:      {np.argsort(a)}")

# -----------------------------------------------
# 8. Stacking and Reshaping
# -----------------------------------------------
print("\n--- 8. Reshaping & Stacking ---")

a = np.arange(12)
print(f"Original (1D): {a}")
print(f"Reshaped (3x4):\n{a.reshape(3, 4)}")
print(f"Reshaped (2x6):\n{a.reshape(2, 6)}")

r1 = np.array([1, 2, 3])
r2 = np.array([4, 5, 6])
print(f"Vertical stack:\n{np.vstack([r1, r2])}")
print(f"Horizontal stack: {np.hstack([r1, r2])}")

print("\n" + "=" * 50)
print("         END OF SHOWCASE")
print("=" * 50)
