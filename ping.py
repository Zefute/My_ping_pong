from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed


window = display.set_mode((700,500))
display.set_caption('Поймай, если сможешь!!!')
background = transform.scale(image.load('table.png'),(700,500))

#Создаем текстовые оповещения
font.init()
font1 = font.SysFont(None, 70)
win = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('YOU LOSE!', True, (255, 0, 0))

#создвем два класса
player1 = Player('rocket.png', 0, 200, 50, 90, 5)
player2 = Player('rocket.png', 650, 200, 50, 90, 5)

#мячик)))
ball = GameSprite('ball.png', 325 , 225 , 50, 50, 0)
speed_x = 3
speed_y = 3

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
        player1.update_right()
        player2.update_left()
        player1.reset()
        player2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *=-1
    clock.tick(FPS)
    display.update()
