import pygame
from sys import exit
import math
from random import randint

class Space_ship:
    def __init__(self, size, p):
        self.p = p
        self.size = size
        self.img = pygame.image.load("Images/space_ship" + str(self.p) + ".png")
        self.img = pygame.transform.scale(self.img, (self.img.get_width()*2, self.img.get_height()*2))
        if self.p == 2:
            self.rect = self.img.get_rect(midleft = (0, self.size[1]/2))
            self.angle = -90
        elif self.p == 1:
            self.rect = self.img.get_rect(midright = (self.size[0], self.size[1]/2))
            self.angle = 90
        self.max_vel = 7.5
        self.vel = 0
        self.rotation_vel = 4
        self.acceleration = 0.2
        self.forward = False
        self.backward = False
        self.bullets = []
        self.bullet_delay = 0
        self.radians = 0
        self.vertical = 0
        self.horizontal = 0
        self.score = 0
        self.pressed = True
        self.ghost = False
        self.ghost_rate = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if self.p == 1:
            if keys[pygame.K_RIGHT]:
                self.angle -= self.rotation_vel
            if keys[pygame.K_LEFT]:
                self.angle += self.rotation_vel
            if keys[pygame.K_UP]:
                self.forward = True
            if keys[pygame.K_DOWN]:
                self.backward = True
            if keys[pygame.K_SPACE] and self.bullet_delay <= 0 and self.pressed == False:
                pew.play()
                self.shoot()
                self.bullet_delay = 15
                self.pressed = True
            elif not keys[pygame.K_SPACE]:
                self.pressed = False
        elif self.p == 2:
            if keys[pygame.K_d]:
                self.angle -= self.rotation_vel
            if keys[pygame.K_a]:
                self.angle += self.rotation_vel
            if keys[pygame.K_w]:
                self.forward = True
            if keys[pygame.K_s]:
                self.backward = True
            if keys[pygame.K_LSHIFT] and self.bullet_delay <= 0 and self.pressed == False:
                pew.play()
                self.shoot()
                self.bullet_delay = 15
                self.pressed = True
            elif not keys[pygame.K_LSHIFT]:
                self.pressed = False

    def speed_up(self, forward):
        if forward and self.vel >= 0:
            self.vel = min(self.vel + self.acceleration, self.max_vel)
        elif not forward and self.vel <= 0:
            self.vel = max(self.vel - self.acceleration, self.max_vel*-1)
        elif forward and self.vel < 0:
            self.vel = min(self.vel + self.acceleration*4, 0)
        elif not forward and self.vel > 0:
            self.vel = max(self.vel - self.acceleration*4, 0)
        self.move()

    def move(self):
        self.radians = math.radians(self.angle)
        self.vertical = math.cos(self.radians) * self.vel
        self.horizontal = math.sin(self.radians) * self.vel

        if self.rect.right - self.horizontal < 0:
            self.rect.left = self.size[0]
        elif self.rect.left - self.horizontal > self.size[0]:
            self.rect.right = 0

        if self.rect.bottom - self.vertical < 0:
            self.rect.top = self.size[1]
        elif self.rect.top - self.vertical > self.size[1]:
            self.rect.bottom = 0

        self.rect.x -= self.horizontal
        self.rect.y -= self.vertical

    def slow_down(self):
        if self.vel > 0:
            self.vel = max(self.vel - self.acceleration/4, 0)
        else:
            self.vel = min(self.vel + self.acceleration/4, 0)
        self.move()

    def shoot(self):
        self.bullets.append(Bullet(self.rect, self.angle, self.size, self.p))

    def change_img(self):
        if self.ghost == True:
            self.img = pygame.image.load("Images/space_ship" + str(self.p) + "_ghost.png")
            self.img = pygame.transform.scale(self.img, (self.img.get_width()*2, self.img.get_height()*2))
        else:
            self.img = pygame.image.load("Images/space_ship" + str(self.p) + ".png")
            self.img = pygame.transform.scale(self.img, (self.img.get_width()*2, self.img.get_height()*2))


    def update(self, screen):
        self.bullet_delay -= 1
        self.forward = False
        self.backward = False
        self.input()
        if self.forward:
            self.speed_up(True)
        elif self.backward:
            self.speed_up(False)
        else:
            self.slow_down()
        self.ghost_rate -=  1
        if self.ghost_rate > 0:
            self.ghost = True
        else:
            self.ghost = False
        self.change_img()
        blit_rotate_center(screen, self.img, (self.rect.x, self.rect.y), self.angle)

class Bullet:
    def __init__(self, rect, angle, size, p):
        self.p = p
        self.img = pygame.image.load("Images/bullet" + str(self.p) + ".png")
        self.rect = self.img.get_rect(center = (rect.centerx, rect.centery))
        self.angle = angle
        self.size = size
        self.vel = 15
        self.radians = 0
        self.vertical = 0
        self.horizontal = 0

    def move(self):
        self.radians = math.radians(self.angle)
        self.vertical = math.cos(self.radians) * self.vel
        self.horizontal = math.sin(self.radians) * self.vel

        self.rect.y -= self.vertical
        self.rect.x -= self.horizontal

    def update(self, screen):
        blit_rotate_center(screen, self.img, (self.rect.x, self.rect.y), self.angle)

def blit_rotate_center(screen, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    screen.blit(rotated_image, new_rect.topleft)

class Comet:
    def __init__(self, size, p_size):
        self.size = size
        self.img = pygame.Surface((p_size[0]/4, p_size[1]/4))
        self.randint = randint(0, 10)
        if self.randint == 0:
            self.rgb = (255, 255, 255)
        else:
            self.rgb = (128, 128, 128)
        self.img.fill(self.rgb)
        self.rect = self.img.get_rect(midbottom = (randint(0, self.size[0]), 0))
        self.vel = 3

    def move(self):
        self.rect.y += self.vel

    def update(self, screen):
        screen.blit(self.img, self.rect)

class Star:
    def __init__(self, size, p_size):
        self.size = size
        self.img = pygame.Surface((p_size[0]/16, p_size[1]/16))
        self.img.fill((255, 255, 0))
        self.rect = self.img.get_rect(midbottom = (randint(0, self.size[0]), 0))
        self.vel = 5

    def move(self):
        self.rect.y += self.vel

    def update(self, screen):
        screen.blit(self.img, self.rect)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FRAMERATE = 60
game_active = False

pew = pygame.mixer.Sound("Sound/pew.mp3")
oof = pygame.mixer.Sound("Sound/oof2.mp3")
geest = pygame.mixer.Sound("Sound/geest.mp3")

font = pygame.font.Font("Fonts/Minecraft.ttf", 50)
big_font = pygame.font.Font("Fonts/Minecraft.ttf", 150)

space_ship1 = Space_ship(size, 1)
space_ship2 = Space_ship(size, 2)
kill_index1 = []
kill_index2 = []

stars = []
kill_index3 = []
star_rate = FRAMERATE/60

comets = []
kill_index4 = []
comet_rate = FRAMERATE/2

score1_surf = font.render(f"{space_ship1.score}", False, (167, 54, 56))
score1_rect = score1_surf.get_rect(topleft = (0, 0))

score2_surf = font.render(f"{space_ship2.score}", False, (54, 137, 167))
score2_rect = score2_surf.get_rect(topright = (size[0], 0))

title_surf = big_font.render("Spacerer", False, (200, 200, 200))
title_rect = title_surf.get_rect(midtop = (size[0]/2, 50))

space_surf = font.render("press p to start", False, (200, 200, 200))
space_rect = space_surf.get_rect(center = (size[0]/2, size[1]/8*5))

winner = ""
winner_surf = font.render(f"{winner} won the round!", False, (200, 200, 200))
winner_rect = winner_surf.get_rect(center = (size[0]/2, size[1]/8*7))

seconds = 60
time_str = ""
if math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60) < 10:
    time_str = f"{math.floor(math.ceil(seconds)/60)}:0{math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60)}"
elif math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60) >= 10:
    time_str = f"{math.floor(math.ceil(seconds)/60)}:{math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60)}"
time_surf = font.render(time_str, False, (200, 200, 200))
time_rect = time_surf.get_rect(midtop = (size[0]/2, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and game_active == False:
                space_ship1 = Space_ship(size, 1)
                space_ship2 = Space_ship(size, 2)
                kill_index1 = []
                kill_index2 = []
                stars = []
                kill_index3 = []
                star_rate = FRAMERATE/60
                comets = []
                kill_index4 = []
                comet_rate = FRAMERATE/2
                seconds = 120
                game_active = True
            if event.key == pygame.K_q and game_active == True:
                game_active = False

    screen.fill((0, 0, 50))
    star_rate -=  1
    if star_rate <= 0:
        stars.append(Star(size, space_ship1.img.get_size()))
        star_rate = 1
    for i, star in enumerate(stars):
        star.move()
        if star.rect.top + star.vel > size[1]:
            kill_index3.append(i)
        star.update(screen)
    if kill_index3 != []:
        for i in kill_index3:
            stars.pop(i)
            for j, k in enumerate(kill_index3):
                kill_index3[j] -= 1
        kill_index3 = []
    if game_active:
        seconds -= 1/FRAMERATE
        if math.ceil(seconds) == 0:
            if space_ship2.score > space_ship1.score:
                winner = "WASD"
            elif space_ship1.score > space_ship2.score:
                winner = "arrow keys"
            else:
                winner = "tie"
            winner_surf = font.render(f"{winner} won the round!", False, (200, 200, 200))
            winner_rect = winner_surf.get_rect(center = (size[0]/2, size[1]/8*7))
            game_active = False
        comet_rate -=  1
        if comet_rate <= 0:
            comets.append(Comet(size, space_ship1.img.get_size()))
            comet_rate = 30
        for i, bullet in enumerate(space_ship1.bullets):
            bullet.move()
            if bullet.rect.right - bullet.horizontal < 0:
                kill_index1.append(i)
            elif bullet.rect.left - bullet.horizontal > space_ship1.size[0]:
                kill_index1.append(i)
            elif bullet.rect.bottom - bullet.vertical < 0:
                kill_index1.append(i)
            elif bullet.rect.top - bullet.vertical > space_ship1.size[1]:
                kill_index1.append(i)
            elif bullet.rect.colliderect(space_ship2.rect) and space_ship2.ghost == False:
                oof.play()
                space_ship1.score += 1
                kill_index1.append(i)
            bullet.update(screen)
        if kill_index1 != []:
            for i in kill_index1:
                space_ship1.bullets.pop(i)
                for j, k in enumerate(kill_index1):
                    kill_index1[j] -= 1
            kill_index1 = []

        for i, bullet in enumerate(space_ship2.bullets):
            bullet.move()
            if bullet.rect.right - bullet.horizontal < 0:
                kill_index2.append(i)
            elif bullet.rect.left - bullet.horizontal > space_ship2.size[0]:
                kill_index2.append(i)
            elif bullet.rect.bottom - bullet.vertical < 0:
                kill_index2.append(i)
            elif bullet.rect.top - bullet.vertical > space_ship2.size[1]:
                kill_index2.append(i)
            elif bullet.rect.colliderect(space_ship1.rect) and space_ship1.ghost == False:
                oof.play()
                space_ship2.score += 1
                kill_index2.append(i)
            bullet.update(screen)
        if kill_index2 != []:
            for i in kill_index2:
                space_ship2.bullets.pop(i)
                for j, k in enumerate(kill_index2):
                    kill_index2[j] -= 1
            kill_index2 = []

        for i, comet in enumerate(comets):
            comet.move()
            if comet.rect.top + comet.vel > size[1]:
                kill_index4.append(i)
            elif comet.rect.colliderect(space_ship1.rect) and comet.rgb == (128, 128, 128) and space_ship1.ghost == False:
                oof.play()
                space_ship1.score -= 1
                kill_index4.append(i)
            elif comet.rect.colliderect(space_ship2.rect) and comet.rgb == (128, 128, 128) and space_ship2.ghost == False:
                oof.play()
                space_ship2.score -= 1
                kill_index4.append(i)
            elif comet.rect.colliderect(space_ship1.rect) and comet.rgb == (255, 255, 255):
                geest.play()
                space_ship1.ghost_rate = FRAMERATE*5
                kill_index4.append(i)
            elif comet.rect.colliderect(space_ship2.rect) and comet.rgb == (255, 255, 255):
                geest.play()
                space_ship2.ghost_rate = FRAMERATE*5
                kill_index4.append(i)
            comet.update(screen)
        if kill_index4 != []:
            for i in kill_index4:
                comets.pop(i)
                for j, k in enumerate(kill_index4):
                    kill_index4[j] -= 1
            kill_index4 = []

        time_str = ""
        if math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60) < 10:
            time_str = f"{math.floor(math.ceil(seconds)/60)}:0{math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60)}"
        elif math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60) >= 10:
            time_str = f"{math.floor(math.ceil(seconds)/60)}:{math.ceil(seconds)-(math.floor(math.ceil(seconds)/60)*60)}"
        time_surf = font.render(time_str, False, (200, 200, 200))
        time_rect = time_surf.get_rect(midtop = (size[0]/2, 0))

        space_ship1.update(screen)
        space_ship2.update(screen)
        score1_surf = font.render(f"{space_ship1.score}", False, (167, 54, 56))
        score1_rect = score1_surf.get_rect(topright = (size[0], 0))
        score2_surf = font.render(f"{space_ship2.score}", False, (54, 137, 167))
        score2_rect = score2_surf.get_rect(topleft = (0, 0))
        screen.blit(score1_surf, score1_rect)
        screen.blit(score2_surf, score2_rect)
        screen.blit(time_surf, time_rect)

    else:
        screen.blit(title_surf, title_rect)
        screen.blit(space_surf, space_rect)
        if winner != "":
            screen.blit(winner_surf, winner_rect)

    pygame.display.update()
    clock.tick(FRAMERATE)
