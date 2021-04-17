
#импорт
from pygame import *
#окно
okno = display.set_mode((300,200))
fon = transform.scale(image.load("images.jpg"), (300, 200))
#класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

#цикл игры
game = True
while game:
    for e in event.get():
            if e.type==QUIT:
                run=False
    okno.blit(fon,(0, 0))
