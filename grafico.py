# arrays-numpy
codigo sobre aula e trabalho de numpy
#código da aula:

import numpy as np
from scipy import linalg, optimize
import matplotlib.pyplot as plt

print("=== Demonstração da Biblioteca SciPy ===\n")

# 1. RESOLVENDO UM SISTEMA DE EQUAÇÕES LINEARES
print("1. Resolvendo sistema de equações lineares:")
print("   Sistema: 3x + 2y = 12")
print("            x - y = 1")

# Matriz dos coeficientes
A = np.array([[3, 2], [1, -1]])
# Vetor dos termos independentes
b = np.array([12, 1])

# Resolvendo o sistema
solucao = linalg.solve(A, b)
print(f"   Solução: x = {solucao[0]:.2f}, y = {solucao[1]:.2f}")

# 2. ENCONTRANDO O MÍNIMO DE UMA FUNÇÃO
print("\n2. Encontrando mínimo da função f(x) = x² + 10*sin(x)")

def funcao(x):
    return x**2 + 10*np.sin(x)

# Encontrando o mínimo
resultado = optimize.minimize(funcao, x0=0)
minimo_x = resultado.x[0]
minimo_y = resultado.fun

print(f"   Mínimo encontrado em x = {minimo_x:.2f}")
print(f"   Valor da função no mínimo: f(x) = {minimo_y:.2f}")

# 3. VISUALIZAÇÃO (opcional - se quiser mostrar gráfico)
print("\n3. Visualização da função e do mínimo encontrado")

# Criando pontos para o gráfico
x = np.linspace(-5, 5, 400)
y = funcao(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='f(x) = x² + 10*sin(x)')
plt.plot(minimo_x, minimo_y, 'ro', markersize=8, label=f'Mínimo ({minimo_x:.2f}, {minimo_y:.2f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Otimização com SciPy')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

print("\n=== Fim da demonstração ===")
