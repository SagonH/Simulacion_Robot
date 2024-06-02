
# Importación de las librerías principales
import pygame
import pytmx
import sys
from robot import Robot
import csv
import os
import dividir_imagen  # Módulo no utilizado en este fragmento de código
from Automatizacion import automatizacion

# Importación de las librerías propias del código
import Constantes
from mundo import Mundo

# Inicialización de Pygame
pygame.init()

# Abrir ventana
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
# Nombre de la ventana
pygame.display.set_caption("Simulación del robot")

# Variable global para el ángulo en el que se encuentra el robot
angulo_robot = 0

# Definir las variables de movimiento del robot
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# Cargar las imágenes del mundo
tile_list = []

for x in range(Constantes.TILE_TYPES):
    tile_image = pygame.image.load(f"tiles//tile ({x+1}).png")
    tile_image = pygame.transform.scale(tile_image, (Constantes.TILE_SIZE, Constantes.TILE_SIZE))
    tile_list.append(tile_image)

# Crear una matriz de datos del mundo
world_data = []

for fila in range(Constantes.FILAS):
    filas = [47] * Constantes.COLUMNAS
    world_data.append(filas)

# Cargar el archivo con el laberinto desde un archivo CSV
with open("lab.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y] = int(columna)

# Crear un objeto de la clase Mundo
world = Mundo()
world.process_data(world_data, tile_list)

# Configurar el reloj para controlar la velocidad de fotogramas por segundo (FPS)
reloj = pygame.time.Clock()

# Definir imagen del robot y escalarla
# aquí se define robotsito de tipo Robot
robot_image = pygame.image.load("assets//images//robot//imgrobot.png")
robot_image = pygame.transform.scale(robot_image,
                                     (robot_image.get_width()*Constantes.ESCALA_ROBOT,
                                     robot_image.get_height()*Constantes.ESCALA_ROBOT))
robotsito = Robot(487, 624, robot_image)

# Bucle principal del juego
run_automatico = False
run_manual = False

"""while run:
    # Correr a 60 FPS
    reloj.tick(Constantes.FPS)

    # Llenar la ventana con el color de fondo
    ventana.fill(Constantes.COLOR_FONDO)

    # Dibujar el mundo en la ventana
    world.draw(ventana)


    # Calcular el movimiento del robot
    numpix_x = 0
    numpix_y = 0

    if mover_arriba:
        numpix_y = -Constantes.VEL_ROBOT
    if mover_abajo:
        numpix_y = Constantes.VEL_ROBOT
    if mover_izquierda:
        numpix_x = -Constantes.VEL_ROBOT
    if mover_derecha:
        numpix_x = Constantes.VEL_ROBOT  

    # Mover al robot
    robotsito.movimiento(numpix_x, numpix_y, world.obstaculos_tiles)

    # Actualizar la rotación del robot
    robotsito.actualizar_rotacion()
    
    # Actualizar la variable global angulo_robot
    angulo_robot = robotsito.angle
    # print(angulo_robot)

    # Dibujar al robot en la ventana
    robotsito.dibujar(ventana)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_RIGHT:
                robotsito.rotar('derecha')
            if event.key == pygame.K_LEFT:
                robotsito.rotar('izquierda')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False

    # Actualizar la ventana de Pygame
    pygame.display.update()"""


    