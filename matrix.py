import numpy as np

# Create two random 3x3 matrices
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
print("\nA + B:\n", A + B)

# Matrix subtraction
print("\nA - B:\n", A - B)

# Matrix multiplication
print("\nA * B:\n", np.dot(A, B))

# Matrix transpose
print("\nTranspose of A:\n", A.T)
