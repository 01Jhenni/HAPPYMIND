import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 1100, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bem-vindo ao HappyMind")

home_background = pygame.image.load("background.gif")
home_background = pygame.transform.scale(home_background, (screen_width, screen_height))

game1_background = pygame.image.load("jogo1.gif")
game1_background = pygame.transform.scale(game1_background, (screen_width, screen_height))

game2_background = pygame.image.load("jogo2.gif")
game2_background = pygame.transform.scale(game2_background, (screen_width, screen_height))

game3_background = pygame.image.load("jogo3.gif")
game3_background = pygame.transform.scale(game3_background, (screen_width, screen_height))

pygame.mixer.music.load("puzzle-game-bright-casual-video-game-music-249202.mp3")
pygame.mixer.music.play(-1)

WHITE = (255,255,255)
BLACK = (0,0,33)

font_large = pygame.font.Font("C:\\Users\\SUPORTE\\Downloads\\eight-bit-dragon-font\\EightBitDragon-anqx.ttf", 74)
font_small = pygame.font.Font("C:\\Users\\SUPORTE\\Downloads\\eight-bit-dragon-font\\EightBitDragon-anqx.ttf", 36)

welcome_text = font_large.render("Bem-vindo ao HappyMind", True, WHITE)
name_prompt = font_small.render("Informe seu nome:", True, WHITE)
input_box = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)
button_box = pygame.Rect(screen_width // 2 - 125, screen_height // 2 + 100, 250, 60)

user_text = ""
active_input = False
current_screen = "home"
character_selected = None

male_image = pygame.image.load("per.png")
female_image = pygame.image.load("pers.png")
male_image = pygame.transform.scale(male_image, (150, 150))
female_image = pygame.transform.scale(female_image, (150, 150))

game1_img = pygame.image.load("numero.jpg").convert_alpha()
game1_img = pygame.transform.scale(game1_img, (200, 200))
game2_img = pygame.image.load("cores.jpg").convert_alpha()
game2_img = pygame.transform.scale(game2_img, (200, 200))
game3_img = pygame.image.load("som.jpg").convert_alpha()
game3_img = pygame.transform.scale(game3_img, (200, 200))

game1_rect = game1_img.get_rect(center=(screen_width // 4, screen_height // 2))
game2_rect = game2_img.get_rect(center=(screen_width // 2, screen_height // 2))
game3_rect = game3_img.get_rect(center=(3 * screen_width // 4, screen_height // 2))

trophy_img = pygame.image.load("trofeu (2).png").convert_alpha()
victory_sound = pygame.mixer.Sound("puzzle-game-bright-casual-video-game-music-249202.mp3")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))

    border_rect = text_rect.inflate(10, 10)  
    pygame.draw.rect(surface, BLACK, border_rect) 
    surface.blit(text_obj, text_rect) 


def draw_character(character):
    if character == "Homem":
        screen.blit(male_image, (screen_width // 2 - 200, screen_height // 2 - 100))
    elif character == "Mulher":
        screen.blit(female_image, (screen_width // 2 - 200, screen_height // 2 - 100))

def character_selection_screen():
    global character_selected
    while True:
        screen.fill(BLACK)
        draw_text("Escolha seu Personagem", font_large, WHITE, screen, screen_width // 2, 100)

        male_icon_rect = male_image.get_rect(center=(screen_width // 3, screen_height // 2))
        female_icon_rect = female_image.get_rect(center=(2 * screen_width // 3, screen_height // 2))
        screen.blit(male_image, male_icon_rect)
        screen.blit(female_image, female_icon_rect)

        draw_text("Meliodas", font_small, WHITE, screen, screen_width // 3, screen_height // 2 + 100)
        draw_text("Chichi", font_small, WHITE, screen, 2 * screen_width // 3, screen_height // 2 + 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if male_icon_rect.collidepoint(event.pos):
                    character_selected = "Homem"
                    return  
                elif female_icon_rect.collidepoint(event.pos):
                    character_selected = "Mulher"
                    return  
        pygame.display.flip()


def game_selection_screen():
    screen.fill(BLACK)
    draw_text("Escolha seu Jogo", font_large, WHITE, screen, screen_width // 2, 100)
    screen.blit(game1_img, game1_rect)
    screen.blit(game2_img, game2_rect)
    screen.blit(game3_img, game3_rect)
    pygame.display.flip()

def numbers_game():
    questions = [
        ("Quanto é 2 + 3?", [5, 6, 7], 0),
        ("Quanto é 4 + 6?", [9, 10, 11], 0),
        ("Quanto é 7 + 8?", [13, 14, 15], 0),
    ]
    score = 0
    screen.blit(game1_background, (0, 0)) 
    draw_character(character_selected) 
    for question, options, correct_answer in questions:
        draw_text(question, font_large, WHITE, screen, screen_width // 2, 100)
        for i, option in enumerate(options):
            draw_text(str(option), font_small, WHITE, screen, screen_width // 2, 200 + i * 60)

        pygame.display.flip()

        waiting_for_answer = True
        while waiting_for_answer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if screen_width // 2 - 50 < mouse_pos[0] < screen_width // 2 + 50:
                        if 200 + correct_answer * 60 < mouse_pos[1] < 200 + (correct_answer + 1) * 60:
                            score += 1
                            waiting_for_answer = False

        pygame.time.delay(1000)

    show_victory()


def colors_game():
    questions = [
        ("Qual cor é a primeira?", ["Vermelho", "Azul", "Verde"], 0),
        ("Qual cor é a segunda?", ["Amarelo", "Azul", "Laranja"], 1),
        ("Qual cor é a terceira?", ["Roxo", "Verde", "Branco"], 2),
    ]
    score = 0
    screen.blit(game2_background, (0, 0)) 
    draw_character(character_selected) 
    for question, options, correct_answer in questions:
        draw_text(question, font_large, WHITE, screen, screen_width // 2, 100)
        for i, option in enumerate(options):
            draw_text(option, font_small, WHITE, screen, screen_width // 2, 200 + i * 60)

        pygame.display.flip()

        waiting_for_answer = True
        while waiting_for_answer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if screen_width // 2 - 50 < mouse_pos[0] < screen_width // 2 + 50:
                        if 200 + correct_answer * 60 < mouse_pos[1] < 200 + (correct_answer + 1) * 60:
                            score += 1
                            waiting_for_answer = False

        pygame.time.delay(1000)

    show_victory()

def sounds_game():
    questions = [
        ("Qual som é este?", ["Som 1", "Som 2", "Som 3"], 0),
        ("Qual som é este?", ["Som 2", "Som 3", "Som 1"], 1),
        ("Qual som é este?", ["Som 3", "Som 1", "Som 2"], 2),
    ]
    score = 0
    screen.blit(game3_background, (0, 0)) 
    draw_character(character_selected) 
    for question, options, correct_answer in questions:
        draw_text(question, font_large, WHITE, screen, screen_width // 2, 100)
        for i, option in enumerate(options):
            draw_text(option, font_small, WHITE, screen, screen_width // 2, 200 + i * 60)

        pygame.display.flip()

        waiting_for_answer = True
        while waiting_for_answer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if screen_width // 2 - 50 < mouse_pos[0] < screen_width // 2 + 50:
                        if 200 + correct_answer * 60 < mouse_pos[1] < 200 + (correct_answer + 1) * 60:
                            score += 1
                            waiting_for_answer = False

        pygame.time.delay(1000)

    show_victory()

def show_victory():
    screen.fill(BLACK)
    screen.blit(trophy_img, (screen_width // 2 - 350, screen_height // 2 - 350))
    victory_sound.play()
    draw_text("Você venceu!", font_large, WHITE, screen, screen_width // 2, screen_height // 2 + 100)
    pygame.display.flip()
    pygame.time.delay(3000)

while True:
    if current_screen == "home":
        screen.fill(BLACK)
        screen.blit(home_background, (0, 0)) 
        draw_text("Bem-vindo ao HappyMind", font_large, WHITE, screen, screen_width // 2, 100)
        draw_text("Pressione Enter para começar", font_small, WHITE, screen, screen_width // 2, screen_height // 2 + 150)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current_screen = "character_selection"

    if current_screen == "character_selection":
        character_selection_screen()
        current_screen = "game_selection"

    if current_screen == "game_selection":
        game_selection_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game1_rect.collidepoint(event.pos):
                    numbers_game()
                elif game2_rect.collidepoint(event.pos):
                    colors_game()
                elif game3_rect.collidepoint(event.pos):
                    sounds_game()
