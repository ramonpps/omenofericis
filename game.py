import pygame as pg
import sys
from world import World
from settings import TILE_SIZE

class Game:
    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(24, 12, self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                sq = self.world.world[x][y]["cart_rect"]
                rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                pg.draw.rect(self.screen, (0, 0, 255), rect, 1)
        pg.display.flip()

    def controle_mouse(self):
        mouse = pg.math.vetor(pg.math.get_pos())
        mouse_deslocamento_vetor = pg.math.vetor()
        
        