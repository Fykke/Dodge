import pygame
from random import randint, choice
import json
import os
import sys
pygame.init()

pathname = os.path.dirname(__file__)        
path = os.path.abspath(pathname)
def glob():
    global path
    return path
glob()
################################################################# OPEN DATA FOR SCOREBOARD
try:
    with open(fr'{path}\data.json', 'r') as datajson:
        try:
            data = json.load(datajson)
        except json.decoder.JSONDecodeError:
            data = {}
            with open(fr'{path}\data.json', "w") as write_file:
                json.dump(data, write_file, indent=3)
except FileNotFoundError:
    if not os.path.exists('json'):
        os.makedirs('json')
    data = {"None1": {'score': 0, 'time': 0}}
    with open(fr'{path}\data.json', "w") as write_file:
        json.dump(data, write_file, indent=3)
################################################################################# CONSTANTS ->>

W, H = 600, 400
FPS = 60
clock = pygame.time.Clock()
icon = pygame.image.load(fr"{path}\bot5.png")
THEME = [(200, 30, 0), (255, 203, 91)]

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dodge!")
pygame.display.set_icon(icon)
colors = {1: ['first', 'first_2'], 2: ['second', 'second_2'], 3: ['third', 'third_2'], 4: ['fourth', 'fourth_2']}
key = randint(1, 4)
COLOR1 = colors[key][0]
COLOR2 = colors[key][1]

normalnames = []
normalscores = []
normaltime = []
dictionary = {}
listtoclear = []
#####################################################SCORE FUNCTIONS
def clear():
    with open(fr'{path}\data.json', 'r') as datajson:
        data = json.load(datajson)
    for i in data:
        if 'None' in i:
            listtoclear.append(i)
        else:
            dictionary[i] = {'score': data[i]['score'], 'time': data[i]['time']}
    for i in listtoclear:
        data.pop(i)

    data = dictionary
    with open(fr'{path}\data.json', "w") as write_file:
        json.dump(data, write_file, indent=3)

def create(new):
    with open(fr'{path}\data.json', "w") as write_file:
        data.update(new)
        json.dump(data, write_file, indent=3)

with open(fr'{path}\data.json', 'r') as datajson:
    data = json.load(datajson)

length = 5 - len(data)

if length != 0:
    clear()
    new = {'None1': {'score': 0, 'time': 0}}
    new2 = {'None2': {'score': 0, 'time': 0}}
    new3 = {'None3': {'score': 0, 'time': 0}}
    new4 = {'None4': {'score': 0, 'time': 0}}
    new5 = {'None5': {'score': 0, 'time': 0}}
    create(new)
    create(new2)
    create(new3)
    create(new4)
    create(new5)

def sort(x):
    for i in data:
        if data[i]['score'] == x:
            normalnames.append(i)
    del normalnames[5:]
    del normalscores[5:]
    del normaltime[5:]

with open(fr'{path}\data.json', 'r') as datajson:
    data = json.load(datajson)

def createlists():
    global normalscores, normaltime
    for i in data:
        datascore = data[i]['score']
        datatime = data[i]['time']
        normalscores.append(datascore)
        normaltime.append(datatime)

    normalscores = sorted(normalscores)
    normalscores.reverse()
    normaltime = sorted(normaltime)
    normaltime.reverse()

    for i in normalscores:
        sort(i)


createlists()

########################################################## COLOR/AUDIO/PICTURES/FONT/MOUSE OVER
def colortheme(x):    #CHOOSE THEME
    if x == 'first':
        COLOR1 = (200, 30, 0)
        return COLOR1
    elif x == 'first_2':
        COLOR2 = (255, 203, 91)
        return COLOR2
    if x == 'second':
        COLOR1 = (147, 77, 204)
        return COLOR1
    elif x == 'second_2':
        COLOR2 = (204, 77, 189)
        return COLOR2
    if x == 'third':
        COLOR1 = (63, 169, 78)
        return COLOR1
    elif x == 'third_2':
        COLOR2 = (127, 220, 54)
        return COLOR2
    if x == 'fourth':
        COLOR1 = (215, 217, 206)
        return COLOR1
    elif x == 'fourth_2':
        COLOR2 = (115, 115, 115)
        return COLOR2

def pic(x, y = 0):     #CHOOSE PICTURE
    if 'player' in x:
        playerpic = [fr"{path}\player.png", fr"{path}\player2.png", fr"{path}\player3.png", \
                    fr"{path}\player4.png", fr"{path}\player5.png"]
        a = choice(playerpic)
        return a
    if 'bot' in x:
        botpic = [fr"{path}\bot.png", fr"{path}\bot2.png", fr"{path}\bot3.png", \
                fr"{path}\bot4.png", fr"{path}\bot5.png", fr"{path}\bot5_2.png", \
                fr"{path}\bot5_3.png"]
        b = choice(botpic)
        return b
    if 'fed' in x:    
        fedpic = [fr"{path}\bot5.png", fr"{path}\bot5_2.png", fr"{path}\bot5_3.png"]
        b = choice(fedpic)
        return b
    if 'skin' in x:
        skin = [fr"{path}\player.png", fr"{path}\player2.png", fr"{path}\player3.png", \
                    fr"{path}\player4.png", fr"{path}\player5.png"]
        c = skin[y]
        return c

def font(x):    #ALL FONT IN THE GAME
    font = pygame.font.Font(fr"{path}\EvilEmpire-4BBVK.ttf", x)
    return font

b = pic('bot')
a = pic('player')
volume = 1
current = 518   

def funcaudio(x, y = volume):    #ALL AUDIO IN THE GAME
    audio = pygame.mixer.Sound(fr'{path}\{x}')
    audio.set_volume(volume)
    return audio

def mouseover(x, y):    
    if x.collidepoint(pygame.mouse.get_pos()):
        x = pygame.draw.rect(sc, (colortheme(COLOR2)), (y))
        
def showcurrent(x): # SKIN
    pygame.draw.rect(sc, (55, 55, 55), (120, 215, 396, 7))
    pygame.draw.rect(sc, (colortheme(COLOR2)), (x-2, 200, 11, 11))

def showdigit(x, pos, y=0): #DIGITS IN SETTINGS -> AUDIO
    if y != 0:
        digit = font(24).render(str(x), 1, (colortheme(COLOR1)))
        pos_digit = digit.get_rect(center=(pos, y))
        sc.blit(digit, pos_digit)
    else:
        digit = font(48).render(str(x), 1, (colortheme(COLOR1)))
        pos_digit = digit.get_rect(center=(pos, 270))
        sc.blit(digit, pos_digit)
def changevolume(x, y):   #CHANGE GLOBAL VOLUME
    global current, volume
    volume = x
    current = y
    funcaudio('hitbutton.wav').play()
########################################################### MAIN MENU

def menu(playerskin, botskin):
    main_menu = True
    while main_menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:

                if 239 < x < 380 and 182 < y < 216:
                    funcaudio('hitbutton.wav').play()
                    game(playerskin, botskin)
                    main_menu = False

                if 256 < x < 363 and 217 < y < 252:
                    funcaudio('hitbutton.wav').play()
                    main_menu = False    
                    settings(playerskin)
                    
                if 275 < x < 345 and 252 < y < 287:
                    funcaudio('hitbutton.wav').play()
                    main_menu = False    
                    scoreboard(playerskin, botskin)

                if 283 < x < 336 and 287 < y < 322:
                    sys.exit()
                    

        sc.fill((55, 55, 55))
        pygame.draw.rect(sc, (colortheme(COLOR1)), (237, 155, 145, 3))

        menu_name = font(64).render('DODGE!', 1, (colortheme(COLOR1)))
        pos_menu_name = menu_name.get_rect(center=(312, 110))

        menu_start = font(32).render('START GAME', 1, (colortheme(COLOR1)))
        pos_menu_start = menu_start.get_rect(center=(310, 200))
        
        menu_options = font(32).render('SETTINGS', 1, (colortheme(COLOR1)))
        pos_menu_options = menu_options.get_rect(center=(310, 235))

        menu_top = font(32).render('SCORE', 1, (colortheme(COLOR1)))
        pos_menu_top = menu_top.get_rect(center=(310, 270))

        menu_quit = font(32).render('QUIT', 1, (colortheme(COLOR1)))
        pos_menu_quit = menu_quit.get_rect(center=(310, 305))

        sc.blit(menu_name, pos_menu_name)
        sc.blit(menu_start, pos_menu_start)
        sc.blit(menu_options, pos_menu_options)
        sc.blit(menu_top, pos_menu_top)
        sc.blit(menu_quit, pos_menu_quit)

        if pos_menu_start.collidepoint(pygame.mouse.get_pos()):
            menu_start = font(32).render('START GAME', 1, (colortheme(COLOR2)))
            sc.blit(menu_start, pos_menu_start)
        if pos_menu_options.collidepoint(pygame.mouse.get_pos()):
            menu_options = font(32).render('SETTINGS', 1, (colortheme(COLOR2)))
            sc.blit(menu_options, pos_menu_options)
        if pos_menu_top.collidepoint(pygame.mouse.get_pos()):
            menu_top = font(32).render('SCORE', 1, (colortheme(COLOR2)))
            sc.blit(menu_top, pos_menu_top)
        if pos_menu_quit.collidepoint(pygame.mouse.get_pos()):
            menu_quit = font(32).render('QUIT', 1, (colortheme(COLOR2)))
            sc.blit(menu_quit, pos_menu_quit)

        pygame.display.update()
        clock.tick(FPS)

########################################################### SETTINGS MENU

def settings(playerskin):
    settings_menu = True
    while settings_menu == True:
        x, y = pygame.mouse.get_pos()
        sc.fill((55, 55, 55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if 0 < x < 51 and 0 < y < 31:
                    funcaudio('hitbutton.wav').play()
                    settings_menu = False
                    menu(a, b)

            if event.type == pygame.MOUSEBUTTONUP:
                if 14 < x < 94 and 87 < y < 122:
                    funcaudio('hitbutton.wav').play()  
                    settings_menu = False
                    changetheme(playerskin)

            if event.type == pygame.MOUSEBUTTONUP:
                if 14 < x < 86 and 121 < y < 156:
                    funcaudio('hitbutton.wav').play()
                    changeaudio(current, playerskin)

            if event.type == pygame.MOUSEBUTTONUP:
                if 14 < x < 80 and 155 < y < 190:
                    funcaudio('hitbutton.wav').play()
                    changeskin(playerskin)
        
        settings_name = font(54).render('SETTINGS', 1, (colortheme(COLOR1)))
        pos_settings_name = settings_name.get_rect(center=(310, 50))

        settings_theme = font(32).render('THEME', 1, (colortheme(COLOR1)))
        pos_settings_theme = settings_theme.get_rect(center=(54, 105))

        settings_audio = font(32).render('AUDIO', 1, (colortheme(COLOR1)))
        pos_settings_audio = settings_audio.get_rect(center=(50, 139))

        settings_skin = font(32).render('SKIN', 1, (colortheme(COLOR1)))
        pos_settings_skin = settings_skin.get_rect(center=(42, 173))

        line = pygame.draw.rect(sc, (colortheme(COLOR1)), (100, 80, 3, 105)); line = line

        sc.blit(settings_name, pos_settings_name)
        sc.blit(settings_audio, pos_settings_audio)
        sc.blit(settings_theme, pos_settings_theme)
        sc.blit(settings_skin, pos_settings_skin)

        back = pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 0, 50, 30))
        arrow = pygame.image.load(fr"{path}\arrow.png").convert_alpha()

        if back.collidepoint(pygame.mouse.get_pos()):
            back = pygame.draw.rect(sc, (colortheme(COLOR2)), (0, 0, 50, 30))

        if pos_settings_theme.collidepoint(pygame.mouse.get_pos()):
            settings_theme = font(32).render('THEME', 1, (colortheme(COLOR2)))
            sc.blit(settings_theme, pos_settings_theme)

        if pos_settings_audio.collidepoint(pygame.mouse.get_pos()):
            settings_audio = font(32).render('AUDIO', 1, (colortheme(COLOR2)))
            sc.blit(settings_audio, pos_settings_audio)

        if pos_settings_skin.collidepoint(pygame.mouse.get_pos()):
            settings_skin = font(32).render('SKIN', 1, (colortheme(COLOR2)))
            sc.blit(settings_skin, pos_settings_skin)

        sc.blit(arrow, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

########################################################### SETTINGS -> FRAMES WIDGETS

def settingswidgets():
    settings_name = font(54).render('SETTINGS', 1, (colortheme(COLOR1)))
    pos_settings_name = settings_name.get_rect(center=(310, 50))
    back = pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 0, 50, 30))
    arrow = pygame.image.load(fr"{path}\arrow.png").convert_alpha()
    pygame.draw.rect(sc, (colortheme(COLOR1)), (100, 80, 3, 292))
    pygame.draw.rect(sc, (colortheme(COLOR1)), (100, 120, 420, 3))
    sc.blit(settings_name, pos_settings_name)
    if back.collidepoint(pygame.mouse.get_pos()):
        back = pygame.draw.rect(sc, (colortheme(COLOR2)), (0, 0, 50, 30))
    sc.blit(arrow, (0, 0))

########################################################### SETTINGS -> THEME

def changetheme(playerskin):
    global COLOR1, COLOR2
    changetheme_menu = True
    while changetheme_menu == True:
        x, y = pygame.mouse.get_pos()
        sc.fill((55, 55, 55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if 0 < x < 51 and 0 < y < 31:
                    funcaudio('hitbutton.wav').play()
                    settings(playerskin)

            if event.type == pygame.MOUSEBUTTONUP:
                if 360 < x < 440 and 147 < y < 182:
                    funcaudio('hitbutton.wav').play()
                    COLOR1 = colors[1][0]
                    COLOR2 = colors[1][1]
            if event.type == pygame.MOUSEBUTTONUP:
                if 360 < x < 440 and 204 < y < 239:
                    funcaudio('hitbutton.wav').play()
                    COLOR1 = colors[2][0]
                    COLOR2 = colors[2][1]
            if event.type == pygame.MOUSEBUTTONUP:
                if 360 < x < 440 and 264 < y < 299:
                    funcaudio('hitbutton.wav').play()
                    COLOR1 = colors[3][0]
                    COLOR2 = colors[3][1]
            if event.type == pygame.MOUSEBUTTONUP:
                if 360 < x < 440 and 324 < y < 359:
                    funcaudio('hitbutton.wav').play()
                    COLOR1 = colors[4][0]
                    COLOR2 = colors[4][1]

        settingswidgets()
        change_theme = font(32).render('THEME', 1, (colortheme(COLOR1)))
        pos_change_theme = change_theme.get_rect(center=(310, 105))

        settings_theme = font(32).render('THEME', 1, (colortheme(COLOR1)))
        pos_settings_theme = settings_theme.get_rect(center=(54, 105))

        theme1 = pygame.image.load(fr"{path}\theme1.png").convert()
        theme2 = pygame.image.load(fr"{path}\theme2.png").convert()
        theme3 = pygame.image.load(fr"{path}\theme3.png").convert()
        theme4 = pygame.image.load(fr"{path}\theme4.png").convert()

        theme1_select = font(32).render('SELECT', 1, (colortheme(COLOR1)))
        pos_theme1_select = theme1_select.get_rect(center=(400, 165))
        theme2_select = font(32).render('SELECT', 1, (colortheme(COLOR1)))
        pos_theme2_select = theme1_select.get_rect(center=(400, 222))
        theme3_select = font(32).render('SELECT', 1, (colortheme(COLOR1)))
        pos_theme3_select = theme1_select.get_rect(center=(400, 282))
        theme4_select = font(32).render('SELECT', 1, (colortheme(COLOR1)))
        pos_theme4_select = theme1_select.get_rect(center=(400, 342))


        sc.blit(theme1, (110, 137))
        sc.blit(theme2, (110, 197))
        sc.blit(theme3, (110, 257))
        sc.blit(theme4, (110, 317))
        sc.blit(theme1_select, pos_theme1_select)
        sc.blit(theme2_select, pos_theme2_select)
        sc.blit(theme3_select, pos_theme3_select)
        sc.blit(theme4_select, pos_theme4_select)
        sc.blit(settings_theme, pos_settings_theme)
        sc.blit(change_theme, pos_change_theme)
        
        if pos_theme1_select.collidepoint(pygame.mouse.get_pos()):
            theme1_select = font(32).render('SELECT', 1, (colortheme(COLOR2)))
            sc.blit(theme1_select, pos_theme1_select)

        if pos_theme2_select.collidepoint(pygame.mouse.get_pos()):
            theme2_select = font(32).render('SELECT', 1, (colortheme(COLOR2)))
            sc.blit(theme2_select, pos_theme2_select)

        if pos_theme3_select.collidepoint(pygame.mouse.get_pos()):
            theme3_select = font(32).render('SELECT', 1, (colortheme(COLOR2)))
            sc.blit(theme3_select, pos_theme3_select)

        if pos_theme4_select.collidepoint(pygame.mouse.get_pos()):
            theme4_select = font(32).render('SELECT', 1, (colortheme(COLOR2)))
            sc.blit(theme4_select, pos_theme4_select)

        pygame.display.update()
        clock.tick(FPS)


########################################################### SETTINGS -> AUDIO

def changeaudio(x, playerskin):
    global volume
    global current
    changeaudio_menu = True
    while changeaudio_menu == True:
        x, y = pygame.mouse.get_pos()
        sc.fill((55, 55, 55))
        showcurrent(current)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if 0 < x < 51 and 0 < y < 31:
                    funcaudio('hitbutton.wav').play()
                    settings(playerskin)
            if event.type == pygame.MOUSEBUTTONUP:
                if 119 < x < 131 and 229 < y < 245:
                    changevolume(0.1, 122)
                if 163 < x < 175 and 229 < y < 245:
                    changevolume(0.2, 166)
                if 207 < x < 219 and 229 < y < 245:
                    changevolume(0.3, 210)
                if 251 < x < 263 and 229 < y < 245:
                    changevolume(0.4, 254)
                if 295 < x < 307 and 229 < y < 245:
                    changevolume(0.5, 298)
                if 339 < x < 351 and 229 < y < 245:
                    changevolume(0.6, 324)
                if 383 < x < 395 and 229 < y < 245:
                    changevolume(0.7, 386)
                if 427 < x < 439 and 229 < y < 245:
                    changevolume(0.8, 430)
                if 475 < x < 487 and 229 < y < 245:
                    changevolume(0.9, 478)
                if 515 < x < 527 and 229 < y < 245:
                    changevolume(1, 518)

        settingswidgets()
        change_audio = font(32).render('AUDIO', 1, (colortheme(COLOR1)))
        pos_change_audio = change_audio.get_rect(center=(310, 105))

        settings_audio = font(32).render('AUDIO', 1, (colortheme(COLOR1)))
        pos_settings_audio = settings_audio.get_rect(center=(54, 105))

        pygame.draw.rect(sc, (colortheme(COLOR1)), (120, 235, 400, 5))
        a1 = pygame.draw.rect(sc, (colortheme(COLOR1)), (120, 230, 11, 15))
        a2 = pygame.draw.rect(sc, (colortheme(COLOR1)), (164, 230, 11, 15))
        a3 = pygame.draw.rect(sc, (colortheme(COLOR1)), (208, 230, 11, 15))
        a4 = pygame.draw.rect(sc, (colortheme(COLOR1)), (252, 230, 11, 15))
        a5 = pygame.draw.rect(sc, (colortheme(COLOR1)), (296, 230, 11, 15))
        a6 = pygame.draw.rect(sc, (colortheme(COLOR1)), (340, 230, 11, 15))
        a7 = pygame.draw.rect(sc, (colortheme(COLOR1)), (384, 230, 11, 15))
        a8 = pygame.draw.rect(sc, (colortheme(COLOR1)), (428, 230, 11, 15))
        a9 = pygame.draw.rect(sc, (colortheme(COLOR1)), (476, 230, 11, 15))
        a10 = pygame.draw.rect(sc, (colortheme(COLOR1)), (516, 230, 11, 15))

        showdigit(1, 126)
        showdigit(2, 170)
        showdigit(3, 214)
        showdigit(4, 256)
        showdigit(5, 302)
        showdigit(6, 346)
        showdigit(7, 390)
        showdigit(8, 434)
        showdigit(9, 482)
        showdigit(10, 524)
        sc.blit(settings_audio, pos_settings_audio)
        sc.blit(change_audio, pos_change_audio)
        
        mouseover(a1, (120, 230, 11, 15))
        mouseover(a2, (164, 230, 11, 15))
        mouseover(a3, (208, 230, 11, 15))
        mouseover(a4, (252, 230, 11, 15))
        mouseover(a5, (296, 230, 11, 15))
        mouseover(a6, (340, 230, 11, 15))
        mouseover(a7, (384, 230, 11, 15))
        mouseover(a8, (428, 230, 11, 15))
        mouseover(a9, (476, 230, 11, 15))
        mouseover(a10, (516, 230, 11, 15))

        pygame.display.update()
        clock.tick(FPS)

########################################################### SETTINGS -> SKIN

def changeskin(playerskin):
    global a
    changeskin_menu = True
    while changeskin_menu == True:
        x, y = pygame.mouse.get_pos()
        sc.fill((55, 55, 55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if 0 < x < 51 and 0 < y < 31:
                    funcaudio('hitbutton.wav').play()
                    settings(playerskin)
                if 255 < x < 275 and 200 < y < 220:
                    funcaudio('hitbutton.wav').play()
                    a = pic('skin', 0)
                if 280 < x < 300 and 200 < y < 220:
                    funcaudio('hitbutton.wav').play()
                    a = pic('skin', 1)
                if 305 < x < 325 and 200 < y < 220:
                    funcaudio('hitbutton.wav').play()
                    a = pic('skin', 2)
                if 330 < x < 350 and 200 < y < 220:
                    funcaudio('hitbutton.wav').play()
                    a = pic('skin', 3)
                if 355 < x < 375 and 200 < y < 220:
                    funcaudio('hitbutton.wav').play()
                    a = pic('skin', 4)

        settingswidgets()
        change_skin = font(32).render('SKIN', 1, (colortheme(COLOR1)))
        pos_change_skin = change_skin.get_rect(center=(310, 105))

        settings_skin = font(32).render('SKIN', 1, (colortheme(COLOR1)))
        pos_settings_skin = settings_skin.get_rect(center=(54, 105))
        
        current_skin = font(32).render('CURRENT SKIN', 1, (colortheme(COLOR1)))
        pos_current_skin = current_skin.get_rect(center=(200, 150))

        playerskinimage = pygame.image.load(a).convert_alpha()
        c = pic('skin', 0)
        pic1 = pygame.image.load(c).convert_alpha()
        c = pic('skin', 1)
        pic2 = pygame.image.load(c).convert_alpha()
        c = pic('skin', 2)
        pic3 = pygame.image.load(c).convert_alpha()
        c = pic('skin', 3)
        pic4 = pygame.image.load(c).convert_alpha()
        c = pic('skin', 4)
        pic5 = pygame.image.load(c).convert_alpha()
        
        sc.blit(settings_skin, pos_settings_skin)
        sc.blit(change_skin, pos_change_skin)
        sc.blit(current_skin, pos_current_skin)
        sc.blit(playerskinimage, (340, 138))
        sc.blit(pic1, (255, 200))
        sc.blit(pic2, (280, 200))
        sc.blit(pic3, (305, 200))
        sc.blit(pic4, (330, 200))
        sc.blit(pic5, (355, 200))
        
        pygame.display.update()
        clock.tick(FPS)

########################################################### SETTINGS -> SCORE

def scoreboard(playerskin, botskin):
    #with open(r'pygame\Dodge\data\data.json', 'r') as datajson:
    #    data = json.load(datajson)
    scoreboard_menu = True
    while scoreboard_menu == True:
        x, y = pygame.mouse.get_pos()
        sc.fill((55, 55, 55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    
                
            if event.type == pygame.MOUSEBUTTONUP:
                if 0 < x < 51 and 0 < y < 31:
                    funcaudio('hitbutton.wav').play()
                    menu(playerskin, botskin)
        
        back = pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 0, 50, 30))
        arrow = pygame.image.load(fr"{path}\arrow.png").convert_alpha()

        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 120, 600, 3))    #vertical
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 80, 600, 3))    #vertical
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 397, 600, 3))    #vertical
        pygame.draw.rect(sc, (colortheme(COLOR1)), (199, 80, 3, 320))   #horizontal
        pygame.draw.rect(sc, (colortheme(COLOR1)), (399, 80, 3, 320))   #horizontal
        pygame.draw.rect(sc, (colortheme(COLOR1)), (597, 80, 3, 320))   #horizontal
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 80, 3, 320))     #horizontal
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 175, 600, 3))   #1st line
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 231, 600, 3))   #2nd line
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 286, 600, 3))   #3rd line
        pygame.draw.rect(sc, (colortheme(COLOR1)), (0, 342, 600, 3))   #4th line

        scoreboard_username = font(32).render('NAME', 1, (colortheme(COLOR1)))
        pos_scoreboard_username = scoreboard_username.get_rect(center=(103, 103))

        scoreboard_score = font(32).render('SCORE', 1, (colortheme(COLOR1)))
        pos_scoreboard_score = scoreboard_score.get_rect(center=(300, 103))

        scoreboard_time = font(32).render('TIME ALIME', 1, (colortheme(COLOR1)))
        pos_scoreboard_time = scoreboard_time.get_rect(center=(500, 103))

        scoreboard_name = font(54).render('SCOREBOARD', 1, (colortheme(COLOR1)))
        pos_scoreboard_name = scoreboard_name.get_rect(center=(310, 50))

        if back.collidepoint(pygame.mouse.get_pos()):
            back = pygame.draw.rect(sc, (colortheme(COLOR2)), (0, 0, 50, 30))

        showdigit(normalnames[0], 103, y=150)
        showdigit(normalscores[0], 300, y=150)
        showdigit(normaltime[0], 500, y=150)

        showdigit(normalnames[1], 103, y=206)
        showdigit(normalscores[1], 300, y=206)
        showdigit(normaltime[1], 500, y=206)

        showdigit(normalnames[2], 103, y=261)
        showdigit(normalscores[2], 300, y=261)
        showdigit(normaltime[2], 500, y=261)

        showdigit(normalnames[3], 103, y=317)
        showdigit(normalscores[3], 300, y=317)
        showdigit(normaltime[3], 500, y=317)

        showdigit(normalnames[4], 103, y=372)
        showdigit(normalscores[4], 300, y=372)
        showdigit(normaltime[4], 500, y=372)

        sc.blit(scoreboard_name, pos_scoreboard_name)
        sc.blit(arrow, (0, 0))
        sc.blit(scoreboard_username, pos_scoreboard_username)
        sc.blit(scoreboard_score, pos_scoreboard_score)
        sc.blit(scoreboard_time, pos_scoreboard_time)
        pygame.display.update()   

########################################################### GAME LOOP

def game(playerskin, botskin):
    global count, seconds
    game_over = False
    count = 0
    count2 = 0
    seconds = 0
    xplayer = W // 2
    yplayer = H // 2
    playerspeed = 5
    botspeed = 5
    botspeed2 = 5
    xbot = 1000
    xbot2 = 1000
    ybot = randint(0, 320)
    ybot2 = randint(0, 320)
    
    start_ticks=pygame.time.get_ticks()
    
    bot_surf = pygame.image.load(botskin).convert_alpha()
    bot_mask = pygame.mask.from_surface(bot_surf)
    bot_surf2 = pygame.image.load(botskin).convert_alpha()
    bot_mask2 = pygame.mask.from_surface(bot_surf2)

    player_surf = pygame.image.load(playerskin).convert_alpha()
    player_surf_mask = pygame.mask.from_surface(player_surf)

    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        score = font(48).render(str(count), 1, (colortheme(COLOR1)))
        pos = score.get_rect(center=(310, 75))

        sc.fill((30, 30, 30))
        sc.blit(score, pos)

        sc.blit(player_surf, (xplayer, yplayer))
        sc.blit(bot_surf, (xbot, ybot))
        if seconds > 1.5:
            sc.blit(bot_surf2, (xbot2, ybot2))
            xbot2 -= botspeed2
        
        first = randint(0, ybot)
        second = randint(ybot, 320)

        botoffset = (int(xbot) - int(xbot), int(ybot) - int(ybot2))
        botcollide = bot_mask.overlap(bot_mask2, botoffset)
        
        offset = (int(xplayer) - int(xbot), int(yplayer) - int(ybot))
        offset2 = (int(xplayer) - int(xbot2), int(yplayer) - int(ybot2))

        xbot -= botspeed

        if xbot > 600:
            if botcollide:
                ybot = randint(first, second)
        if xbot2 > 600:
            if botcollide:
                ybot2 = randint(first, second)

        keys = pygame.key.get_pressed()   
        if keys[pygame.K_LEFT]:
            xplayer -= playerspeed
        if keys[pygame.K_UP]:
            yplayer -= playerspeed
        if keys[pygame.K_RIGHT]:
            xplayer += playerspeed
        if keys[pygame.K_DOWN]:
            yplayer += playerspeed

        if xbot2 < -60:
            xbot2 = 700
            ybot2 = randint(0, 320) #320
            count2 += 1
            if count2 % 5 == 0:
                ybot2 = randint(0, 320)
                botspeed2 += 1.5
                if 'bot5' in botskin:
                    b = pic('fed')
                    bot_surf2 = pygame.image.load(b).convert_alpha()
                if ybot2 > 320:
                    ybot2 = 320
                if ybot2 < 0:
                    ybot2 = 0
                if botspeed2 >= 15.5:
                    botspeed2 = 15.5

        if xbot < -60:
            xbot = 700
            ybot = randint(0, 320) #320
            count += 1
            if count % 5 == 0:
                ybot = randint(yplayer-35, yplayer+35)
                botspeed += 1.5
                if 'bot5' in botskin:
                    b = pic('fed')
                    bot_surf = pygame.image.load(b).convert_alpha()
                if ybot > 320:
                    ybot = 320
                if ybot < 0:
                    ybot = 0
                if botspeed >= 15.5:
                    botspeed = 15.5
                    funcaudio('count.wav').play()
                else:
                    funcaudio('speed_up.wav').play()
            else:
                funcaudio('count.wav').play()

        elif yplayer > 390:
            yplayer = -10
            funcaudio('wall.wav').play()
        elif yplayer < -10:
            yplayer = 390
            funcaudio('wall.wav').play()
        elif xplayer < 0:
            xplayer = 0
        elif xplayer > 580:
            xplayer = 580


        result = bot_mask.overlap(player_surf_mask, offset)
        result2 = bot_mask2.overlap(player_surf_mask, offset2)

        if result or result2:
            funcaudio('hit.wav').play()
            lose(playerskin, botskin, count, seconds)
            game_over = True

        pygame.display.update()
        clock.tick(FPS)

########################################################### FRAME AFTER DEATH 

def lose(playerskin, botskin, count, seconds):
    global b
    
    user_text = ''
    input_rect = pygame.Rect(69, 323, 198, 34)
    color_active = pygame.Color(colortheme(COLOR2))
    color_passive = pygame.Color(colortheme(COLOR1))
    color = color_passive
    active = False
    createaccount = True
    lose_menu = True
    while lose_menu == True:
        save_score = font(48).render('SAVE SCORE', 1, (colortheme(COLOR1)))
        pos_save_score = save_score.get_rect(center=(430, 340))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if 69 < x < 270 and 254 < y < 306:
                    funcaudio('hitbutton.wav').play()
                    botskin = pic('bot')
                    game(playerskin, botskin)
                    lose_menu = False
                if 318 < x < 542 and 254 < y < 306:
                    funcaudio('hitbutton.wav').play()
                    menu(playerskin, botskin)
                    lose_menu = False 
                if pos_save_score.collidepoint(pygame.mouse.get_pos()):
                    with open(fr'{path}\data.json', 'r') as datajson:
                        data = json.load(datajson)

                    if len(user_text) > 2:
                        for i in data:
                            if user_text == i and count < data[i]['score']:
                                createaccount = False

                        if createaccount == False:        
                            user_text = ''
                        else:

                            normalnames.append(user_text) 
                            normalscores.append(count) 
                            normaltime.append(seconds)
                            
                            new = {user_text: {'score': count, 'time': seconds}}
                            create(new)
                            createlists()  
                            user_text = ''

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                        if len(user_text) > 9:
                            user_text = user_text[:-1]
                        elif 'none' in user_text:
                            user_text = ''

        s = pygame.Surface((600,400), pygame.SRCALPHA)
        s.fill((30,30,30,19)) #TRANSPARENCY
        sc.blit(s, (0,0))

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(sc, color, input_rect, 2)
        
        text_surface = font(32).render(user_text, 1, (colortheme(COLOR1)))

        lose = font(64).render('GAME OVER', 1, (colortheme(COLOR1)))
        pos_lose = lose.get_rect(center=(305, 75))

        pygame.draw.rect(sc, (colortheme(COLOR1)), (174, 106, 259, 3))

        time_score = font(32).render(f'TIME ALIVE: {int(seconds)} SEC', 1, (colortheme(COLOR1)))
        pos_time = time_score.get_rect(center=(300, 135))

        lose_score = font(32).render(f'SCORE: {count}', 1, (colortheme(COLOR1)))
        pos_score = lose_score.get_rect(center=(300, 175))

        again = font(48).render('PLAY AGAIN', 1, (colortheme(COLOR1)))
        pos_again = again.get_rect(center=(170, 280))

        tothemenu = font(48).render('TO THE MENU', 1, (colortheme(COLOR1)))
        pos_tothemenu = tothemenu.get_rect(center=(430, 280))

        sc.blit(lose, pos_lose)
        sc.blit(lose_score, pos_score)
        sc.blit(time_score, pos_time)
        sc.blit(again, pos_again)
        sc.blit(tothemenu, pos_tothemenu)
        sc.blit(save_score, pos_save_score)
        sc.blit(text_surface, (input_rect.x+2, input_rect.y + 1))

        if pos_again.collidepoint(pygame.mouse.get_pos()):
            again = font(48).render('PLAY AGAIN', 1, (colortheme(COLOR2)))  #200 250 110
            sc.blit(again, pos_again)
        if pos_tothemenu.collidepoint(pygame.mouse.get_pos()):
            tothemenu = font(48).render('TO THE MENU', 1, (colortheme(COLOR2)))
            sc.blit(tothemenu, pos_tothemenu)
        if pos_save_score.collidepoint(pygame.mouse.get_pos()):
            save_score = font(48).render('SAVE SCORE', 1, (colortheme(COLOR2)))
            sc.blit(save_score, pos_save_score)
        
        pygame.display.update()
        clock.tick(FPS)

######################## CALL THE MENU

menu(a, b)