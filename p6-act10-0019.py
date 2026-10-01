import numpy as np
import cv2
# Vision artificial Act10 NC = 0019
# Lee la imagen en escala de grises
img = cv2.imread("Drift.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("Drift 0019", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea 
print("La linea 0019")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("Line 0019", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crea una imagen negra
img = np.zeros((512, 512, 3), np.uint8)

# Parámetros del círculo:
centro = (256, 256)      # Centro de la imagen (x, y)
radio = 100              # Radio del círculo en píxeles
color = (255, 255, 255)  # Color blanco en formato BGR
grosor = 3               # Grosor de la línea (usa -1 si quieres el círculo relleno)

# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "vision artificial", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
# Abre la ventana con la imagen
cv2.imshow("Line 0019", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def on_trackbar(val):
  print(val)

import cv2
import numpy as np

def on_trackbar(val):
    pass  # No es necesario imprimir el valor si solo quieres actualizar la imagen

# Crea una imagen negra y la ventana
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('frame')

# Crea los trackbars
cv2.createTrackbar('R', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'frame', 0, 255, on_trackbar)

while True:
    cv2.imshow('frame', img)
    
    # Presiona 'ESC' para salir
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Si el usuario cierra la ventana con la "X", sale limpiamente del bucle
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    b = cv2.getTrackbarPos('B', 'frame')

    # Actualiza el color (OpenCV usa BGR)
    img[:] = [b, g, r]

cv2.destroyAllWindows()
# Abre la ventana con la imagen
cv2.imshow("Drift.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img = cv2.imread('Drift.jpg', 0)

if img is None:
    print("Error: No se encontró la imagen 'image1.png'")
else:
    # Genera las imágenes umbralizadas
    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    # Lista de imágenes y títulos para mostrarlas una por una
    imagenes = [
        ('BINARY', thr1),
        ('BINARY_INV', thr2),
        ('TRUNC', thr3),
        ('TOZERO', thr4),
        ('TOZERO_INV', thr5)
    ]

    for titulo, imagen in imagenes:
        cv2.imshow(titulo, imagen)
        cv2.waitKey(0)  # Presiona cualquier tecla para pasar a la siguiente
        cv2.destroyAllWindows()

print("Programa realizado por jesus arriaga 0019")
