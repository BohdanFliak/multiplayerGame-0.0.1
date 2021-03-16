import random

import pygame

from bot_settings import give_bot
from items import item
from load import idle, walk, kick, dying, idle_l, walk_l, kick_l, dying_l, idle_bot, walk_bot, attack_bot, dying_bot, idle_l_bot, walk_l_bot, attack_l_bot, dying_l_bot, returned_background_index, shadow
from network import Network
from player import *

pygame.font.init()


class Canvas:
    def __init__(self, w, h, name="Test"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((1680, 1050), pygame.FULLSCREEN)
        pygame.display.set_caption(name)
    @staticmethod
    def update():
        pygame.display.update()
    def get_canvas(self):
        return self.screen
    def draw_background(self):
        self.screen.fill((255, 255, 255))
class Toucher:
    def __init__(self, x, y, w, h, color, long):
        self.x = x
        self.y = y
        self.color = color
        self.width = w
        self.height = h
        self.start_x = x
        self.long_w = long
        self.long = long - w
        self.rect = pygame.Rect(x, y, w, h)
        self.touched = False
        self.font = pygame.font.SysFont(None, 25)

    def draw(self, win, money):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(str(int((self.x - self.start_x) / self.long * money)), True, (0, 0, 0))
        win.blit(text, (int(self.long_w / 2) - round(text.get_width()/2) + self.start_x, self.y + self.height + 5))
        pygame.draw.rect(win, (0, 0, 0), (self.start_x, self.y, self.long_w, 25), 1)

    def touch(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.touched = True
            pygame.mouse.get_rel()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.touched = False
        if self.touched is True:
            self.rect.move_ip(pygame.mouse.get_rel()[0],0)
            self.rect.clamp_ip(self.start_x, 0, self.long_w, 1000)
            self.x = self.rect.x

class Button:
    def __init__(self, x, y, w, h, color=(0, 0, 0), way=None, text=None, font_size=None):
        self.x = x
        self.y = y
        self.color = color
        self.width = w
        self.height = h
        if way != None:
            self.image = pygame.transform.scale(pygame.image.load(way), (int(480/(400/w)), int(480/(170/h))))
            if font_size != None:
                font = pygame.font.SysFont(None, font_size)
                self.text = font.render(text, True, self.color)
            else:
                self.text = None
        else:
            self.image = None
            self.text = None
    def draw(self, win):
        if self.image == None:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        else:
            win.blit(self.image, (self.x - (int(480/(400/self.width)/12)), self.y-int(480/(170/self.height)/(480/155))))
            if self.text != None:
                win.blit(self.text, (self.x + int(self.width/2) - round(self.text.get_width()/2), self.y + int(self.height/2) - round(self.text.get_height()/2)))
    def click(self, pos):
        if pos.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x1 = pos[0]
            y1 = pos[1]
            if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
                return True
            else:
                return False
background_item = pygame.transform.scale(pygame.image.load("assets/bg.png"), (90, 60))
items_icon = [pygame.transform.scale(pygame.image.load("assets/items/1.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/2.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/3.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/4.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/5.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/6.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/7.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/8.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/9.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/10.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/11.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/12.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/13.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/14.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/15.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/16.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/17.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/18.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/19.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/20.png"), (90, 60)),
pygame.transform.scale(pygame.image.load("assets/items/21.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/22.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/23.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/24.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/25.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/26.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/27.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/28.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/29.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/30.png"), (90, 60)),
pygame.transform.scale(pygame.image.load("assets/items/31.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/32.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/33.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/34.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/35.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/36.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/37.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/38.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/39.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/40.png"), (90, 60)),
pygame.transform.scale(pygame.image.load("assets/items/41.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/42.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/43.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/44.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/45.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/46.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/47.png"), (90, 60)),
              pygame.transform.scale(pygame.image.load("assets/items/48.png"), (90, 60)),
              ]

class Button_Buy:
    def __init__(self, x, y, w, h, index, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.width = w
        self.height = h
        self.item_index = index
        self.popup_draw = False
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))
        win.blit(background_item, (self.x, self.y))
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 2)
        try:
            win.blit(items_icon[item(self.item_index)[4]-1], (self.x, self.y))
        except:
            text = font.render(str(self.item_index), True, (0, 0, 0))
            win.blit(text, (self.x + int(self.width/2) - round(text.get_width()/2), self.y + int(self.height/2) - round(text.get_height()/2)))
    def draw_popup(self, win):
        if self.popup_draw:
            pygame.draw.rect(win, (255, 255, 255), (self.x - 140, self.y - 30, 130, 90))
            pygame.draw.rect(win, (0, 0, 0), (self.x - 140, self.y - 30, 130, 90), 1)
            text = font.render(item(self.item_index)[0], True, (0, 0, 0))
            win.blit(text, (self.x - 75 - round(text.get_width()/2), self.y - 25))
            text = font.render(str(item(self.item_index)[1]), True, (0, 0, 0))
            win.blit(text, (self.x - 75 - round(text.get_width()/2), self.y - 10))
            for cycle_index in range(len(item(self.item_index)[2])):
                text = font.render(item(self.item_index)[2][cycle_index]+": "+str(item(self.item_index)[3][cycle_index]), True, (0, 0, 0))
                win.blit(text, (self.x - 75 - round(text.get_width() / 2), self.y + 5 + 15 * cycle_index))

    def click(self, event):
        pos = pygame.mouse.get_pos()
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.popup_draw = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        else:
            self.popup_draw = False
            return False
class Button_Sell:
    def __init__(self, x, y, w, h, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.width = w
        self.height = h
        self.item_index = None
        self.popup_draw = False
    def draw(self, win):
        win.blit(background_item, (self.x, self.y))
        #pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 1)
        if self.item_index != None:
            pygame.draw.rect(win, (255, 255, 255), (self.x + 1, self.y + 1, self.width - 2, self.height - 2))
            #text = font.render(str(self.item_index), True, (0, 0, 0))
            #win.blit(text, (self.x + int(self.width/2) - round(text.get_width()/2), self.y + int(self.height/2) - round(text.get_height()/2)))
            try:
                win.blit(items_icon[item(self.item_index)[4] - 1], (self.x, self.y))
            except:
                text = font.render(str(self.item_index), True, (0, 0, 0))
                win.blit(text, (self.x + int(self.width / 2) - round(text.get_width() / 2),
                                self.y + int(self.height / 2) - round(text.get_height() / 2)))
            if self.popup_draw:
                pygame.draw.rect(win, (255, 255, 255), (self.x - 140, self.y - 30, 130, 90))
                pygame.draw.rect(win, (0, 0, 0), (self.x - 140, self.y - 30, 130, 90), 1)
                text = font.render(item(self.item_index)[0], True, (0, 0, 0))
                win.blit(text, (self.x - 75 - round(text.get_width() / 2), self.y - 25))
                text = font.render(str(item(self.item_index)[1]), True, (0, 0, 0))
                win.blit(text, (self.x - 75 - round(text.get_width() / 2), self.y - 10))
                for cycle_index in range(len(item(self.item_index)[2])):
                    text = font.render(item(self.item_index)[2][cycle_index]+": "+str(item(self.item_index)[3][cycle_index]), True, (0, 0, 0))
                    win.blit(text, (self.x - 75 - round(text.get_width() / 2), self.y + 5 + 15 * cycle_index))

    def click(self, event):
        pos = pygame.mouse.get_pos()
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.popup_draw = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        else:
            self.popup_draw = False
            return False

background_player_choise = pygame.image.load("game_background/b5.png")
background_player_choise_small = pygame.transform.scale(background_player_choise, (700, 370))
background_player_choise_small1 = pygame.transform.scale(pygame.image.load("game_background/i4.png"), (2560, 1440))
class Button_Choise_Hero:
    def __init__(self, x, y, index, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.width = 170
        self.height = 285
        self.image = pygame.transform.scale(pygame.image.load(attributes(index)[12]), (315, 315))
        self.name = font_B.render(attributes(index)[13], True, (255, 0, 0))
        if self.name.get_width() > 155:
            self.name = font.render(attributes(index)[13], True, (255, 0, 0))
        self.popup_draw = False
    def draw(self, win):
        win.blit(background_player_choise_small, (self.x, self.y), (0, 100, self.width, self.height))
        win.blit(background_player_choise_small1, (self.x+10, self.y+10), (340, 200, 150, 210))
        pygame.draw.rect(win, (0, 255, 255), (self.x+10, self.y+10, 150, 210), 1)
        pygame.draw.rect(win, (255, 255, 255), (self.x+5, self.y+230, 160, 50))

        win.blit(self.image, (self.x - 65, self.y - 50))
        win.blit(self.name, (self.x + 85 - round(self.name.get_width()/2), self.y + 255 - round(self.name.get_height()/2)))

    def click(self, event):
        pos = pygame.mouse.get_pos()
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.popup_draw = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        else:
            self.popup_draw = False
            return False

class Attributes_Info:
    def __init__(self):
        self.x = 500
        self.y = 835
        self.color = (0, 0, 0)
        self.width = 85
        self.height = 140
        self.popup_draw = False
        self.image = pygame.transform.scale(pygame.image.load("game_background/b3.png"), (300, 190))

    def draw_popup(self, canvas, strength, items_strength, agility, items_agility, intelligence, items_intelligence, start_hp, items_hp, start_speed , items_speed, start_damage, items_damage, s_level, a_level, i_level):
        #pygame.draw.rect(canvas, (255, 255, 255), (500, 785, 300, 190))
        canvas.blit(self.image, (500, 785))
        pygame.draw.rect(canvas, (0, 0, 0), (500, 785, 300, 190), 1)
        text = font.render("Strength: " + str(strength) + " + " + str(items_strength) + " ( + " + str(s_level) + " per level )", True, (0, 0, 0))
        canvas.blit(text, (502, 785+5))
        text = font.render("Agility: " + str(agility) + " + " + str(items_agility) + " ( + " + str(a_level) + " per level )", True, (0, 0, 0))
        canvas.blit(text, (501, 813+5))
        text = font.render("Intelligence: " + str(intelligence) + " + " + str(items_intelligence) + " ( + " + str(i_level) + " per level )", True, (0, 0, 0))
        canvas.blit(text, (508, 847+5))
        text = font.render("HP: " + str((strength + items_strength) * 20) + " + " + str(start_hp + items_hp) + " (strength * 20)",True, (0, 0, 0))
        canvas.blit(text, (501, 875+5))
        text = font.render("Speed: " + str((agility + items_agility) / 10) + " + " + str(start_speed + items_speed) + " (agility / 10)", True, (0, 0, 0))
        canvas.blit(text, (502, 903+5))
        text = font.render("Damage: " + str(intelligence + items_intelligence) + " + " + str(start_damage + items_damage) + " (intelligence * 1)", True, (0, 0, 0))
        canvas.blit(text, (500, 931+5))

    def show(self, event):
        pos = pygame.mouse.get_pos()
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.popup_draw = True
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #return True
        else:
            self.popup_draw = False
            #return False


class Player:
    def __init__(self, player_index, index):
        self.x = 790
        self.y = 455
        self.false_x = self.x + position(player_index)[0]
        self.false_y = self.y + position(player_index)[1]
        self.index = index
        self.start_x = self.x
        self.start_y = self.y
        self.start_false_x = self.false_x
        self.start_false_y = self.false_y


        self.dir = True
        self.show = 0
        self.action = 0
        self.show_attackig = False

        self.width = 100
        self.height = 140
        # hearts
        self.hearts = 3
        # hearts
        # something
        self.attack = False
        self.m_seconds = 0
        self.reload = 30
        # something
        # levels
        self.exp = 0
        self.false_exp = 0
        self.level = 1
        # levels
        # box
        self.hitbox = [20, 30, 60, 100]
        self.attackbox = [0, 0, 100, 140]
        self.hitbox_x = 45
        self.hitbox_y = 40
        self.img_x = 45
        self.img_y = 40
        # box
        # inventory
        self.inventory = [None, None, None, None, None]
        # money
        self.money = 500
        # money
        # bets
        self.bet = 0
        self.bet_player = 0
        self.wave_add = -1
        self.bet_versus = [None, None]
        # log
        self.log_info = []
        self.log_info_money = []
         # log
        # attributes ---------------------------------------------------------------------------------------------------
        self.strength = attributes(index)[0]
        self.agility = attributes(index)[1]
        self.intelligence = attributes(index)[2]
        self.start_hp = attributes(index)[3]
        self.start_speed = attributes(index)[4]
        self.start_damage = attributes(index)[5]
        self.start_regen = attributes(index)[6]
        self.start_evasion = attributes(index)[7]
        self.start_attack_speed = attributes(index)[8]

        self.strength_level = attributes(index)[9]
        self.agility_level = attributes(index)[10]
        self.intelligence_level = attributes(index)[11]

        self.items_strength = 0
        self.items_agility = 0
        self.items_intelligence = 0

        self.items_hp = 0
        self.items_speed = 0
        self.items_damage = 0
        self.items_regen = 0
        self.items_evasion = 0
        self.items_attack_speed = 0

        # haracteristic in logic must calculate all haract.
        self.hp = 100

        self.speed = 20
        self.damage = 10
        self.max_hp = 100
        self.regen = 0
        self.evasion = 0
        self.attack_speed = 30

        # attributes ---------------------------------------------------------------------------------------------------


        self.idle = []
        self.walk = []
        self.kick = []
        self.dying = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []
        self.dying_l = []

        for i in range(0, 18):
            self.idle.append(idle[index][i])
            self.idle_l.append(idle_l[index][i])
        for i in range(0, 24):
            self.walk.append(walk[index][i])
            self.walk_l.append(walk_l[index][i])
        for i in range(0,12):
            self.kick.append(kick[index][i])
            self.kick_l.append(kick_l[index][i])
        for i in range(0,15):
            self.dying.append(dying[index][i])
            self.dying_l.append(dying_l[index][i])

        self.shadow = shadow

        self.show_box = False
    def draw(self, get_canvas, time):
        #if self.dir:
        #    get_canvas.blit(self.shadow, (self.x - self.width/2 + 5, self.y - self.height/2 + 129))
        #elif not self.dir:
        get_canvas.blit(self.shadow, (self.x - self.width/2 + 5, self.y - self.height/2 + 134))

        # pygame.draw.rect(get_canvas, (0, 255, 0), (self.x - self.width/2, self.y - self.height/2, self.width, self.height), 1)
        if self.show_box:
            # draw hit box
            pygame.draw.rect(get_canvas, (0, 0, 0), (self.x + self.hitbox[0] - self.width/2, self.y + self.hitbox[1] - self.height/2, self.hitbox[2], self.hitbox[3]), 1)
            # draw attack box
            pygame.draw.rect(get_canvas, (255, 0, 0), (self.x + self.attackbox[0] - self.width/2, self.y + self.attackbox[1] - self.height/2, self.attackbox[2], self.attackbox[3]), 1)
        # draw hp bar
        #pygame.draw.rect(get_canvas, (0, 0, 0), (self.x - 6, self.y - 21, 62, 12))
        #pygame.draw.rect(get_canvas, (0, 255, 0), (self.x - 5, self.y - 20, self.hp / (100 / 60), 10))
        if self.action == 'walk':
            if self.dir == False:
                get_canvas.blit(self.walk_l[self.show % 24], (self.x - 105, self.y - 97))
            elif self.dir == True:
                get_canvas.blit(self.walk[self.show % 24], (self.x - 95, self.y - 97))
            if time % 2 == 0:
                self.show += 1
        if self.action == 'attack':
            if self.dir == False:
                try:
                    get_canvas.blit(self.kick_l[self.show], (self.x - 105, self.y - 97))
                except:
                    self.show_attackig = False
                    self.action = 'idle'
                    self.show = 0
            elif self.dir == True:
                try:
                    get_canvas.blit(self.kick[self.show], (self.x - 95, self.y - 97))
                except:
                    self.show_attackig = False
                    self.action = 'idle'
                    self.show = 0
            if time % 2 == 0:
                self.show += 1
        if self.action == 'idle':
            if self.dir == False:
                get_canvas.blit(self.idle_l[self.show % 18], (self.x - 105, self.y - 97))
            elif self.dir == True:
                get_canvas.blit(self.idle[self.show % 18], (self.x - 95, self.y - 97))
            if time % 3 == 0:
                self.show += 1
        if self.action == 'd':
            if self.dir == False:
                try:
                    get_canvas.blit(self.dying_l[self.show], (self.x - 105, self.y - 97))
                except:
                    self.action = None
            elif self.dir == True:
                try:
                    get_canvas.blit(self.dying[self.show], (self.x - 95, self.y - 97))
                except:
                    self.action = None
            if time % 2 == 0:
                self.show += 1
    def move(self, keys, m_seconds):
        x = 0
        y = 0
        pass_x_r = False
        pass_x_l = False
        pass_y_u = False
        pass_y_d = False

        self.speed = int(self.speed)
        if self.action != 'attack':

            if keys[pygame.K_RIGHT]:
                if self.false_x + self.speed + self.width / 2 < 2090:
                    # for prmk in prmks_1:
                    #    if self.false_y in range(prmk[1] + self.speed, prmk[1] + prmk[3]):
                    #        if self.false_x + self.speed > prmk[0] and self.false_x + self.speed < prmk[0] + prmk[2]:
                    #            pass_x_r = True
                    if not pass_x_r:
                        if self.x + self.speed + self.width / 2 < 1230:
                            self.x += self.speed
                            self.false_x += self.speed
                        else:
                            self.false_x += self.speed
                            x -= self.speed
                    self.action = 'walk'
                    if self.dir != True:
                        self.dir = True
                        # self.hitbox_x = 45
                        # self.attackbox_x = 100
                        # self.hpbox_x = 45
            else:
                if self.m_seconds - self.reload + 24 < m_seconds:
                    self.action = 'idle'
            if keys[pygame.K_LEFT]:
                if self.false_x - self.speed - self.width / 2 > -410:
                    # for prmk in prmks_1:
                    #    if self.false_y in range(prmk[1] + self.speed, prmk[1] + prmk[3]):
                    #        if self.false_x - self.speed < prmk[0] + prmk[2] and self.false_x - self.speed > prmk[0]:
                    #            pass_x_l = True
                    if not pass_x_l:
                        if self.x - self.speed - self.width / 2 > 450:
                            self.x -= self.speed
                            self.false_x -= self.speed
                        else:
                            self.false_x -= self.speed
                            x += self.speed
                    self.action = 'walk'
                    if self.dir != False:
                        self.dir = False
                        # self.hitbox_x = 55
                        # self.attackbox_x = 64
                        # self.hpbox_x = 55
            if keys[pygame.K_UP]:
                if self.false_y - self.speed - self.height / 2 > -725:
                    # for prmk in prmks_1:
                    #    if self.false_x in range(prmk[0] + self.speed, prmk[0] + prmk[2]):
                    #        if self.false_y - self.speed < prmk[1] + prmk[3] and self.false_y - self.speed > prmk[1]:
                    #            pass_y_u = True
                    if not pass_y_u:
                        if self.y - self.speed - self.height / 2 > 300:
                            self.y -= self.speed
                            self.false_y -= self.speed
                        else:
                            self.false_y -= self.speed
                            y += self.speed
                self.action = 'walk'
            if keys[pygame.K_DOWN]:
                if self.false_y + self.speed + self.height / 2 < 1775:
                    # for prmk in prmks_1:
                    #    if self.false_x in range(prmk[0] + self.speed, prmk[0] + prmk[2]):
                    #        if self.false_y + self.speed > prmk[1] and self.false_y + self.speed < prmk[1] + prmk[3]:
                    #            pass_y_d = True
                    if not pass_y_d:
                        if self.y + self.speed + self.height / 2 < 750:
                            self.y += self.speed
                            self.false_y += self.speed
                        else:
                            self.false_y += self.speed
                            y -= self.speed
                self.action = 'walk'
            if keys[pygame.K_SPACE]:
                if self.m_seconds + self.reload <= m_seconds:
                    self.attack = True
                    self.m_seconds = m_seconds
                    self.action = 'attack'
                    self.show_attackig = True
                    self.show = 0

        if self.show_attackig is True and self.action == 'idle':
            self.action = 'attack'
            if self.show >= len(self.kick):
                self.show_attackig = False
        return x, y
    def attacking(self, enemy):
        if self.attack:
            if (self.x - self.width/2 + self.attackbox[0] in range(int(enemy.x) + enemy.hitbox[0], int(enemy.x) + enemy.hitbox[0] + enemy.hitbox[2]) or
                self.x - self.width/2 + self.attackbox[0] + self.attackbox[2] in range(int(enemy.x) + enemy.hitbox[0], int(enemy.x) + enemy.hitbox[0] + enemy.hitbox[2])) and(self.y - self.height/2 + self.attackbox[1] in range(int(enemy.y) + enemy.hitbox[1], int(enemy.y) + enemy.hitbox[1] + enemy.hitbox[3]) or
                 self.y - self.height/2 + self.attackbox[1] + self.attackbox[3] in range(int(enemy.y) + enemy.hitbox[1], int(enemy.y) + enemy.hitbox[1] + enemy.hitbox[3])):
                return self.damage
            elif (enemy.x + enemy.hitbox[0] in range(int(self.x - self.width/2) + self.attackbox[0], int(self.x - self.width/2) + self.attackbox[0] + self.attackbox[2]) or
                enemy.x + enemy.hitbox[0] + enemy.hitbox[2] in range(int(self.x - self.width/2) + self.attackbox[0], int(self.x - self.width/2) + self.attackbox[0] + self.attackbox[2])) and(enemy.y + enemy.hitbox[1] in range(int(self.y - self.height/2) + self.attackbox[1], int(self.y - self.height/2) + self.attackbox[1] + self.attackbox[3]) or
                 enemy.y + enemy.hitbox[1] + enemy.hitbox[3] in range(int(self.y - self.height/2) + self.attackbox[1], int(self.y - self.height/2) + self.attackbox[1] + self.attackbox[3])):
                return self.damage
            # elif
            # тут треба зробити таке сам але навпаки якщо кут хітбоксу знаходиться між кординатами атак боксу
            else:
                return 0
        else:
            return 0
    def attacking_enemy(self, enemy):
        if self.attack:
            self.attack = False
            if (self.x - self.width/2 + self.attackbox[0] in range(int(enemy.false_x) + enemy.hitbox[0], int(enemy.false_x) + enemy.hitbox[0] + enemy.hitbox[2]) or
                self.x - self.width/2 + self.attackbox[0] + self.attackbox[2] in range(int(enemy.false_x) + enemy.hitbox[0], int(enemy.false_x) + enemy.hitbox[0] + enemy.hitbox[2])) and(self.y - self.height/2 + self.attackbox[1] in range(int(enemy.false_y) + enemy.hitbox[1], int(enemy.false_y) + enemy.hitbox[1] + enemy.hitbox[3]) or
                 self.y - self.height/2 + self.attackbox[1] + self.attackbox[3] in range(int(enemy.false_y) + enemy.hitbox[1], int(enemy.false_y) + enemy.hitbox[1] + enemy.hitbox[3])):
                return self.damage
            elif (enemy.false_x + enemy.hitbox[0] in range(int(self.x - self.width/2) + self.attackbox[0], int(self.x - self.width/2) + self.attackbox[0] + self.attackbox[2]) or
                enemy.false_x + enemy.hitbox[0] + enemy.hitbox[2] in range(int(self.x - self.width/2) + self.attackbox[0], int(self.x - self.width/2) + self.attackbox[0] + self.attackbox[2])) and(enemy.false_y + enemy.hitbox[1] in range(int(self.y - self.height/2) + self.attackbox[1], int(self.y - self.height/2) + self.attackbox[1] + self.attackbox[3]) or
                 enemy.false_y + enemy.hitbox[1] + enemy.hitbox[3] in range(int(self.y - self.height/2) + self.attackbox[1], int(self.y - self.height/2) + self.attackbox[1] + self.attackbox[3])):
                return self.damage
            # elif
            # тут треба зробити таке сам але навпаки якщо кут хітбоксу знаходиться між кординатами атак боксу
            else:
                return 0
        else:
            return 0
    def restart_items(self):
        self.items_strength = 0
        self.items_agility = 0
        self.items_intelligence = 0
        self.items_hp = 0
        self.items_speed = 0
        self.items_damage = 0
        self.items_regen = 0
        self.items_evasion = 0
        self.items_attack_speed = 0
        for item_inventory in self.inventory:
            if item_inventory != None:
                for attribute in item(item_inventory)[2]:
                    if attribute == "STR":
                        self.items_strength += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "AGI":
                        self.items_agility += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "INT":
                        self.items_intelligence += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "HP":
                        self.items_hp += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "SPD":
                        self.items_speed += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "DMG":
                        self.items_damage += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]

# True - right False - left
class Players:
    def __init__(self, index):
        self.x = 0
        self.y = 0
        self.false_x = 0
        self.false_y = 0
        self.width = 100
        self.height = 140
        self.dir = True
        self.show = 0
        self.action = 0
        self.inventory = [None, None, None, None, None]
        # hearts
        self.hearts = 3
        self.idle = []
        self.walk = []
        self.kick = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []

        for i in range(0, 18):
            self.idle.append(idle[index][i])
            self.idle_l.append(idle_l[index][i])
        for i in range(0, 24):
            self.walk.append(walk[index][i])
            self.walk_l.append(walk_l[index][i])
        for i in range(0,12):
            self.kick.append(kick[index][i])
            self.kick_l.append(kick_l[index][i])

        self.shadow = shadow
    def draw(self, get_canvas):
        get_canvas.blit(self.shadow, (self.false_x + 5, self.false_y + 134))
        # pygame.draw.rect(get_canvas, (0, 0, 255), (self.false_x, self.false_y, self.width, self.height), 1)
        if self.action == 'idle':
            if self.dir == False:
                get_canvas.blit(self.idle_l[self.show % 18], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.idle[self.show % 18], (self.false_x - 45, self.false_y - 27))
        if self.action == 'walk':
            if self.dir == False:
                get_canvas.blit(self.walk_l[self.show % 24], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.walk[self.show % 24], (self.false_x - 45, self.false_y - 27))
        if self.action == 'attack':
            if self.dir == False:
                get_canvas.blit(self.kick_l[self.show % 12], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.kick[self.show % 12], (self.false_x - 45, self.false_y - 27))



class Spectator_Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.false_x = 0
        self.false_y = 0
        self.width = 100
        self.height = 140
        self.dir = True
        self.show = 0
        self.action = 0
        self.inventory = [None, None, None, None, None]
        self.max_hp = 100
        self.hp = self.max_hp
        # self.images
        self.idle = []
        self.walk = []
        self.kick = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []

        self.shadow = shadow

    def draw(self, get_canvas):
        get_canvas.blit(self.shadow, (self.false_x + 5, self.false_y + 134))

        # pygame.draw.rect(get_canvas, (0, 0, 255), (self.false_x, self.false_y, self.width, self.height))
        # draw hp bar
        pygame.draw.rect(get_canvas, (0, 0, 0), (self.false_x - 6, self.false_y - 26, 112, 17))
        pygame.draw.rect(get_canvas, (0, 255, 0), (self.false_x - 5, self.false_y - 25, self.hp / (self.max_hp / 110), 15))
        if self.action == 'idle':
            if self.dir == False:
                get_canvas.blit(self.idle_l[self.show % 18], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.idle[self.show % 18], (self.false_x - 45, self.false_y - 27))
        if self.action == 'walk':
            if self.dir == False:
                get_canvas.blit(self.walk_l[self.show % 24], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.walk[self.show % 24], (self.false_x - 45, self.false_y - 27))
        if self.action == 'attack':
            if self.dir == False:
                get_canvas.blit(self.kick_l[self.show % 12], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.kick[self.show % 12], (self.false_x - 45, self.false_y - 27))

    def re_index(self, index, level):
        strength = attributes(index)[0]
        start_hp = attributes(index)[3]
        strength_level = attributes(index)[9]
        items_strength = 0
        items_hp = 0
        for item_inventory in self.inventory:
            try:
                item_inventory = int(item_inventory)
            except:
                item_inventory = None
            if item_inventory != None:
                for attribute in item(item_inventory)[2]:
                    if attribute == "STR":
                        items_strength += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "HP":
                        items_hp += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
        if level > 1:
            strength += strength_level * (level - 1)
        self.max_hp = start_hp + (strength + items_strength) * 20 + items_hp
        # self.images change
        self.idle = []
        self.walk = []
        self.kick = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []

        for i in range(0, 18):
            self.idle.append(idle[index][i])
            self.idle_l.append(idle_l[index][i])
        for i in range(0, 24):
            self.walk.append(walk[index][i])
            self.walk_l.append(walk_l[index][i])
        for i in range(0,12):
            self.kick.append(kick[index][i])
            self.kick_l.append(kick_l[index][i])

class Enemy:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.false_x = 0
        self.false_y = 0
        self.dir = True
        self.show = 0
        self.action = 0
        self.inventory = [None, None, None, None, None]
        self.hitbox = [20, 30, 60, 100]
        self.max_hp = 100
        self.hp = self.max_hp
        # haracteristic
        self.speed = 2

        self.idle = []
        self.walk = []
        self.kick = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []

        self.show_box = False
        self.shadow = shadow
    def draw(self, get_canvas):
        get_canvas.blit(self.shadow, (self.false_x + 5, self.false_y + 134))

        #pygame.draw.rect(get_canvas, (255, 0, 0), (self.false_x, self.false_y, 100, 140))
        if self.show_box:
            # draw hit box
            pygame.draw.rect(get_canvas, (0, 0, 0), (self.false_x + self.hitbox[0], self.y + self.hitbox[1], self.hitbox[2], self.hitbox[3]), 1)

        pygame.draw.rect(get_canvas, (0, 0, 0), (self.false_x - 6, self.false_y - 26, 112, 17))
        if self.hp > 0:
            pygame.draw.rect(get_canvas, (0, 255, 0), (self.false_x - 5, self.false_y - 25, self.hp / (self.max_hp / 110), 15))
        if self.action == 'idle':
            if self.dir == False:
                get_canvas.blit(self.idle_l[self.show % 18], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.idle[self.show % 18], (self.false_x - 45, self.false_y - 27))
        if self.action == 'walk':
            if self.dir == False:
                get_canvas.blit(self.walk_l[self.show % 24], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.walk[self.show % 24], (self.false_x - 45, self.false_y - 27))
        if self.action == 'attack':
            if self.dir == False:
                get_canvas.blit(self.kick_l[self.show % 12], (self.false_x - 55, self.false_y - 27))
            elif self.dir == True:
                get_canvas.blit(self.kick[self.show % 12], (self.false_x - 45, self.false_y - 27))

    def re_index(self, index, level):
        strength = attributes(index)[0]
        start_hp = attributes(index)[3]
        strength_level = attributes(index)[9]
        items_strength = 0
        items_hp = 0
        for item_inventory in self.inventory:
            try:
                item_inventory = int(item_inventory)
            except:
                item_inventory = None
            if item_inventory != None:
                for attribute in item(item_inventory)[2]:
                    if attribute == "STR":
                        items_strength += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
                    elif attribute == "HP":
                        items_hp += item(item_inventory)[3][item(item_inventory)[2].index(attribute)]
        if level > 1:
            strength += strength_level * (level - 1)
        self.max_hp = start_hp + (strength + items_strength) * 20 + items_hp
        self.hp = self.max_hp
        # self.images change
        self.idle = []
        self.walk = []
        self.kick = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []

        for i in range(0, 18):
            self.idle.append(idle[index][i])
            self.idle_l.append(idle_l[index][i])
        for i in range(0, 24):
            self.walk.append(walk[index][i])
            self.walk_l.append(walk_l[index][i])
        for i in range(0,12):
            self.kick.append(kick[index][i])
            self.kick_l.append(kick_l[index][i])

class Bot:
    def __init__(self, index):
        self.x = -200
        self.y = -200
        if random.randint(0, 1) == 1:
            self.false_x = random.randint(0, 700)
        else:
            self.false_x = random.randint(1700, 2400)
        if random.randint(0, 1) == 1:
            self.false_y = random.randint(0, 680)
        else:
            self.false_y = random.randint(1680, 2360)

        self.width = 100
        self.height = 140

        self.action = 'walk'
        self.dir = True
        self.show = 0
        # something
        self.attack = False
        self.m_seconds = 0
        # haracteristic
        # if index
        self.color = (0, 0, 255)
        self.max_hp = give_bot(index)[0]
        self.speed = give_bot(index)[1]
        self.damage = give_bot(index)[2]
        self.reload = give_bot(index)[3]
        self.gold = give_bot(index)[4]
        self.exp = give_bot(index)[5]
        self.image = give_bot(index)[6]
        self.name = give_bot(index)[7]
        self.hp = self.max_hp



        self.idle = []
        self.walk = []
        self.kick = []
        self.dying = []

        self.walk_l = []
        self.idle_l = []
        self.kick_l = []
        self.dying_l = []

        index = self.image

        if index >= 0 and index <= 2:
            self.m_x = -70
            self.m_y = -11
            self.hitbox = [15, 20, 70, 120]
            self.attackbox = [60, 30, 85, 80]
            self.shadow = shadow
            self.shadow_m_x = 2
            self.shadow_m_y = 129
        if index >= 3 and index <= 5:
            self.m_x = -70
            self.m_y = -11
            self.hitbox = [15, 20, 70, 120]
            self.attackbox = [60, 30, 85, 80]
            self.shadow = shadow
            self.shadow_m_x = 2
            self.shadow_m_y = 129
        if index >= 6 and index <= 8:
            self.m_x = -40
            self.m_y = -16
            self.hitbox = [30, 30, 50, 65]
            self.attackbox = [60, 30, 50, 65]
            self.shadow = shadow
            self.shadow_m_x = 12
            self.shadow_m_y = 94
        if index >= 9 and index <= 11:
            self.m_x = -40
            self.m_y = -16
            self.hitbox = [30, 30, 50, 65]
            self.attackbox = [60, 30, 50, 65]
            self.shadow = shadow
            self.shadow_m_x = 12
            self.shadow_m_y = 94

        for i in range(0, 12):
            self.idle.append(idle_bot[index][i])
            self.idle_l.append(idle_l_bot[index][i])
        for i in range(0, len(walk_bot[index])):
            self.walk.append(walk_bot[index][i])
            self.walk_l.append(walk_l_bot[index][i])
        for i in range(0, 12):
            self.kick.append(attack_bot[index][i])
            self.kick_l.append(attack_l_bot[index][i])
        for i in range(0, 15):
            self.dying.append(dying_bot[index][i])
            self.dying_l.append(dying_l_bot[index][i])
        self.show_box = False
    def draw(self, get_canvas, time):
        get_canvas.blit(self.shadow, (self.x + self.shadow_m_x, self.y + self.shadow_m_y))
        if self.action != 'd':
            #pygame.draw.rect(get_canvas, self.color, (self.x, self.y, self.width, self.height))
            # draw attack box
            if self.dir:
                if self.m_y == -11:
                    self.attackbox[0] = 60
                elif self.m_y == -16:
                    self.attackbox[0] = 60

            elif not self.dir:
                if self.m_y == -11:
                    self.attackbox[0] = -45
                elif self.m_y == -16:
                    self.attackbox[0] = 0
            if self.show_box:
                # draw hit box
                pygame.draw.rect(get_canvas, (0, 0, 0),
                                 (self.x + self.hitbox[0], self.y + self.hitbox[1], self.hitbox[2], self.hitbox[3]), 1)
                pygame.draw.rect(get_canvas, (255, 0, 0),
                                 (self.x + self.attackbox[0], self.y + self.attackbox[1], self.attackbox[2],
                                  self.attackbox[3]),
                                 1)

            # draw hp bar
            pygame.draw.rect(get_canvas, (0, 0, 0), (self.x - 6, self.y - 26, 112, 17))
        if self.hp > 0:
            pygame.draw.rect(get_canvas, (0, 255, 0), (self.x - 5, self.y - 25, self.hp / (self.max_hp / 110), 15))
        elif self.hp <= 0 and self.action != 'd':
            self.action = 'd'
            self.show = 0
        #if self.action == 'idle':
        #    if self.dir == False:
        #        get_canvas.blit(self.idle_l[self.show % 12], (self.x + self.m_x, self.y + self.m_y))
        #    elif self.dir == True:
        #        get_canvas.blit(self.idle[self.show % 12], (self.x + self.m_x, self.y + self.m_y))
        #    if time % 2 == 0:
        #        self.show += 1
        if self.action == 'attack':
            if self.dir == False:
                try:
                    get_canvas.blit(self.kick_l[self.show], (self.x + self.m_x, self.y + self.m_y))
                except:
                    self.action = 'walk'
            elif self.dir == True:
                try:
                    get_canvas.blit(self.kick[self.show], (self.x + self.m_x, self.y + self.m_y))
                except:
                    self.action = 'walk'
            if time % 2 == 0:
                self.show += 1
        if self.action == 'walk':
            if self.dir == False:
                get_canvas.blit(self.walk_l[self.show % len(self.walk)], (self.x + self.m_x, self.y + self.m_y))
            elif self.dir == True:
                get_canvas.blit(self.walk[self.show % len(self.walk)], (self.x+ self.m_x, self.y + self.m_y))
            if time % 3 == 0:
                self.show += 1
        if self.action == 'd':
            if self.dir == False:
                try:
                    get_canvas.blit(self.dying_l[self.show], (self.x + self.m_x, self.y + self.m_y))
                except:
                    self.action = None
            elif self.dir == True:
                try:
                    get_canvas.blit(self.dying[self.show], (self.x + self.m_x, self.y + self.m_y))
                except:
                    self.action = None
            if time % 2 == 0:
                self.show += 1

    def attacking(self, x, y, w, h, time):
        attack = False
        # if self.action == attack and self.show == last image then action = idle
        #if self.action != attack
        if self.action == 'walk':
            if self.false_x + self.attackbox[0] + self.attackbox[2] < x and self.false_y + self.attackbox[1] + \
                    self.attackbox[3] < y:
                self.false_x += int(self.speed / 2)
                if not self.dir:
                    self.dir = True
                self.false_y += int(self.speed / 2)
            elif self.false_x + self.attackbox[0] + self.attackbox[2] < x + 5:
                self.false_x += int(self.speed / 2)
                if not self.dir:
                    self.dir = True
            elif self.false_y + self.attackbox[1] + self.attackbox[3] < y + 5:
                self.false_y += int(self.speed / 2)
            else:
                attack = True
            if self.false_x + self.attackbox[0] > x + w and self.y + self.attackbox[1] > y + h:
                self.false_x -= int(self.speed / 2)
                if self.dir:
                    self.dir = False
                self.false_y -= int(self.speed / 2)
            elif self.false_x + self.attackbox[0] > x + w - 5:
                self.false_x -= int(self.speed / 2)
                if self.dir:
                    self.dir = False
            elif self.false_y + self.attackbox[1] > y + h - 5:
                self.false_y -= int(self.speed / 2)
            else:
                if attack:
                    if time >= self.m_seconds:
                        self.action = 'attack'
                        self.m_seconds = time + self.reload
                        self.show = 0
                        self.attack = True
                        return True

        if self.attack is True and time > self.m_seconds - self.reload + 10:
            self.attack = False

font_counter_1 = pygame.font.SysFont(None, 150)
def counter(seconds, get_canvas):
    text = font_counter_1.render(str(seconds), True, (255, 0, 0))
    get_canvas.blit(text, (840 - round(text.get_width()/2), 525 - round(text.get_height()/2)))


lobby_buttons = [Button(25, 10, 50, 50, (255, 0, 0)), Button(1542, 843, 100, 34, (255, 255, 0)),
                 Button(175, 150, 75, 20, (0, 255, 255)), Button(290, 147, 25, 25, (128, 128, 128)),
                 Button(1005, 260, 25, 25, (255, 0, 0), "buttons\i4.png", "X", 25), Button(650, 600, 380, 140, (255, 0, 0), "buttons\i20.png", "Exit", 172),
                 Button(1615, 155, 30, 30, (255, 0, 0)), Button(475, 205, 30, 30, (255, 0, 0))]
#Button(650, 700, 380, 140, (255, 0, 0), "buttons\i20.png", "Exit", 172)
#Button(1115, 310, 25, 25, (255, 0, 0), "buttons\i4.png", "X", 25)
# 0 menu, 1 shop, 2 bets, 3 hide bets, 4 exit from menu, 5 exit, 6 exit shop
shop_buttons = [Button_Buy(1175, 200, 82, 56, 0), Button_Buy(1267, 200, 82, 56, 1), Button_Buy(1359, 200, 82, 56, 2), Button_Buy(1451, 200, 82, 56, 3), Button_Buy(1543, 200, 82, 56, 4),
                Button_Buy(1175, 266, 82, 56, 5), Button_Buy(1267, 266, 82, 56, 6), Button_Buy(1359, 266, 82, 56, 7), Button_Buy(1451, 266, 82, 56, 8), Button_Buy(1543, 266, 82, 56, 9),
                Button_Buy(1175, 332, 82, 56, 10), Button_Buy(1267, 332, 82, 56, 11), Button_Buy(1359, 332, 82, 56, 12), Button_Buy(1451, 332, 82, 56, 13), Button_Buy(1543, 332, 82, 56, 14),
                Button_Buy(1175, 396, 82, 56, 15), Button_Buy(1267, 396, 82, 56, 16), Button_Buy(1359, 396, 82, 56, 17), Button_Buy(1451, 396, 82, 56, 18), Button_Buy(1543, 396, 82, 56, 19),
                Button_Buy(1175, 464, 82, 56, 20), Button_Buy(1267, 464, 82, 56, 21), Button_Buy(1359, 464, 82, 56, 22), Button_Buy(1451, 464, 82, 56, 23), Button_Buy(1543, 464, 82, 56, 24),
                Button_Buy(1175, 530, 82, 56, 25), Button_Buy(1267, 530, 82, 56, 26), Button_Buy(1359, 530, 82, 56, 27), Button_Buy(1451, 530, 82, 56, 28), Button_Buy(1543, 530, 82, 56, 29)
                #,Button_Buy(1175, 596, 82, 56, 30), Button_Buy(1267, 596, 82, 56, 31), Button_Buy(1359, 596, 82, 56, 32), Button_Buy(1451, 596, 82, 56, 33), Button_Buy(1543, 596, 82, 56, 34),
                #Button_Buy(1175, 662, 82, 56, 35), Button_Buy(1267, 662, 82, 56, 36), Button_Buy(1359, 662, 82, 56, 37), Button_Buy(1451, 662, 82, 56, 38), Button_Buy(1543, 662, 82, 56, 39),
                #Button_Buy(1175, 728, 82, 56, 40), Button_Buy(1267, 728, 82, 56, 41), Button_Buy(1359, 728, 82, 56, 42), Button_Buy(1451, 728, 82, 56, 43), Button_Buy(1543, 728, 82, 56, 44)
                ]

spectator_button = Button(175, 160, 75, 20, (255, 0, 0))

hit_box_button = Button(650, 450, 380, 140, (255, 255, 0), "buttons\i20.png", "Hit Box", 102)

toucher = Toucher(110, 710, 25, 25, (255, 0, 0), 300)
bets_buttons = [Button(70, 750, 90, 60), Button(360, 750, 90, 60)]

#attributes show
show_attributes = Attributes_Info()

canvas = Canvas(500, 500)
clock = pygame.time.Clock()
game_background = pygame.image.load("game_background/i4.png")

font = pygame.font.SysFont(None, 25)
font_B = pygame.font.SysFont(None, 36)

background_player_1 = pygame.image.load("game_background/b1.png")
background_player_2 = pygame.transform.scale(pygame.image.load("game_background/b2.png"), (250, 200))
background_player_3 = pygame.transform.scale(pygame.image.load("game_background/b2.png"), (290, 250))
background_player_4 = pygame.transform.scale(pygame.image.load("game_background/b3.png"), (300, 300))
background_player_5 = pygame.transform.scale(pygame.image.load("game_background/b3.png"), (960, 540))
background_player_6 = pygame.transform.scale(pygame.image.load("game_background/b4.png"), (500, 500))
background_player_7 = pygame.transform.scale(pygame.image.load("game_background/b4.png"), (500, 650))

background_player_1 = pygame.transform.scale(background_player_1, (155, 155))
background_item_small = pygame.image.load("assets/bg.png")
background_item_small_2 = pygame.transform.scale(background_item_small, (50, 50))


background_item_small = pygame.transform.scale(background_item_small, (25, 25))

items_icon_small = []
items_icon_small_2 = []
for cycle_index in range(len(items_icon)):
    items_icon_small.append(pygame.transform.scale(items_icon[cycle_index], (25, 25)))
    items_icon_small_2.append(pygame.transform.scale(items_icon[cycle_index], (50, 50)))

def game_s(player_index, index, net):
    inventory_buttons = [Button_Sell(1365, 885, 90, 60), Button_Sell(1455, 885, 90, 60), Button_Sell(1545, 885, 90, 60),
                         Button_Sell(1365, 945, 90, 60), Button_Sell(1455, 945, 90, 60)]
    wave = 1
    m_seconds = 0
    # players in lobby
    bots = []
    # bots when player_index != player versus
    # enemy when player_index == player versus

    one_time = True

    run = True
    ready = True
    bots_generate = True

    spectator = False
    menu = False
    shop = False
    bets = False

    map = [-410 - position(player_index)[0], -725 - position(player_index)[1]]
    start_map = [-410 - position(player_index)[0], -725 - position(player_index)[1]]

    player_bets = []

    player = Player(player_index, index)
    enemy = Enemy()
    spectator_players = [Spectator_Player(), Spectator_Player()]
    error = True
    while error:
        try:
            game = net.send("get")
        except:
            run = False
        try:
            if player_index == 0:
                players = [Players(int(game.player[1].split('#')[1])), Players(int(game.player[2].split('#')[1]))]
            elif player_index == 1:
                players = [Players(int(game.player[0].split('#')[1])), Players(int(game.player[2].split('#')[1]))]
            elif player_index == 2:
                players = [Players(int(game.player[0].split('#')[1])), Players(int(game.player[1].split('#')[1]))]
            error = False
        except:
            continue
    while run:
        clock.tick(60)
        try:
            game = net.send("get")
        except:
            run = False
            print("Couldn't get game")
            print('leave?')
            break
        if game.bothWent():
            try:
                game = net.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break
        #lobby = game.lobby

        # one time on start
        if one_time:
            players_q = []
            for cycle_index in game.player:
                if cycle_index != None:
                    players_q.append(int(cycle_index.split('#')[1]))
                else:
                    players_q.append(None)
        # one time on start

        # send ---------------------------------------------------------------------------------------------------------
        if game.lobby is True:
            if player_index == game.versus[0] or player_index == game.versus[1]:
                # data = "x:5#y:10#move#item1#item2#item3#item4#item5#bet#betamount"
                data = str(int(player.false_x)+360) + '#' + str(int(player.false_y)+655) + '#' + str(player.dir) + '#' + str(player.action) + '#' + str(
                    player.show) + '#' + str(int(player.bet)) + '#' + str(player.bet_player) + '#' + str(player.inventory[0]) + '#' + str(player.inventory[1]) + '#' + str(player.inventory[2]) + '#' + str(player.inventory[3]) + '#' + str(player.inventory[4]) + '#' + str(player.level)

            else:
                # ++++++#item1#item2#item3#item4#item5"
                data = str(int(player.false_x)+360) + '#' + str(int(player.false_y)+655) + '#' + str(player.dir) + '#' + str(player.action) + '#' + str(
                    player.show) + '#' + str(int(player.bet)) + '#' + str(player.bet_player)
                    #   + '#' + str(p.inventory[0]) + '#' + str(p.inventory[1]) + '#' + str(
                    #p.inventory[2]) + '#' + str(p.inventory[3]) + '#' + str(p.inventory[4])
        if game.lobby is False:
            if player_index == game.versus[0] or player_index == game.versus[1]:
                data = str(int(player.false_x)+360) + '#' + str(int(player.false_y)+655) + '#' + str(player.dir) + '#' + str(player.action) + '#' + str(
                    player.show) + '#' + str(enemy.hp)
            else:
                data = '200#200#left#idle'
        if game.lobby is False and ready is True:
            ready = False
            data = 'r'
        if game.hearts[player_index] == 0 and game.f_win == None:
            data = "-10000#-1000#0#0#0#0#0"
        net.send(data)
        # send ---------------------------------------------------------------------------------------------------------
        # rec ----------------------------------------------------------------------------------------------------------
        server_data = []

        if game.lobby is True:
            try:
                server_data.append(game.player_lobby[0].split('#'))
                server_data.append(game.player_lobby[1].split('#'))
                server_data.append(game.player_lobby[2].split('#'))
            except:
                server_data.append([200, 200, 'left', 'idle', 0, 0, 2])
                server_data.append([200, 200, 'left', 'idle', 0, 0, 2])
                server_data.append([200, 200, 'left', 'idle', 0, 0, 2])
                print('start')
            #try:
                #if len(bots) == 0:
            if bots_generate and game.start_time - game.time < 20:
                try:
                    bots = []
                    for cycle_index in range(0, int(game.bots.split('#')[1])):
                        bots.append(Bot(int(game.bots.split('#')[0])))
                    bots_generate = False
                except:
                    pass

            try:
                index = 0
                bets_game = []
                player_bets = []
                for cycle_index in range(0, 3):
                    if int(cycle_index) != int(player_index):
                        players[index].x = int(server_data[cycle_index][0])
                        players[index].y = int(server_data[cycle_index][1])
                        if server_data[cycle_index][2] == 'True':
                            players[index].dir = True
                        elif server_data[cycle_index][2] == 'False':
                            players[index].dir = False
                        players[index].action = str(server_data[cycle_index][3])
                        players[index].show = int(server_data[cycle_index][4])
                        index += 1
                    bets_game.append(int(server_data[cycle_index][5]))
                    player_bets.append(int(server_data[cycle_index][6]))
                    if player_index == game.versus[0] or player_index == game.versus[1]:
                        if player_index == game.versus[0] and cycle_index == game.versus[1]:
                            enemy.inventory[0] = server_data[cycle_index][7]
                            enemy.inventory[1] = server_data[cycle_index][8]
                            enemy.inventory[2] = server_data[cycle_index][9]
                            enemy.inventory[3] = server_data[cycle_index][10]
                            enemy.inventory[4] = server_data[cycle_index][11]
                            enemy.re_index(players_q[game.versus[1]], int(server_data[cycle_index][12]))
                        elif player_index == game.versus[1] and cycle_index == game.versus[0]:
                            enemy.inventory[0] = server_data[cycle_index][7]
                            enemy.inventory[1] = server_data[cycle_index][8]
                            enemy.inventory[2] = server_data[cycle_index][9]
                            enemy.inventory[3] = server_data[cycle_index][10]
                            enemy.inventory[4] = server_data[cycle_index][11]
                            enemy.re_index(players_q[game.versus[0]], int(server_data[cycle_index][12]))
                    # elif player_index != game.versus[0] and player_index != game.versus[1]:
                    if cycle_index == game.versus[0]:
                        spectator_players[0].inventory[0] = server_data[cycle_index][7]
                        spectator_players[0].inventory[1] = server_data[cycle_index][8]
                        spectator_players[0].inventory[2] = server_data[cycle_index][9]
                        spectator_players[0].inventory[3] = server_data[cycle_index][10]
                        spectator_players[0].inventory[4] = server_data[cycle_index][11]
                        spectator_players[0].re_index(players_q[game.versus[0]], int(server_data[cycle_index][12]))
                    elif cycle_index == game.versus[1]:
                        spectator_players[1].inventory[0] = server_data[cycle_index][7]
                        spectator_players[1].inventory[1] = server_data[cycle_index][8]
                        spectator_players[1].inventory[2] = server_data[cycle_index][9]
                        spectator_players[1].inventory[3] = server_data[cycle_index][10]
                        spectator_players[1].inventory[4] = server_data[cycle_index][11]
                        spectator_players[1].re_index(players_q[game.versus[1]], int(server_data[cycle_index][12]))
            except:
                pass

        elif game.lobby is False:
            if player_index == game.versus[0] or player_index == game.versus[1]:
                if player_index == game.versus[0]:
                    server_data = game.player_lobby[game.versus[1]].split('#')
                    # if game.versus[0] ==
                    try:
                        enemy.x = int(server_data[0])
                        enemy.y = int(server_data[1])
                        if server_data[2] == 'True':
                            enemy.dir = True
                        elif server_data[2] == 'False':
                            enemy.dir = False
                        enemy.action = str(server_data[3])
                        enemy.show = int(server_data[4])
                        player.hp = int(server_data[5])
                    except:
                        pass
                elif player_index == game.versus[1]:
                    server_data = game.player_lobby[game.versus[0]].split('#')
                    try:
                        enemy.x = int(server_data[0])
                        enemy.y = int(server_data[1])
                        if server_data[2] == 'True':
                            enemy.dir = True
                        elif server_data[2] == 'False':
                            enemy.dir = False
                        enemy.action = str(server_data[3])
                        enemy.show = int(server_data[4])
                        player.hp = int(server_data[5])
                    except:
                        pass
            else:
                if spectator:
                    try:
                        server_data = game.player_lobby[game.versus[0]].split('#')
                        spectator_players[0].x = int(server_data[0])
                        spectator_players[0].y = int(server_data[1])
                        if server_data[2] == 'True':
                            spectator_players[0].dir = True
                        elif server_data[2] == 'False':
                            spectator_players[0].dir = False
                        spectator_players[0].action = str(server_data[3])
                        spectator_players[0].show = int(server_data[4])
                        spectator_players[1].hp = int(server_data[5])

                        server_data = game.player_lobby[game.versus[1]].split('#')
                        spectator_players[1].x = int(server_data[0])
                        spectator_players[1].y = int(server_data[1])
                        if server_data[2] == 'True':
                            spectator_players[1].dir = True
                        elif server_data[2] == 'False':
                            spectator_players[1].dir = False
                        spectator_players[1].action = str(server_data[3])
                        spectator_players[1].show = int(server_data[4])
                        spectator_players[0].hp = int(server_data[5])
                    except:
                        pass
        # rec ----------------------------------------------------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if lobby_buttons[0].click(event):
                menu = True
            if game.lobby:
                if lobby_buttons[1].click(event):
                    shop = True
                if lobby_buttons[2].click(event):
                    bets = True
            if lobby_buttons[3].click(event):
                if lobby_buttons[3].y == 147:
                    lobby_buttons[3].y = 90
                    lobby_buttons[2].y = 93
                    spectator_button.y = 103
                elif lobby_buttons[3].y == 90:
                    lobby_buttons[3].y = 147
                    lobby_buttons[2].y = 150
                    spectator_button.y = 160
            if menu:
                if lobby_buttons[4].click(event):
                    menu = False
                if hit_box_button.click(event):
                    if player.show_box:
                        player.show_box = False
                        enemy.show_box = False
                        hit_box_button.color = (255, 255, 0)
                    else:
                        player.show_box = True
                        enemy.show_box = True
                        hit_box_button.color = (255, 0, 255)
                if lobby_buttons[5].click(event):
                    run = False
            if shop and game.lobby:
                for buttons_click in shop_buttons:
                    if buttons_click.click(event):
                        if player.money - item(shop_buttons.index(buttons_click))[1] >= 0:
                            for inventory_cycle in player.inventory:
                                if inventory_cycle != None:
                                    continue
                                elif inventory_cycle == None:
                                    # bye
                                    # btns_shop_sell[self.inventory.index(inventory)].get_info(btns_shop.index(button_shop),int(time / 60))
                                    #shop_buttons_sell[
                                    #    player.inventory.index(inventory_cycle)].item_index = shop_buttons.index(
                                    #    buttons_click)
                                    #btns_inventory[self.inventory.index(inventory)].get_info(btns_shop.index(button_shop),int(time / 60))
                                    inventory_buttons[player.inventory.index(inventory_cycle)].item_index = shop_buttons.index(buttons_click)
                                    # self.inventory_time[self.inventory.index(inventory)] = int(time / 60)
                                    player.inventory[player.inventory.index(inventory_cycle)] = shop_buttons.index(buttons_click)
                                    player.money -= item(shop_buttons.index(buttons_click))[1]
                                    # self.restart()
                                    # update haracterisitcs
                                    player.restart_items()
                                    break
                if lobby_buttons[6].click(event):
                    shop = False
            if bets and game.lobby:
                if player_index != game.versus[0] and player_index != game.versus[1]:
                    # toucher
                    toucher.touch(event)
                    for buttons_click in bets_buttons:
                        if buttons_click.click(event):
                            if player.money - int((toucher.x - toucher.start_x) / toucher.long * player.money) >= 0:
                                # update bets
                                player.bet += int((toucher.x - toucher.start_x) / toucher.long * player.money)
                                player.wave_add = game.wave + 1
                                player.bet_player = bets_buttons.index(buttons_click)
                                player.bet_versus[0] = game.versus[0]
                                player.bet_versus[1] = game.versus[1]
                                # update money
                                player.money -= int((toucher.x - toucher.start_x) / toucher.long * player.money)
                                # return toucher to start
                                toucher.x = toucher.start_x
                                toucher.rect.x = toucher.start_x
                if lobby_buttons[7].click(event):
                    bets = False
            # selling
            if game.lobby:
                for buttons_click in inventory_buttons:
                    if buttons_click.click(event) and player.inventory[inventory_buttons.index(buttons_click)] != None:
                        # sell
                        # shop_buttons_sell[shop_buttons_sell.index(buttons_click)].get_info(20, None)
                        # btns_inventory[btns_shop_sell.index(button_shop)].get_info(20, None)
                        # if int(time / 60) - self.inventory_time[btns_shop_sell.index(button_shop)] <= 10:
                        player.money += item(buttons_click.item_index)[1]
                        # else:
                        #    self.money += int(price[self.inventory[btns_shop_sell.index(button_shop)]] / 2)
                        # player.inventory_time[btns_shop_sell.index(button_shop)] = None
                        player.inventory[inventory_buttons.index(buttons_click)] = None
                        # shop_buttons_sell[shop_buttons_sell.index(buttons_click)].item_index = None
                        inventory_buttons[inventory_buttons.index(buttons_click)].item_index = None
                        # self.restart()
                        # update harcteristics
                        player.restart_items()
                        break
            # spectator buttons---------------------------------------------------------------------------------------------
            if not game.lobby and not spectator:
                if player_index != game.versus[0] and player_index != game.versus[1] and game.player_ready[player_index]:
                    if spectator_button.click(event):
                        spectator = True
                        map[0] = -410
                        map[1] = -725

            # spectator buttons---------------------------------------------------------------------------------------------
            # attribytes show info -------------------
            if not spectator:
                show_attributes.show(event)
            # attribytes show info -------------------

        keys = pygame.key.get_pressed()
        # moving camara when spectator
        if spectator and not game.lobby:
            if keys[pygame.K_UP]:
                map[1] += 5
            if keys[pygame.K_DOWN]:
                map[1] -= 5
            if keys[pygame.K_LEFT]:
                map[0] += 5
            if keys[pygame.K_RIGHT]:
                map[0] -= 5
        # movement
        if not spectator and player.hp > 0:
            movement = player.move(keys, m_seconds)
            map[0] += movement[0]
            map[1] += movement[1]
        # logic --------------------------------------------------------------------------------------------------------
        m_seconds += 1
        ready = False
        if not game.lobby:
            bots_generate = True
        if game.lobby:
            spectator = False
        if not game.lobby:
            # if player kill all bots then bots = None if player hp < 0 bots = None
            if (player_index == game.versus[0] or player_index == game.versus[1]) and not game.player_ready[
                player_index]:
                bots = []
                enemy.hp -= player.attacking_enemy(enemy)
                if enemy.hp < 0:
                    ready = True
            elif player_index != game.versus[0] and player_index != game.versus[1] and not game.player_ready[player_index]:
                for bot_attacking in bots:
                    if (
                    bot_attacking.attacking(player.hitbox[0] + player.false_x + 360, player.hitbox[1] + player.false_y + 655, player.hitbox[2],
                                            player.hitbox[3], m_seconds)):
                        player.hp -= bot_attacking.damage
                for bot_attacking in bots:
                    attack_damage = player.attacking(bot_attacking)
                    if attack_damage > 0:
                        bot_attacking.hp -= attack_damage
                        player.attack = False
                        break
                    if bots.index(bot_attacking) == len(bots)-1:
                        player.attack = False
                for bot_attacking in bots:
                    if bot_attacking.action == None:
                        player.exp += bots[bots.index(bot_attacking)].exp
                        player.money += bots[bots.index(bot_attacking)].gold

                        bots.pop(bots.index(bot_attacking))
                if len(bots) == 0 or player.hp <= 0:
                    bots = []
                    player.hp = 0
                    ready = True
        if game.lobby:
            # add money
            sum_bets_player0 = 0
            sum_bets_player1 = 0
            for cycle_index in range(0, len(player_bets)):
                if player_bets[cycle_index] == 0:
                    sum_bets_player0 += bets_game[cycle_index]
                if player_bets[cycle_index] == 1:
                    sum_bets_player1 += bets_game[cycle_index]
            if player.wave_add == game.wave and game.wave > 0:
                # player.money
                if player.bet_versus[player.bet_player] == game.winner:
                    if player.bet_player == 0:
                        #try:
                        player.money += int(player.bet * (sum_bets_player0 / (sum_bets_player0 + sum_bets_player1)))
                        player.log_info.append("You win "+str(int(player.bet * (sum_bets_player0 / (sum_bets_player0 + sum_bets_player1))))+" for make a bet")
                        #except:
                            #player.money += player.bet
                            #player.log_info.append("You win " + str(player.bet) + " for make a bet")

                    elif player.bet_player == 1:
                        # try:
                        player.money += int(player.bet * (sum_bets_player1 / (sum_bets_player0 + sum_bets_player1)))
                        player.log_info.append("You win "+str(int(player.bet * (sum_bets_player1 / (sum_bets_player0 + sum_bets_player1))))+" for make a bet")
                        #except:
                        # player.money += player.bet
                        #    player.log_info.append("You win " + str(player.bet) + " for make a bet")
                if game.winner == 20 and player.bet > 0:
                    player.money += player.bet
                    player.log_info.append("You win " + str(player.bet) + " for make a bet")

                # clear
                player.wave_add = 0
                player.bet = 0
                player.bet_player = 0
                player.bet_versus = [None, None]

            # add to log who will fight
            if wave != game.wave and m_seconds > 10:
                if game.wave > 0:
                    if game.winner != 20:
                        player.log_info.append("In "+str(game.wave)+" wave win " + str(game.player[game.winner]))
                    else:
                        player.log_info.append("In "+str(game.wave)+" wave noone win")
                if player_index == game.versus[0] or player_index == game.versus[1]:
                    if player_index == game.versus[0]:
                        player.log_info.append("In this wave you will fight vs " + str(game.player[game.versus[1]]))
                    elif player_index == game.versus[1]:
                        player.log_info.append("In this wave you will fight vs " + str(game.player[game.versus[0]]))
                elif player_index != game.versus[0] and player_index != game.versus[1]:
                    # print(game.player)
                    player.log_info.append("In this wave " + str(game.player[game.versus[0]])+" will fight vs "+str(game.player[game.versus[1]]))
                    player.log_info.append("You will fight vs " + str(game.bots))
                wave = game.wave
            # log  lenght
            if len(player.log_info) > 5:
                player.log_info.pop(0)

        # players x,y ------------------------------------
        if game.lobby:
            for cycle_index in players:
                cycle_index.false_x = map[0] + cycle_index.x
                cycle_index.false_y = map[1] + cycle_index.y
        # bots x,y ------------------------------------
        if not game.lobby and player_index != game.versus[0] and player_index != game.versus[1]:
            for cycle_index in bots:
                cycle_index.x = map[0] + cycle_index.false_x
                cycle_index.y = map[1] + cycle_index.false_y
        # enemy x,y ------------------------------------
        if not game.lobby and (player_index == game.versus[0] or player_index == game.versus[1]):
            enemy.false_x = map[0] + enemy.x
            enemy.false_y = map[1] + enemy.y
        if not game.lobby and spectator:
            for cycle_index in spectator_players:
                cycle_index.false_x = map[0] + cycle_index.x
                cycle_index.false_y = map[1] + cycle_index.y
        # on start---
        if game.time == game.start_time:
            player.x = 790
            player.y = 455
            if player_index != game.versus[0] and player_index != game.versus[1]:
                player.false_x = 790
                player.false_y = 455
                map[0] = -410
                map[1] = -725
            elif player_index == game.versus[0]:
                player.false_x = 690
                player.false_y = 455
                player.dir = True
                map[0] = -310
                map[1] = -725
            elif player_index == game.versus[1]:
                player.false_x = 890
                player.false_y = 455
                player.dir = False
                map[0] = -510
                map[1] = -725

        elif game.time == game.start_time - 30:
            player.x = player.start_x
            player.y = player.start_y
            player.false_x = player.start_false_x
            player.false_y = player.start_false_y
            map[0] = start_map[0]
            map[1] = start_map[1]
        # on start---
        # players x,y ------------------------------------
        # levels ------------------------------------------
        if player.exp != player.false_exp:
            player.false_exp = player.exp
            if player.level != 10 and player.exp >= levels[player.level]:
                player.level += 1
                player.strength += player.strength_level
                player.agility += player.agility_level
                player.intelligence += player.intelligence_level
        # levels ------------------------------------------
        # all attributes ----------------------------------
        if game.lobby:

            player.max_hp = player.start_hp + (player.strength + player.items_strength) * 20 + player.items_hp
            player.speed = player.start_speed + (player.agility + player.items_agility) / 10 + player.items_speed
            player.damage = player.start_damage + (player.intelligence + player.items_intelligence) + player.items_damage

            player.regen = player.start_regen + (player.strength + player.items_strength) + player.items_regen
            player.evasion = player.start_evasion + (player.agility + player.items_agility) + player.items_evasion
            player.attack_speed = player.start_attack_speed + (player.intelligence + player.items_intelligence) + player.items_attack_speed
        # all attributes ----------------------------------
        if game.lobby:
            player.hp = player.max_hp

        # logic --------------------------------------------------------------------------------------------------------
        canvas.draw_background()
        # draw map -----------------------------------------------------------------------------------------------------
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (0, 0, 1680, 1050))
        pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (map[0], map[1], 2500, 2500))
        # if game.lobby:
        canvas.get_canvas().blit(game_background, (map[0]-500, map[1]))

        # draw map -----------------------------------------------------------------------------------------------------
        # draw players -------------------------------------------------------------------------------------------------
        #if not spectator and not game.lobby:
        #    player.draw(canvas.get_canvas(), m_seconds)
        # lobby players
        if game.lobby:
            # sorting
            f_l = [players[0].false_y, players[1].false_y, player.y - int(player.height/2)]
            f_l.sort()

            draw_player = True
            for cycle_index in range(0, len(players)+1):
                if f_l[cycle_index] == player.y - int(player.height/2) and draw_player:
                    player.draw(canvas.get_canvas(), m_seconds)
                    draw_player = False
                    continue
                else:
                    for players_y in players:
                        if f_l[cycle_index] == players_y.false_y:
                            # draw others
                            players_y.draw(canvas.get_canvas())
            # sorting

        # draw bots:
        elif not game.lobby and not spectator:
            if player_index != game.versus[0] and player_index != game.versus[1] and not game.player_ready[player_index]:
                f_l = [player.y - int(player.height / 2)]
                if len(bots) > 0:
                    for player_draw in bots:
                        f_l.append(player_draw.y)
                    #player_draw.draw(canvas.get_canvas(), m_seconds)
                #player.draw(canvas.get_canvas(), m_seconds)

                # sorting
                f_l.sort()
                draw_player = True
                for cycle_index in range(0, len(bots) + 1):
                    if f_l[cycle_index] == player.y - int(player.height / 2) and draw_player:
                        player.draw(canvas.get_canvas(), m_seconds)
                        draw_player = False
                        continue
                    else:
                        for players_y in bots:
                            if f_l[cycle_index] == players_y.y:
                                # draw others
                                players_y.draw(canvas.get_canvas(), m_seconds)
                # sorting

            if player_index == game.versus[0] or player_index == game.versus[1]:
                if enemy.false_y > player.y - int(player.height / 2):
                    player.draw(canvas.get_canvas(), m_seconds)
                    enemy.draw(canvas.get_canvas())
                elif enemy.false_y <= player.y - int(player.height / 2):
                    enemy.draw(canvas.get_canvas())
                    player.draw(canvas.get_canvas(), m_seconds)
        # spectator
        if spectator and player_index != game.versus[0] and player_index != game.versus[1] and not (game.player_ready[game.versus[0]] and game.player_ready[game.versus[1]]):
#            for players_draw in spectator_players:
#                players_draw.draw(canvas.get_canvas())
            f_l = []
            for players_draw in spectator_players:
                #players_draw.draw(canvas.get_canvas())
            #for player_draw in bots:
                f_l.append(players_draw.false_y)
                # player_draw.draw(canvas.get_canvas(), m_seconds)
            # player.draw(canvas.get_canvas(), m_seconds)
            # sorting
            f_l.sort()
            for cycle_index in range(0, len(spectator_players)):
                for players_y in spectator_players:
                    if f_l[cycle_index] == players_y.false_y:
                        # draw others
                        players_y.draw(canvas.get_canvas())
            # sorting
        elif (spectator or (player_index == game.versus[0] or player_index == game.versus[1])) and (game.player_ready[game.versus[0]] and game.player_ready[game.versus[1]]):
            text = font.render("Waiting for other players ...", True, (0, 0, 0))
            canvas.get_canvas().blit(text, (840 - round(text.get_width() / 2), 525 - round(text.get_height() / 2)))
        # draw players -------------------------------------------------------------------------------------------------
        # top ----------------------------------------------------------------------------------------------------------
        lobby_buttons[0].draw(canvas.get_canvas())
        pygame.draw.rect(canvas.get_canvas(), (128, 0, 0), (25, 10, 50, 50), 1)
        x = 835 - (3 - 1) * 50
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (343, 0, 984, 88))
        for i in range(0, 3):
            if game.hearts[i] > 0:
                pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (x, 10, 75, 75))
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (x, 10, 75, 75), 1)
                if players_q[i] != None:
                    pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (x+1, 11, 73, 73))
                    if not game.lobby and game.player_ready[i]:
                        # ready
                        pygame.draw.rect(canvas.get_canvas(), (255, 255, 0), (x + 1, 11, 73, 73))
                    if not game.lobby and not game.player_ready[i]:
                        # not ready
                        pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (x + 1, 11, 73, 73))
                    canvas.get_canvas().blit(choise_images_icon[players_q[i]], (x-10, -5))
            x += 100
        # level player on right
        if not spectator:
            #pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (1350, 10, 300, 400))
            #pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (1350, 10, 300, 400), 1)
            # draw right mini-log
            text = font.render("Wave:" + str(game.wave), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (1485 - round(text.get_width() / 2), 20))
            if player_index == game.versus[0]:
                text = font.render("Your enemy is " + str(game.player[game.versus[1]]), True, (0, 0, 0))
                canvas.get_canvas().blit(text, (1485 - round(text.get_width() / 2), 40))
            if player_index == game.versus[1]:
                text = font.render("Your enemy is " + str(game.player[game.versus[0]]), True, (0, 0, 0))
                canvas.get_canvas().blit(text, (1485 - round(text.get_width() / 2), 40))
            if player_index != game.versus[0] and player_index != game.versus[1]:
                if game.bots != None:
                    try:
                        text = font.render("Your enemy is " + str(len(bots))+ " " +str(bots[0].name)+"'s", True, (0, 0, 0))
                        canvas.get_canvas().blit(text, (1485 - round(text.get_width() / 2), 40))
                    except:
                        pass
            y_cycle = 65
            for log_info_draw in player.log_info:
                text = font.render(log_info_draw, True, (0, 0, 0))
                canvas.get_canvas().blit(text, (1360, y_cycle))
                # text = font.render(str(player.log_info_money[player.log_info.index(log_info_draw)]), True, (0, 0, 0))
                # canvas.get_canvas().blit(text, (55, y_cycle))
                y_cycle += 25

        # draw time
        pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (800, 88, 70, 30))
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (800, 88, 70, 30), 1)
        if game.lobby:
            text = font.render("0:" + str(game.start_time - game.time), True, (0, 0, 0))
            if game.start_time - game.time <= 3 and game.start_time - game.time >= 1:
                counter(game.start_time - game.time, canvas.get_canvas())
        else:
            text = font.render("0:" + str(60 - game.time + game.start_time), True, (0, 0, 0))
            if (60 - game.time + game.start_time) <= 3 and (60 - game.time + game.start_time) >= 1:
                counter((60 - game.time + game.start_time), canvas.get_canvas())
        canvas.get_canvas().blit(text, (835 - round(text.get_width()/2), 103 - round(text.get_height()/2)))
        # top ----------------------------------------------------------------------------------------------------------
        # bets ---------------------------------------------------------------------------------------------------------
        if lobby_buttons[3].y == 147:
            canvas.get_canvas().blit(background_player_4, (100, 10), (20, 20, 225, 150))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (100, 10, 225, 150), 1)

        if lobby_buttons[3].y == 90:
            canvas.get_canvas().blit(background_player_4, (100, 10), (20, 20, 225, 93))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (100, 10, 225, 93), 1)
        if game.lobby:
            lobby_buttons[2].draw(canvas.get_canvas())
        lobby_buttons[3].draw(canvas.get_canvas())
        # versus players
        try:
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (125, 15, 50, 50))
            canvas.get_canvas().blit(choise_images_icon[players_q[game.versus[0]]], (125, 15), (22, 20, 50, 50))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (125, 15, 50, 50), 1)
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (250, 15, 50, 50))
            canvas.get_canvas().blit(choise_images_icon[players_q[game.versus[1]]], (250, 15), (22, 20, 50, 50))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (250, 15, 50, 50), 1)
        except:
            pass
        try:
            if sum_bets_player0 != None:
                pass
        except:
            sum_bets_player0 = 0
            sum_bets_player1 = 0
        if lobby_buttons[3].y == 147:
            x = 113
            for i in range(0, 3):
                canvas.get_canvas().blit(background_item_small, (x, 70))
                try:
                    if int(spectator_players[0].inventory[i]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(items_icon_small[item(int(spectator_players[0].inventory[i]))[4] - 1], (x, 70))
                        except:
                            text = font.render(str(spectator_players[0].inventory[i]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                            x + 12 - round(text.get_width() / 2), 82 - round(text.get_height() / 2)))
                except:
                    pass
                x += 25
            x = 125
            for i in range(0, 2):
                canvas.get_canvas().blit(background_item_small, (x, 95))
                try:
                    if int(spectator_players[0].inventory[i+3]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(items_icon_small[item(int(spectator_players[0].inventory[i+3]))[4] - 1], (x, 95))
                        except:
                            text = font.render(str(spectator_players[0].inventory[i+3]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                            x + 12 - round(text.get_width() / 2), 107 - round(text.get_height() / 2)))
                except:
                    pass
                x += 25
            x = 237
            for i in range(0, 3):
                canvas.get_canvas().blit(background_item_small, (x, 70))
                try:
                    if int(spectator_players[1].inventory[i]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(items_icon_small[item(int(spectator_players[1].inventory[i]))[4] - 1], (x, 70))
                        except:
                            text = font.render(str(spectator_players[1].inventory[i]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                            x + 12 - round(text.get_width() / 2), 82 - round(text.get_height() / 2)))
                except:
                    pass
                x += 25
            x = 250
            for i in range(0, 2):
                canvas.get_canvas().blit(background_item_small, (x, 95))
                try:
                    if int(spectator_players[1].inventory[i+3]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(items_icon_small[item(int(spectator_players[1].inventory[i+3]))[4] - 1], (x, 95))
                        except:
                            text = font.render(str(spectator_players[1].inventory[i+3]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                            x + 12 - round(text.get_width() / 2), 107 - round(text.get_height() / 2)))
                except:
                    pass
                x += 25
            text = font.render("$ " + str(sum_bets_player0), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (150 - round(text.get_width() / 2), 125))
            text = font.render("$ " + str(sum_bets_player1), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (275 - round(text.get_width() / 2), 125))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (290, 147, 25, 25), 1)
            if game.lobby:
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (175, 150, 75, 20), 1)
        elif lobby_buttons[3].y == 90:
            text = font.render("$ " + str(sum_bets_player0), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (150 - round(text.get_width() / 2), 68))
            text = font.render("$ " + str(sum_bets_player1), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (275 - round(text.get_width() / 2), 68))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (290, 90, 25, 25), 1)
            if game.lobby:
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (175, 93, 75, 20), 1)
        # bets ---------------------------------------------------------------------------------------------------------
        # spectator buttons---------------------------------------------------------------------------------------------
        if not game.lobby and not spectator:
            if player_index != game.versus[0] and player_index != game.versus[1] and game.player_ready[player_index]:
                spectator_button.draw(canvas.get_canvas())
                if lobby_buttons[3].y == 147:
                    pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (175, 160, 75, 20), 1)
                elif lobby_buttons[3].y == 90:
                    pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (175, 103, 75, 20), 1)
                text = font.render("Spectate", True, (0, 0, 0))
                canvas.get_canvas().blit(text, (213 - round(text.get_width() / 2), spectator_button.y))
        # spectator buttons---------------------------------------------------------------------------------------------

        # pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (25, 25, 300, 400), 1)
        # border
        # pygame.draw.rect(canvas.get_canvas(), (0, 255, 0), (450, 300, 780, 450), 1)
        # bottom -------------------------------------------------------------------------------------------------------
        # background mini-map
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (20, 820, 210, 210))
        # mini-map
        pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (25, 825, 200, 200))
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (25, 825, 200, 200), 1)
        # player
        if not spectator:
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 0), (50 + 8 + int((player.false_x - player.width/2) / 12.5), 825 + 50 + 8 + int((player.false_y - player.height/2) / 12.5), 8, 11))
        # players in lobby
        if game.lobby:
            for cycle_index in players:
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (
                50 + 8 + int((cycle_index.x - cycle_index.width / 2 - 360) / 12.5),
                825 + 50 + 8 + int((cycle_index.y - cycle_index.height / 2 - 655) / 12.5), 8, 11))
        elif not game.lobby and player_index != game.versus[0] and player_index != game.versus[1]:
            for cycle_index in bots:
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (
                    50 + 8 + int((cycle_index.false_x - cycle_index.width / 2 - 360) / 12.5),
                    825 + 50 + 8 + int((cycle_index.false_y - cycle_index.height / 2 - 655) / 12.5), 8, 11))
        if not game.lobby and spectator:
            for cycle_index in spectator_players:
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 255), (
                    50 + 8 + int((cycle_index.x - cycle_index.width / 2 - 360) / 12.5),
                    825 + 50 + 8 + int((cycle_index.y - cycle_index.height / 2 - 655) / 12.5), 8, 11))

        # inventory
        if not spectator:
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (1350, 835, 300, 190))
            pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (1355, 840, 290, 40))
            canvas.get_canvas().blit(background_player_3, (1355, 840), (0, 50, 290, 40))
            text = font_B.render("$ " + str(player.money), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (1370, 848))
            if game.lobby:
                lobby_buttons[1].draw(canvas.get_canvas())
                pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (1542, 843, 100, 34), 1)
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (1365, 885, 270, 120), 1)
        #x = 1365
        #for i in range(0, 3):
        #    pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (x, 885, 90, 60))
        #    pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (x, 885, 90, 60), 1)
        #    x += 90
        #x = 1365
        #for i in range(0, 2):
        #    pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (x, 945, 90, 60))
        #    pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (x, 945, 90, 60), 1)
        #    x += 90
            for draw_button in inventory_buttons:
                draw_button.draw(canvas.get_canvas())
            # hp
            pygame.draw.rect(canvas.get_canvas(), (128, 128, 128), (590, 975, 500, 50))
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 0), (590, 975, player.hp / (player.max_hp / 500), 50))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (590, 975, 500, 50), 1)
            text = font_B.render(str(player.hp) + "/" + str(player.max_hp), True, (0, 128, 0))
            canvas.get_canvas().blit(text, (840 - round(text.get_width()/2), 1000 - round(text.get_height()/2)))
            # hero
            #pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (337, 825, 250, 200))
            canvas.get_canvas().blit(background_player_2, (337, 825))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (337, 825, 250, 200), 1)
            text = font.render("S:"+str(player.strength)+"+"+str(player.items_strength), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (502, 835))
            text = font.render("A:"+str(player.agility)+"+"+str(player.items_agility), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (501, 849))
            text = font.render("I:"+str(player.intelligence)+"+"+str(player.items_intelligence), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (508, 863))
            text = font.render("H:"+str((player.strength + player.items_strength) * 20)+"+"+str(player.start_hp + player.items_hp), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (501, 883))
            text = font.render("S:"+str((player.agility + player.items_agility) / 10)+"+"+str(player.start_speed + player.items_speed), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (502, 897))
            text = font.render("D:"+str(player.intelligence + player.items_intelligence)+"+"+str(player.start_damage + player.items_damage), True, (255, 255, 255))
            canvas.get_canvas().blit(text, (500, 911))
            #text = font.render("R:132+100", True, (0, 0, 0))
            #canvas.get_canvas().blit(text, (501, 931))
            #text = font.render("E:132+100", True, (0, 0, 0))
            #canvas.get_canvas().blit(text, (502, 945))
            #text = font.render("A:132+100", True, (0, 0, 0))
            #canvas.get_canvas().blit(text, (501, 959))
            # attribytes show info -------------------
            if show_attributes.popup_draw:
                show_attributes.draw_popup(canvas.get_canvas(), player.strength, player.items_strength, player.agility, player.items_agility, player.intelligence, player.items_intelligence, player.start_hp, player.items_hp, player.start_speed , player.items_speed, player.start_damage, player.items_damage, player.strength_level, player.agility_level, player.intelligence_level)
            # attribytes show info -------------------


            # hearts
            x_cordinat = 650 - (game.hearts[player_index] - 1) * 7
            for cycle_index in range(0, game.hearts[player_index]):
                pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (x_cordinat, 995, 10, 10))
                x_cordinat += 15

            #player.regen = player.start_regen + (player.strength + player.items_strength) + player.items_regen
            #player.evasion = player.start_evasion + (player.agility + player.items_agility) + player.items_evasion
            #player.attack_speed = player.start_attack_speed + (player.intelligence + player.items_intelligence) + player.items_attack_speed

            canvas.get_canvas().blit(background_player_1, (344, 832))
            #pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (344, 832, 155, 155))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (344, 832, 155, 155), 1)
            canvas.get_canvas().blit(player_icon[player.index], (327, 835), (50, 50, 172, 152))

            # level
            pygame.draw.rect(canvas.get_canvas(), (255, 255, 0), (344, 990, 30, 30))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (344, 990, 30, 30), 1)
            text = font.render(str(player.level), True, (255, 0, 0))
            canvas.get_canvas().blit(text, (359 - round(text.get_width() / 2), 1005 - round(text.get_height() / 2)))
            pygame.draw.rect(canvas.get_canvas(), (128, 128, 128), (374, 995, 205, 20))
            if player.level != 10:
                text = font.render(str(player.exp - levels[player.level - 1]) + " / " + str(levels[player.level] - levels[player.level - 1]), True, (0, 0, 0))
                pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (374, 995, (player.exp - levels[player.level - 1]) / ((levels[player.level] - levels[player.level - 1]) / 205), 20))
            else:
                text = font.render("Max", True, (0, 0, 0))
                pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (374, 995, 205, 20))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (374, 995, 205, 20), 1)
            canvas.get_canvas().blit(text, (476 - round(text.get_width() / 2), 997))
            # level

        # bottom -------------------------------------------------------------------------------------------------------



        # shop ---------------------------------------------------------------------------------------------------------
        if shop and game.lobby:
            #pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (1150, 150, 500, 650))
            canvas.get_canvas().blit(background_player_7, (1150, 150))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (1150, 150, 500, 650), 1)
            lobby_buttons[6].draw(canvas.get_canvas())
            for draw_button in shop_buttons:
                draw_button.draw(canvas.get_canvas())
            for draw_button in shop_buttons:
                draw_button.draw_popup(canvas.get_canvas())
        # shop ---------------------------------------------------------------------------------------------------------
        # bets ---------------------------------------------------------------------------------------------------------
        if bets and game.lobby:
            canvas.get_canvas().blit(background_player_6, (10, 200))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (10, 200, 500, 500), 1)
            lobby_buttons[7].draw(canvas.get_canvas())

            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (75, 215, 100, 100), 1)
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (76, 216, 98, 98))
            canvas.get_canvas().blit(versus_images_icon[players_q[game.versus[0]]], (60, 195))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (345, 215, 100, 100), 1)
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (346, 216, 98, 98))
            canvas.get_canvas().blit(versus_images_icon[players_q[game.versus[1]]], (330, 195))

            x = 50
            for i in range(0, 3):
                canvas.get_canvas().blit(background_item_small_2, (x, 325))
                try:
                    if int(spectator_players[0].inventory[i]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(items_icon_small_2[item(int(spectator_players[0].inventory[i]))[4] - 1], (x, 325))
                        except:
                            text = font.render(str(spectator_players[0].inventory[i]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                            x + 25 - round(text.get_width() / 2), 350 - round(text.get_height() / 2)))
                except:
                    pass

                x += 50
            x = 75
            for i in range(0, 2):
                canvas.get_canvas().blit(background_item_small_2, (x, 375))
                try:
                    if int(spectator_players[0].inventory[i+3]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(
                                items_icon_small_2[item(int(spectator_players[0].inventory[i+3]))[4] - 1], (x, 375))
                        except:
                            text = font.render(str(spectator_players[0].inventory[i+3]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                                x + 25 - round(text.get_width() / 2), 400 - round(text.get_height() / 2)))
                except:
                    pass

                x += 50
            x = 320
            for i in range(0, 3):
                canvas.get_canvas().blit(background_item_small_2, (x, 325))
                try:
                    if int(spectator_players[1].inventory[i]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(items_icon_small_2[item(int(spectator_players[1].inventory[i]))[4] - 1], (x, 325))
                        except:
                            text = font.render(str(spectator_players[1].inventory[i]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                            x + 25 - round(text.get_width() / 2), 350 - round(text.get_height() / 2)))
                except:
                    pass
                x += 50
            x = 345
            for i in range(0, 2):
                canvas.get_canvas().blit(background_item_small_2, (x, 375))
                try:
                    if int(spectator_players[1].inventory[i+3]) in range(0, 100):
                        try:
                            canvas.get_canvas().blit(
                                items_icon_small_2[item(int(spectator_players[1].inventory[i+3]))[4] - 1], (x, 375))
                        except:
                            text = font.render(str(spectator_players[1].inventory[i+3]), True, (0, 0, 0))
                            canvas.get_canvas().blit(text, (
                                x + 25 - round(text.get_width() / 2), 400 - round(text.get_height() / 2)))
                except:
                    pass
                x += 50
            #pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (40, 435, 170, 100), 1)
            #pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (310, 435, 170, 100), 1)

            y1 = y2 = 440
            for cycle_index in range(0, len(player_bets)):
                if bets_game[cycle_index] == 0:
                    continue
                if player_bets[cycle_index] == 0:
                    # draw image
                    text = font.render(str(cycle_index), True, (0, 0, 0))
                    canvas.get_canvas().blit(text, (
                    50 - round(text.get_width() / 2), (y1 + 10 - round(text.get_height() / 2))))
                    pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (40, y1, 20, 20), 1)
                    # nickname
                    text = font.render(str(game.player[cycle_index].split('#')[0]), True, (0, 0, 0))
                    canvas.get_canvas().blit(text, (75, y1))
                    # bet
                    text = font.render(str(bets_game[cycle_index]), True, (0, 0, 0))
                    canvas.get_canvas().blit(text, (230 - round(text.get_width() / 2), y1))
                    y1 += 30
                if player_bets[cycle_index] == 1:
                    # image
                    text = font.render(str(cycle_index), True, (0, 0, 0))
                    canvas.get_canvas().blit(text, (
                    320 - round(text.get_width() / 2), (y2 + 10 - round(text.get_height() / 2))))
                    pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (310, y2, 20, 20), 1)
                    # nickname
                    text = font.render(str(game.player[cycle_index].split('#')[0]), True, (0, 0, 0))
                    canvas.get_canvas().blit(text, (345, y2))
                    # bet
                    text = font.render(str(bets_game[cycle_index]), True, (0, 0, 0))
                    canvas.get_canvas().blit(text, (295 - round(text.get_width() / 2), y2))
                    y2 += 30

            if player_index != game.versus[0] and player_index != game.versus[1]:
                canvas.get_canvas().blit(background_player_5, (60, 700), (280, 0, 400, 115))
                pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (60, 700, 400, 115), 1)
                toucher.draw(canvas.get_canvas(), player.money)
                for draw_button in bets_buttons:
                    draw_button.draw(canvas.get_canvas())
        # bets ---------------------------------------------------------------------------------------------------------
        # menu must be last --------------------------------------------------------------------------------------------
        if menu:
            pygame.draw.rect(canvas.get_canvas(), (128, 128, 128), (640, 250, 400, 500))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (640, 250, 400, 500), 1)
            lobby_buttons[4].draw(canvas.get_canvas())
            lobby_buttons[5].draw(canvas.get_canvas())
            hit_box_button.draw(canvas.get_canvas())
        # menu ---------------------------------------------------------------------------------------------------------
        canvas.update()
test_buttons = [Button_Choise_Hero(100, 90, 0), Button_Choise_Hero(300, 90, 1), Button_Choise_Hero(500, 90, 2), Button_Choise_Hero(700, 90, 3), Button_Choise_Hero(100, 400, 4), Button_Choise_Hero(300, 400, 5), Button_Choise_Hero(500, 400, 6), Button_Choise_Hero(700, 400, 7),  Button_Choise_Hero(100, 730, 8), Button_Choise_Hero(300, 730, 9), Button_Choise_Hero(500, 730, 10), Button_Choise_Hero(700, 730, 11)]
test_exit_button = Button(25, 10, 50, 50, (255, 0, 0))
choise_images = [pygame.image.load(attributes(0)[12]), pygame.image.load(attributes(1)[12]), pygame.image.load(attributes(2)[12]), pygame.image.load(attributes(3)[12]), pygame.image.load(attributes(4)[12]), pygame.image.load(attributes(5)[12]), pygame.image.load(attributes(6)[12]), pygame.image.load(attributes(7)[12]), pygame.image.load(attributes(8)[12]), pygame.image.load(attributes(9)[12]), pygame.image.load(attributes(10)[12]), pygame.image.load(attributes(11)[12])]
choise_images_icon = [pygame.transform.scale(pygame.image.load(attributes(0)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(1)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(2)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(3)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(4)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(5)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(6)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(7)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(8)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(9)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(10)[12]), (100, 100)), pygame.transform.scale(pygame.image.load(attributes(11)[12]), (100, 100))]
versus_images_icon = [pygame.transform.scale(pygame.image.load(attributes(0)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(1)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(2)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(3)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(4)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(5)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(6)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(7)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(8)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(9)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(10)[12]), (134, 134)), pygame.transform.scale(pygame.image.load(attributes(11)[12]), (134, 134))]
player_icon = [pygame.transform.scale(choise_images[0], (300, 300)), pygame.transform.scale(choise_images[1], (300, 300)), pygame.transform.scale(choise_images[2], (300, 300)), pygame.transform.scale(choise_images[3], (300, 300)), pygame.transform.scale(choise_images[4], (300, 300)), pygame.transform.scale(choise_images[5], (300, 300)), pygame.transform.scale(choise_images[6], (300, 300)), pygame.transform.scale(choise_images[7], (300, 300)), pygame.transform.scale(choise_images[8], (300, 300)), pygame.transform.scale(choise_images[9], (300, 300)), pygame.transform.scale(choise_images[10], (300, 300)), pygame.transform.scale(choise_images[11], (300, 300))]


def choise_hero(show_image_backgrond):
    run = True
    net = Network()
    try:
        player_index = int(net.getP())
    except:
        run = False
        return True
    name = "aJIxiM1k"
    send = False
    last_opened = None
    while run:
        clock.tick(60)
        try:
            game = net.send("get")
        except:
            print("Couldn't get game")
            break
        players_q = []
        for cycle_index in game.player:
            if cycle_index != None:
                players_q.append(int(cycle_index.split('#')[1]))
            else:
                players_q.append(None)
        if send:
            net.send(name)
        if game.ready:
            if not send:
                index = random.randint(0, 11)
                while index in players_q:
                    index = random.randint(0, 11)
                game = net.send(name + "#" + str(index))
            game_s(player_index, index, net)
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if test_exit_button.click(event):
                run = False
            if not send:
                for cycle_index in test_buttons:
                    if test_buttons.index(cycle_index) in players_q:
                        continue
                    if cycle_index.click(event):
                        name += "#" + str(test_buttons.index(cycle_index))
                        index = test_buttons.index(cycle_index)
                        send = True
        canvas.draw_background()
        canvas.get_canvas().blit(menu_background[show_image_backgrond%4], (0, 0))
        # top ----------------------------------------------------------------------------------------------------------
        test_exit_button.draw(canvas.get_canvas())
        pygame.draw.rect(canvas.get_canvas(), (128, 0, 0), (25, 10, 50, 50), 1)

        x = 835 - (3 - 1) * 50
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (343, 0, 984, 88))
        for i in range(0, 3):
            pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (x, 10, 75, 75))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (x, 10, 75, 75), 1)
            if players_q[i] != None:
                pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (x+1, 11, 73, 73))
                canvas.get_canvas().blit(choise_images_icon[players_q[i]], (x-10, -5))
            x += 100
        for draw_buttons in test_buttons:
            if test_buttons.index(draw_buttons) in players_q:
                continue
            draw_buttons.draw(canvas.get_canvas())
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (950, 90, 600, 800))
        pygame.draw.rect(canvas.get_canvas(), (255, 255, 255), (960, 100, 580, 780))
        canvas.get_canvas().blit(background_player_choise, (965, 105), (0, 350, 460, 600))
        #pygame.draw.rect(canvas.get_canvas(), (0, 255, 255,), (965, 105, 460, 600))
        pygame.draw.rect(canvas.get_canvas(), (0, 0, 0,), (965, 105, 460, 600), 5)
        for cycle_index in test_buttons:
            if cycle_index.popup_draw:
                last_opened = test_buttons.index(cycle_index)
        if last_opened != None:
            text = font_B.render(attributes(last_opened)[13], True, (0, 0, 0))
            canvas.get_canvas().blit(text, (1185 - round(text.get_width() / 2), 720))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (1175 - round(text.get_width() / 2), 715, round(text.get_width()) + 20, 32), 3)
            canvas.get_canvas().blit(choise_images[last_opened], (760, -50))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (957, 752, 268, 60), 1)
            text = font.render("Strength: "+str(attributes(last_opened)[0])+"  (+"+str(attributes(last_opened)[9])+" per level)", True, (0, 0, 0))
            canvas.get_canvas().blit(text, (960, 755))
            text = font.render("Agility: "+str(attributes(last_opened)[1])+"  (+"+str(attributes(last_opened)[10])+" per level)", True, (0, 0, 0))
            canvas.get_canvas().blit(text, (960, 775))
            text = font.render("Intelligence: "+str(attributes(last_opened)[2])+"  (+"+str(attributes(last_opened)[11])+" per level)", True, (0, 0, 0))
            canvas.get_canvas().blit(text, (960, 795))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (957, 812, 268, 60), 1)
            text = font.render("Healthpoint: "+str(attributes(last_opened)[0]*20)+" + "+str(attributes(last_opened)[3]), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (960, 815))
            text = font.render("Speed: "+str(attributes(last_opened)[1]/10)+" + "+str(attributes(last_opened)[4]), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (960, 835))
            text = font.render("Damage: "+str(attributes(last_opened)[2])+" + "+str(attributes(last_opened)[5]), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (960, 855))
            pygame.draw.rect(canvas.get_canvas(), (0, 0, 0), (1232, 812, 268, 60), 1)
            text = font.render("Regen: "+str(attributes(last_opened)[6]), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (1235, 815))
            text = font.render("Evasion: "+str(attributes(last_opened)[7]), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (1235, 835))
            text = font.render("Attack Speed: "+str(attributes(last_opened)[8]), True, (0, 0, 0))
            canvas.get_canvas().blit(text, (1235, 855))

        canvas.update()
menu_buttons = [Button(650, 500, 380, 140, (255, 255, 255), "buttons\i11.png", "Play", 142), Button(650, 700, 380, 140, (255, 0, 0), "buttons\i20.png", "Exit", 172),
                Button(25, 25, 50, 20, (255, 255, 255), "buttons\i2.png", "change", 15)]
exit_error_menu_button = Button(1115, 310, 25, 25, (255, 0, 0), "buttons\i4.png", "X", 25)
# 0 - play, 1 - exit
menu_background = [pygame.image.load("main_background/i01.png"), pygame.image.load("main_background/i02.png"), pygame.image.load("main_background/i03.png"), pygame.image.load("main_background/i04.png")]
def menu(background_index):
    run = True
    show_error = False
    show_image_backgrond = background_index
    font_error = pygame.font.SysFont(None, 70)
    text_error = [font_error.render("Can't find the game", True, (0, 0, 0)), font_error.render("try again later", True, (0, 0, 0))]
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if not show_error:
                if menu_buttons[0].click(event):
                    if choise_hero(show_image_backgrond):
                        show_error = True
                    else:
                        # change background
                        show_image_backgrond = random.randint(0, 3)
                if menu_buttons[1].click(event):
                    run = False
                if menu_buttons[2].click(event):
                    show_image_backgrond += 1
            if show_error:
                if exit_error_menu_button.click(event):
                    show_error = False
        canvas.draw_background()
        canvas.get_canvas().blit(menu_background[show_image_backgrond%4], (0, 0))
        for draw_buttons in menu_buttons:
            draw_buttons.draw(canvas.get_canvas())
        if show_error:
            pygame.draw.rect(canvas.get_canvas(), (205, 205, 205), (550, 300, 600, 300))
            pygame.draw.rect(canvas.get_canvas(), (0, 255, 255), (550, 300, 600, 300), 3)
            for text_draw in range(0, 2):
                canvas.get_canvas().blit(text_error[text_draw], (850 - round(text_error[text_draw].get_width()/2), 400 - round(text_error[text_draw].get_height()/2) + text_draw * round(text_error[text_draw].get_height())))
            exit_error_menu_button.draw(canvas.get_canvas())
        canvas.update()
def loading_(per_cent, background_index):
    canvas.draw_background()
    canvas.get_canvas().blit(menu_background[background_index%4], (0, 0))
    text = font_B.render(str(per_cent) + " %", True, (0, 0, 0))
    pygame.draw.rect(canvas.get_canvas(), (128, 128, 128), (590, 750, 500, 100))
    pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (590, 750, per_cent*5, 100))
    canvas.get_canvas().blit(text, (840 - round(text.get_width() / 2), 800 - round(text.get_height() / 2)))
    for event in pygame.event.get():
        if menu_buttons[2].click(event):
            background_index += 1
    menu_buttons[2].draw(canvas.get_canvas())
    canvas.update()
    return background_index


def start():
    #background_index = random.randint(0, 3)
    per_cent = 0
    """
    for q in range(1, 13):
        background_index = loading_(per_cent, background_index)

        way = "sprite\_bot_"+str(q)
        action = "\I"
        idle_bot.append([])
        idle_l_bot.append([])
        for i in range(0, 12):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            idle_bot[q-1].append(pygame.image.load(way + action + add))
            idle_l_bot[q-1].append(pygame.transform.flip(idle_bot[q-1][i], True, False))

        per_cent += 1
        background_index = loading_(per_cent, background_index)

        action = "\A"
        attack_bot.append([])
        attack_l_bot.append([])
        for i in range(0, 12):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            attack_bot[q-1].append(pygame.image.load(way + action + add))
            attack_l_bot[q-1].append(pygame.transform.flip(attack_bot[q-1][i], True, False))
        per_cent += 1
        background_index = loading_(per_cent, background_index)

        action = "\D"
        dying_bot.append([])
        dying_l_bot.append([])
        for i in range(0, 15):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            dying_bot[q-1].append(pygame.image.load(way + action + add))
            dying_l_bot[q-1].append(pygame.transform.flip(dying_bot[q-1][i], True, False))

        per_cent += 1
        background_index = loading_(per_cent, background_index)

        action = "\W"
        walk_bot.append([])
        walk_l_bot.append([])
        r = 18
        if q>= 10:
            r = 12
        for i in range(0, r):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            walk_bot[q-1].append(pygame.image.load(way + action + add))
            walk_l_bot[q-1].append(pygame.transform.flip(walk_bot[q-1][i], True, False))
        per_cent += 1


        background_index = loading_(per_cent, background_index)

        way = "sprite\hero_"+str(q)
        action = "\Idle"
        idle.append([])
        idle_l.append([])
        for i in range(0, 18):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            idle[q-1].append(pygame.image.load(way + action + add))
            idle_l[q-1].append(pygame.transform.flip(idle[q-1][i], True, False))

        per_cent += 1
        background_index = loading_(per_cent, background_index)

        action = "\Kicking"
        kick.append([])
        kick_l.append([])
        for i in range(0, 12):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            kick[q-1].append(pygame.image.load(way + action + add))
            kick_l[q-1].append(pygame.transform.flip(kick[q-1][i], True, False))
        per_cent += 1
        background_index = loading_(per_cent, background_index)

        action = "\Dying"
        dying.append([])
        dying_l.append([])
        for i in range(0, 15):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            dying[q-1].append(pygame.image.load(way + action + add))
            dying_l[q-1].append(pygame.transform.flip(dying[q-1][i], True, False))

        per_cent += 1
        background_index = loading_(per_cent, background_index)

        action = "\Walking"
        walk.append([])
        walk_l.append([])
        for i in range(0, 24):
            if i < 10:
                add = '\i0' + str(i) + ".png"
            else:
                add = '\i' + str(i) + ".png"
            walk[q-1].append(pygame.image.load(way + action + add))
            walk_l[q-1].append(pygame.transform.flip(walk[q-1][i], True, False))
        per_cent += 1

    """
    # from load import *
    #q = load()
    #idle = q[0]
    menu(returned_background_index)
if __name__ == '__main__':
    start()
    #menu(3)
    #game_s(1, 1)
