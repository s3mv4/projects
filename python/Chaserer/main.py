import pygame
import sys
import random

class Catcher(pygame.sprite.Sprite):
    def __init__(self):
        global runner_side
        global catcher_direction
        super().__init__()
        if runner_side == "left":
            catcher_direction = "left"
            self.image = pygame.image.load("Images/catcher_left.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect(midright = (700, 300))
        else:
            catcher_direction = "right"
            self.image = pygame.image.load("Images/catcher_right.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect(midleft = (100, 300))
        self.vel = [0, 0]

    def velocity(self):
        if self.vel[0] > 0:
            self.rect.x += 2.5
        if self.vel[0] < 0:
            self.rect.x -= 2.5
        if self.vel[1] > 0:
            self.rect.y += 2.5
        if self.vel[1] < 0:
            self.rect.y -= 2.5


        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def input(self):
        global runner_side
        global catcher_direction
        keys = pygame.key.get_pressed()
        if runner_side == "left":
            if keys[pygame.K_UP]:
                catcher_direction = "up"
                self.vel[1] = -1
            elif keys[pygame.K_DOWN]:
                catcher_direction = "down"
                self.vel[1] = 1
            else:
                self.vel[1] = 0
            if keys[pygame.K_LEFT]:
                catcher_direction = "left"
                self.vel[0] = -1
            elif keys[pygame.K_RIGHT]:
                catcher_direction = "right"
                self.vel[0] = 1
            else:
                self.vel[0] = 0
        else:
            if keys[pygame.K_w]:
                catcher_direction = "up"
                self.vel[1] = -1
            elif keys[pygame.K_s]:
                catcher_direction = "down"
                self.vel[1] = 1
            else:
                self.vel[1] = 0
            if keys[pygame.K_a]:
                catcher_direction = "left"
                self.vel[0] = -1
            elif keys[pygame.K_d]:
                catcher_direction = "right"
                self.vel[0] = 1
            else:
                self.vel[0] = 0

    def animation(self):
        if catcher_direction == "up":
            self.image = pygame.image.load("Images/catcher_up.png").convert_alpha()
        if catcher_direction == "down":
            self.image = pygame.image.load("Images/catcher_down.png").convert_alpha()
        if catcher_direction == "left":
            self.image = pygame.image.load("Images/catcher_left.png").convert_alpha()
        if catcher_direction == "right":
            self.image = pygame.image.load("Images/catcher_right.png").convert_alpha()

    def create_fireball(self):
        fireball_x = self.rect.centerx + 5
        fireball_y = self.rect.centery
        fireball_direction = catcher_direction
        return Fireball(fireball_x, fireball_y, fireball_direction)

    def update(self):
        self.velocity()
        self.input()
        self.animation()
        self.image = pygame.transform.scale(self.image, (64, 64))

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load("Images/fireball_left.png")
        self.rect = self.image.get_rect(center = (x, y))
        self.direction = direction

    def update(self):
        if self.direction == "up":
            self.image = pygame.image.load("Images/fireball_up.png")
            self.rect.y -= 10
        if self.direction == "down":
            self.image = pygame.image.load("Images/fireball_down.png")
            self.rect.y += 10
        if self.direction == "left":
            self.image = pygame.image.load("Images/fireball_left.png")
            self.rect.x -= 10
        if self.direction == "right":
            self.image = pygame.image.load("Images/fireball_right.png")
            self.rect.x += 10

        if self.rect.right <= 0 or self.rect.left >= 800 or self.rect.bottom <= 0 or self.rect.top >= 600:
            self.kill()

        if game_active == False:
            self.kill()

class Runner(pygame.sprite.Sprite):
    def __init__(self):
        global runner_side
        super().__init__()
        self.image = pygame.image.load("Images/runner.png")
        if runner_side == "left":
            self.rect = self.image.get_rect(center = (100, 300))
        else:
             self.rect = self.image.get_rect(center = (700, 300))
        self.vel = [0, 0]

    def input(self):
        global runner_side
        keys = pygame.key.get_pressed()
        if runner_side == "left":
            if keys[pygame.K_w]:
                self.vel[1] = -1
            elif keys[pygame.K_s]:
                self.vel[1] = 1
            else:
                self.vel[1] = 0
            if keys[pygame.K_a]:
                self.vel[0] = -1
            elif keys[pygame.K_d]:
                self.vel[0] = 1
            else:
                self.vel[0] = 0
        else:
            if keys[pygame.K_UP]:
                self.vel[1] = -1
            elif keys[pygame.K_DOWN]:
                self.vel[1] = 1
            else:
                self.vel[1] = 0
            if keys[pygame.K_LEFT]:
                self.vel[0] = -1
            elif keys[pygame.K_RIGHT]:
                self.vel[0] = 1
            else:
                self.vel[0] = 0

    def velocity(self):
        if self.vel[0] > 0:
            self.rect.x += 5
        if self.vel[0] < 0:
            self.rect.x -= 5
        if self.vel[1] > 0:
            self.rect.y += 5
        if self.vel[1] < 0:
            self.rect.y -= 5

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def update(self):
        self.input()
        self.velocity()

def collisions():
    global winner, restarts
    if pygame.sprite.groupcollide(catcher_group, runner_group, True, True):
        winner = "catcher"
        restarts += 1
        return False
    elif pygame.sprite.groupcollide(fireball_group, runner_group, True, True):
        winner = "catcher"
        restarts += 1
        return False
    elif current_time - time_time >30000:
        winner = "runner"
        restarts += 1
        return False
    else:
        return True

def blitters():
    fireball_group.draw(screen)
    fireball_group.update()
    catcher_group.draw(screen)
    catcher_group.update()
    runner_group.draw(screen)
    runner_group.update()

def timer():
    global time_time, game_active
    if current_time - time_time < 1000:
        time = 30
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 1000 and current_time - time_time < 2000:
        time = 29
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 2000 and current_time - time_time < 3000:
        time = 28
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 3000 and current_time - time_time < 4000:
        time = 27
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 4000 and current_time - time_time < 5000:
        time = 26
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 5000 and current_time - time_time < 6000:
        time = 25
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 6000 and current_time - time_time < 7000:
        time = 24
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 7000 and current_time - time_time < 8000:
        time = 23
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 8000 and current_time - time_time < 9000:
        time = 22
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 9000 and current_time - time_time < 10000:
        time = 21
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 10000 and current_time - time_time < 11000:
        time = 20
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 11000 and current_time - time_time < 12000:
        time = 19
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 12000 and current_time - time_time < 13000:
        time = 18
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 13000 and current_time - time_time < 14000:
        time = 17
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 14000 and current_time - time_time < 15000:
        time = 16
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 15000 and current_time - time_time < 16000:
        time = 15
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 16000 and current_time - time_time < 17000:
        time = 14
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 17000 and current_time - time_time < 18000:
        time = 13
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 18000 and current_time - time_time < 19000:
        time = 12
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 19000 and current_time - time_time < 20000:
        time = 11
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 20000 and current_time - time_time < 21000:
        time = 10
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 21000 and current_time - time_time < 22000:
        time = 9
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 22000 and current_time - time_time < 23000:
        time = 8
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 23000 and current_time - time_time < 24000:
        time = 7
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 24000 and current_time - time_time < 25000:
        time = 6
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 25000 and current_time - time_time < 26000:
        time = 5
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 26000 and current_time - time_time < 27000:
        time = 4
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 27000 and current_time - time_time < 28000:
        time = 3
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 28000 and current_time - time_time < 29000:
        time = 2
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 29000 and current_time - time_time < 30000:
        time = 1
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)
    if current_time - time_time > 30000:
        time = 0
        timer_text = timer_font.render(f"{time}", False, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(midtop = (400, 25))
        screen.blit(timer_text, timer_text_rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game_active = False

title_font = pygame.font.Font(None, 150)
timer_font = pygame.font.Font("Fonts/Minecraft.ttf", 50)
winner_font = pygame.font.Font(None, 50)

current_time = 0
talk_time = 0
time = 30
time_time = 0

restarts = 0

winner = 0

runner_side = 0

pew_sound = pygame.mixer.Sound("Audio/pew.mp3")

talk_sounds = [pygame.mixer.Sound("Audio/pakken.mp3"), pygame.mixer.Sound("Audio/pakken.mp3")]

catcher = Catcher()
catcher_group = pygame.sprite.Group()
catcher_group.add(catcher)

runner = Runner()
runner_group = pygame.sprite.Group()
runner_group.add(runner)

catcher_direction = 0

fireball_directions = []

fireball_group = pygame.sprite.Group()

shoot_time = -750

q_press = False

title_text = title_font.render("chaserer", True, (0, 0, 0))
title_text_rect = title_text.get_rect(center = (400, 300))

winner_text = winner_font.render(f"winner: {winner}", False, (0, 0, 0))
winner_text_rect = winner_text.get_rect(midbottom = (400, 500))

timer_text = timer_font.render(f"{time}", True, (255, 255, 255))
timer_text_rect = timer_text.get_rect(midtop = (400, 25))

title_catcher = pygame.image.load("Images/catcher_title.png")
title_catcher = pygame.transform.scale(title_catcher, (128, 128))
title_catcher_rect = title_catcher.get_rect(topleft = (600, 100))

title_runner = pygame.image.load("Images/runner_title.png")
title_runner = pygame.transform.scale(title_runner, (128, 128))
title_runner_rect = title_runner.get_rect(topright = (200, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_active is False:
            if event.key == pygame.K_p:
                runner_side = random.choice(["left", "right"])
                catcher.__init__()
                fireball_group.update()
                runner.__init__()
                talk_time = pygame.time.get_ticks()
                time_time = pygame.time.get_ticks()
                time = 30
                q_press = False
                game_active = True
                start_time = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN and game_active is True:
            if event.key == pygame.K_SPACE and current_time - shoot_time >= 750:
                pew_sound.play()
                fireball_group.add(catcher.create_fireball())
                shoot_time = pygame.time.get_ticks()
            if event.key == pygame.K_q:
                q_press = True
                game_active = False



    if game_active is True:
        game_active = collisions()
        current_time = pygame.time.get_ticks()

        if current_time - talk_time >= random.randint(7500, 10000):
            talk_sound = random.choice(talk_sounds)
            talk_sound.play()
            talk_time = pygame.time.get_ticks()

        screen.fill((0, 0, 0))
        blitters()
        timer()
    else:
        screen.fill((102, 6, 214))
        screen.blit(title_catcher, title_catcher_rect)
        screen.blit(title_runner, title_runner_rect)
        screen.blit(title_text, title_text_rect)
        pygame.draw.rect(screen, (0, 0, 0), title_catcher_rect, 5)
        pygame.draw.rect(screen, (0, 0, 0), title_runner_rect, 5)
        if restarts != 0 and q_press is False:
            winner_text = winner_font.render(f"winner: {winner}", True, (0, 0, 0))
            winner_text_rect = winner_text.get_rect(midbottom = (400, 500))
            screen.blit(winner_text, winner_text_rect)

    pygame.display.update()
    clock.tick(60)
