'''
import numpy as np
import pygame
import serial
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla (no necesaria para la entrada de usuario)
# screen = pygame.display.set_mode((640, 480))

try:
    # Abrir el puerto serie
    puerto = serial.Serial("COM3", 9600)
    time.sleep(2)  # Esperar un poco para que se establezca la conexión
    print("Puerto serial conectado")
except serial.SerialException as e:
    print("Error conectando al puerto serial")
    exit()



pygame.init()
# Bucle principal
running = True
img = np.zeros((100,100),dtype='uint8')

screen = pygame.display.set_mode((100,100))

while running:

    screen.fill((0, 0, 0))

    # Esperar eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Si se presiona la tecla 'a', salir del bucle
            if event.key == pygame.K_a:
                pygame.quit()
                running = False
            # Si se presiona la tecla 'q', enviar '1' al puerto serie
            elif event.key == pygame.K_q:
                try:
                    puerto.write(b'1')
                    print("Se envió '1' al puerto serial.")
                except serial.SerialException as e:
                    print("Error al escribir en el puerto serial:", e)

# Cerrar el puerto serie
puerto.close()
print("Puerto serial cerrado correctamente.")
'''

'''
import serial

arduino = serial.Serial("COM3", 9600)

while True:
    datos = arduino.readline().decode().strip()
    print("Arduino dice:", datos)
'''
import serial
import pygame
import numpy as np
import time
import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Control de LED con Pygame")

# Color negro
BLACK = (0, 0, 0)

# Abrir el puerto serie
arduino = serial.Serial("COM3", 9600)

# Bucle principal de Pygame
running = True
while running:
    # Mantener la pantalla en negro
    screen.fill(BLACK)

    # Manejar eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                arduino.write(b'a')  # Enviar 'a' para encender el LED
            elif event.key == pygame.K_w:
                arduino.write(b'w')  # Enviar 'd' para cerrar el programa
            elif event.key == pygame.K_s:
                arduino.write(b's')  # Enviar 'd' para cerrar el programa
            elif event.key == pygame.K_d:
                arduino.write(b'd')  # Enviar 'd' para cerrar el programa
            elif event.key == pygame.K_q:
                arduino.write(b'd')  # Enviar 'd' para cerrar el programa
                running = False

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar el puerto serie
arduino.close()

# Salir de Pygame
pygame.quit()




















