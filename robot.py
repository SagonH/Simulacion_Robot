import pygame
from mundo import Mundo

class Robot():
    def __init__(self,x,y,image):
        self.image=image
        self.original_image = image # guardamos la imagen original
        self.forma = pygame.Rect(0,0,image.get_width(),image.get_height())
        self.forma.center = (x,y)
        self.angle = 0
        self.target_angle = 0
        self.rotating = False # Bandera que nos indica si estamos rotando o no

    def dibujar(self,interfaz):
        # Rotar la imagen antes de dibujarla
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        new_rect = rotated_image.get_rect (center=self.forma.center)
        interfaz.blit(rotated_image, new_rect.topleft)
        #pygame.draw.rect(interfaz,(250,230,0),self.forma,1) 

    def movimiento(self, numpix_x, numpix_y, obstaculo_tiles): 
        posicion_pantalla = [480,624]
        self.forma.x=self.forma.x + numpix_x
        for obstacle in obstaculo_tiles:
            if obstacle[1].colliderect(self.forma):
                print(" Colision detectada")
                if numpix_x > 0:
                    self.forma.right = obstacle[1].left
                if numpix_x < 0:
                    self.forma.left = obstacle[1].right

         
        self.forma.y=self.forma.y + numpix_y
        for obstacle in obstaculo_tiles:
            if obstacle[1].colliderect(self.forma):
                print(" Colision detectada")
                if numpix_y > 0:
                    self.forma.bottom = obstacle[1].top
                if numpix_y < 0:
                    self.forma.top = obstacle[1].bottom


    def rotar(self, direccion):
        if direccion == 'derecha':
            self.target_angle = (self.angle - 90) % 360  # Establecer el ángulo objetivo
        elif direccion == 'izquierda':
            self.target_angle = (self.angle + 90) % 360  # Establecer el ángulo objetivo
        self.rotating = True  # Iniciar rotación

    def actualizar_rotacion(self):
        if self.rotating:
            # Calcular la diferencia entre el ángulo actual y el ángulo objetivo
            difference = (self.target_angle - self.angle) % 360
            if difference > 180:
                difference -= 360  # Esto elige la dirección más corta

            # Incrementar o decrementar el ángulo actual hacia el ángulo objetivo
            if difference > 0:
                self.angle = (self.angle + 2) % 360
                if (self.target_angle - self.angle) % 360 > difference:
                    self.angle = self.target_angle
                    self.rotating = False
            elif difference < 0:
                self.angle = (self.angle - 2) % 360
                if (self.angle - self.target_angle) % 360 > -difference:
                    self.angle = self.target_angle
                    self.rotating = False
                    
            # actualizar la variable global angulo_robot        
            global angulo_robot
            angulo_robot = self.angle
           