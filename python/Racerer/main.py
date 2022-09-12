import pygame
from sys import exit
import math

class Car:

    def __init__(self):
        self.img = pygame.image.load("Images/car.png")
        self.img = pygame.transform.scale(self.img, (self.img.get_width()*2, self.img.get_height()*2))
        self.rect = self.img.get_rect(center = (size[0]/2, size[1]/2))
        self.max_vel = 30
        self.vel = 0
        self.rotation_vel = 4
        self.angle = 0
        self.acceleration = 0.2
        self.vroom_rate = 0
        self.piep_rate = 0
        self.forward = False
        self.backward = False
        self.press = False
        self.sound_rate = 0
        self.lap = 1
        self.laps = 1
        self.letsgo = True

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
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        track_rect.y += vertical
        track_rect.x += horizontal

    def slow_down(self):
        if self.vel > 0:
            self.vel = max(self.vel - self.acceleration/4, 0)
        else:
            self.vel = min(self.vel + self.acceleration/4, 0)
        self.move()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_vel
        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_vel
        if keys[pygame.K_UP]:
            self.forward = True
        if keys[pygame.K_DOWN]:
            self.backward = True

    def update(self, screen):
        global checkpoints, game_active, final_time, start_time
        self.forward = False
        self.backward = False
        self.input()
        if self.forward:
            self.speed_up(True)
            if self.sound_rate <= 0:
                if self.vroom_rate == 0:
                    vroom.play()
                    self.vroom_rate = 10
                else:
                    self.vroom_rate -= 1
        elif self.backward:
            self.speed_up(False)
            if self.sound_rate <= 0:
                if self.piep_rate == 0:
                    piep.play()
                    self.piep_rate = 50
                else:
                    self.piep_rate -= 1
        else:
            self.slow_down()

        for i, checkpoint in enumerate(checkpoints):
            if self.rect.colliderect(pygame.Rect((track_rect.x-checkpoint[0].x+200, track_rect.y-checkpoint[0].y), (checkpoint_img.get_width(), checkpoint_img.get_height()))):
                checkpoints.pop(i)
                pygame.mixer.music.stop()
                checkpoint_sound.play()
                self.sound_rate = 40

        if self.rect.colliderect(pygame.Rect((track_rect.x-finish[0].x, track_rect.y-finish[0].y), (finish_img.get_width(), finish_img.get_height()))) and checkpoints == [] and self.lap < self.laps:
            pygame.mixer.music.stop()
            finish_sound.play()
            self.sound_rate = 30
            self.lap += 1
            checkpoints = [[-290.0, -4371, -180], [-597.0, -5248, -140], [-1844.0, -5868, -104], [-3566.0, -6204, -96], [-5892.0, -6566, -92], [-7769.0, -6815, -116], [-9346.0, -5997, -16], [-8758.0, -4397, 32], [-7557.0, -4477, 152], [-6370.0, -5574, 112], [-4726.0, -4729, -12], [-3675.0, -4066, 92], [-2482.0, -3783, 136], [-1825.0, -4214, 24], [-1860.0, -3211, -60], [-3521.0, -2643, -100], [-4958.0, -3408, -136], [-6241.0, -4507, -100], [-7049.0, -3910, -44], [-8492.0, -3371, -84], [-9758.0, -4087, -124], [-10506.0, -4479, -112], [-11582.0, -4913, -100], [-12712.0, -4288, -56], [-13527.0, -3117, -24], [-13239.0, -1381, 40], [-11941.0, -752, 92], [-10393.0, -1126, 124], [-9505.0, -2512, 200], [-10516.0, -3072, 268], [-11108.0, -2563, 332], [-11234.0, -1558, 376], [-10371.0, -698, 408], [-9255.0, -917, 504], [-7455.0, -2141, 444], [-6876.0, -1213, 360], [-6158.0, -483, 456], [-4600.0, -708, 472], [-1232.0, -1524, 476]]

            for i, checkpoint in enumerate(checkpoints[:]):
                checkpoints[i].insert(0, checkpoint_img.get_rect(topleft = (checkpoints[i][0], checkpoints[i][1])))
                checkpoints[i].pop(1)
                checkpoints[i].pop(1)
        elif self.rect.colliderect(pygame.Rect((track_rect.x-finish[0].x, track_rect.y-finish[0].y), (finish_img.get_width(), finish_img.get_height()))) and checkpoints == [] and self.lap == self.laps:
            pygame.mixer.music.stop()
            finish_sound.play()
            self.sound_rate = 30
            game_active = False
            final_time = f"{current_time[:-3]}.{current_time[-3:]}"

        elif self.rect.colliderect(pygame.Rect((track_rect.x-finish[0].x, track_rect.y-finish[0].y), (finish_img.get_width(), finish_img.get_height()))) and self.letsgo:
            self.sound_rate = 30
            letsgo.play()
            self.letsgo = False

        if self.letsgo:
            start_time = pygame.time.get_ticks()



        if self.sound_rate > 0:
            self.sound_rate -= 1

        blit_rotate_center(screen, self.img, (self.rect.x, self.rect.y), self.angle)

def blit_rotate_center(screen, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    screen.blit(rotated_image, new_rect.topleft)

pygame.init()

size = (800, 600)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

track = pygame.image.load("Images/track.png")
track = pygame.transform.scale(track, (track.get_width()*7, track.get_height()*7))
track_rect = track.get_rect(topleft = (-170, -2575))

car = Car()

vroom = pygame.mixer.Sound("Sound/vroom.mp3")
piep = pygame.mixer.Sound("Sound/piep.mp3")
checkpoint_sound = pygame.mixer.Sound("Sound/checkpoint.mp3")
finish_sound = pygame.mixer.Sound("Sound/finish.mp3")
letsgo = pygame.mixer.Sound("Sound/letsgo.mp3")

font = pygame.font.Font("Fonts/Minecraft.ttf", 50)
big_font = pygame.font.Font("Fonts/Minecraft.ttf", 150)

title_surf = big_font.render("Racerer", False, (255, 0, 0))
title_rect = title_surf.get_rect(midtop = (size[0]/2, 50))

space_surf = font.render("press space to start", False, (255, 0, 0))
space_rect = space_surf.get_rect(center = (size[0]/2, size[1]/8*5))

laps_surf = font.render(f"Lap:{car.lap}/{car.laps}", False, (255, 0, 0))
laps_rect = space_surf.get_rect(topleft = (0, 0))
laps_bg = pygame.Surface((laps_surf.get_width(), laps_surf.get_height()))
laps_bg.fill((50, 50, 50))

start_time = 0
time = int(pygame.time.get_ticks())
current_time = str(time - start_time)
time_surf = font.render(f"{current_time[:-3]}.{current_time[-3:]}", False, (255, 0, 0))
time_rect = time_surf.get_rect(midtop = (size[0]/2, 0))
time_bg = pygame.Surface((time_surf.get_width(), time_surf.get_height()))
time_bg.fill((50, 50, 50))

game_active = False
final_time = 0

ftime_surf = font.render(f"{final_time}", False, (255, 0, 0))
ftime_rect = ftime_surf.get_rect(midbottom = (size[0]/2, size[1]-75))

checkpoint_img = pygame.image.load("Images/checkpoint.png")
checkpoint_img = pygame.transform.scale(checkpoint_img, (checkpoint_img.get_width()*2, checkpoint_img.get_height()*2))

checkpoints = [[-290.0, -4371, -180], [-597.0, -5248, -140], [-1844.0, -5868, -104], [-3566.0, -6204, -96], [-5892.0, -6566, -92], [-7769.0, -6815, -116], [-9346.0, -5997, -16], [-8758.0, -4397, 32], [-7557.0, -4477, 152], [-6370.0, -5574, 112], [-4726.0, -4729, -12], [-3675.0, -4066, 92], [-2482.0, -3783, 136], [-1825.0, -4214, 24], [-1860.0, -3211, -60], [-3521.0, -2643, -100], [-4958.0, -3408, -136], [-6241.0, -4507, -100], [-7049.0, -3910, -44], [-8492.0, -3371, -84], [-9758.0, -4087, -124], [-10506.0, -4479, -112], [-11582.0, -4913, -100], [-12712.0, -4288, -56], [-13527.0, -3117, -24], [-13239.0, -1381, 40], [-11941.0, -752, 92], [-10393.0, -1126, 124], [-9505.0, -2512, 200], [-10516.0, -3072, 268], [-11108.0, -2563, 332], [-11234.0, -1558, 376], [-10371.0, -698, 408], [-9255.0, -917, 504], [-7455.0, -2141, 444], [-6876.0, -1213, 360], [-6158.0, -483, 456], [-4600.0, -708, 472], [-1232.0, -1524, 476]]

for i, checkpoint in enumerate(checkpoints[:]):
    checkpoints[i].insert(0, checkpoint_img.get_rect(topleft = (checkpoints[i][0], checkpoints[i][1])))
    checkpoints[i].pop(1)
    checkpoints[i].pop(1)

finish_img = pygame.image.load("Images/finish.png")
finish_img = pygame.transform.scale(finish_img, (finish_img.get_width()*2, finish_img.get_height()*2))
finish = [finish_img.get_rect(topleft = (-470, -2975)), -180]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_active:
                track_rect = track.get_rect(topleft = (-170, -2875))

                car = Car()

                final_time = 0

                checkpoints = [[-290.0, -4371, -180], [-597.0, -5248, -140], [-1844.0, -5868, -104], [-3566.0, -6204, -96], [-5892.0, -6566, -92], [-7769.0, -6815, -116], [-9346.0, -5997, -16], [-8758.0, -4397, 32], [-7557.0, -4477, 152], [-6370.0, -5574, 112], [-4726.0, -4729, -12], [-3675.0, -4066, 92], [-2482.0, -3783, 136], [-1825.0, -4214, 24], [-1860.0, -3211, -60], [-3521.0, -2643, -100], [-4958.0, -3408, -136], [-6241.0, -4507, -100], [-7049.0, -3910, -44], [-8492.0, -3371, -84], [-9758.0, -4087, -124], [-10506.0, -4479, -112], [-11582.0, -4913, -100], [-12712.0, -4288, -56], [-13527.0, -3117, -24], [-13239.0, -1381, 40], [-11941.0, -752, 92], [-10393.0, -1126, 124], [-9505.0, -2512, 200], [-10516.0, -3072, 268], [-11108.0, -2563, 332], [-11234.0, -1558, 376], [-10371.0, -698, 408], [-9255.0, -917, 504], [-7455.0, -2141, 444], [-6876.0, -1213, 360], [-6158.0, -483, 456], [-4600.0, -708, 472], [-1232.0, -1524, 476]]

                for i, checkpoint in enumerate(checkpoints[:]):
                    checkpoints[i].insert(0, checkpoint_img.get_rect(topleft = (checkpoints[i][0], checkpoints[i][1])))
                    checkpoints[i].pop(1)
                    checkpoints[i].pop(1)

                game_active = True
            if event.key == pygame.K_q and game_active:
                game_active = False

    if game_active:
        time = int(pygame.time.get_ticks())
        current_time = str(time - start_time)
        if len(current_time) > 3:
            time_surf = font.render(f"{current_time[:-3]}.{current_time[-3:]}", False, (255, 0, 0))
        else:
            time_surf = font.render(current_time, False, (255, 0, 0))
        time_rect = time_surf.get_rect(midtop = (size[0]/2, 0))
        time_bg = pygame.Surface((time_surf.get_width(), time_surf.get_height()))
        time_bg.fill((50, 50, 50))

        laps_surf = font.render(f"Lap:{car.lap}/{car.laps}", False, (255, 0, 0))
        laps_rect = space_surf.get_rect(topleft = (0, 0))
        laps_bg = pygame.Surface((laps_surf.get_width(), laps_surf.get_height()))
        laps_bg.fill((50, 50, 50))

        screen.fill((50, 50, 50))
        screen.blit(track, track_rect)
        car.update(screen)
        for checkpoint in checkpoints[:]:
            blit_rotate_center(screen, checkpoint_img, (track_rect.x-checkpoint[0].x+200, track_rect.y-checkpoint[0].y), checkpoint[1])
        blit_rotate_center(screen, finish_img, (track_rect.x-finish[0].x, track_rect.y-finish[0].y), finish[1])
        if not car.letsgo:
            screen.blit(time_bg, (time_rect.x, time_rect.y))
            screen.blit(time_surf, time_rect)
            if car.laps != 1:
                screen.blit(laps_bg, (laps_rect.x, laps_rect.y))
                screen.blit(laps_surf, laps_rect)

    else:
        screen.fill((50, 50, 50))
        screen.blit(track, track_rect)
        screen.blit(title_surf, title_rect)
        screen.blit(space_surf, space_rect)
        if final_time:
            ftime_surf = font.render(f"{final_time}", False, (255, 0, 0))
            ftime_rect = ftime_surf.get_rect(midbottom = (size[0]/2, size[1]-75))
            screen.blit(ftime_surf, ftime_rect)
    pygame.display.update()
    clock.tick(60)
