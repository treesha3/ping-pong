from pygame import*
font.init()
from time import time as timer

window = display.set_mode((1300,700))

display.set_caption('Пинг - понг')

clock = time.Clock()
font2 = font.Font(None, 80)

FPS = 144
speed_x = -3
speed_y = 3
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed


pl1 = Player1('racket.png', 50, 300, 25,200, 5)
pl2 = Player2('racket.png', 1250, 300, 25,200, 5)
ball = GameSprite('tenis_ball.png', 650, 300, 50, 50 ,3)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    window.fill((200,255,255))

    if not finish:        
        pl1.reset()
        pl1.update()
        pl2.reset()
        pl2.update()  
        ball.reset()
        ball.update()  

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(pl2,ball) or sprite.collide_rect(pl1,ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 640:
            speed_x *= 1
            speed_y *= -1  

        if ball.rect.y < 5:
            speed_x *= 1
            speed_y *= -1     


        if ball.rect.x < 50:
            finish = True
            lose_text = font2.render('ИГРОК 1 ПРОИГРАЛ', True, (255,0,0))
            window.blit(lose_text, (400,300))

        if ball.rect.x > 1250:
            finish = True
            lose_text = font2.render('ИГРОК 2 ПРОИГРАЛ', True, (255,0,0))
            window.blit(lose_text, (400,300))     

    else:
        finish = False
        time.delay(3000)
        
    display.update()
    clock.tick(FPS)