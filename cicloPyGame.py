import pygame, sys #libreria del sistema

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((246, 147, 48)) #completa el fondo de la panalla de un color, en este caso naranja
pygame.display.set_caption("Ciclo básico de pygame")

pygame.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    pygame.display.flip()

pygame.quit()
sys.exit() #nos aseguramos que se cierra del todo, sin que se bloquee. 