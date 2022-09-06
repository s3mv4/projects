import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Platformer/Images/player_idle/player_idle1_right.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(display_size[0] / 2, 50))
        self.vel = [0, 0]
        self.flipside = 0
        self.air_timer = 0
        self.on_ground = False
        self.can_2jump = False
        self.idle_animation = [
        pygame.image.load("Platformer/Images/player_idle/player_idle1_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_idle/player_idle2_right.png").convert_alpha()
        ]
        self.walking_animation = [
        pygame.image.load("Platformer/Images/player_walk/player_walk1_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk2_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk3_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk4_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk5_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk6_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk7_right.png").convert_alpha(),
        pygame.image.load("Platformer/Images/player_walk/player_walk8_right.png").convert_alpha()
        ]
        self.idle_frame = 0
        self.walking_frame = 0
        self.jumps = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jumps <= 1 and self.can_2jump is True:
            self.vel[1] = -4
            self.can_2jump = False
            self.on_ground = False
            self.jumps += 1
        if keys[pygame.K_UP] and self.jumps <= 1 and self.can_2jump is True:
            self.vel[1] = -4
            self.can_2jump = False
            self.on_ground = False
            self.jumps += 1
        if not keys[pygame.K_SPACE] and not keys[pygame.K_UP]:
            self.can_2jump = True
        if keys[pygame.K_LEFT]:
            self.vel[0] = -2
            self.flipside = 0
            self.idle_frame = 0
        elif keys[pygame.K_RIGHT]:
            self.vel[0] = 2
            self.flipside = 1
            self.idle_frame = 0

        else:
            self.vel[0] = 0

    def player_y_vel(self):
        if self.on_ground is True:
            self.jumps = 0
        self.vel[1] += 0.2
        if self.vel[1] > 3:
            self.vel[1] = 3
        self.rect.y += self.vel[1]

    def player_x_vel(self):
        self.rect.x += self.vel[0]
        if self.rect.right >= display_size[0]:
            self.rect.right = display_size[0]
        if self.rect.left <= 0:
            self.rect.left = 0

    def animation_idle(self):
        if self.vel[0] == 0 and self.on_ground == True:
            self.idle = True
        else:
            self.idle = False
        if self.idle == True:
            self.walking_frame = 0
            self.image = self.idle_animation[int(self.idle_frame)]
            if int(self.idle_frame) == 0:
                self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
            elif int(self.idle_frame) == 1:
                self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y + 2))
            self.idle_frame += 0.05
            if self.idle_frame >= len(self.idle_animation):
                self.idle_frame = 0
            if self.flipside == 1:
                self.idle_animation = [
                pygame.image.load("Platformer/Images/player_idle/player_idle1_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_idle/player_idle2_right.png").convert_alpha()
                ]
            elif self.flipside == 0:
                self.idle_animation = [
                pygame.image.load("Platformer/Images/player_idle/player_idle1_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_idle/player_idle2_left.png").convert_alpha()
                ]

    def animation_walking(self):
        if self.vel[0] != 0 and self.on_ground == True:
            self.walking = True
        else:
            self.walking = False
        if self.walking == True:
            self.image = self.walking_animation[int(self.walking_frame)]
            self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
            self.walking_frame += 0.5
            if self.walking_frame >= len(self.walking_animation):
                self.walking_frame = 0
            if self.flipside == 1:
                self.walking_animation = [
                pygame.image.load("Platformer/Images/player_walk/player_walk1_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk2_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk3_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk4_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk5_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk6_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk7_right.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk8_right.png").convert_alpha()
                ]
            elif self.flipside == 0:
                self.walking_animation = [
                pygame.image.load("Platformer/Images/player_walk/player_walk1_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk2_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk3_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk4_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk5_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk6_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk7_left.png").convert_alpha(),
                pygame.image.load("Platformer/Images/player_walk/player_walk8_left.png").convert_alpha()
                ]

    def animation_jump(self):
        if self.walking == False and self.idle == False:
            if self.flipside == 1:
                self.image = pygame.image.load("Platformer/Images/player_walk/player_walk3_right.png").convert_alpha()
            elif self.flipside == 0:
                self.image = pygame.image.load("Platformer/Images/player_walk/player_walk3_left.png").convert_alpha()

    def collisions(self):
        for tile_rect in tile_rects:
            if self.rect.colliderect(tile_rect):
                if abs(tile_rect.top - self.rect.bottom) <= 5:
                    self.on_ground = True
                    self.rect.bottom = tile_rect.top
                    self.vel[1] = 0
                if abs(tile_rect.bottom - self.rect.top) <= 4:
                    self.rect.top = tile_rect.bottom
                    self.vel[1] = 0
                if abs(tile_rect.right - self.rect.left) <= 2:
                    self.rect.left = tile_rect.right
                    self.vel[0] = 0
                if abs(tile_rect.left - self.rect.right) <= 2:
                    self.rect.right = tile_rect.left
                    self.vel[0] = 0


    def update(self):
        self.player_input()
        self.player_y_vel()
        self.player_x_vel()
        self.animation_idle()
        self.animation_walking()
        self.animation_jump()
        self.collisions()

def blitters():
    global tile_rects

    display.fill((0, 255, 255))

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt, (x * tile_size, y * tile_size))
            if tile == '2':
                display.blit(grass, (x * tile_size, y * tile_size))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            x += 1

        y += 1

    player.draw(display)
    player.update()

    surf = pygame.transform.scale(display, (screen_size))
    screen.blit(surf, (0, 0))


pygame.init()

screen_size = (1000, 750)
screen = pygame.display.set_mode((screen_size))

display_size = (screen_size[0] / 3.125, screen_size[1] / 3.125)
display = pygame.Surface((display_size))

pygame.display.set_caption('Platformer')

clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())

grass = pygame.image.load("Platformer/Images/grass.png").convert_alpha()
dirt = pygame.image.load("Platformer/Images/dirt.png").convert_alpha()
tile_size = grass.get_width()

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2'],
            ['1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Render everything
    blitters()

    # Update display
    pygame.display.update()
    clock.tick(60)