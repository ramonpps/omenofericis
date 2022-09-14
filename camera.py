import pygame as pg
grupo_camera = pg.sprite.Group()
class Camera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        #deslocamento da camera
        self.deslocamento = pg.math.Vector2()
        self.metade_largura = self.display_surface.get_size()[0]//2
        self.metade_altura = self.display_surface.get_size()[1]//2

        #caixa de visao
        self.camera_bordas = {'esquerda': 1500,'direita': 1500,'cima': 750,'baixo': 750}
        esquerda = self.camera_bordas['esquerda']
        cima = self.camera_bordas['cima']
        largura = self.display_surface.get_size()[0] - (self.camera_bordas['esquerda'] + self.camera_bordas['direita'])
        altura = self.display_surface.get_size()[1] - (self.camera_bordas['cima'] + self.camera_bordas['baixo'])
        self.camera_rect = pg.Rect(esquerda,cima,largura,altura)

    def controle_mouse(self):
        #capturar a posição do mouse
        mouse = pg.math.Vector2(pg.mouse.get_pos())
        mouse_deslocamento_vetor = pg.math.Vector2()
        
        #bordas de onde o mouse não deve ultrapassar
        self.camera_bordas = {'esquerda': 1500,'direita': 1500,'cima': 750,'baixo': 750}
        borda_esquerda = self.camera_bordas['esquerda']
        borda_cima = self.camera_bordas['cima']
        borda_direita = self.display.get_window_size()[0] - self.camera_bordas['direita']
        borda_baixo = self.display.get_surface_size()[1] - self.camera_bordas['baixo'] 

        #verificando a posição X do mouse
        if borda_cima < mouse.y < borda_baixo:
            if mouse.x < borda_esquerda:
                mouse_deslocamento_vetor.x = mouse.x - borda_esquerda
                pg.mouse.set_pos((borda_esquerda,mouse.y))

        self.deslocamento += mouse_deslocamento_vetor