import os
import sys
import time
from random import randrange
import pygame
from win32api import GetSystemMetrics

FPS = 50

m = 10000000
l = 100000000
f = 1000000000
b = 10000000000


def exit_p():
    global vol
    file = open('DataBase.txt', 'w')
    file.write(str(vol)[:5])
    file.close()
    sys.exit()


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


def final():
    global vol, hod, mo, li, fr, bi, mo1, li1, fr1, bi1
    mo1 = True
    li1 = True
    fr1 = True
    bi1 = True
    hod = 0
    mo = 0
    li = 0
    fr = 0
    bi = 0
    if vol != 0:
        pygame.mixer.music.set_volume(.1)
    else:
        pygame.mixer.music.set_volume(0)
    fon = pygame.transform.scale(load_image('3.jpg'), (W, H))
    running = True
    start_img = pygame.transform.scale(load_image('play_btn.png'), (W * 0.3, H * 0.2))
    exit_img = pygame.transform.scale(load_image('exit_btn.png'), (W * 0.3, H * 0.2))
    settings_img = pygame.transform.scale(load_image('settings_btn.png'), (W * 0.3, H * 0.2))
    while running:
        screen.blit(fon, (0, 0))
        start_button = Button(W // 2 - (W * .2 // 2) - 5, H // 4 - (H * .4 // 2), start_img, 0.8)
        settings_button = Button(W // 2 - (W * .2 // 2) - 2, H // 2.2 - (H * .4 // 2), settings_img, 0.8)
        exit_button = Button(W // 2 - (W * .2 // 2), H // 1.5 - (H * .4 // 2), exit_img, 0.8)
        if start_button.draw(screen):
            btn_sound.play()
            main_disp()
            running = False
        elif settings_button.draw(screen):
            btn_sound.play()
            volume_pl_min_window()
        elif exit_button.draw(screen):
            btn_sound.play()
            time.sleep(.2)
            exit_p()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
        pygame.display.update()

    pygame.mixer.music.set_volume(vol)


def cube():
    global W
    global H
    global screen
    a = 0.4 * W
    x1 = 0.28 * W
    y1 = 0.2 * H
    running = True
    u = 0
    pygame.draw.rect(screen, 'white', ((x1, y1), (a, a)), 0)
    pygame.draw.circle(screen, 'black', (x1 + 0.5 * a, y1 + 0.5 * a), 0.125 * a)
    pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.2 * a), 0.125 * a)
    pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.2 * a), 0.125 * a)
    pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.8 * a), 0.125 * a)
    pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.8 * a), 0.125 * a)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                i1 = event.pos[0]
                i2 = event.pos[1]
                if x1 <= i1 <= x1 + a and y1 <= i2 <= y1 + a:
                    for i in range(15):
                        spin_c_sound.play()
                        u = randrange(1, 7)
                        pygame.draw.rect(screen, 'white', ((x1, y1), (a, a)), 0)
                        if u == 1:
                            pygame.draw.circle(screen, 'black', (x1 + 0.5 * a, y1 + 0.5 * a), 0.125 * a)
                        if u == 2:
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.8 * a), 0.125 * a)
                        if u == 3:
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.8 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.5 * a, y1 + 0.5 * a), 0.125 * a)
                        if u == 4:
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.8 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.8 * a), 0.125 * a)
                        if u == 5:
                            pygame.draw.circle(screen, 'black', (x1 + 0.5 * a, y1 + 0.5 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.8 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.8 * a), 0.125 * a)
                        if u == 6:
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.2 * a, y1 + 0.8 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.8 * a, y1 + 0.8 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.5 * a, y1 + 0.2 * a), 0.125 * a)
                            pygame.draw.circle(screen, 'black', (x1 + 0.5 * a, y1 + 0.8 * a), 0.125 * a)
                        time.sleep(0.2)
                        pygame.display.update()
                    time.sleep(3)
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
                    u = 0
        pygame.display.flip()
    return u


def terminate():
    pygame.quit()
    exit_p()


def start_screen():
    global screen
    global W
    global H
    fon = pygame.transform.scale(load_image('1.jpg'), (W, H))
    screen.blit(fon, (0, 0))
    start_img = pygame.transform.scale(load_image('play_btn.png'), (W * 0.3, H * 0.2))
    exit_img = pygame.transform.scale(load_image('exit_btn.png'), (W * 0.3, H * 0.2))
    settings_img = pygame.transform.scale(load_image('settings_btn.png'), (W * 0.3, H * 0.2))
    run = True
    while run:
        start_button = Button(W // 1.3 - (W * .3 // 2) - 9, H // 3 - (H * .4 // 2), start_img, 1)
        settings_button = Button(W // 1.3 - (W * .3 // 2) - 4, H // 1.7 - (H * .4 // 2), settings_img, 1)
        exit_button = Button(W // 1.3 - (W * .3 // 2), H // 1.2 - (H * .4 // 2), exit_img, 1)
        screen.blit(fon, (0, 0))
        if start_button.draw(screen):
            btn_sound.play()
            main_disp()
            run = False
        elif settings_button.draw(screen):
            btn_sound.play()
            volume_pl_min_window()
        elif exit_button.draw(screen):
            btn_sound.play()
            time.sleep(.2)
            exit_p()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


def volume_pl_min_window():
    global vol
    pygame.mixer.music.set_volume(vol)
    fon = pygame.transform.scale(load_image('4.jpg'), (W, H))
    screen.blit(fon, (0, 0))
    running = True
    plus_img = load_image('plus.png')
    minus_img = load_image('minus.png')
    gr = pygame.transform.scale(load_image('gromkost.png'), (W * 0.43, H * 0.35))
    while running:
        minus_btn = Button(W // 2.5, H // 2, minus_img, .8)
        plus_btn = Button(W // 2, H // 2, plus_img, .8)
        gromkost = Button(W // 1.9 - (W * .43 // 2), H // 2.5 - (H * .35 // 2), gr, .8)
        if gromkost.draw(screen):
            pass
        if minus_btn.draw(screen):
            if vol >= .1:
                vol -= .1
            else:
                vol = 0
            time.sleep(.1)
            pygame.mixer.music.set_volume(vol)
        elif plus_btn.draw(screen):
            if vol <= .9:
                vol += .1
            else:
                vol = 1
            time.sleep(.1)
            pygame.mixer.music.set_volume(vol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
        pygame.display.update()


def menu():
    global vol
    if vol != 0:
        pygame.mixer.music.set_volume(.1)
    else:
        pygame.mixer.music.set_volume(0)
    fon = pygame.transform.scale(load_image('3.jpg'), (W, H))
    running = True
    start_img = pygame.transform.scale(load_image('play_btn.png'), (W * 0.3, H * 0.2))
    exit_img = pygame.transform.scale(load_image('exit_btn.png'), (W * 0.3, H * 0.2))
    settings_img = pygame.transform.scale(load_image('settings_btn.png'), (W * 0.3, H * 0.2))
    while running:
        screen.blit(fon, (0, 0))
        start_button = Button(W // 2 - (W * .2 // 2) - 5, H // 4 - (H * .4 // 2), start_img, 0.8)
        settings_button = Button(W // 2 - (W * .2 // 2) - 2, H // 2.2 - (H * .4 // 2), settings_img, 0.8)
        exit_button = Button(W // 2 - (W * .2 // 2), H // 1.5 - (H * .4 // 2), exit_img, 0.8)
        if start_button.draw(screen):
            btn_sound.play()
            running = False
        elif settings_button.draw(screen):
            btn_sound.play()
            volume_pl_min_window()
        elif exit_button.draw(screen):
            btn_sound.play()
            time.sleep(.2)
            exit_p()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
        pygame.display.update()
    pygame.mixer.music.set_volume(vol)


def deistv(screen1, b, uch):
    global intro_text
    pr1 = load_image('deis.png')
    run = True
    i = intro_text
    while run:
        pr = pygame.transform.scale(pr1, (W * 0.7, H * 0.6))
        screen.blit(dog_surf, dog_rect)
        screen.blit(road1, (0.08 * W, 0.008 * H))
        mouse.draw(screen)
        lion.draw(screen)
        frog.draw(screen)
        bird.draw(screen)
        kub.draw(screen)
        text_coord = 0.083 * H
        font = pygame.font.Font(None, int(0.02 * W))
        for line in i:
            string_rendered = font.render(line, True, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 0.009 * W
            intro_rect.top = text_coord
            intro_rect.x = 0.25 * W
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        screen1.blit(pr, (0.13 * W, 0.15 * H))
        pygame.draw.circle(screen1, 'black', (0.76 * W, 0.21 * H), 15)
        pygame.draw.circle(screen1, 'white', (0.76 * W, 0.21 * H), 15, 2)
        pygame.draw.line(screen1, 'white', (0.755 * W, 0.20 * H), (0.7645 * W, 0.22 * H), width=1)
        pygame.draw.line(screen1, 'white', (0.755 * W, 0.22 * H), (0.7645 * W, 0.20 * H), width=1)
        if b == 7:
            if uch == 0:
                w = 'Мышки'
            elif uch == 1:
                w = 'Льва'
            elif uch == 2:
                w = 'Лягушки'
            elif uch == 3:
                w = 'Птички'
            else:
                w = 'Error'
            intro_text = [f'Игрок с фишкой {w}, Вы попали',
                          f'на клетку с заданием.',
                          f'Сделайте по комплименту каждому игроку!']
            text_coord = 0.35 * H
            font = pygame.font.Font(None, int(0.03 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.23 * W
                text_coord += intro_rect.height
                screen1.blit(string_rendered, intro_rect)
        elif b == 13:
            if uch == 0:
                w = 'Мышки'
            elif uch == 1:
                w = 'Льва'
            elif uch == 2:
                w = 'Лягушки'
            elif uch == 3:
                w = 'Птички'
            else:
                w = 'Error'
            intro_text = [f'Игрок с фишкой {w}, Вы попали',
                          f'на клетку с заданием.',
                          f'Спойте детскую песенку, которую ',
                          f'выберут остальные!']
            text_coord = 0.35 * H
            font = pygame.font.Font(None, int(0.03 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.23 * W
                text_coord += intro_rect.height
                screen1.blit(string_rendered, intro_rect)
        elif b == 29:
            if uch == 0:
                w = 'Мышки'
            elif uch == 1:
                w = 'Льва'
            elif uch == 2:
                w = 'Лягушки'
            elif uch == 3:
                w = 'Птички'
            else:
                w = 'Error'
            intro_text = [f'Игрок с фишкой {w}, Вы попали',
                          f'на клетку с заданием.',
                          f'Опишите одного из игроков, ',
                          f'а другие пусть угадают,',
                          f'кого Вы загадали!']
            text_coord = 0.35 * H
            font = pygame.font.Font(None, int(0.03 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.23 * W
                text_coord += intro_rect.height
                screen1.blit(string_rendered, intro_rect)
        elif b == 18:
            if uch == 0:
                w = 'Мышки'
            elif uch == 1:
                w = 'Льва'
            elif uch == 2:
                w = 'Лягушки'
            elif uch == 3:
                w = 'Птички'
            else:
                w = 'Error'
            intro_text = [f'Игрок с фишкой {w}, Вы попали',
                          f'на клетку с заданием.',
                          f'Говорите с одним игроком, ',
                          f'а смотрите на другого!']
            text_coord = 0.35 * H
            font = pygame.font.Font(None, int(0.03 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.23 * W
                text_coord += intro_rect.height
                screen1.blit(string_rendered, intro_rect)
        elif b == 24:
            if uch == 0:
                w = 'Мышки'
            elif uch == 1:
                w = 'Льва'
            elif uch == 2:
                w = 'Лягушки'
            elif uch == 3:
                w = 'Птички'
            else:
                w = 'Error'
            intro_text = [f'Игрок с фишкой {w}, Вы попали',
                          f'на клетку с заданием.',
                          f'Нарисуйте игрока слева от Вас, ',
                          f'держа карандаш левой рукой!']
            text_coord = 0.35 * H
            font = pygame.font.Font(None, int(0.03 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.23 * W
                text_coord += intro_rect.height
                screen1.blit(string_rendered, intro_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                i1 = event.pos[0]
                i2 = event.pos[1]
                if 0.755 * W <= i1 <= 0.7645 * W and 0.20 * H <= i2 <= 0.22 * H:
                    run = False


def winner(player):
    global winners
    if player not in winners:
        winners.append(player)
    if len(winners) == 3:
        if 'птица' not in winners:
            winners.append('птица')
        elif 'лев' not in winners:
            winners.append('лев')
        elif 'мышь' not in winners:
            winners.append('мышь')
        elif 'лягушка' not in winners:
            winners.append('лягушка')
        intro_text = [f'Первое место - {winners[0]}',
                      f'Второе место - {winners[1]}',
                      f'Третье место - {winners[2]}',
                      f'Четвёртое место - {winners[3]}']
        text_coord = 0.35 * H
        font = pygame.font.Font(None, int(0.03 * W))
        pr1 = load_image('deis.png')
        pr = pygame.transform.scale(pr1, (W * 0.7, H * 0.6))
        screen.blit(dog_surf, dog_rect)
        screen.blit(road1, (0.08 * W, 0.008 * H))
        mouse.draw(screen)
        lion.draw(screen)
        frog.draw(screen)
        bird.draw(screen)
        kub.draw(screen)
        screen.blit(pr, (0.13 * W, 0.15 * H))
        for line in intro_text:
            string_rendered = font.render(line, True, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 0.009 * W
            intro_rect.top = text_coord
            intro_rect.x = 0.23 * W
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        pygame.display.update()
        time.sleep(3)
        final()


def update(hodit, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird, centr):
    global mo, li, fr, bi, fi, first, second, third, fourth, mo1, li1, fr1, bi1, n
    n = '0'
    try:
        if hodit == 0:
            if mo <= 32:
                e = centr[mo][0]
                r = centr[mo][1]
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                mouse.draw(screen)
            else:
                e = 10000000
                r = 10000000
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                mouse.draw(screen)
                mo += 3
                mo1 = False
                fi += 1
                if fi == 1:
                    first = 'мышь'
                elif fi == 2:
                    second = 'мышь'
                elif fi == 3:
                    third = 'мышь'
                elif fi == 4:
                    fourth = 'мышь'
                winner('мышь')
            if pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite1):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite2):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite3):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
        elif hodit == 1:
            if li <= 32:
                e = centr[li][0]
                r = centr[li][1]
            else:
                li += 4
                li1 = False
                e = 100000000
                r = 100000000
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                lion.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'лев'
                elif fi == 2:
                    second = 'лев'
                elif fi == 3:
                    third = 'лев'
                elif fi == 4:
                    fourth = 'лев'
                winner('мышь')
            sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            lion.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite2):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite3):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
        elif hodit == 2:
            if fr <= 32:
                e = centr[fr][0]
                r = centr[fr][1]
            else:
                fr += 5
                fr1 = False
                e = 1000000000
                r = 1000000000
                sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                frog.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'лягушка'
                elif fi == 2:
                    second = 'лягушка'
                elif fi == 3:
                    third = 'лягушка'
                elif fi == 4:
                    fourth = 'лягушка'
                winner('лягушка')
            sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            frog.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite1):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite3):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
        elif hodit == 3:
            if bi <= 32:
                e = centr[bi][0]
                r = centr[bi][1]
            else:
                bi += 6
                bi1 = False
                e = 1500000
                r = 1500000
                sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                bird.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'птица'
                elif fi == 2:
                    second = 'птица'
                elif fi == 3:
                    third = 'птица'
                elif fi == 4:
                    fourth = 'птица'
                winner('птица')
            sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            bird.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite1):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite2):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
        if hodit == 0:
            if mo <= 32:
                e = centr[mo][0]
                r = centr[mo][1]
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                mouse.draw(screen)
            else:
                mo += 3
                mo1 = False
                e = 10000000
                r = 10000000
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                mouse.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'мышь'
                elif fi == 2:
                    second = 'мышь'
                elif fi == 3:
                    third = 'мышь'
                elif fi == 4:
                    fourth = 'мышь'
                winner('мышь')
            if pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite1):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite2):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite3):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
        elif hodit == 1:
            if li <= 32:
                e = centr[li][0]
                r = centr[li][1]
            else:
                li += 4
                li1 = False
                e = 100000000
                r = 100000000
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                lion.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'лев'
                elif fi == 2:
                    second = 'лев'
                elif fi == 3:
                    third = 'лев'
                elif fi == 4:
                    fourth = 'лев'
                winner('мышь')
            sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            lion.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite2):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite3):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
        elif hodit == 2:
            if fr <= 32:
                e = centr[fr][0]
                r = centr[fr][1]
            else:
                fr += 5
                fr1 = False
                e = 1000000000
                r = 1000000000
                sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                frog.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'лягушка'
                elif fi == 2:
                    second = 'лягушка'
                elif fi == 3:
                    third = 'лягушка'
                elif fi == 4:
                    fourth = 'лягушка'
                winner('лягушка')
            sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            frog.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite1):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite3):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
        elif hodit == 3:
            if bi <= 32:
                e = centr[bi][0]
                r = centr[bi][1]
            else:
                bi += 6
                bi1 = False
                e = 1500000
                r = 1500000
                sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                bird.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'птица'
                elif fi == 2:
                    second = 'птица'
                elif fi == 3:
                    third = 'птица'
                elif fi == 4:
                    fourth = 'птица'
                winner('птица')
            sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            bird.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite1):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite2):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
        if hodit == 0:
            if mo <= 32:
                e = centr[mo][0]
                r = centr[mo][1]
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                mouse.draw(screen)
            else:
                mo += 3
                mo1 = False
                e = 10000000
                r = 10000000
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                mouse.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'мышь'
                elif fi == 2:
                    second = 'мышь'
                elif fi == 3:
                    third = 'мышь'
                elif fi == 4:
                    fourth = 'мышь'
                winner('мышь')
            if pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite1):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite2):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite, sprite3):
                n = 'sprite'
                if mo < 32:
                    e = centr[mo + 1][0]
                    r = centr[mo + 1][1]
                    mo += 1
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                else:
                    mo += 3
                    mo1 = False
                    e = 10000000
                    r = 10000000
                    sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    mouse.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'мышь'
                    elif fi == 2:
                        second = 'мышь'
                    elif fi == 3:
                        third = 'мышь'
                    elif fi == 4:
                        fourth = 'мышь'
                    winner('мышь')
        elif hodit == 1:
            if li <= 32:
                e = centr[li][0]
                r = centr[li][1]
            else:
                li += 4
                li1 = False
                e = 100000000
                r = 100000000
                sprite.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                lion.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'лев'
                elif fi == 2:
                    second = 'лев'
                elif fi == 3:
                    third = 'лев'
                elif fi == 4:
                    fourth = 'лев'
                winner('мышь')
            sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            lion.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite2):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite1, sprite3):
                n = 'sprite1'
                if li < 32:
                    e = centr[li + 1][0]
                    r = centr[li + 1][1]
                    li += 1
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                else:
                    li += 4
                    li1 = False
                    e = 100000000
                    r = 100000000
                    sprite1.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    lion.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лев'
                    elif fi == 2:
                        second = 'лев'
                    elif fi == 3:
                        third = 'лев'
                    elif fi == 4:
                        fourth = 'лев'
                    winner('лев')
        elif hodit == 2:
            if fr <= 32:
                e = centr[fr][0]
                r = centr[fr][1]
            else:
                fr += 5
                fr1 = False
                e = 1000000000
                r = 1000000000
                sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                frog.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'лягушка'
                elif fi == 2:
                    second = 'лягушка'
                elif fi == 3:
                    third = 'лягушка'
                elif fi == 4:
                    fourth = 'лягушка'
                winner('лягушка')
            sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            frog.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite1):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite2, sprite3):
                n = 'sprite2'
                if fr < 32:
                    e = centr[fr + 1][0]
                    r = centr[fr + 1][1]
                    fr += 1
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                else:
                    fr += 5
                    fr1 = False
                    e = 1000000000
                    r = 1000000000
                    sprite2.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    frog.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'лягушка'
                    elif fi == 2:
                        second = 'лягушка'
                    elif fi == 3:
                        third = 'лягушка'
                    elif fi == 4:
                        fourth = 'лягушка'
                    winner('лягушка')
        elif hodit == 3:
            if bi <= 32:
                e = centr[bi][0]
                r = centr[bi][1]
            else:
                bi += 6
                bi1 = False
                e = 1500000
                r = 1500000
                sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                bird.draw(screen)
                fi += 1
                if fi == 1:
                    first = 'птица'
                elif fi == 2:
                    second = 'птица'
                elif fi == 3:
                    third = 'птица'
                elif fi == 4:
                    fourth = 'птица'
                winner('птица')
            sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
            bird.draw(screen)
            if pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite1):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite2):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
            elif pygame.sprite.collide_rect_ratio(0.5)(sprite3, sprite):
                n = 'sprite3'
                if bi < 32:
                    e = centr[bi + 1][0]
                    r = centr[bi + 1][1]
                    bi += 1
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                else:
                    bi += 6
                    bi1 = False
                    e = 1500000
                    r = 1500000
                    sprite3.rect = pygame.Rect(int(e - 0.04 * W), int(r - 0.143 * H), int(0.075 * W), int(0.134 * H))
                    bird.draw(screen)
                    fi += 1
                    if fi == 1:
                        first = 'птица'
                    elif fi == 2:
                        second = 'птица'
                    elif fi == 3:
                        third = 'птица'
                    elif fi == 4:
                        fourth = 'птица'
                    winner('птица')
    except IndexError:
        mo += 1
        li += 1
        fr += 1
        bi += 1
        if li >= 33:
            winner('лев')
            sprite1.remove()
        if mo >= 33:
            winner('мышь')
            sprite.remove()
        if bi >= 33:
            winner('птица')
            sprite3.remove()
        if fr >= 33:
            winner('лягушка')
            sprite2.remove()
    pygame.display.update()
    return n


def motion(u, hodit, i1, i2, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird, dog_surf,
           dog_rect, road1, centr, kub):
    x2 = i1
    y2 = i2
    x3 = i1
    y3 = i1
    m = False
    drawing = True
    running = True
    w = 'Мышки'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_p()
            if event.type == pygame.MOUSEBUTTONUP:
                screen.blit(dog_surf, dog_rect)
                screen.blit(road1, (0.08 * W, 0.008 * H))
                mouse.draw(screen)
                lion.draw(screen)
                frog.draw(screen)
                bird.draw(screen)
                kub.draw(screen)
                if u == 1:
                    intro_text = [f"Игрок с фишкой {w}, переместите ",
                                  f"Вашу фишку на {u} клетку вперёд!"]
                elif u == 2 or u == 3 or u == 4:
                    intro_text = [f"Игрок с фишкой {w}, переместите ",
                                  f"Вашу фишку на {u} клетки вперёд!"]
                elif u == 5 or u == 6:
                    intro_text = [f"Игрок с фишкой {w}, переместите ",
                                  f"Вашу фишку на {u} клеток вперёд!"]
                elif u == 0:
                    intro_text = ['Подкиньте кубик ещё раз']
                else:
                    intro_text = ['Ошибка, перезапустите игру']
                text_coord = 0.083 * H
                font = pygame.font.Font(None, int(0.02 * W))
                for line in intro_text:
                    string_rendered = font.render(line, True, pygame.Color('black'))
                    intro_rect = string_rendered.get_rect()
                    text_coord += 0.009 * W
                    intro_rect.top = text_coord
                    intro_rect.x = 0.25 * W
                    text_coord += intro_rect.height
                    screen.blit(string_rendered, intro_rect)
                p = update(hodit, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird, centr)
                return p
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    m = True
                    x3, y3 = event.pos[0], event.pos[1]
        if drawing:
            if m:
                w = x3 - x2
                h = y3 - y2
                y2 = y3
                x2 = x3
                if hodit == 0:
                    sprite.rect = sprite.rect.move(w, h)
                    screen.blit(dog_surf, dog_rect)
                    screen.blit(road1, (0.08 * W, 0.008 * H))
                    mouse.draw(screen)
                    lion.draw(screen)
                    frog.draw(screen)
                    bird.draw(screen)
                    kub.draw(screen)
                    w = 'Мышки'
                elif hodit == 1:
                    sprite1.rect = sprite1.rect.move(w, h)
                    screen.blit(dog_surf, dog_rect)
                    screen.blit(road1, (0.08 * W, 0.008 * H))
                    mouse.draw(screen)
                    lion.draw(screen)
                    frog.draw(screen)
                    bird.draw(screen)
                    w = 'Льва'
                    kub.draw(screen)
                elif hodit == 2:
                    sprite2.rect = sprite2.rect.move(w, h)
                    screen.blit(dog_surf, dog_rect)
                    screen.blit(road1, (0.08 * W, 0.008 * H))
                    mouse.draw(screen)
                    lion.draw(screen)
                    frog.draw(screen)
                    bird.draw(screen)
                    w = 'Лягушки'
                    kub.draw(screen)
                elif hodit == 3:
                    sprite3.rect = sprite3.rect.move(w, h)
                    screen.blit(dog_surf, dog_rect)
                    screen.blit(road1, (0.08 * W, 0.008 * H))
                    mouse.draw(screen)
                    lion.draw(screen)
                    frog.draw(screen)
                    bird.draw(screen)
                    w = 'Птички'
                    kub.draw(screen)
                if u == 1:
                    intro_text = [f"Игрок с фишкой {w}, переместите ",
                                  f"Вашу фишку на {u} клетку вперёд!"]
                elif u == 2 or u == 3 or u == 4:
                    intro_text = [f"Игрок с фишкой {w}, переместите ",
                                  f"Вашу фишку на {u} клетки вперёд!"]
                elif u == 5 or u == 6:
                    intro_text = [f"Игрок с фишкой {w}, переместите ",
                                  f"Вашу фишку на {u} клеток вперёд!"]
                elif u == 0:
                    intro_text = ['Подкиньте кубик ещё раз']
                else:
                    intro_text = ['Ошибка, перезапустите игру']
                text_coord = 0.083 * H
                font = pygame.font.Font(None, int(0.02 * W))
                for line in intro_text:
                    string_rendered = font.render(line, True, pygame.Color('black'))
                    intro_rect = string_rendered.get_rect()
                    text_coord += 0.009 * W
                    intro_rect.top = text_coord
                    intro_rect.x = 0.25 * W
                    text_coord += intro_rect.height
                    screen.blit(string_rendered, intro_rect)
                pygame.display.update()


def main_disp():
    global mo, li, fr, bi, hod, vol, hodit, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird, centr, kub
    global dog_surf, dog_rect, road1, intro_text
    centr = [(0.13 * W, 0.24 * H), (0.13 * W, 0.33 * H), (0.13 * W, 0.42 * H), (0.13 * W, 0.51 * H),
             (0.13 * W, 0.6 * H), (0.13 * W, 0.68 * H),
             (0.2 * W, 0.68 * H), (0.27 * W, 0.68 * H),
             (0.27 * W, 0.6 * H), (0.27 * W, 0.51 * H), (0.27 * W, 0.42 * H), (0.34 * W, 0.42 * H),
             (0.41 * W, 0.42 * H),
             (0.48 * W, 0.42 * H), (0.48 * W, 0.51 * H), (0.55 * W, 0.51 * H),
             (0.62 * W, 0.51 * H), (0.62 * W, 0.42 * H), (0.62 * W, 0.33 * H), (0.62 * W, 0.24 * H),
             (0.62 * W, 0.15 * H),
             (0.69 * W, 0.15 * H), (0.76 * W, 0.15 * H), (0.82 * W, 0.15 * H),
             (0.82 * W, 0.24 * H), (0.82 * W, 0.33 * H), (0.82 * W, 0.42 * H), (0.82 * W, 0.51 * H),
             (0.82 * W, 0.6 * H),
             (0.82 * W, 0.68 * H), (0.76 * W, 0.68 * H), (0.69 * W, 0.68 * H), (0.62 * W, 0.68 * H)]
    dog_surf = pygame.transform.scale(load_image('2.jpg'), (W, H))
    dog_surf = pygame.transform.scale(dog_surf, (W, H))
    dog_rect = dog_surf.get_rect(
        bottomright=(W, H))
    road = load_image("road.png")
    road1 = pygame.transform.scale(road, (W, 0.65 * H))
    ##########################
    mouse = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image1 = load_image("mouse.png")
    sprite.image = pygame.transform.scale(sprite.image1, (0.075 * W, 0.134 * H))
    sprite.rect = sprite.image.get_rect()
    mouse.add(sprite)
    sprite.rect.x = 0.025 * W
    sprite.rect.y = 0.10 * H
    ##########################
    lion = pygame.sprite.Group()
    sprite1 = pygame.sprite.Sprite()
    sprite1.image1 = load_image("lion.png")
    sprite1.image = pygame.transform.scale(sprite1.image1, (0.0625 * W, 0.11 * H))
    sprite1.rect = sprite1.image.get_rect()
    lion.add(sprite1)
    sprite1.rect.x = 0.07 * W
    sprite1.rect.y = 0.11 * H
    ##########################
    frog = pygame.sprite.Group()
    sprite2 = pygame.sprite.Sprite()
    sprite2.image1 = load_image("frog.png")
    sprite2.image = pygame.transform.scale(sprite2.image1, (0.054 * W, 0.097 * H))
    sprite2.rect = sprite2.image.get_rect()
    sprite2.rect.x = 0.115 * W
    sprite2.rect.y = 0.115 * H
    frog.add(sprite2)
    ##########################
    bird = pygame.sprite.Group()
    sprite3 = pygame.sprite.Sprite()
    sprite3.image1 = load_image("bird.png")
    sprite3.image = pygame.transform.scale(sprite3.image1, (0.067 * W, 0.12 * H))
    sprite3.rect = sprite3.image.get_rect()
    bird.add(sprite3)
    sprite3.rect.x = 0.154 * W
    sprite3.rect.y = 0.105 * H
    ##########################
    kub = pygame.sprite.Group()
    sprite4 = pygame.sprite.Sprite()
    sprite4.image1 = load_image("cube_btn.png")
    sprite4.image = pygame.transform.scale(sprite4.image1, (0.16 * W, 0.15 * H))
    sprite4.rect = sprite4.image.get_rect()
    kub.add(sprite4)
    sprite4.rect.x = 0.85 * W
    sprite4.rect.y = 0.27 * H
    ##########################
    running = True
    k = True
    hod = 0
    u = 0
    g = False
    r = False
    e = '0'
    j = '0'
    zadan = [7, 13, 18, 24, 29]
    pygame.mixer.music.set_volume(vol)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_p()
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    menu()
                elif event.key == pygame.K_UP:
                    if vol <= .9:
                        vol += .1
                    else:
                        vol = 1
                    pygame.mixer.music.set_volume(vol)
                elif event.key == pygame.K_DOWN:
                    if vol >= .1:
                        vol -= .1
                    else:
                        vol = 0
                    pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                i1 = event.pos[0]
                i2 = event.pos[1]
                if sprite4.rect.collidepoint(i1, i2):
                    u = cube()
                    k = False
                    g = True
                    r = False
                elif sprite.rect.collidepoint(i1, i2):
                    if hod == 0:
                        if u != 0:
                            mo += u
                            e = motion(u, hod, i1, i2, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird,
                                       dog_surf, dog_rect, road1, centr, kub)
                            if mo in zadan:
                                deistv(screen, mo, 0)
                            if li1:
                                hod = 1
                            else:
                                if fr1:
                                    hod = 2
                                else:
                                    hod = 3
                            g = False
                            r = True
                            u = 0
                elif sprite1.rect.collidepoint(i1, i2):
                    if hod == 1:
                        if u != 0:
                            li += u
                            e = motion(u, hod, i1, i2, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird,
                                       dog_surf, dog_rect, road1, centr, kub)
                            if li in zadan:
                                deistv(screen, li, 1)
                            g = False
                            r = True
                            if fr1:
                                hod = 2
                            else:
                                if bi1:
                                    hod = 3
                                else:
                                    hod = 0
                            u = 0
                elif sprite2.rect.collidepoint(i1, i2):
                    if hod == 2:
                        if u != 0:
                            fr += u
                            e = motion(u, hod, i1, i2, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird,
                                       dog_surf, dog_rect, road1, centr, kub)
                            if fr in zadan:
                                deistv(screen, fr, 2)
                            g = False
                            r = True
                            if bi1:
                                hod = 3
                            else:
                                if mo1:
                                    hod = 0
                                else:
                                    hod = 1
                            u = 0
                elif sprite3.rect.collidepoint(i1, i2):
                    if hod == 3:
                        if u != 0:
                            bi += u
                            e = motion(u, hod, i1, i2, sprite, mouse, sprite1, lion, sprite2, frog, sprite3, bird,
                                       dog_surf, dog_rect, road1, centr, kub)
                            if bi in zadan:
                                deistv(screen, bi, 3)
                            g = False
                            r = True
                            if mo1:
                                hod = 0
                            else:
                                if li1:
                                    hod = 1
                                else:
                                    hod = 2
                            u = 0
        screen.blit(dog_surf, dog_rect)
        screen.blit(road1, (0.08 * W, 0.008 * H))
        mouse.draw(screen)
        lion.draw(screen)
        frog.draw(screen)
        bird.draw(screen)
        kub.draw(screen)
        if k:
            intro_text = ["Приветствуем вас в игре Foki.",
                          "Игрок с фишкой Мышки, Ваш ход!",
                          "Вы можете сделать ход, подбросив кубик."]
            text_coord = 0.083 * H
            font = pygame.font.Font(None, int(0.02 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.25 * W
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        if g:
            if hod == 0:
                w = 'Мышки'
            elif hod == 1:
                w = 'Льва'
            elif hod == 2:
                w = 'Лягушки'
            elif hod == 3:
                w = 'Птички'
            else:
                w = 'Error'
            if u == 1:
                intro_text = [f"Игрок с фишкой {w}, переместите ",
                              f"Вашу фишку на {u} клетку вперёд!"]
            elif u == 2 or u == 3 or u == 4:
                intro_text = [f"Игрок с фишкой {w}, переместите ",
                              f"Вашу фишку на {u} клетки вперёд!"]
            elif u == 5 or u == 6:
                intro_text = [f"Игрок с фишкой {w}, переместите ",
                              f"Вашу фишку на {u} клеток вперёд!"]
            elif u == 0:
                intro_text = ['Подкиньте кубик ещё раз']
            else:
                intro_text = ['Ошибка, перезапустите игру']
            text_coord = 0.083 * H
            font = pygame.font.Font(None, int(0.02 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.25 * W
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        if r:
            if hod == 0:
                w = 'Мышки'
            elif hod == 1:
                w = 'Льва'
            elif hod == 2:
                w = 'Лягушки'
            elif hod == 3:
                w = 'Птички'
            else:
                w = 'Error'
            if e == '0':
                intro_text = [f"Игрок с фишкой {w}, Ваш ход!",
                              f"Вы можете сделать ход, подбросив кубик."]
            else:
                if e == 'sprite':
                    j = 'Мышки'
                elif e == 'sprite1':
                    j = 'Льва'
                elif e == 'sprite2':
                    j = 'Лягушки'
                elif e == 'sprite3':
                    j = 'Птички'
                intro_text = [f'Игрок с фишкой {j}, Вам повезло,',
                              f'и Вы перемещены вперёд!',
                              f"Игрок с фишкой {w}, Ваш ход!",
                              f"Вы можете сделать ход, подбросив кубик."]
            text_coord = 0.083 * H
            font = pygame.font.Font(None, int(0.02 * W))
            for line in intro_text:
                string_rendered = font.render(line, True, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 0.009 * W
                intro_rect.top = text_coord
                intro_rect.x = 0.25 * W
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit_p()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    f = open('DataBase.txt', 'r')
    vol = float(f.read())
    winners = []
    pygame.init()
    pygame.mixer.music.load('sounds/fond.mp3')
    pygame.mixer.music.play(-1)
    if vol != 0:
        pygame.mixer.music.set_volume(.1)
    else:
        pygame.mixer.music.set_volume(0)
    btn_sound = pygame.mixer.Sound('sounds/press_btn.wav')
    spin_c_sound = pygame.mixer.Sound('sounds/spin_cube.wav')
    W = GetSystemMetrics(0)
    H = GetSystemMetrics(1)
    screen = W, H
    hod = 0
    mo = 0
    li = 0
    fr = 0
    bi = 0
    mo1 = True
    li1 = True
    fr1 = True
    bi1 = True
    first = 0
    second = 0
    third = 0
    fourth = 0
    fi = 0
    n = '0'
    screen = pygame.display.set_mode(screen)
    clock = pygame.time.Clock()
    start_screen()
    pygame.quit()
