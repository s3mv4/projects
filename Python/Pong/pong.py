import pygame, sys, random

def ball_collisions():
    global ball_velocity_y, ball_velocity_x, score1, score2, score_time
    if ball_rect.colliderect(player1_rect) and ball_velocity_x < 0:
        if abs(ball_rect.left - player1_rect.right) < 10:
            ball_velocity_x *= -1
        elif abs(ball_rect.bottom - player1_rect.top) < 10 and ball_velocity_y > 0:
            ball_velocity_y *= -1
        elif abs(ball_rect.top - player1_rect.bottom) < 10 and ball_velocity_y < 0:
            ball_velocity_y *= -1

    if ball_rect.colliderect(player2_rect) and ball_velocity_x > 0:
        if abs(ball_rect.right - player2_rect.left) < 10:
            ball_velocity_x *= -1
        elif abs(ball_rect.bottom - player2_rect.top) < 10 and ball_velocity_y > 0:
            ball_velocity_y *= -1
        elif abs(ball_rect.top - player2_rect.bottom) < 10 and ball_velocity_y < 0:
            ball_velocity_y *= -1

    if ball_rect.top <= 0 or ball_rect.bottom >= 500:
        ball_velocity_y *= -1
    if ball_rect.left <= 0:
        score2 += 1
        score_time = pygame.time.get_ticks()
    if ball_rect.right >= 850:
        score1 += 1
        score_time = pygame.time.get_ticks()

def player_movement():
    if player1_rect.top <= 0:
        player1_rect.top = 0
    if player1_rect.bottom >= 500:
        player1_rect.bottom = 500
    if player2_rect.top <= 0:
        player2_rect.top = 0
    if player2_rect.bottom >= 500:
        player2_rect.bottom = 500

    player1_rect.y += player1_velocity
    player2_rect.y += player2_velocity

def ball_restart():
    global ball_velocity_y, ball_velocity_x, score_time, current_time, ball_resets

    current_time = pygame.time.get_ticks()

    ball_rect.center = (425, 250)

    if current_time - score_time <= 1000:
        three = small_font.render("3", False, (255, 255, 255))
        three_rect = three.get_rect(center = (425, 300))
        pygame.draw.rect(screen, (0,0,0), three_rect)
        screen.blit(three, three_rect)
    if current_time - score_time >= 1000 and current_time - score_time <= 2000:
        two = small_font.render("2", False, (255,255,255))
        two_rect = two.get_rect(center = (425, 300))
        pygame.draw.rect(screen, (0,0,0), two_rect)
        screen.blit(two, two_rect)
    if current_time - score_time >= 2000 and current_time - score_time <= 3000:
        one = small_font.render("1", False, (255,255,255))
        one_rect = one.get_rect(center = (425, 300))
        pygame.draw.rect(screen, (0,0,0), one_rect)
        screen.blit(one, one_rect)


    if current_time - score_time < 3000:
        ball_velocity_x = 0
        ball_velocity_y = 0
        player2_velocity = 0
    else:
        score_time = 0
        ball_resets += 1
        ball_velocity_y = 5 * random.choice((1, -1))
        ball_velocity_x = 5 * random.choice((1, -1))
        player2_velocity = 5




pygame.init()

# Window
screen = pygame.display.set_mode((850,500))
screen.fill((0,0,0))

# Game active
game_active = False
game_active_singleplayer = False
game_active_multiplayer = False

# Framerate
clock = pygame.time.Clock()

# Fonts and text
small_font = pygame.font.Font("Fonts/Minecraft.ttf", 25)
big_font = pygame.font.Font("Fonts/Minecraft.ttf", 150)

title_text = big_font.render("PONG", False, (255, 255, 255))
title_text_rect = title_text.get_rect(center = (425, 250))

singleplayer_text = small_font.render("press 1 for singleplayer", False, (255, 255, 255))
singleplayer_text_rect = singleplayer_text.get_rect(midbottom = (212.5, 475))

multiplayer_text = small_font.render("press 2 for multiplayer", False, (255, 255, 255))
multiplayer_text_rect = multiplayer_text.get_rect(midbottom = (637.5, 475))

quit_text = small_font.render("press Q to quit", False, (255, 255, 255))
quit_text_rect = quit_text.get_rect(midbottom = (425, 475))

# Player 1
player1 = pygame.Surface((15,110))
player1.fill((255,255,255))
player1_rect = player1.get_rect(midleft = (0,250))
player1_velocity = 0

# Player 2
player2 = pygame.Surface((15,110))
player2.fill((255,255,255))
player2_rect = player2.get_rect(midright = (850,250))
player2_velocity = 0

# Ball
ball = pygame.Surface((15,15))
ball.fill((255,255,255))
ball_rect = ball.get_rect(center = (425, 250))
ball_velocity_y = 5
ball_velocity_x = 5
ball_resets = 0

# Score
score1 = 0
score2 = 0
score1_text = small_font.render(f"{score1}", False, (255,255,255))
score1_rect = score1_text.get_rect(midtop = (375, 25))
score2_text = small_font.render(f"{score2}", False, (255,255,255))
score2_rect = score1_text.get_rect(midtop = (475, 25))

# Timer
score_time = 0
current_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and game_active_multiplayer:
                player1_velocity -= 5
            elif event.key == pygame.K_s and game_active_multiplayer:
                player1_velocity += 5
            elif event.key == pygame.K_UP:
                if game_active_multiplayer:
                    player2_velocity -= 5
                else:
                    player1_velocity -=5
            elif event.key == pygame.K_DOWN:
                if game_active_multiplayer:
                    player2_velocity += 5
                else:
                    player1_velocity += 5
            elif event.key == pygame.K_q and game_active:
                game_active_singleplayer = False
                game_active_multiplayer = False
                game_active = False
                score1 = 0
                score2 = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and game_active_multiplayer:
                player1_velocity = 0
            elif event.key == pygame.K_s and game_active_multiplayer:
                player1_velocity = 0
            elif event.key == pygame.K_UP:
                if game_active_multiplayer:
                    player2_velocity = 0
                else:
                    player1_velocity = 0
            elif event.key == pygame.K_DOWN:
                if game_active_multiplayer:
                    player2_velocity = 0
                else:
                    player1_velocity = 0
        if event.type == pygame.KEYDOWN and game_active == False:
            if event.key == pygame.K_1:
                player2_velocity = 5
                player2_rect.midright = (850, 250)
                player1_rect.midleft = (0, 250)
                game_active = True
                game_active_singleplayer = True
                score_time = pygame.time.get_ticks()
            if event.key == pygame.K_2:
                player2_velocity = 0
                player2_rect.midright = (850, 250)
                player1_rect.midleft = (0, 250)
                ball_rect.center = (425, 250)
                game_active = True
                game_active_multiplayer = True
                score_time = pygame.time.get_ticks()
    if game_active:

        if game_active_singleplayer:
            # Blitters
            screen.fill((0,0,0))
            screen.blit(player1, player1_rect)
            screen.blit(player2, player2_rect)
            pygame.draw.aaline(screen, (255,255,255), (425,0), (425,500))
            pygame.draw.rect(screen, (0,0,0), quit_text_rect)
            screen.blit(quit_text, quit_text_rect)
            screen.blit(ball, ball_rect)
            screen.blit(score1_text, score1_rect)
            screen.blit(score2_text, score2_rect)

            if score_time is not 0:
                ball_restart()

            ball_collisions()

            # Ball movement
            ball_rect.y += ball_velocity_y
            ball_rect.x += ball_velocity_x

            player_movement()

            if ball_velocity_y is not 0:
                if player2_rect.bottom <= ball_rect.y:
                    player2_velocity = 8
                if player2_rect.top >= ball_rect.y:
                    player2_velocity = -8
            else:
                player2_velocity = 0

            score1_text = small_font.render(f"{score1}", False, (255,255,255))
            score2_text = small_font.render(f"{score2}", False, (255,255,255))

            if ball_velocity_x <= 10 and ball_velocity_y <= 10:
                if ball_velocity_y >= 0:
                    ball_velocity_y += 0.005
                if ball_velocity_y <= 0:
                    ball_velocity_y += -0.005
                if ball_velocity_x >= 0:
                    ball_velocity_x += 0.005
                if ball_velocity_x <= 0:
                    ball_velocity_x += -0.005

        if game_active_multiplayer:
            # Blitters
            screen.fill((0,0,0))
            screen.blit(player1, player1_rect)
            screen.blit(player2, player2_rect)
            pygame.draw.aaline(screen, (255,255,255), (425,0), (425,500))
            pygame.draw.rect(screen, (0,0,0), quit_text_rect)
            screen.blit(quit_text, quit_text_rect)
            screen.blit(ball, ball_rect)
            screen.blit(score1_text, score1_rect)
            screen.blit(score2_text, score2_rect)

            if score_time is not 0:
                ball_restart()

            ball_collisions()

            # Ball movement
            ball_rect.y += ball_velocity_y
            ball_rect.x += ball_velocity_x

            player_movement()

            score1_text = small_font.render(f"{score1}", False, (255,255,255))
            score2_text = small_font.render(f"{score2}", False, (255,255,255))

            if ball_velocity_y >= 0:
                ball_velocity_y += 0.005
            if ball_velocity_y <= 0:
                ball_velocity_y += -0.005
            if ball_velocity_x >= 0:
                ball_velocity_x += 0.005
            if ball_velocity_x <= 0:
                ball_velocity_x += -0.005
    else:
        screen.fill((0,0,0))
        screen.blit(title_text, title_text_rect)
        screen.blit(singleplayer_text, singleplayer_text_rect)
        screen.blit(multiplayer_text, multiplayer_text_rect)

    pygame.display.update()
    clock.tick(60)
