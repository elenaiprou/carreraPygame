import pygame, sys
from pygame.locals import *
import random

class Runner():
    __custome = ('turtle', 'fish', 'prawn', 'moray', 'octopus') 
    
    def __init__(self, x=0, y=0):
        ixCustome =random.randint(0,4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__custome[ixCustome]))
        self.position = [x, y]
        self.name = "" 
        
    def avance(self):
        self.position[0] += random.randint(1, 3)

class Game():

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) #la pantalla viene definida y no se deberia poder modificar, es "privado"
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Mover el bichito")
        
        self.runner = Runner(320, 240)
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        runnerY = self.runner.position[1]
                        runnerY -= 5
                        self.runner.position[1] = runnerY    
                    elif event.key == K_DOWN:
                        self.runner.position[1] += 5                        
                    elif event.key == K_LEFT:
                        self.runner.position[0] = self.runner.position[0] - 5                        
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5                    
                    else:           
                        pass
            
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()