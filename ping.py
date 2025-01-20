from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (50,50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed



window = display.set_mode((700,500))
display.set_caption('Поймай, если сможешь!!!')
background = transform.scale(image.load('table.png'),(700,500))

#Создаем текстовые оповещения
font.init()
font1 = font.SysFont(None, 70)
win = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('YOU LOSE!', True, (255, 0, 0))


game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))

    clock.tick(FPS)
    display.update()