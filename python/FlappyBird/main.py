import pygame
from sys import exit
from random import randint
from math import floor

class Pipe:
    def __init__(self):
        self.scored = False
        self.height1 = randint(1, 21)
        self.pipe1 = pygame.Surface((50, height/32*self.height1))
        self.pipe1.fill((0, 128, 0))
        self.pipe1_rect = self.pipe1.get_rect(topleft = (width, 0)) 
        self.height2 = 22-self.height1
        self.pipe2 = pygame.Surface((50, height/32*self.height2))
        self.pipe2.fill((0, 128, 0))
        self.pipe2_rect = self.pipe2.get_rect(bottomleft = (width, height))
    def update(self):
        global pipes, score
        self.pipe1_rect.x -= 3
        self.pipe2_rect.x -= 3
        screen.blit(self.pipe1, self.pipe1_rect)
        screen.blit(self.pipe2, self.pipe2_rect)
        if self.pipe1_rect.right < 0 and self.pipe2_rect.right < 0:
            pipes.pop(0)
            pipes.append(Pipe())
        if self.pipe1_rect.colliderect(player_rect) or self.pipe2_rect.colliderect(player_rect):
            jammer_sound.play()
            pipes = []
            player_rect.centery = height/2
            pipes.append(Pipe())
        if self.pipe1_rect.right <= player_rect.left and self.pipe1_rect.right <= player_rect.left and self.scored == False:
            score_sound.play()
            score += 1
            self.scored = True


pygame.init()

# Screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Framerate
clock = pygame.time.Clock()

# Player
player = pygame.image.load("hoofd.png").convert_alpha()
player = pygame.transform.scale(player, (player.get_width()/4, player.get_width()/4))
player_rect = player.get_rect(center = (width/4, height/2))
player_vel_y = 0

# Pipes
pipes = [Pipe()]

# Sounds
jammer_sound = pygame.mixer.Sound("jammer.mp3")
jump_sound = pygame.mixer.Sound("jump.mp3")
score_sound = pygame.mixer.Sound("score.mp3")

# Score
score = 0
score_font = pygame.font.Font(None, 100)
score_text = score_font.render(f"{score}", True, (255, 255, 255))
score_text_rect = score_text.get_rect(topleft = (0, 0))

# Time
time = [1, 0]
time_str = ""
for i in time:
    if i < 10:
        time_str += "0" + str(i)
    else:
        time_str += str(i)
time_font = pygame.font.Font(None, 90)
time_text = time_font.render(f"{time_str}", True, (255, 255, 255))
time_text_rect = time_text.get_rect(bottomleft = (0, height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_vel_y = -5
                jump_sound.play()

    # Velocities
    player_vel_y += 0.15
    player_rect.y += player_vel_y

    if player_rect.bottom + player_vel_y >= height:
        player_rect.bottom = height
        player_vel_y = 0
    if player_rect.top + player_vel_y <= 0:
        player_rect.top = 0
        player_vel_y = 0.15

    # Blitters
    screen.fill((0,0,0))
    screen.blit(player, player_rect)

    score_text = score_font.render(f"{score}", True, (255, 255, 255))
    score_text_rect = score_text.get_rect(topleft = (0, 0))
    screen.blit(score_text, score_text_rect)

    if floor(time[1]) < 0:
        if time[0] == 0:
            print(score)
            pygame.quit()
            exit()
        else:
            time[0] -= 1
            time[1] = 60
    time_str = ""
    for i in time:
        if floor(i) < 10:
            time_str += "0" + str(floor(i))
        else:
            time_str += str(floor(i))
    time_str = time_str[:2] + ":" + time_str[2:]

    time_text = time_font.render(f"{time_str}", True, (255, 255, 255))
    time_text_rect = time_text.get_rect(bottomleft = (0, height))
    screen.blit(time_text, time_text_rect)

    time[1] -= 1/120

    for pipe in pipes:
        pipe.update()

    # Screen updates
    pygame.display.update()
    clock.tick(120)
