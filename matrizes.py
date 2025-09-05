import numpy as np

# Definir as matrizes
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

resultado = np.dot(A, B)

print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)
print("\nResultado da multiplicação (A . B):")
print(resultado)
