import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

addition = A + B
print("=== Sum of two matrices is ===\n",addition)

print("\n")

subtraction = B - A
print("=== Subtraction of two matrices is ===\n",subtraction)

print("\n")

multiplication = A * B
print("=== Multiplication of two matrices is ===\n",multiplication)

print("\n")

dot_product = A @ B
print("=== Matrix Multiplication of two matrices is ===\n",dot_product)

print("\n")

transpose_A = A.T
print("=== Transpose of matrix A is ===\n",transpose_A)

print("\n")

transpose_B = B.T
print("=== Transpose of matrix B is ===\n",transpose_B)

print("\n")

determinant_A = np.round(np.linalg.det(A), 2)
print("=== Determinant of matrix A is ===\n",determinant_A)

print("\n")

determinant_B = np.round(np.linalg.det(B), 2)
print("=== Determinant of matrix B is ===\n",determinant_B)

print("\n")

inverse_A = np.linalg.inv(A)
print("=== Inverse of matrix A is ===\n",inverse_A)

print("\n")

inverse_B = np.linalg.inv(B)
print("=== Inverse of matrix B is ===\n",inverse_B)

print("\n")

eigenvalues , eigenvectors = np.linalg.eig(A)
print("=== Eigenvalues ===\n", eigenvalues)
print("=== Eigenvectors ===\n", eigenvectors)

print("\n")

eigenvalues , eigenvectors = np.linalg.eig(B)
print("=== Eigenvalues ===\n", eigenvalues)
print("=== Eigenvectors ===\n", eigenvectors)