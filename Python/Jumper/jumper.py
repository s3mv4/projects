import pygame # Importeert de pygame module van python die gebruikt word om games te maken.
from sys import exit # Importeert de exit functie van de sys module die gebruikt word om pygame af te sluiten.
from random import randint # Importeert de randint methode van random die gebruikt word om een willekeurig getal te genereren.

def display_score(): # Maakt een functie aan om de score te laten zien.
    current_time = int(pygame.time.get_ticks() / 1000) - start_time # Zet de current_time variabel naar de tijd hoelang de game aan het runnen is.
    if  game_active == True: # Checkt of de game aan het runnen is en anders laat hij het game over scherm zien.
        score_surf = small_font.render(f"{current_time}", False, (0,0,0)) # Zet de score_surf naar de score die zich op het scherm kan laten zien.
        score_rect = score_surf.get_rect(midtop = (700,25)) # Maakt een rectangle aan voor score_surf.
    if game_active == False: # Checkt of de game niet het runnen is en anders kun je spelen.
        score_surf = small_font.render(f"{current_time}", False, (255,0,0)) # Zet de score_surf naar de score die zich op het scherm kan laten zien.
        score_rect = score_surf.get_rect(midtop = (700,25)) # Maakt een rectangle aan voor score_surf.
    screen.blit(score_surf, score_rect) # Laat de score_surf zien op het scherm.
    return current_time # Maakt van de current_time een globale variabel.

def obstacle_movement(obstacle_list): # Maakt een functie aan om de obstacles te laten zien op het scherm.
    if obstacle_list: # Checkt of er iets in de obstacle_list zit.
        for obstacle_rect in obstacle_list: # Checkt of er een obstakel in obstacle_list zit.
            obstacle_rect.x -= 7 # Beweegt de obstakels naar links.

            if obstacle_rect.bottom == 350: # Checkt of de onderkant van het obstakel 350 is op de y.
                screen.blit(enemy_surf, obstacle_rect) # Zet het obstakel op de grond op het scherm.
            else: # Checkt of de onderkant van het obstakel 350 is op de y en als dat niet zo is dan:
                screen.blit(enemy_surf2, obstacle_rect) # Zet het vliegende obstakel op het scherm.

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] # Checkt of het obstakel van het scherm is en als dat zo is word het obstakel verwijderd.

        return obstacle_list # Maakt van obstacle_list een globale variabel
    else: return [] # Checkt of er iets in de obstacle_list zit en anders maakt hij hem leeg.

def collisions(player,obstacles): # Maakt een functie aan om te zorgen dat de speler doodgaat als hij een obstakel aanraakt.
    if obstacles: # Checkt of er een obstakel bestaat.
        for obstacle_rect in obstacles: # Checkt of een obstakel bestaat.
            if player.colliderect(obstacle_rect): return False # Checkt of de speler een obstakel aanraakt en als dat zo is zet hij de game_active op False.
    return True # Als de speler niet een obstakel aanraakt zet hij de game_active op True.




pygame.init() # Initieert pygame
screen = pygame.display.set_mode((1400,400)) # Maakt het scherm aan.
pygame.display.set_caption("Jumper") # Maakt een titel voor het scherm aan.
clock = pygame.time.Clock() # Maakt een framerate aan.
keys = pygame.key.get_pressed() # Maakt een variabel aan om te kijken of toetsen worden ingedrukt.
score = 0 # Zet de score op 0.
start_time = 0 # Zet de start_time op 0 die later gebruikt word voor de tijd.

large_font = pygame.font.Font("Fonts/Minecraft.ttf", 200) # Maakt een font aan.
small_font = pygame.font.Font("Fonts/Minecraft.ttf", 50) # Maakt een font aan.
smaller_font = pygame.font.Font("Fonts/Minecraft.ttf", 25) # Maakt een font aan.
smallerer_font = pygame.font.Font("Fonts/Minecraft.ttf", 20) # Maakt een font aan.

ground_surf = pygame.Surface((1400, 50)) # Maakt de grond aan.
ground_surf.fill((34,139,34)) # Geeft de grond een kleur.
ground_rect = ground_surf.get_rect(bottomleft = (0, 400)) # Maakt een rectangle aan voor de grond.

sky_surf = pygame.Surface((1400, 350)) # Maakt de lucht aan.
sky_surf.fill((135,206,235)) # Geeft de lucht een kleur.
sky_rect = sky_surf.get_rect(topleft = (0, 0)) # Maakt een rectangle aan voor de lucht.

title_surf = small_font.render("Jumperer", False, (34,139,34)) # Maakt de titel aan voor het spel.
title_rect = title_surf.get_rect(midtop = (700, 25)) # Maakt een rectangle voor de titel voor het spel.

message_surf = small_font.render("press space to start", False, (34,139,34)) # Zet een bericht op het titelscherm
message_rect = message_surf.get_rect(midbottom = (700, 350)) # Geeft het bericht op het titelscherm een rectangle

highscore_surf = smaller_font.render("highscore: 151 by zemmer", False, (34,139,34)) # Zet de highscore op het titelscherm.
highscore_rect = highscore_surf.get_rect(midbottom = (700,400)) # Maakt een rectangle voor de highscore.

player_surf = pygame.image.load("Images/shrek.png").convert_alpha() # Maakt de speler aan.
player_surf = pygame.transform.scale(player_surf,(54, 120)) # Geeft de speler een andere grootte.
player_rect = player_surf.get_rect(bottomleft = (25,350)) # Geeft de speler een rectangle.
player_gravity = 0 # Zet de zwaartekracht op 0.

enemy_surf = pygame.image.load("Images/drollemans.png").convert_alpha() # Maakt het obstakel op de grond aan.
enemy_surf = pygame.transform.scale(enemy_surf, (85.5, 94.5)) # Geeft het obstakel een andere grootte.

enemy_surf2 = pygame.image.load("Images/vliegendedollo.png").convert_alpha() # Maakt het obstakel in de lucht aan.
enemy_surf2 = pygame.transform.scale(enemy_surf2, (117, 58)) # Geeft het obstakel een andere grootte.

obstacle_rect_list = [] # Maakt de obstacle_rect_list leeg.
obstacle_timer = pygame.USEREVENT + 1 # Maakt een evenement aan voor de obstacle_timer.
pygame.time.set_timer(obstacle_timer,1000) # Zet een timer met de obstacle_timer.

def credits(): # Maakt een functie om alle credits te laten zien
    c1_surf = smallerer_font.render("Credits:", False, (34,139,34))
    c1_rect = c1_surf.get_rect(topleft = (25,25))
    c2_surf = smallerer_font.render("Programming: Sem", False, (34,139,34))
    c2_rect = c2_surf.get_rect(topleft = (25,50))
    c3_surf = smallerer_font.render("Pixel art: Renzo, Duco", False, (34,139,34))
    c3_rect = c3_surf.get_rect(topleft = (25,75))
    c4_surf = smallerer_font.render("Top donator: Pierre", False, (34,139,34))
    c4_rect = c4_surf.get_rect(topleft = (25,100))

    screen.blit(c1_surf, c1_rect)
    screen.blit(c2_surf, c2_rect)
    screen.blit(c3_surf, c3_rect)
    screen.blit(c4_surf, c4_rect)

game_active = False # Zet de game_active op False zodat de game niet gelijk begint.

while True: # Maakt een main loop aan.
    for event in pygame.event.get(): # Checkt of er een evenement gebeurd.
        if event.type == pygame.QUIT: # Checkt of er op de X word geklikt om het scherm af te sluiten
            pygame.quit() # Sluit pygame af
            exit() # Sluit het scherm af
        if game_active: # Checkt of je de game aan het spelen bent
            if event.type == pygame.KEYDOWN: # Checkt of er een toets word ingedrukt.
                if event.key == pygame.K_SPACE and player_rect.bottom == 350: # Checkt of de spatie-toets word ingedrukt en als de speler op de grond staat.
                    player_gravity = -25 # Zorgt dat de speler springt.
                elif event.key == pygame.K_UP and player_rect.bottom == 350: # Checkt of het pijltje omhoog word ingedrukt en als de speler op de grond staat.
                    player_gravity = -25 # Zorgt dat de speler springt.

                elif event.key == pygame.K_DOWN: # Checkt op het pijltje omlaag word ingedrukt.
                    player_surf = pygame.image.load("Images/shrekbukke.png").convert_alpha() # Veranderd de foto van de speler naar de buk-foto.
                    player_surf = pygame.transform.scale(player_surf,(54, 66)) # Veranderd de grootte van de foto voor de speler.
                    player_rect = player_surf.get_rect(bottomleft = (25,player_rect.bottom)) # Maakt een ractangle voor de speler aan.
                    player_gravity = 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_surf = pygame.image.load("Images/shrek.png").convert_alpha() # Veranderd de foto van de speler naar de normale foto.
                    player_surf = pygame.transform.scale(player_surf,(54, 120)) # Veranderd de grootte van de foto van de speler.
                    player_rect = player_surf.get_rect(bottomleft = (25,player_rect.bottom)) # Maakt een ractangle voor de speler aan.
        else: # Checkt of je de game aan het spelen bent en anders laat hij het game over scherm zien
            if event.type == pygame.KEYDOWN: # Checkt of er een toets word ingedrukt.
                if event.key == pygame.K_SPACE: # Checkt of de spatie-toets word ingedrukt.
                    player_surf = pygame.image.load("Images/shrek.png").convert_alpha() # Veranderd de foto van de speler naar de normale foto.
                    player_surf = pygame.transform.scale(player_surf,(54, 120)) # Veranderd de grootte van de foto van de speler.
                    player_rect = player_surf.get_rect(bottomleft = (25,player_rect.bottom)) # Maakt een ractangle voor de speler aan.
                    start_time = int(pygame.time.get_ticks() / 1000) # Zet de start_time naar de huidige tijd.
                    game_active = True # Zet de game_active naar True waardoor de game begint.
        if event.type == obstacle_timer and game_active: # Checkt of een obstakel van het scherm af is gegaan en als de game bezig is.
            if randint(0,2): # Genereert een willekeurig nummer tussen 0 en 2, en als het nummer niet nul is:
                obstacle_rect_list.append(enemy_surf.get_rect(bottomright = (randint(1400,1600),350))) # Zet het obstakel op de grond op het scherm
            else: # Als het nummer nul is dan:
                obstacle_rect_list.append(enemy_surf2.get_rect(bottomright = (randint(1400,1600),250))) # Zet het obstakel in de lucht op het scherm

    if game_active: # Als de game aan het runnen is:
        screen.blit(sky_surf, sky_rect) # Zet de lucht op het scherm.
        screen.blit(ground_surf, ground_rect) # Zet de grond op het scherm.
        screen.blit(player_surf, player_rect) # Zet de speler op het scherm.
        score = display_score() # Zet de score variabel naar de display_score() functie.


        player_gravity += 1 # Maakt de zwaartekracht sterker.
        player_rect.y += player_gravity # Veranderd de y van de speler doormiddel van de zwaartekracht.
        if player_rect.bottom >= 350: player_rect.bottom = 350 # Zorgt ervoor dat de speler op de grond kan staan.



        obstacle_rect_list = obstacle_movement(obstacle_rect_list) # zet de obstacle_rect_list lijst naar de obstacle_movement() functie.

        game_active = collisions(player_rect, obstacle_rect_list) # Zorgt dat de game het game over scherm laat zien als de speler een obstakel aanraakt doormiddel van de collisions() functie.

    else: # Als de game niet aan het runnen is dan:
        screen.fill((135,206,235)) # Geeft het scherm een kleur.
        screen.blit(title_surf, title_rect) # Zet de titel op het scherm.
        obstacle_rect_list.clear() # Maakt de obstakel lijst leeg
        player_surf = pygame.image.load("Images/shrektitel.png").convert_alpha() # Laat de titel-foto zien.
        player_surf = pygame.transform.scale(player_surf, (168,192)) # Verandert de grootte van de foto van de titel-foto.
        player_rect = player_surf.get_rect(center = (650, 200)) # Maakt een rectangle aan voor de titel-foto.
        screen.blit(player_surf,player_rect) # Zet de titel-foto op het scherm.
        if score == 0: # Als de game voor het eerst word opgestart and:
            screen.blit(message_surf, message_rect) #  Zet het bericht op het scherm.
        else: # Als de game niet voor het eerst word opgestart dan:
            score_message = small_font.render(f"your score : {score}", False, (34,139,34)) # Laat je eindscore zien op het game over scherm.
            score_message_rect = score_message.get_rect(midbottom = (700, 350)) # Geeft de eindscore een rectangle.
            screen.blit(score_message, score_message_rect) # Zet de eindscore op het scherm.
            screen.blit(highscore_surf, highscore_rect) # Zet de highscore op het scherm.
            credits() # Laat de credits zien

    pygame.display.update() # Updatet de display elke keer dat de loop rondgaat.
    clock.tick(60) # Zet de framerate op 60.
