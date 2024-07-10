import random
import pygame
import sys
import os
import time

"""
This script is a Flappy Bird game implemented with Pygame. The game includes features
such as collision detection, dynamic background, and score tracking. 
The player's name is entered at the start, and the score is saved in a file.
"""

print("Session start:", time.strftime("%d/%m/%Y"), "at", time.strftime("%H:%M:%S"))

def game_floor():
    screen.blit(floor_base, (floor_x_pos, 750))
    screen.blit(floor_base, (floor_x_pos + 580, 750))

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            print('Game Over: HIT a pipe!')
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 750:
        die_sound.play()
        print('Game Over: HIT the floor!')
        return False
    return True

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    return (pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300)),
            pipe_surface.get_rect(midtop=(700, random_pipe_pos)))

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface, pipe)
        else:
            screen.blit(pygame.transform.flip(pipe_surface, False, True), pipe)

def enter_name_screen():
    name = ''
    name_font = pygame.font.Font(None, 50)
    name_prompt = name_font.render('Enter your name:', True, (255, 255, 255))
    name_prompt_rect = name_prompt.get_rect(center=(width // 2, height // 2 - 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    return name
        screen.blit(background, (0, 0))
        screen.blit(name_prompt, name_prompt_rect)
        name_surface = name_font.render(name, True, (255, 255, 255))
        name_rect = name_surface.get_rect(center=(width // 2, height // 2 + 50))
        screen.blit(name_surface, name_rect)
        pygame.display.update()
        clock.tick(60)

def game_over():
    screen.blit(game_over_message, game_over_rect)
    score_surface = pygame.font.Font(None, 50).render(f"Final score: {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(width // 2, height // 2 + 200))
    screen.blit(score_surface, score_rect)
    game_floor()
    pygame.display.update()
    pygame.time.delay(1200)

pygame.init()
pygame.display.set_caption('Flappy Bird | 0x414854')
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0
score = 0
width = 580
height = 800
screen = pygame.display.set_mode((width, height))

background = pygame.image.load('./Assets/bg_night_flappy_bird.png').convert()
background = pygame.transform.scale2x(background)

bird = pygame.image.load('./Assets/bird-2.png').convert_alpha()
bird = pygame.transform.scale(bird, (60, 60))
bird_rect = bird.get_rect(center=(100, 400))

name = enter_name_screen()
print(f'Player name: {name}')

floor_base = pygame.image.load('./Assets/floor.png').convert()
floor_base = pygame.transform.scale2x(floor_base)
floor_x_pos = 0

start_message = pygame.image.load('./Assets/start_message.png').convert_alpha()
start_message = pygame.transform.scale(start_message, (int(start_message.get_width() * 1.2), int(start_message.get_height() * 1.2)))
start_message_rect = start_message.get_rect(center=(290, 400))

game_over_message = pygame.image.load('./Assets/game_over_message.png')
game_over_rect = game_over_message.get_rect(center=(290, 400))

pipe_surface = pygame.image.load('./Assets/pipe.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_height = [400, 600, 800]
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1600)

flap_sound = pygame.mixer.Sound('./Assets/Sounds/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('./Assets/Sounds/sfx_hit.wav')
die_sound = pygame.mixer.Sound('./Assets/Sounds/sfx_die.wav')
point_sound = pygame.mixer.Sound('./Assets/Sounds/sfx_point.wav')

game_active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User quit the game.")
            print('Session end:', time.strftime('%d/%m/%Y'), 'at', time.strftime('%H:%M:%S'))
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and not game_active:
                print("User quit the game.")
                print('Session end:', time.strftime('%d/%m/%Y'), 'at', time.strftime('%H:%M:%S'))
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement = -8
                    flap_sound.play()
                else:
                    bird_rect.center = (100, 400)
                    bird_movement = 0
                    pipe_list.clear()
                    score = 0
                    game_active = True
                    print('New game started at', time.strftime('%H:%M:%S'))
            if event.key == pygame.K_ESCAPE and not game_active:
                bird_rect.center = (100, 400)
                bird_movement = 0
                pipe_list.clear()
                score = 0
                game_active = True
                print('New game started at', time.strftime('%H:%M:%S'))
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    screen.blit(background, (0, 0))
    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        for pipe in pipe_list:
            if bird_rect.colliderect(pipe):
                game_active = False
                hit_sound.play()
                print(f'Your final score is : {score}')
                script_dir = os.path.dirname(os.path.abspath(__file__))
                folder_path = os.path.join(script_dir, 'users')
                os.makedirs(folder_path, exist_ok=True)
                file_name = name + '_user.txt'
                file_path = os.path.join(folder_path, file_name)
                
                with open(file_path, 'a') as file:
                    file.write(f'{name}: {score}\n')
                
                print(f"Player score added to the list: {file_name} at", time.strftime('%H:%M:%S'))
                break
            elif bird_rect.top <= -100 or bird_rect.bottom >= height - 50:
                game_active = False
                die_sound.play()
                break
            elif bird_rect.centerx > pipe.centerx and pipe.right > bird_rect.centerx:
                score += 1
                point_sound.play()

        if not check_collision(pipe_list):
            game_over()
            game_active = False

        score_surface = pygame.font.Font(None, 50).render(str(score), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(width // 2, 50))
        screen.blit(score_surface, score_rect)
    else:
        screen.blit(start_message, start_message_rect)

    floor_x_pos -= 1
    game_floor()
    if floor_x_pos <= -580:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
