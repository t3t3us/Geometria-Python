import numpy as np
import matplotlib.pyplot as plt

triangulo = np.array([[2, 2], [4, 2], [3, 4], [2, 2]])

def transladar(figura, tx, ty):
    return figura + np.array([tx, ty])

def escalar(figura, sx, sy):
    matriz = np.array([[sx, 0], [0, sy]])
    return figura.dot(matriz)

def rotacionar(figura, angulo):
    rad = np.deg2rad(angulo)
    matriz = np.array([[np.cos(rad), -np.sin(rad)],
                       [np.sin(rad), np.cos(rad)]])
    return figura.dot(matriz)

triangulo_transladado = transladar(triangulo, -7, -5)
triangulo_escalado = escalar(triangulo, 2.0, 0.5)
triangulo_rotacionado = rotacionar(triangulo, 60)

triangulo_temp = rotacionar(triangulo, -45)
triangulo_combinado = transladar(triangulo_temp, 5, -5)

plt.figure(figsize=(10, 10))

plt.plot(triangulo[:,0], triangulo[:,1], 'b-', label="Original (Triângulo)")
plt.plot(triangulo_transladado[:,0], triangulo_transladado[:,1], 'g-', label="Transladado (-7, -5)")
plt.plot(triangulo_escalado[:,0], triangulo_escalado[:,1], 'r-', label="Escalado (2x, 0.5y)")
plt.plot(triangulo_rotacionado[:,0], triangulo_rotacionado[:,1], 'm-', label="Rotacionado (60°)")
plt.plot(triangulo_combinado[:,0], triangulo_combinado[:,1], 'c-', label="Combinado (Rotacionado -45° -> Transladado)")

plt.legend()
plt.grid(True)
plt.title("Transformações Geométricas em Computação Gráfica")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.axis('equal')
plt.show()
