import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('fondo.jpg')
# Modificar dimensiones
img_resized = cv2.resize(img, (600, 300))


# Conversion a escala de grises
img_gris = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

# Mostrar imagen
cv2.imshow('Imagen original',img_resized)
cv2.imshow('Imagen en blanco y negro', img_gris)


# Dibujar formas basicas
img_rect = cv2.rectangle(img_resized.copy(), (50, 50), (250, 250), (0, 255, 0), 4)
img_circle = cv2.circle(img_resized.copy(), (150, 150), 50, (0, 0, 255), 3)
cv2.imshow('Círculo', img_circle)

#Traslacion
M = np.float32([[1, 0, 100], [0, 1, 50]]) # Matriz de traslación
img_trasladada = cv2.warpAffine(img_resized, M, (img_resized.shape[1], img_resized.shape[0]))  # imagen trasladada
cv2.imshow('Imagen Trasladada', img_trasladada)

#Rotacion
(h, w) = img_resized.shape[:2]
centro = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(centro, 45, 1.0)  #Matriz de rotación
img_rotada = cv2.warpAffine(img_resized, M, (w, h)) # Aplicar la rotación
cv2.imshow('Imagen Rotada', img_rotada)

# Escalamiento
img_escalada = cv2.resize(img_resized, (0, 0), fx=0.75, fy=0.75)
cv2.imshow('Imagen Escalada', img_escalada) # Mostrar la imagen escalada

# Matriz de transformación de perspectiva
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [280, 220]])
M = cv2.getPerspectiveTransform(pts1, pts2)
# Aplicar la transformación de perspectiva
img_perspectiva = cv2.warpPerspective(img_resized, M, (img_resized.shape[1], img_resized.shape[0]))
# Mostrar la imagen transformada
cv2.imshow('Imagen de Perspectiva', img_perspectiva)

# Cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()