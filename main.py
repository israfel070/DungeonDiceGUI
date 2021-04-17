import random
import pygame
import pygame_menu


screen_width = 320
screen_height = 520
done = False
White = (255, 255, 255)


pygame.init()
pygame.display.set_caption('Dungeon Dice')
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
width = screen.get_width()
height = screen.get_height()
rollsound = pygame.mixer.Sound("roll.mp3")
font = pygame.font.SysFont('Arial', 100, True, False)


def rolld20():
    d20output = random.randint(1, 20)
    rollvalue = str(d20output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


def rolld12():
    d12output = random.randint(1, 12)
    rollvalue = str(d12output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


def rolld10():
    d10output = random.randint(1, 10)
    rollvalue = str(d10output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


def rolld8():
    d8output = random.randint(1, 8)
    rollvalue = str(d8output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


def rolld6():
    d6output = random.randint(1, 6)
    rollvalue = str(d6output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


def rolld4():
    d4output = random.randint(1, 4)
    rollvalue = str(d4output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


def rolld100():
    d100output = random.randint(1, 100)
    rollvalue = str(d100output)
    text = font.render(rollvalue, True, White)
    screen.blit(text, (width - 190, height - 450))
    pygame.mixer.Sound.play(rollsound)
    pygame.display.update()
    pygame.time.wait(2000)


menu = pygame_menu.Menu('Dungeon Dice', screen_width, screen_height,
                        theme=pygame_menu.themes.THEME_DARK, columns=2, rows=4)


menu.add.button('D4', rolld4)
menu.add.button('D6', rolld6)
menu.add.button('D8', rolld8)
menu.add.button('D10', rolld10)
menu.add.button('D12', rolld12)
menu.add.button('D20', rolld20)
menu.add.button('D100', rolld100)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
