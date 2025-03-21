import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('fondo.jpg')
# Modificar dimensiones
img = cv2.resize(img, (600, 300))
cv2.imshow('Imagen original',img)

#Deteccion de bordes con Canny
bordes = cv2.Canny(img, 100, 200)
# Mostrar los bordes
cv2.imshow('Bordes', bordes)

img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, umbral = cv2.threshold(img_gris, 127, 255, cv2.THRESH_BINARY)    # Aplicar la umbralización
contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Encontrar los contornos
# Dibujar los contornos en la imagen original (convertida a color)
img_contorno = cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
# Mostrar la imagen con los contornos
cv2.imshow('Contornos detectados', img_contorno)





# Cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()