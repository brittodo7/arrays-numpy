import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Criando um array com coordenadas 3D (x, y, z)
dados = np.array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
])
# Separando os eixos
x = dados[:, 0]
y = dados[:, 1]
z = dados[:, 2]
# Criando o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='black', marker='x')
# Rótulos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
plt.title("Visualização de pontos 3D com NumPy")
plt.show()
