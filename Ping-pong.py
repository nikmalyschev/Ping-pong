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

rocket_l = Player('rocket.png', 0, 420, 10)
rocket_r = Player('rocket.png', 620, 420, 10)
ball = GameSprite('ball.png', 350, 350, 2)

x_speed = 3
y_speed = 3

font.init()
font = font.Font(None, 70)

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

        ball.rect.x += x_speed
        ball.rect.y += y_speed

        if ball.rect.y <= 0 or ball.rect.y >= 450:
            y_speed *= -1
        if sprite.collide_rect(ball, rocket_l) or sprite.collide_rect(ball, rocket_r):
            x_speed *= -1
        if ball.rect.x >= 650:
            p1 = font.render('Player 1 lose!', True, (0, 0, 0))
            window.blit(p1, (200, 200))
            finish = True
        if ball.rect.x <= 0:
            p2 = font.render('Player 2 lose!', True, (0, 0, 0))
            window.blit(p2, (200, 200))
            finish = True

    clock.tick(FPS)
    display.update()