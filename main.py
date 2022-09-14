import pygame as pg
from game import Game
from camera import Camera
from random import randint
from settings import camera_bordas

def main():
    running = True
    playing = True
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()

    #inicia a camera    
    camera = Camera()

    #implementar menus

    #implementar jogo
    game = Game(screen, clock)

    while running == True:
        #menu inicial aqui
        while playing == True:
            #game loop aqui
            camera.controle_mouse()
            game.run()

if __name__ == "__main__":
    main()