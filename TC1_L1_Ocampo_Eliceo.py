import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('foto2.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (800, 400))
cv2.imshow('Imagen original',img)

# Hallo histograma
histograma = np.zeros(256, dtype=int)  #array para almacenar las frecuencias
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        intensidad = img[i, j]       # valor de intensidad del píxel
        histograma[intensidad] += 1  # aumenta frecuenciar

#Umbral
threshold = 100

# Se reconstruye la imagen 
img2 = np.zeros_like(img)
#Aplico transformada
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        intensidad = img[i, j]  
        if intensidad < threshold:
            intensidad2 = int( intensidad*255/threshold )
        if intensidad >= threshold:
            intensidad2 = intensidad
        img2[i, j] = int(intensidad2)

#Histograma reconstruido
histograma2 = np.zeros(256, dtype=int) #nuevas frecuencias
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        intensidad2 = img2[i, j]  # valor de intensidad del píxel
        histograma2[intensidad2] += 1  # Incrementar la cantidad de cada intensidad

cv2.imshow('Imagen Reconstruida', img2)

# Graficar el histograma
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(histograma)
plt.title('Histograma Original')
plt.subplot(1, 2, 2)
plt.plot(histograma2)
plt.title('Histograma Transformado')
plt.show()

# Cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()