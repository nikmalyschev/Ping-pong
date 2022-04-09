from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.png'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

rocket_l = Player('rocket.png', -25, 420, 10)
rocket_r = Player('rocket.png', 650, 420, 10)
ball = GameSprite('ball.png', 350, 350, 2)

clock = time.Clock()
FPS = 60

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background, (0, 0))
        rocket_l.reset()
        rocket_l.update_l()
        rocket_r.reset()
        rocket_r.update_r()
        ball.reset()

    clock.tick(FPS)
    display.update()