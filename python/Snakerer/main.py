import pygame
from sys import exit
from random import randint

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

game_active = False

small_font = pygame.font.Font("Fonts/Minecraft.ttf", 50)
medium_font = pygame.font.Font("Fonts/Minecraft.ttf", 50)
big_font = pygame.font.Font("Fonts/Minecraft.ttf", 125)

title_text = big_font.render("SNAKERER", False, (0, 255, 0))
title_text_rect = title_text.get_rect(center = (width/2, height/8*3))

space_text = medium_font.render("press space to start", False, (0, 255, 255))
space_text_rect = space_text.get_rect(center = (width/2, height/8*5))

snake1 = [[80, 0], [60, 0], [40, 0], [20, 0], [0, 0]]

snake2 = [[width-100, height-20], [width-80, height-20], [width-60, height-20], [width-40, height-20], [width-20, height-20]]

respawns = 0

chap_sound = pygame.mixer.Sound("Audio/chap.mp3")

food = []
while food == []:
    food = [randint(0, 39)*20, randint(0, 29)*20]
    if food in snake1 or food in snake2:
        food = []

moving1 = {"left": False, "right": True, "up": False, "down": False}

moving2 = {"left": True, "right": False, "up": False, "down": False}

snakerate = 15

change1 = True
change2 = True

p1_over = False
p2_over = False

winner = ""

def make_surf(color):
    surf = pygame.Surface((20, 20))
    surf.fill(color)
    return surf

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if not game_active:
                if event.key == pygame.K_SPACE:
                    snake1 = [[80, 0], [60, 0], [40, 0], [20, 0], [0, 0]]
                    snake2 = [[width-100, height-20], [width-80, height-20], [width-60, height-20], [width-40, height-20], [width-20, height-20]]
                    respawns = 0
                    food = []
                    while food == []:
                        food = [randint(0, 39)*20, randint(0, 29)*20]
                        if food in snake1 or food in snake2:
                            food = []
                    moving1 = {"left": False, "right": True, "up": False, "down": False}
                    moving2 = {"left": True, "right": False, "up": False, "down": False}
                    snakerate = 15
                    change1 = True
                    change2 = True
                    p1_over = False
                    p2_over = False
                    winner = ""
                    game_active = True
            if change1 and game_active:
                if event.key == pygame.K_DOWN and not moving2["up"] and not moving2["down"]:
                    for key in moving2:
                        moving2[key] = False
                    moving2["down"] = True
                    change1 = False
                if event.key == pygame.K_UP and not moving2["down"] and not moving2["up"]:
                    for key in moving2:
                        moving2[key] = False
                    moving2["up"] = True
                    change1 = False
                if event.key == pygame.K_LEFT and not moving2["right"] and not moving2["left"]:
                    for key in moving2:
                        moving2[key] = False
                    moving2["left"] = True
                    change1 = False
                if event.key == pygame.K_RIGHT and not moving2["left"] and not moving2["right"]:
                    for key in moving2:
                        moving2[key] = False
                    moving2["right"] = True
                    change1 = False
            if change2 and game_active:
                if event.key == pygame.K_s and not moving1["up"] and not moving1["down"]:
                    for key in moving1:
                        moving1[key] = False
                    moving1["down"] = True
                    change2 = False
                if event.key == pygame.K_w and not moving1["down"] and not moving1["up"]:
                    for key in moving1:
                        moving1[key] = False
                    moving1["up"] = True
                    change2 = False
                if event.key == pygame.K_a and not moving1["right"] and not moving1["left"]:
                    for key in moving1:
                        moving1[key] = False
                    moving1["left"] = True
                    change2 = False
                if event.key == pygame.K_d and not moving1["left"] and not moving1["right"]:
                    for key in moving1:
                        moving1[key] = False
                    moving1["right"] = True
                    change2 = False
    if game_active:
        screen.fill((55, 55, 55))
        screen.blit(make_surf((255, 0, 0)), (food[0], food[1]))
        for i, piece in enumerate(snake1):
            screen.blit(make_surf((0, 255, 0)), (piece[0], piece[1]))
        for i, piece in enumerate(snake2):
            screen.blit(make_surf((0, 255, 255)), (piece[0], piece[1]))

        x1 = snake1[0][0]
        y1 = snake1[0][1]
        x2 = snake2[0][0]
        y2 = snake2[0][1]

        if snakerate == 15:
            if moving1["right"]: x1 += 20
            if moving1["left"]: x1 -= 20
            if moving1["up"]: y1 -= 20
            if moving1["down"]: y1 += 20
            temp_pos1 = [x1, y1]
            if moving2["right"]: x2 += 20
            if moving2["left"]: x2 -= 20
            if moving2["up"]: y2 -= 20
            if moving2["down"]: y2 += 20
            temp_pos2 = [x2, y2]
            if x1 < 0 or x1 == width or y1 < 0 or y1 == height or temp_pos1 in snake1[1:] or temp_pos1 in snake2 or temp_pos1 == temp_pos2:
                p1_over = True
            if x2 < 0 or x2 == width or y2 < 0 or y2 == height or temp_pos2 in snake2[1:] or temp_pos2 in snake1 or temp_pos2 == temp_pos1:
                p2_over = True

            if p1_over or p2_over:
                if respawns and p1_over and p2_over:
                    if len(snake1) < len(snake2):
                        winner = "arrows"
                    if len(snake1) > len(snake2):
                        winner = "WASD"
                    if len(snake1) == len(snake2):
                        winner = "tie"
                else:
                    if p1_over and not p2_over:
                        winner = "arrows"
                    if p2_over and not p1_over:
                        winner = "WASD"
                    if p1_over and p2_over:
                        winner = "tie"
                game_active = False
            else:
                if snake1[0] == food:
                    chap_sound.play()
                    snake1.insert(0, [x1, y1])
                    food = []
                    while food == []:
                        food = [randint(0, 39)*20, randint(0, 29)*20]
                        if food in snake1 or food in snake2:
                            food = []
                    respawns += 1
                else:
                    snake1.pop()
                snake1.insert(0, [x1, y1])
                if snake2[0] == food:
                    chap_sound.play()
                    snake2.insert(0, [x2, y2])
                    food = []
                    while food == []:
                        food = [randint(0, 39)*20, randint(0, 29)*20]
                        if food in snake1 or food in snake2:
                            food = []
                    respawns += 1
                else:
                    snake2.pop()
                snake2.insert(0, [x2, y2])
                snakerate = 0
                change1 = True
                change2 = True
        else:
            snakerate += 1
    else:
        screen.fill((55, 55, 55))
        screen.blit(title_text, title_text_rect)
        screen.blit(space_text, space_text_rect)
        if winner != "":
            winner_text = medium_font.render("winner = " + winner, False, (255, 0, 0))
            winner_text_rect = winner_text.get_rect(center = (width/2, height/8*7))
            screen.blit(winner_text, winner_text_rect)
    pygame.display.update()
    clock.tick(120)
