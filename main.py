import pygame, sys
import random

class Runner():
    __custome = ('turtle', 'fish', 'prawn', 'moray', 'octopus') 
    
    def __init__(self, x=0, y=0):
        ixCustome =random.randint(0,4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__custome[ixCustome]))
        self.position = [x, y]
        self.name = "" 
        
    def avance(self):
        self.position[0] += random.randint(1, 2)
        

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __name = ("Speedy", "Lucera", "Tomasa", "Rabbit")
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) #la pantalla viene definida y no se deberia poder modificar, es "privado"
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__name[i]
            self.runners.append(theRunner)
        
    def close(self):
        pygame.quit()
        sys.exit()

        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
    
            for activeRunner in self.runners:
                activeRunner.avance()
                if activeRunner.position[0] >= self.__finishLine:
                #se pone 0 en position, poque queremos la coordenada X que en la lista es la "0" y la Y es la 1
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True               
           
            self.__screen.blit(self.__background, (0, 0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
    
            pygame.display.flip()
        
        while True:
    #esto es para que no se cirre la pantalla solo, si apretar el boton de cierre. Se queda comrpobando los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.close()
                    
      
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()