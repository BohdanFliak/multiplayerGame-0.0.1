#from pygame import  image, transform,
import pygame

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

canvas = Canvas(1680, 1050)
pygame.font.init()
font_B = pygame.font.SysFont(None, 36)


returned_background_index = 3
menu_background = [pygame.image.load("main_background/i01.png"), pygame.image.load("main_background/i02.png"), pygame.image.load("main_background/i03.png"), pygame.image.load("main_background/i04.png")]
menu_button = Button(25, 25, 50, 20, (255, 255, 255), "buttons\i2.png", "change", 15)
def loading_(per_cent, background_index):
    canvas.draw_background()
    canvas.get_canvas().blit(menu_background[background_index%4], (0, 0))
    text = font_B.render(str(per_cent) + " %", True, (0, 0, 0))
    pygame.draw.rect(canvas.get_canvas(), (128, 128, 128), (590, 750, 500, 100))
    pygame.draw.rect(canvas.get_canvas(), (255, 0, 0), (590, 750, per_cent*5, 100))
    canvas.get_canvas().blit(text, (840 - round(text.get_width() / 2), 800 - round(text.get_height() / 2)))
    for event in pygame.event.get():
        if menu_button.click(event):
            background_index += 1
    menu_button.draw(canvas.get_canvas())
    canvas.update()
    return background_index

#idle = [pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_000.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_001.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_002.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_003.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_004.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_005.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_006.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_007.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_008.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_009.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_010.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_011.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_012.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_013.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_014.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_015.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_016.png'),pygame.image.load('PNG Sequences\Idle\Reaper_Man_Idle_017.png')]
#walk = [pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_000.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_001.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_002.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_003.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_004.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_005.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_006.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_007.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_008.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_009.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_010.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_011.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_012.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_013.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_014.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_015.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_016.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_017.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_018.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_019.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_020.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_021.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_022.png'), pygame.image.load('PNG Sequences\Walking\Reaper_Man_Walking_023.png')]
#kick = [pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_000.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_001.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_002.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_003.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_004.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_005.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_006.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_007.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_008.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_009.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_010.png'),pygame.image.load('PNG Sequences\Kicking\Reaper_Man_Kicking_011.png')]
#dying = [pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_000.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_001.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_002.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_003.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_004.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_005.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_006.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_007.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_008.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_009.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_010.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_011.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_012.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_013.png'),pygame.image.load('PNG Sequences\Dying\Reaper_Man_Dying_014.png')]

per_cent = 0
idle_1 = [pygame.image.load('sprite\hero_1\Idle\i00.png'), pygame.image.load('sprite\hero_1\Idle\i01.png'), pygame.image.load('sprite\hero_1\Idle\i02.png'), pygame.image.load('sprite\hero_1\Idle\i03.png'), pygame.image.load('sprite\hero_1\Idle\i04.png'), pygame.image.load('sprite\hero_1\Idle\i05.png'), pygame.image.load('sprite\hero_1\Idle\i06.png'), pygame.image.load('sprite\hero_1\Idle\i07.png'), pygame.image.load('sprite\hero_1\Idle\i08.png'), pygame.image.load('sprite\hero_1\Idle\i09.png'), pygame.image.load('sprite\hero_1\Idle\i10.png'), pygame.image.load('sprite\hero_1\Idle\i11.png'), pygame.image.load('sprite\hero_1\Idle\i12.png'), pygame.image.load('sprite\hero_1\Idle\i13.png'), pygame.image.load('sprite\hero_1\Idle\i14.png'), pygame.image.load('sprite\hero_1\Idle\i15.png'), pygame.image.load('sprite\hero_1\Idle\i16.png'), pygame.image.load('sprite\hero_1\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_1 = [pygame.image.load('sprite\hero_1\Walking\i00.png'), pygame.image.load('sprite\hero_1\Walking\i01.png'), pygame.image.load('sprite\hero_1\Walking\i02.png'), pygame.image.load('sprite\hero_1\Walking\i03.png'), pygame.image.load('sprite\hero_1\Walking\i04.png'), pygame.image.load('sprite\hero_1\Walking\i05.png'), pygame.image.load('sprite\hero_1\Walking\i06.png'), pygame.image.load('sprite\hero_1\Walking\i07.png'), pygame.image.load('sprite\hero_1\Walking\i08.png'), pygame.image.load('sprite\hero_1\Walking\i09.png'), pygame.image.load('sprite\hero_1\Walking\i10.png'), pygame.image.load('sprite\hero_1\Walking\i11.png'), pygame.image.load('sprite\hero_1\Walking\i12.png'), pygame.image.load('sprite\hero_1\Walking\i13.png'), pygame.image.load('sprite\hero_1\Walking\i14.png'), pygame.image.load('sprite\hero_1\Walking\i15.png'), pygame.image.load('sprite\hero_1\Walking\i16.png'), pygame.image.load('sprite\hero_1\Walking\i17.png'), pygame.image.load('sprite\hero_1\Walking\i18.png'), pygame.image.load('sprite\hero_1\Walking\i19.png'), pygame.image.load('sprite\hero_1\Walking\i20.png'), pygame.image.load('sprite\hero_1\Walking\i21.png'), pygame.image.load('sprite\hero_1\Walking\i22.png'), pygame.image.load('sprite\hero_1\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_1 = [pygame.image.load('sprite\hero_1\Kicking\i00.png'), pygame.image.load('sprite\hero_1\Kicking\i01.png'), pygame.image.load('sprite\hero_1\Kicking\i02.png'), pygame.image.load('sprite\hero_1\Kicking\i03.png'), pygame.image.load('sprite\hero_1\Kicking\i04.png'), pygame.image.load('sprite\hero_1\Kicking\i05.png'), pygame.image.load('sprite\hero_1\Kicking\i06.png'), pygame.image.load('sprite\hero_1\Kicking\i07.png'), pygame.image.load('sprite\hero_1\Kicking\i08.png'), pygame.image.load('sprite\hero_1\Kicking\i09.png'), pygame.image.load('sprite\hero_1\Kicking\i10.png'), pygame.image.load('sprite\hero_1\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_1 = [pygame.image.load('sprite\hero_1\Dying\i00.png'), pygame.image.load('sprite\hero_1\Dying\i01.png'), pygame.image.load('sprite\hero_1\Dying\i02.png'), pygame.image.load('sprite\hero_1\Dying\i03.png'), pygame.image.load('sprite\hero_1\Dying\i04.png'), pygame.image.load('sprite\hero_1\Dying\i05.png'), pygame.image.load('sprite\hero_1\Dying\i06.png'), pygame.image.load('sprite\hero_1\Dying\i07.png'), pygame.image.load('sprite\hero_1\Dying\i08.png'), pygame.image.load('sprite\hero_1\Dying\i09.png'), pygame.image.load('sprite\hero_1\Dying\i10.png'), pygame.image.load('sprite\hero_1\Dying\i11.png'), pygame.image.load('sprite\hero_1\Dying\i12.png'), pygame.image.load('sprite\hero_1\Dying\i13.png'), pygame.image.load('sprite\hero_1\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_1 = []
idle_l_1 = []
kick_l_1 = []
dying_l_1 = []
for i in range(0, 18):
    idle_1[i] = (pygame.transform.scale(idle_1[i], (200, 200)))
    idle_l_1.append(pygame.transform.flip(idle_1[i], True, False))
for i in range(0, 24):
    walk_1[i] = (pygame.transform.scale(walk_1[i], (200, 200)))
    walk_l_1.append(pygame.transform.flip(walk_1[i], True, False))
for i in range(0, 12):
    kick_1[i] = (pygame.transform.scale(kick_1[i], (200, 200)))
    kick_l_1.append(pygame.transform.flip(kick_1[i], True, False))
for i in range(0, 15):
    dying_1[i] = (pygame.transform.scale(dying_1[i], (200, 200)))
    dying_l_1.append(pygame.transform.flip(dying_1[i], True, False))
idle_2 = [pygame.image.load('sprite\hero_2\Idle\i00.png'), pygame.image.load('sprite\hero_2\Idle\i01.png'), pygame.image.load('sprite\hero_2\Idle\i02.png'), pygame.image.load('sprite\hero_2\Idle\i03.png'), pygame.image.load('sprite\hero_2\Idle\i04.png'), pygame.image.load('sprite\hero_2\Idle\i05.png'), pygame.image.load('sprite\hero_2\Idle\i06.png'), pygame.image.load('sprite\hero_2\Idle\i07.png'), pygame.image.load('sprite\hero_2\Idle\i08.png'), pygame.image.load('sprite\hero_2\Idle\i09.png'), pygame.image.load('sprite\hero_2\Idle\i10.png'), pygame.image.load('sprite\hero_2\Idle\i11.png'), pygame.image.load('sprite\hero_2\Idle\i12.png'), pygame.image.load('sprite\hero_2\Idle\i13.png'), pygame.image.load('sprite\hero_2\Idle\i14.png'), pygame.image.load('sprite\hero_2\Idle\i15.png'), pygame.image.load('sprite\hero_2\Idle\i16.png'), pygame.image.load('sprite\hero_2\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_2 = [pygame.image.load('sprite\hero_2\Walking\i00.png'), pygame.image.load('sprite\hero_2\Walking\i01.png'), pygame.image.load('sprite\hero_2\Walking\i02.png'), pygame.image.load('sprite\hero_2\Walking\i03.png'), pygame.image.load('sprite\hero_2\Walking\i04.png'), pygame.image.load('sprite\hero_2\Walking\i05.png'), pygame.image.load('sprite\hero_2\Walking\i06.png'), pygame.image.load('sprite\hero_2\Walking\i07.png'), pygame.image.load('sprite\hero_2\Walking\i08.png'), pygame.image.load('sprite\hero_2\Walking\i09.png'), pygame.image.load('sprite\hero_2\Walking\i10.png'), pygame.image.load('sprite\hero_2\Walking\i11.png'), pygame.image.load('sprite\hero_2\Walking\i12.png'), pygame.image.load('sprite\hero_2\Walking\i13.png'), pygame.image.load('sprite\hero_2\Walking\i14.png'), pygame.image.load('sprite\hero_2\Walking\i15.png'), pygame.image.load('sprite\hero_2\Walking\i16.png'), pygame.image.load('sprite\hero_2\Walking\i17.png'), pygame.image.load('sprite\hero_2\Walking\i18.png'), pygame.image.load('sprite\hero_2\Walking\i19.png'), pygame.image.load('sprite\hero_2\Walking\i20.png'), pygame.image.load('sprite\hero_2\Walking\i21.png'), pygame.image.load('sprite\hero_2\Walking\i22.png'), pygame.image.load('sprite\hero_2\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_2 = [pygame.image.load('sprite\hero_2\Kicking\i00.png'), pygame.image.load('sprite\hero_2\Kicking\i01.png'), pygame.image.load('sprite\hero_2\Kicking\i02.png'), pygame.image.load('sprite\hero_2\Kicking\i03.png'), pygame.image.load('sprite\hero_2\Kicking\i04.png'), pygame.image.load('sprite\hero_2\Kicking\i05.png'), pygame.image.load('sprite\hero_2\Kicking\i06.png'), pygame.image.load('sprite\hero_2\Kicking\i07.png'), pygame.image.load('sprite\hero_2\Kicking\i08.png'), pygame.image.load('sprite\hero_2\Kicking\i09.png'), pygame.image.load('sprite\hero_2\Kicking\i10.png'), pygame.image.load('sprite\hero_2\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_2 = [pygame.image.load('sprite\hero_2\Dying\i00.png'), pygame.image.load('sprite\hero_2\Dying\i01.png'), pygame.image.load('sprite\hero_2\Dying\i02.png'), pygame.image.load('sprite\hero_2\Dying\i03.png'), pygame.image.load('sprite\hero_2\Dying\i04.png'), pygame.image.load('sprite\hero_2\Dying\i05.png'), pygame.image.load('sprite\hero_2\Dying\i06.png'), pygame.image.load('sprite\hero_2\Dying\i07.png'), pygame.image.load('sprite\hero_2\Dying\i08.png'), pygame.image.load('sprite\hero_2\Dying\i09.png'), pygame.image.load('sprite\hero_2\Dying\i10.png'), pygame.image.load('sprite\hero_2\Dying\i11.png'), pygame.image.load('sprite\hero_2\Dying\i12.png'), pygame.image.load('sprite\hero_2\Dying\i13.png'), pygame.image.load('sprite\hero_2\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_2 = []
idle_l_2 = []
kick_l_2 = []
dying_l_2 = []
for i in range(0, 18):
    idle_2[i] = (pygame.transform.scale(idle_2[i], (200, 200)))
    idle_l_2.append(pygame.transform.flip(idle_2[i], True, False))
for i in range(0, 24):
    walk_2[i] = (pygame.transform.scale(walk_2[i], (200, 200)))
    walk_l_2.append(pygame.transform.flip(walk_2[i], True, False))
for i in range(0, 12):
    kick_2[i] = (pygame.transform.scale(kick_2[i], (200, 200)))
    kick_l_2.append(pygame.transform.flip(kick_2[i], True, False))
for i in range(0, 15):
    dying_2[i] = (pygame.transform.scale(dying_2[i], (200, 200)))
    dying_l_2.append(pygame.transform.flip(dying_2[i], True, False))


idle_3 = [pygame.image.load('sprite\hero_3\Idle\i00.png'), pygame.image.load('sprite\hero_3\Idle\i01.png'), pygame.image.load('sprite\hero_3\Idle\i02.png'), pygame.image.load('sprite\hero_3\Idle\i03.png'), pygame.image.load('sprite\hero_3\Idle\i04.png'), pygame.image.load('sprite\hero_3\Idle\i05.png'), pygame.image.load('sprite\hero_3\Idle\i06.png'), pygame.image.load('sprite\hero_3\Idle\i07.png'), pygame.image.load('sprite\hero_3\Idle\i08.png'), pygame.image.load('sprite\hero_3\Idle\i09.png'), pygame.image.load('sprite\hero_3\Idle\i10.png'), pygame.image.load('sprite\hero_3\Idle\i11.png'), pygame.image.load('sprite\hero_3\Idle\i12.png'), pygame.image.load('sprite\hero_3\Idle\i13.png'), pygame.image.load('sprite\hero_3\Idle\i14.png'), pygame.image.load('sprite\hero_3\Idle\i15.png'), pygame.image.load('sprite\hero_3\Idle\i16.png'), pygame.image.load('sprite\hero_3\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_3 = [pygame.image.load('sprite\hero_3\Walking\i00.png'), pygame.image.load('sprite\hero_3\Walking\i01.png'),
          pygame.image.load('sprite\hero_3\Walking\i02.png'), pygame.image.load('sprite\hero_3\Walking\i03.png'),
          pygame.image.load('sprite\hero_3\Walking\i04.png'), pygame.image.load('sprite\hero_3\Walking\i05.png'),
          pygame.image.load('sprite\hero_3\Walking\i06.png'), pygame.image.load('sprite\hero_3\Walking\i07.png'),
          pygame.image.load('sprite\hero_3\Walking\i08.png'), pygame.image.load('sprite\hero_3\Walking\i09.png'),
          pygame.image.load('sprite\hero_3\Walking\i10.png'), pygame.image.load('sprite\hero_3\Walking\i11.png'),
          pygame.image.load('sprite\hero_3\Walking\i12.png'), pygame.image.load('sprite\hero_3\Walking\i13.png'),
          pygame.image.load('sprite\hero_3\Walking\i14.png'), pygame.image.load('sprite\hero_3\Walking\i15.png'),
          pygame.image.load('sprite\hero_3\Walking\i16.png'), pygame.image.load('sprite\hero_3\Walking\i17.png'),
          pygame.image.load('sprite\hero_3\Walking\i18.png'), pygame.image.load('sprite\hero_3\Walking\i19.png'),
          pygame.image.load('sprite\hero_3\Walking\i20.png'), pygame.image.load('sprite\hero_3\Walking\i21.png'),
          pygame.image.load('sprite\hero_3\Walking\i22.png'), pygame.image.load('sprite\hero_3\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_3 = [pygame.image.load('sprite\hero_3\Kicking\i00.png'), pygame.image.load('sprite\hero_3\Kicking\i01.png'),
          pygame.image.load('sprite\hero_3\Kicking\i02.png'), pygame.image.load('sprite\hero_3\Kicking\i03.png'),
          pygame.image.load('sprite\hero_3\Kicking\i04.png'), pygame.image.load('sprite\hero_3\Kicking\i05.png'),
          pygame.image.load('sprite\hero_3\Kicking\i06.png'), pygame.image.load('sprite\hero_3\Kicking\i07.png'),
          pygame.image.load('sprite\hero_3\Kicking\i08.png'), pygame.image.load('sprite\hero_3\Kicking\i09.png'),
          pygame.image.load('sprite\hero_3\Kicking\i10.png'), pygame.image.load('sprite\hero_3\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_3 = [pygame.image.load('sprite\hero_3\Dying\i00.png'), pygame.image.load('sprite\hero_3\Dying\i01.png'),
           pygame.image.load('sprite\hero_3\Dying\i02.png'), pygame.image.load('sprite\hero_3\Dying\i03.png'),
           pygame.image.load('sprite\hero_3\Dying\i04.png'), pygame.image.load('sprite\hero_3\Dying\i05.png'),
           pygame.image.load('sprite\hero_3\Dying\i06.png'), pygame.image.load('sprite\hero_3\Dying\i07.png'),
           pygame.image.load('sprite\hero_3\Dying\i08.png'), pygame.image.load('sprite\hero_3\Dying\i09.png'),
           pygame.image.load('sprite\hero_3\Dying\i10.png'), pygame.image.load('sprite\hero_3\Dying\i11.png'),
           pygame.image.load('sprite\hero_3\Dying\i12.png'), pygame.image.load('sprite\hero_3\Dying\i13.png'),
           pygame.image.load('sprite\hero_3\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_3 = []
idle_l_3 = []
kick_l_3 = []
dying_l_3 = []
for i in range(0, 18):
    idle_3[i] = (pygame.transform.scale(idle_3[i], (200, 200)))
    idle_l_3.append(pygame.transform.flip(idle_3[i], True, False))
for i in range(0, 24):
    walk_3[i] = (pygame.transform.scale(walk_3[i], (200, 200)))
    walk_l_3.append(pygame.transform.flip(walk_3[i], True, False))
for i in range(0, 12):
    kick_3[i] = (pygame.transform.scale(kick_3[i], (200, 200)))
    kick_l_3.append(pygame.transform.flip(kick_3[i], True, False))
for i in range(0, 15):
    dying_3[i] = (pygame.transform.scale(dying_3[i], (200, 200)))
    dying_l_3.append(pygame.transform.flip(dying_3[i], True, False))

idle_4 = [pygame.image.load('sprite\hero_4\Idle\i00.png'), pygame.image.load('sprite\hero_4\Idle\i01.png'), pygame.image.load('sprite\hero_4\Idle\i02.png'), pygame.image.load('sprite\hero_4\Idle\i03.png'), pygame.image.load('sprite\hero_4\Idle\i04.png'), pygame.image.load('sprite\hero_4\Idle\i05.png'), pygame.image.load('sprite\hero_4\Idle\i06.png'), pygame.image.load('sprite\hero_4\Idle\i07.png'), pygame.image.load('sprite\hero_4\Idle\i08.png'), pygame.image.load('sprite\hero_4\Idle\i09.png'), pygame.image.load('sprite\hero_4\Idle\i10.png'), pygame.image.load('sprite\hero_4\Idle\i11.png'), pygame.image.load('sprite\hero_4\Idle\i12.png'), pygame.image.load('sprite\hero_4\Idle\i13.png'), pygame.image.load('sprite\hero_4\Idle\i14.png'), pygame.image.load('sprite\hero_4\Idle\i15.png'), pygame.image.load('sprite\hero_4\Idle\i16.png'), pygame.image.load('sprite\hero_4\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_4 = [pygame.image.load('sprite\hero_4\Walking\i00.png'), pygame.image.load('sprite\hero_4\Walking\i01.png'),
          pygame.image.load('sprite\hero_4\Walking\i02.png'), pygame.image.load('sprite\hero_4\Walking\i03.png'),
          pygame.image.load('sprite\hero_4\Walking\i04.png'), pygame.image.load('sprite\hero_4\Walking\i05.png'),
          pygame.image.load('sprite\hero_4\Walking\i06.png'), pygame.image.load('sprite\hero_4\Walking\i07.png'),
          pygame.image.load('sprite\hero_4\Walking\i08.png'), pygame.image.load('sprite\hero_4\Walking\i09.png'),
          pygame.image.load('sprite\hero_4\Walking\i10.png'), pygame.image.load('sprite\hero_4\Walking\i11.png'),
          pygame.image.load('sprite\hero_4\Walking\i12.png'), pygame.image.load('sprite\hero_4\Walking\i13.png'),
          pygame.image.load('sprite\hero_4\Walking\i14.png'), pygame.image.load('sprite\hero_4\Walking\i15.png'),
          pygame.image.load('sprite\hero_4\Walking\i16.png'), pygame.image.load('sprite\hero_4\Walking\i17.png'),
          pygame.image.load('sprite\hero_4\Walking\i18.png'), pygame.image.load('sprite\hero_4\Walking\i19.png'),
          pygame.image.load('sprite\hero_4\Walking\i20.png'), pygame.image.load('sprite\hero_4\Walking\i21.png'),
          pygame.image.load('sprite\hero_4\Walking\i22.png'), pygame.image.load('sprite\hero_4\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_4 = [pygame.image.load('sprite\hero_4\Kicking\i00.png'), pygame.image.load('sprite\hero_4\Kicking\i01.png'),
          pygame.image.load('sprite\hero_4\Kicking\i02.png'), pygame.image.load('sprite\hero_4\Kicking\i03.png'),
          pygame.image.load('sprite\hero_4\Kicking\i04.png'), pygame.image.load('sprite\hero_4\Kicking\i05.png'),
          pygame.image.load('sprite\hero_4\Kicking\i06.png'), pygame.image.load('sprite\hero_4\Kicking\i07.png'),
          pygame.image.load('sprite\hero_4\Kicking\i08.png'), pygame.image.load('sprite\hero_4\Kicking\i09.png'),
          pygame.image.load('sprite\hero_4\Kicking\i10.png'), pygame.image.load('sprite\hero_4\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_4 = [pygame.image.load('sprite\hero_4\Dying\i00.png'), pygame.image.load('sprite\hero_4\Dying\i01.png'),
           pygame.image.load('sprite\hero_4\Dying\i02.png'), pygame.image.load('sprite\hero_4\Dying\i03.png'),
           pygame.image.load('sprite\hero_4\Dying\i04.png'), pygame.image.load('sprite\hero_4\Dying\i05.png'),
           pygame.image.load('sprite\hero_4\Dying\i06.png'), pygame.image.load('sprite\hero_4\Dying\i07.png'),
           pygame.image.load('sprite\hero_4\Dying\i08.png'), pygame.image.load('sprite\hero_4\Dying\i09.png'),
           pygame.image.load('sprite\hero_4\Dying\i10.png'), pygame.image.load('sprite\hero_4\Dying\i11.png'),
           pygame.image.load('sprite\hero_4\Dying\i12.png'), pygame.image.load('sprite\hero_4\Dying\i13.png'),
           pygame.image.load('sprite\hero_4\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1

walk_l_4 = []
idle_l_4 = []
kick_l_4 = []
dying_l_4 = []
for i in range(0, 18):
    idle_4[i] = (pygame.transform.scale(idle_4[i], (200, 200)))
    idle_l_4.append(pygame.transform.flip(idle_4[i], True, False))
for i in range(0, 24):
    walk_4[i] = (pygame.transform.scale(walk_4[i], (200, 200)))
    walk_l_4.append(pygame.transform.flip(walk_4[i], True, False))
for i in range(0, 12):
    kick_4[i] = (pygame.transform.scale(kick_4[i], (200, 200)))
    kick_l_4.append(pygame.transform.flip(kick_4[i], True, False))
for i in range(0, 15):
    dying_4[i] = (pygame.transform.scale(dying_4[i], (200, 200)))
    dying_l_4.append(pygame.transform.flip(dying_4[i], True, False))
idle_5 = [pygame.image.load('sprite\hero_5\Idle\i00.png'), pygame.image.load('sprite\hero_5\Idle\i01.png'), pygame.image.load('sprite\hero_5\Idle\i02.png'), pygame.image.load('sprite\hero_5\Idle\i03.png'), pygame.image.load('sprite\hero_5\Idle\i04.png'), pygame.image.load('sprite\hero_5\Idle\i05.png'), pygame.image.load('sprite\hero_5\Idle\i06.png'), pygame.image.load('sprite\hero_5\Idle\i07.png'), pygame.image.load('sprite\hero_5\Idle\i08.png'), pygame.image.load('sprite\hero_5\Idle\i09.png'), pygame.image.load('sprite\hero_5\Idle\i10.png'), pygame.image.load('sprite\hero_5\Idle\i11.png'), pygame.image.load('sprite\hero_5\Idle\i12.png'), pygame.image.load('sprite\hero_5\Idle\i13.png'), pygame.image.load('sprite\hero_5\Idle\i14.png'), pygame.image.load('sprite\hero_5\Idle\i15.png'), pygame.image.load('sprite\hero_5\Idle\i16.png'), pygame.image.load('sprite\hero_5\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_5 = [pygame.image.load('sprite\hero_5\Walking\i00.png'), pygame.image.load('sprite\hero_5\Walking\i01.png'),
          pygame.image.load('sprite\hero_5\Walking\i02.png'), pygame.image.load('sprite\hero_5\Walking\i03.png'),
          pygame.image.load('sprite\hero_5\Walking\i04.png'), pygame.image.load('sprite\hero_5\Walking\i05.png'),
          pygame.image.load('sprite\hero_5\Walking\i06.png'), pygame.image.load('sprite\hero_5\Walking\i07.png'),
          pygame.image.load('sprite\hero_5\Walking\i08.png'), pygame.image.load('sprite\hero_5\Walking\i09.png'),
          pygame.image.load('sprite\hero_5\Walking\i10.png'), pygame.image.load('sprite\hero_5\Walking\i11.png'),
          pygame.image.load('sprite\hero_5\Walking\i12.png'), pygame.image.load('sprite\hero_5\Walking\i13.png'),
          pygame.image.load('sprite\hero_5\Walking\i14.png'), pygame.image.load('sprite\hero_5\Walking\i15.png'),
          pygame.image.load('sprite\hero_5\Walking\i16.png'), pygame.image.load('sprite\hero_5\Walking\i17.png'),
          pygame.image.load('sprite\hero_5\Walking\i18.png'), pygame.image.load('sprite\hero_5\Walking\i19.png'),
          pygame.image.load('sprite\hero_5\Walking\i20.png'), pygame.image.load('sprite\hero_5\Walking\i21.png'),
          pygame.image.load('sprite\hero_5\Walking\i22.png'), pygame.image.load('sprite\hero_5\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_5 = [pygame.image.load('sprite\hero_5\Kicking\i00.png'), pygame.image.load('sprite\hero_5\Kicking\i01.png'),
          pygame.image.load('sprite\hero_5\Kicking\i02.png'), pygame.image.load('sprite\hero_5\Kicking\i03.png'),
          pygame.image.load('sprite\hero_5\Kicking\i04.png'), pygame.image.load('sprite\hero_5\Kicking\i05.png'),
          pygame.image.load('sprite\hero_5\Kicking\i06.png'), pygame.image.load('sprite\hero_5\Kicking\i07.png'),
          pygame.image.load('sprite\hero_5\Kicking\i08.png'), pygame.image.load('sprite\hero_5\Kicking\i09.png'),
          pygame.image.load('sprite\hero_5\Kicking\i10.png'), pygame.image.load('sprite\hero_5\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_5 = [pygame.image.load('sprite\hero_5\Dying\i00.png'), pygame.image.load('sprite\hero_5\Dying\i01.png'),
           pygame.image.load('sprite\hero_5\Dying\i02.png'), pygame.image.load('sprite\hero_5\Dying\i03.png'),
           pygame.image.load('sprite\hero_5\Dying\i04.png'), pygame.image.load('sprite\hero_5\Dying\i05.png'),
           pygame.image.load('sprite\hero_5\Dying\i06.png'), pygame.image.load('sprite\hero_5\Dying\i07.png'),
           pygame.image.load('sprite\hero_5\Dying\i08.png'), pygame.image.load('sprite\hero_5\Dying\i09.png'),
           pygame.image.load('sprite\hero_5\Dying\i10.png'), pygame.image.load('sprite\hero_5\Dying\i11.png'),
           pygame.image.load('sprite\hero_5\Dying\i12.png'), pygame.image.load('sprite\hero_5\Dying\i13.png'),
           pygame.image.load('sprite\hero_5\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_5 = []
idle_l_5 = []
kick_l_5 = []
dying_l_5 = []
for i in range(0, 18):
    idle_5[i] = (pygame.transform.scale(idle_5[i], (200, 200)))
    idle_l_5.append(pygame.transform.flip(idle_5[i], True, False))
for i in range(0, 24):
    walk_5[i] = (pygame.transform.scale(walk_5[i], (200, 200)))
    walk_l_5.append(pygame.transform.flip(walk_5[i], True, False))
for i in range(0, 12):
    kick_5[i] = (pygame.transform.scale(kick_5[i], (200, 200)))
    kick_l_5.append(pygame.transform.flip(kick_5[i], True, False))
for i in range(0, 15):
    dying_5[i] = (pygame.transform.scale(dying_5[i], (200, 200)))
    dying_l_5.append(pygame.transform.flip(dying_5[i], True, False))


idle_6 = [pygame.image.load('sprite\hero_6\Idle\i00.png'), pygame.image.load('sprite\hero_6\Idle\i01.png'), pygame.image.load('sprite\hero_6\Idle\i02.png'), pygame.image.load('sprite\hero_6\Idle\i03.png'), pygame.image.load('sprite\hero_6\Idle\i04.png'), pygame.image.load('sprite\hero_6\Idle\i05.png'), pygame.image.load('sprite\hero_6\Idle\i06.png'), pygame.image.load('sprite\hero_6\Idle\i07.png'), pygame.image.load('sprite\hero_6\Idle\i08.png'), pygame.image.load('sprite\hero_6\Idle\i09.png'), pygame.image.load('sprite\hero_6\Idle\i10.png'), pygame.image.load('sprite\hero_6\Idle\i11.png'), pygame.image.load('sprite\hero_6\Idle\i12.png'), pygame.image.load('sprite\hero_6\Idle\i13.png'), pygame.image.load('sprite\hero_6\Idle\i14.png'), pygame.image.load('sprite\hero_6\Idle\i15.png'), pygame.image.load('sprite\hero_6\Idle\i16.png'), pygame.image.load('sprite\hero_6\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_6 = [pygame.image.load('sprite\hero_6\Walking\i00.png'), pygame.image.load('sprite\hero_6\Walking\i01.png'),
          pygame.image.load('sprite\hero_6\Walking\i02.png'), pygame.image.load('sprite\hero_6\Walking\i03.png'),
          pygame.image.load('sprite\hero_6\Walking\i04.png'), pygame.image.load('sprite\hero_6\Walking\i05.png'),
          pygame.image.load('sprite\hero_6\Walking\i06.png'), pygame.image.load('sprite\hero_6\Walking\i07.png'),
          pygame.image.load('sprite\hero_6\Walking\i08.png'), pygame.image.load('sprite\hero_6\Walking\i09.png'),
          pygame.image.load('sprite\hero_6\Walking\i10.png'), pygame.image.load('sprite\hero_6\Walking\i11.png'),
          pygame.image.load('sprite\hero_6\Walking\i12.png'), pygame.image.load('sprite\hero_6\Walking\i13.png'),
          pygame.image.load('sprite\hero_6\Walking\i14.png'), pygame.image.load('sprite\hero_6\Walking\i15.png'),
          pygame.image.load('sprite\hero_6\Walking\i16.png'), pygame.image.load('sprite\hero_6\Walking\i17.png'),
          pygame.image.load('sprite\hero_6\Walking\i18.png'), pygame.image.load('sprite\hero_6\Walking\i19.png'),
          pygame.image.load('sprite\hero_6\Walking\i20.png'), pygame.image.load('sprite\hero_6\Walking\i21.png'),
          pygame.image.load('sprite\hero_6\Walking\i22.png'), pygame.image.load('sprite\hero_6\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_6 = [pygame.image.load('sprite\hero_6\Kicking\i00.png'), pygame.image.load('sprite\hero_6\Kicking\i01.png'),
          pygame.image.load('sprite\hero_6\Kicking\i02.png'), pygame.image.load('sprite\hero_6\Kicking\i03.png'),
          pygame.image.load('sprite\hero_6\Kicking\i04.png'), pygame.image.load('sprite\hero_6\Kicking\i05.png'),
          pygame.image.load('sprite\hero_6\Kicking\i06.png'), pygame.image.load('sprite\hero_6\Kicking\i07.png'),
          pygame.image.load('sprite\hero_6\Kicking\i08.png'), pygame.image.load('sprite\hero_6\Kicking\i09.png'),
          pygame.image.load('sprite\hero_6\Kicking\i10.png'), pygame.image.load('sprite\hero_6\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_6 = [pygame.image.load('sprite\hero_6\Dying\i00.png'), pygame.image.load('sprite\hero_6\Dying\i01.png'),
           pygame.image.load('sprite\hero_6\Dying\i02.png'), pygame.image.load('sprite\hero_6\Dying\i03.png'),
           pygame.image.load('sprite\hero_6\Dying\i04.png'), pygame.image.load('sprite\hero_6\Dying\i05.png'),
           pygame.image.load('sprite\hero_6\Dying\i06.png'), pygame.image.load('sprite\hero_6\Dying\i07.png'),
           pygame.image.load('sprite\hero_6\Dying\i08.png'), pygame.image.load('sprite\hero_6\Dying\i09.png'),
           pygame.image.load('sprite\hero_6\Dying\i10.png'), pygame.image.load('sprite\hero_6\Dying\i11.png'),
           pygame.image.load('sprite\hero_6\Dying\i12.png'), pygame.image.load('sprite\hero_6\Dying\i13.png'),
           pygame.image.load('sprite\hero_6\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_6 = []
idle_l_6 = []
kick_l_6 = []
dying_l_6 = []
for i in range(0, 18):
    idle_6[i] = (pygame.transform.scale(idle_6[i], (200, 200)))
    idle_l_6.append(pygame.transform.flip(idle_6[i], True, False))
for i in range(0, 24):
    walk_6[i] = (pygame.transform.scale(walk_6[i], (200, 200)))
    walk_l_6.append(pygame.transform.flip(walk_6[i], True, False))
for i in range(0, 12):
    kick_6[i] = (pygame.transform.scale(kick_6[i], (200, 200)))
    kick_l_6.append(pygame.transform.flip(kick_6[i], True, False))
for i in range(0, 15):
    dying_6[i] = (pygame.transform.scale(dying_6[i], (200, 200)))
    dying_l_6.append(pygame.transform.flip(dying_6[i], True, False))

idle_7 = [pygame.image.load('sprite\hero_7\Idle\i00.png'), pygame.image.load('sprite\hero_7\Idle\i01.png'), pygame.image.load('sprite\hero_7\Idle\i02.png'), pygame.image.load('sprite\hero_7\Idle\i03.png'), pygame.image.load('sprite\hero_7\Idle\i04.png'), pygame.image.load('sprite\hero_7\Idle\i05.png'), pygame.image.load('sprite\hero_7\Idle\i06.png'), pygame.image.load('sprite\hero_7\Idle\i07.png'), pygame.image.load('sprite\hero_7\Idle\i08.png'), pygame.image.load('sprite\hero_7\Idle\i09.png'), pygame.image.load('sprite\hero_7\Idle\i10.png'), pygame.image.load('sprite\hero_7\Idle\i11.png'), pygame.image.load('sprite\hero_7\Idle\i12.png'), pygame.image.load('sprite\hero_7\Idle\i13.png'), pygame.image.load('sprite\hero_7\Idle\i14.png'), pygame.image.load('sprite\hero_7\Idle\i15.png'), pygame.image.load('sprite\hero_7\Idle\i16.png'), pygame.image.load('sprite\hero_7\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_7 = [pygame.image.load('sprite\hero_7\Walking\i00.png'), pygame.image.load('sprite\hero_7\Walking\i01.png'),
          pygame.image.load('sprite\hero_7\Walking\i02.png'), pygame.image.load('sprite\hero_7\Walking\i03.png'),
          pygame.image.load('sprite\hero_7\Walking\i04.png'), pygame.image.load('sprite\hero_7\Walking\i05.png'),
          pygame.image.load('sprite\hero_7\Walking\i06.png'), pygame.image.load('sprite\hero_7\Walking\i07.png'),
          pygame.image.load('sprite\hero_7\Walking\i08.png'), pygame.image.load('sprite\hero_7\Walking\i09.png'),
          pygame.image.load('sprite\hero_7\Walking\i10.png'), pygame.image.load('sprite\hero_7\Walking\i11.png'),
          pygame.image.load('sprite\hero_7\Walking\i12.png'), pygame.image.load('sprite\hero_7\Walking\i13.png'),
          pygame.image.load('sprite\hero_7\Walking\i14.png'), pygame.image.load('sprite\hero_7\Walking\i15.png'),
          pygame.image.load('sprite\hero_7\Walking\i16.png'), pygame.image.load('sprite\hero_7\Walking\i17.png'),
          pygame.image.load('sprite\hero_7\Walking\i18.png'), pygame.image.load('sprite\hero_7\Walking\i19.png'),
          pygame.image.load('sprite\hero_7\Walking\i20.png'), pygame.image.load('sprite\hero_7\Walking\i21.png'),
          pygame.image.load('sprite\hero_7\Walking\i22.png'), pygame.image.load('sprite\hero_7\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_7 = [pygame.image.load('sprite\hero_7\Kicking\i00.png'), pygame.image.load('sprite\hero_7\Kicking\i01.png'),
          pygame.image.load('sprite\hero_7\Kicking\i02.png'), pygame.image.load('sprite\hero_7\Kicking\i03.png'),
          pygame.image.load('sprite\hero_7\Kicking\i04.png'), pygame.image.load('sprite\hero_7\Kicking\i05.png'),
          pygame.image.load('sprite\hero_7\Kicking\i06.png'), pygame.image.load('sprite\hero_7\Kicking\i07.png'),
          pygame.image.load('sprite\hero_7\Kicking\i08.png'), pygame.image.load('sprite\hero_7\Kicking\i09.png'),
          pygame.image.load('sprite\hero_7\Kicking\i10.png'), pygame.image.load('sprite\hero_7\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_7 = [pygame.image.load('sprite\hero_7\Dying\i00.png'), pygame.image.load('sprite\hero_7\Dying\i01.png'),
           pygame.image.load('sprite\hero_7\Dying\i02.png'), pygame.image.load('sprite\hero_7\Dying\i03.png'),
           pygame.image.load('sprite\hero_7\Dying\i04.png'), pygame.image.load('sprite\hero_7\Dying\i05.png'),
           pygame.image.load('sprite\hero_7\Dying\i06.png'), pygame.image.load('sprite\hero_7\Dying\i07.png'),
           pygame.image.load('sprite\hero_7\Dying\i08.png'), pygame.image.load('sprite\hero_7\Dying\i09.png'),
           pygame.image.load('sprite\hero_7\Dying\i10.png'), pygame.image.load('sprite\hero_7\Dying\i11.png'),
           pygame.image.load('sprite\hero_7\Dying\i12.png'), pygame.image.load('sprite\hero_7\Dying\i13.png'),
           pygame.image.load('sprite\hero_7\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_7 = []
idle_l_7 = []
kick_l_7 = []
dying_l_7 = []
for i in range(0, 18):
    idle_7[i] = (pygame.transform.scale(idle_7[i], (200, 200)))
    idle_l_7.append(pygame.transform.flip(idle_7[i], True, False))
for i in range(0, 24):
    walk_7[i] = (pygame.transform.scale(walk_7[i], (200, 200)))
    walk_l_7.append(pygame.transform.flip(walk_7[i], True, False))
for i in range(0, 12):
    kick_7[i] = (pygame.transform.scale(kick_7[i], (200, 200)))
    kick_l_7.append(pygame.transform.flip(kick_7[i], True, False))
for i in range(0, 15):
    dying_7[i] = (pygame.transform.scale(dying_7[i], (200, 200)))
    dying_l_7.append(pygame.transform.flip(dying_7[i], True, False))

idle_8 = [pygame.image.load('sprite\hero_8\Idle\i00.png'), pygame.image.load('sprite\hero_8\Idle\i01.png'), pygame.image.load('sprite\hero_8\Idle\i02.png'), pygame.image.load('sprite\hero_8\Idle\i03.png'), pygame.image.load('sprite\hero_8\Idle\i04.png'), pygame.image.load('sprite\hero_8\Idle\i05.png'), pygame.image.load('sprite\hero_8\Idle\i06.png'), pygame.image.load('sprite\hero_8\Idle\i07.png'), pygame.image.load('sprite\hero_8\Idle\i08.png'), pygame.image.load('sprite\hero_8\Idle\i09.png'), pygame.image.load('sprite\hero_8\Idle\i10.png'), pygame.image.load('sprite\hero_8\Idle\i11.png'), pygame.image.load('sprite\hero_8\Idle\i12.png'), pygame.image.load('sprite\hero_8\Idle\i13.png'), pygame.image.load('sprite\hero_8\Idle\i14.png'), pygame.image.load('sprite\hero_8\Idle\i15.png'), pygame.image.load('sprite\hero_8\Idle\i16.png'), pygame.image.load('sprite\hero_8\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_8 = [pygame.image.load('sprite\hero_8\Walking\i00.png'), pygame.image.load('sprite\hero_8\Walking\i01.png'),
          pygame.image.load('sprite\hero_8\Walking\i02.png'), pygame.image.load('sprite\hero_8\Walking\i03.png'),
          pygame.image.load('sprite\hero_8\Walking\i04.png'), pygame.image.load('sprite\hero_8\Walking\i05.png'),
          pygame.image.load('sprite\hero_8\Walking\i06.png'), pygame.image.load('sprite\hero_8\Walking\i07.png'),
          pygame.image.load('sprite\hero_8\Walking\i08.png'), pygame.image.load('sprite\hero_8\Walking\i09.png'),
          pygame.image.load('sprite\hero_8\Walking\i10.png'), pygame.image.load('sprite\hero_8\Walking\i11.png'),
          pygame.image.load('sprite\hero_8\Walking\i12.png'), pygame.image.load('sprite\hero_8\Walking\i13.png'),
          pygame.image.load('sprite\hero_8\Walking\i14.png'), pygame.image.load('sprite\hero_8\Walking\i15.png'),
          pygame.image.load('sprite\hero_8\Walking\i16.png'), pygame.image.load('sprite\hero_8\Walking\i17.png'),
          pygame.image.load('sprite\hero_8\Walking\i18.png'), pygame.image.load('sprite\hero_8\Walking\i19.png'),
          pygame.image.load('sprite\hero_8\Walking\i20.png'), pygame.image.load('sprite\hero_8\Walking\i21.png'),
          pygame.image.load('sprite\hero_8\Walking\i22.png'), pygame.image.load('sprite\hero_8\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_8 = [pygame.image.load('sprite\hero_8\Kicking\i00.png'), pygame.image.load('sprite\hero_8\Kicking\i01.png'),
          pygame.image.load('sprite\hero_8\Kicking\i02.png'), pygame.image.load('sprite\hero_8\Kicking\i03.png'),
          pygame.image.load('sprite\hero_8\Kicking\i04.png'), pygame.image.load('sprite\hero_8\Kicking\i05.png'),
          pygame.image.load('sprite\hero_8\Kicking\i06.png'), pygame.image.load('sprite\hero_8\Kicking\i07.png'),
          pygame.image.load('sprite\hero_8\Kicking\i08.png'), pygame.image.load('sprite\hero_8\Kicking\i09.png'),
          pygame.image.load('sprite\hero_8\Kicking\i10.png'), pygame.image.load('sprite\hero_8\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_8 = [pygame.image.load('sprite\hero_8\Dying\i00.png'), pygame.image.load('sprite\hero_8\Dying\i01.png'),
           pygame.image.load('sprite\hero_8\Dying\i02.png'), pygame.image.load('sprite\hero_8\Dying\i03.png'),
           pygame.image.load('sprite\hero_8\Dying\i04.png'), pygame.image.load('sprite\hero_8\Dying\i05.png'),
           pygame.image.load('sprite\hero_8\Dying\i06.png'), pygame.image.load('sprite\hero_8\Dying\i07.png'),
           pygame.image.load('sprite\hero_8\Dying\i08.png'), pygame.image.load('sprite\hero_8\Dying\i09.png'),
           pygame.image.load('sprite\hero_8\Dying\i10.png'), pygame.image.load('sprite\hero_8\Dying\i11.png'),
           pygame.image.load('sprite\hero_8\Dying\i12.png'), pygame.image.load('sprite\hero_8\Dying\i13.png'),
           pygame.image.load('sprite\hero_8\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_8 = []
idle_l_8 = []
kick_l_8 = []
dying_l_8 = []
for i in range(0, 18):
    idle_8[i] = (pygame.transform.scale(idle_8[i], (200, 200)))
    idle_l_8.append(pygame.transform.flip(idle_8[i], True, False))
for i in range(0, 24):
    walk_8[i] = (pygame.transform.scale(walk_8[i], (200, 200)))
    walk_l_8.append(pygame.transform.flip(walk_8[i], True, False))
for i in range(0, 12):
    kick_8[i] = (pygame.transform.scale(kick_8[i], (200, 200)))
    kick_l_8.append(pygame.transform.flip(kick_8[i], True, False))
for i in range(0, 15):
    dying_8[i] = (pygame.transform.scale(dying_8[i], (200, 200)))
    dying_l_8.append(pygame.transform.flip(dying_8[i], True, False))

idle_9 = [pygame.image.load('sprite\hero_9\Idle\i00.png'), pygame.image.load('sprite\hero_9\Idle\i01.png'), pygame.image.load('sprite\hero_9\Idle\i02.png'), pygame.image.load('sprite\hero_9\Idle\i03.png'), pygame.image.load('sprite\hero_9\Idle\i04.png'), pygame.image.load('sprite\hero_9\Idle\i05.png'), pygame.image.load('sprite\hero_9\Idle\i06.png'), pygame.image.load('sprite\hero_9\Idle\i07.png'), pygame.image.load('sprite\hero_9\Idle\i08.png'), pygame.image.load('sprite\hero_9\Idle\i09.png'), pygame.image.load('sprite\hero_9\Idle\i10.png'), pygame.image.load('sprite\hero_9\Idle\i11.png'), pygame.image.load('sprite\hero_9\Idle\i12.png'), pygame.image.load('sprite\hero_9\Idle\i13.png'), pygame.image.load('sprite\hero_9\Idle\i14.png'), pygame.image.load('sprite\hero_9\Idle\i15.png'), pygame.image.load('sprite\hero_9\Idle\i16.png'), pygame.image.load('sprite\hero_9\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_9 = [pygame.image.load('sprite\hero_9\Walking\i00.png'), pygame.image.load('sprite\hero_9\Walking\i01.png'),
          pygame.image.load('sprite\hero_9\Walking\i02.png'), pygame.image.load('sprite\hero_9\Walking\i03.png'),
          pygame.image.load('sprite\hero_9\Walking\i04.png'), pygame.image.load('sprite\hero_9\Walking\i05.png'),
          pygame.image.load('sprite\hero_9\Walking\i06.png'), pygame.image.load('sprite\hero_9\Walking\i07.png'),
          pygame.image.load('sprite\hero_9\Walking\i08.png'), pygame.image.load('sprite\hero_9\Walking\i09.png'),
          pygame.image.load('sprite\hero_9\Walking\i10.png'), pygame.image.load('sprite\hero_9\Walking\i11.png'),
          pygame.image.load('sprite\hero_9\Walking\i12.png'), pygame.image.load('sprite\hero_9\Walking\i13.png'),
          pygame.image.load('sprite\hero_9\Walking\i14.png'), pygame.image.load('sprite\hero_9\Walking\i15.png'),
          pygame.image.load('sprite\hero_9\Walking\i16.png'), pygame.image.load('sprite\hero_9\Walking\i17.png'),
          pygame.image.load('sprite\hero_9\Walking\i18.png'), pygame.image.load('sprite\hero_9\Walking\i19.png'),
          pygame.image.load('sprite\hero_9\Walking\i20.png'), pygame.image.load('sprite\hero_9\Walking\i21.png'),
          pygame.image.load('sprite\hero_9\Walking\i22.png'), pygame.image.load('sprite\hero_9\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_9 = [pygame.image.load('sprite\hero_9\Kicking\i00.png'), pygame.image.load('sprite\hero_9\Kicking\i01.png'),
          pygame.image.load('sprite\hero_9\Kicking\i02.png'), pygame.image.load('sprite\hero_9\Kicking\i03.png'),
          pygame.image.load('sprite\hero_9\Kicking\i04.png'), pygame.image.load('sprite\hero_9\Kicking\i05.png'),
          pygame.image.load('sprite\hero_9\Kicking\i06.png'), pygame.image.load('sprite\hero_9\Kicking\i07.png'),
          pygame.image.load('sprite\hero_9\Kicking\i08.png'), pygame.image.load('sprite\hero_9\Kicking\i09.png'),
          pygame.image.load('sprite\hero_9\Kicking\i10.png'), pygame.image.load('sprite\hero_9\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_9 = [pygame.image.load('sprite\hero_9\Dying\i00.png'), pygame.image.load('sprite\hero_9\Dying\i01.png'),
           pygame.image.load('sprite\hero_9\Dying\i02.png'), pygame.image.load('sprite\hero_9\Dying\i03.png'),
           pygame.image.load('sprite\hero_9\Dying\i04.png'), pygame.image.load('sprite\hero_9\Dying\i05.png'),
           pygame.image.load('sprite\hero_9\Dying\i06.png'), pygame.image.load('sprite\hero_9\Dying\i07.png'),
           pygame.image.load('sprite\hero_9\Dying\i08.png'), pygame.image.load('sprite\hero_9\Dying\i09.png'),
           pygame.image.load('sprite\hero_9\Dying\i10.png'), pygame.image.load('sprite\hero_9\Dying\i11.png'),
           pygame.image.load('sprite\hero_9\Dying\i12.png'), pygame.image.load('sprite\hero_9\Dying\i13.png'),
           pygame.image.load('sprite\hero_9\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1

walk_l_9 = []
idle_l_9 = []
kick_l_9 = []
dying_l_9 = []
for i in range(0, 18):
    idle_9[i] = (pygame.transform.scale(idle_9[i], (200, 200)))
    idle_l_9.append(pygame.transform.flip(idle_9[i], True, False))
for i in range(0, 24):
    walk_9[i] = (pygame.transform.scale(walk_9[i], (200, 200)))
    walk_l_9.append(pygame.transform.flip(walk_9[i], True, False))
for i in range(0, 12):
    kick_9[i] = (pygame.transform.scale(kick_9[i], (200, 200)))
    kick_l_9.append(pygame.transform.flip(kick_9[i], True, False))
for i in range(0, 15):
    dying_9[i] = (pygame.transform.scale(dying_9[i], (200, 200)))
    dying_l_9.append(pygame.transform.flip(dying_9[i], True, False))

idle_10 = [pygame.image.load('sprite\hero_10\Idle\i00.png'), pygame.image.load('sprite\hero_10\Idle\i01.png'), pygame.image.load('sprite\hero_10\Idle\i02.png'), pygame.image.load('sprite\hero_10\Idle\i03.png'), pygame.image.load('sprite\hero_10\Idle\i04.png'), pygame.image.load('sprite\hero_10\Idle\i05.png'), pygame.image.load('sprite\hero_10\Idle\i06.png'), pygame.image.load('sprite\hero_10\Idle\i07.png'), pygame.image.load('sprite\hero_10\Idle\i08.png'), pygame.image.load('sprite\hero_10\Idle\i09.png'), pygame.image.load('sprite\hero_10\Idle\i10.png'), pygame.image.load('sprite\hero_10\Idle\i11.png'), pygame.image.load('sprite\hero_10\Idle\i12.png'), pygame.image.load('sprite\hero_10\Idle\i13.png'), pygame.image.load('sprite\hero_10\Idle\i14.png'), pygame.image.load('sprite\hero_10\Idle\i15.png'), pygame.image.load('sprite\hero_10\Idle\i16.png'), pygame.image.load('sprite\hero_10\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_10 = [pygame.image.load('sprite\hero_10\Walking\i00.png'), pygame.image.load('sprite\hero_10\Walking\i01.png'),
          pygame.image.load('sprite\hero_10\Walking\i02.png'), pygame.image.load('sprite\hero_10\Walking\i03.png'),
          pygame.image.load('sprite\hero_10\Walking\i04.png'), pygame.image.load('sprite\hero_10\Walking\i05.png'),
          pygame.image.load('sprite\hero_10\Walking\i06.png'), pygame.image.load('sprite\hero_10\Walking\i07.png'),
          pygame.image.load('sprite\hero_10\Walking\i08.png'), pygame.image.load('sprite\hero_10\Walking\i09.png'),
          pygame.image.load('sprite\hero_10\Walking\i10.png'), pygame.image.load('sprite\hero_10\Walking\i11.png'),
          pygame.image.load('sprite\hero_10\Walking\i12.png'), pygame.image.load('sprite\hero_10\Walking\i13.png'),
          pygame.image.load('sprite\hero_10\Walking\i14.png'), pygame.image.load('sprite\hero_10\Walking\i15.png'),
          pygame.image.load('sprite\hero_10\Walking\i16.png'), pygame.image.load('sprite\hero_10\Walking\i17.png'),
          pygame.image.load('sprite\hero_10\Walking\i18.png'), pygame.image.load('sprite\hero_10\Walking\i19.png'),
          pygame.image.load('sprite\hero_10\Walking\i20.png'), pygame.image.load('sprite\hero_10\Walking\i21.png'),
          pygame.image.load('sprite\hero_10\Walking\i22.png'), pygame.image.load('sprite\hero_10\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_10 = [pygame.image.load('sprite\hero_10\Kicking\i00.png'), pygame.image.load('sprite\hero_10\Kicking\i01.png'),
          pygame.image.load('sprite\hero_10\Kicking\i02.png'), pygame.image.load('sprite\hero_10\Kicking\i03.png'),
          pygame.image.load('sprite\hero_10\Kicking\i04.png'), pygame.image.load('sprite\hero_10\Kicking\i05.png'),
          pygame.image.load('sprite\hero_10\Kicking\i06.png'), pygame.image.load('sprite\hero_10\Kicking\i07.png'),
          pygame.image.load('sprite\hero_10\Kicking\i08.png'), pygame.image.load('sprite\hero_10\Kicking\i09.png'),
          pygame.image.load('sprite\hero_10\Kicking\i10.png'), pygame.image.load('sprite\hero_10\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_10 = [pygame.image.load('sprite\hero_10\Dying\i00.png'), pygame.image.load('sprite\hero_10\Dying\i01.png'),
           pygame.image.load('sprite\hero_10\Dying\i02.png'), pygame.image.load('sprite\hero_10\Dying\i03.png'),
           pygame.image.load('sprite\hero_10\Dying\i04.png'), pygame.image.load('sprite\hero_10\Dying\i05.png'),
           pygame.image.load('sprite\hero_10\Dying\i06.png'), pygame.image.load('sprite\hero_10\Dying\i07.png'),
           pygame.image.load('sprite\hero_10\Dying\i08.png'), pygame.image.load('sprite\hero_10\Dying\i09.png'),
           pygame.image.load('sprite\hero_10\Dying\i10.png'), pygame.image.load('sprite\hero_10\Dying\i11.png'),
           pygame.image.load('sprite\hero_10\Dying\i12.png'), pygame.image.load('sprite\hero_10\Dying\i13.png'),
           pygame.image.load('sprite\hero_10\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_10 = []
idle_l_10 = []
kick_l_10 = []
dying_l_10 = []
for i in range(0, 18):
    idle_10[i] = (pygame.transform.scale(idle_10[i], (200, 200)))
    idle_l_10.append(pygame.transform.flip(idle_10[i], True, False))
for i in range(0, 24):
    walk_10[i] = (pygame.transform.scale(walk_10[i], (200, 200)))
    walk_l_10.append(pygame.transform.flip(walk_10[i], True, False))
for i in range(0, 12):
    kick_10[i] = (pygame.transform.scale(kick_10[i], (200, 200)))
    kick_l_10.append(pygame.transform.flip(kick_10[i], True, False))
for i in range(0, 15):
    dying_10[i] = (pygame.transform.scale(dying_10[i], (200, 200)))
    dying_l_10.append(pygame.transform.flip(dying_10[i], True, False))

idle_11 = [pygame.image.load('sprite\hero_11\Idle\i00.png'), pygame.image.load('sprite\hero_11\Idle\i01.png'), pygame.image.load('sprite\hero_11\Idle\i02.png'), pygame.image.load('sprite\hero_11\Idle\i03.png'), pygame.image.load('sprite\hero_11\Idle\i04.png'), pygame.image.load('sprite\hero_11\Idle\i05.png'), pygame.image.load('sprite\hero_11\Idle\i06.png'), pygame.image.load('sprite\hero_11\Idle\i07.png'), pygame.image.load('sprite\hero_11\Idle\i08.png'), pygame.image.load('sprite\hero_11\Idle\i09.png'), pygame.image.load('sprite\hero_11\Idle\i10.png'), pygame.image.load('sprite\hero_11\Idle\i11.png'), pygame.image.load('sprite\hero_11\Idle\i12.png'), pygame.image.load('sprite\hero_11\Idle\i13.png'), pygame.image.load('sprite\hero_11\Idle\i14.png'), pygame.image.load('sprite\hero_11\Idle\i15.png'), pygame.image.load('sprite\hero_11\Idle\i16.png'), pygame.image.load('sprite\hero_11\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_11 = [pygame.image.load('sprite\hero_11\Walking\i00.png'), pygame.image.load('sprite\hero_11\Walking\i01.png'),
          pygame.image.load('sprite\hero_11\Walking\i02.png'), pygame.image.load('sprite\hero_11\Walking\i03.png'),
          pygame.image.load('sprite\hero_11\Walking\i04.png'), pygame.image.load('sprite\hero_11\Walking\i05.png'),
          pygame.image.load('sprite\hero_11\Walking\i06.png'), pygame.image.load('sprite\hero_11\Walking\i07.png'),
          pygame.image.load('sprite\hero_11\Walking\i08.png'), pygame.image.load('sprite\hero_11\Walking\i09.png'),
          pygame.image.load('sprite\hero_11\Walking\i10.png'), pygame.image.load('sprite\hero_11\Walking\i11.png'),
          pygame.image.load('sprite\hero_11\Walking\i12.png'), pygame.image.load('sprite\hero_11\Walking\i13.png'),
          pygame.image.load('sprite\hero_11\Walking\i14.png'), pygame.image.load('sprite\hero_11\Walking\i15.png'),
          pygame.image.load('sprite\hero_11\Walking\i16.png'), pygame.image.load('sprite\hero_11\Walking\i17.png'),
          pygame.image.load('sprite\hero_11\Walking\i18.png'), pygame.image.load('sprite\hero_11\Walking\i19.png'),
          pygame.image.load('sprite\hero_11\Walking\i20.png'), pygame.image.load('sprite\hero_11\Walking\i21.png'),
          pygame.image.load('sprite\hero_11\Walking\i22.png'), pygame.image.load('sprite\hero_11\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_11 = [pygame.image.load('sprite\hero_11\Kicking\i00.png'), pygame.image.load('sprite\hero_11\Kicking\i01.png'),
          pygame.image.load('sprite\hero_11\Kicking\i02.png'), pygame.image.load('sprite\hero_11\Kicking\i03.png'),
          pygame.image.load('sprite\hero_11\Kicking\i04.png'), pygame.image.load('sprite\hero_11\Kicking\i05.png'),
          pygame.image.load('sprite\hero_11\Kicking\i06.png'), pygame.image.load('sprite\hero_11\Kicking\i07.png'),
          pygame.image.load('sprite\hero_11\Kicking\i08.png'), pygame.image.load('sprite\hero_11\Kicking\i09.png'),
          pygame.image.load('sprite\hero_11\Kicking\i10.png'), pygame.image.load('sprite\hero_11\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_11 = [pygame.image.load('sprite\hero_11\Dying\i00.png'), pygame.image.load('sprite\hero_11\Dying\i01.png'),
           pygame.image.load('sprite\hero_11\Dying\i02.png'), pygame.image.load('sprite\hero_11\Dying\i03.png'),
           pygame.image.load('sprite\hero_11\Dying\i04.png'), pygame.image.load('sprite\hero_11\Dying\i05.png'),
           pygame.image.load('sprite\hero_11\Dying\i06.png'), pygame.image.load('sprite\hero_11\Dying\i07.png'),
           pygame.image.load('sprite\hero_11\Dying\i08.png'), pygame.image.load('sprite\hero_11\Dying\i09.png'),
           pygame.image.load('sprite\hero_11\Dying\i10.png'), pygame.image.load('sprite\hero_11\Dying\i11.png'),
           pygame.image.load('sprite\hero_11\Dying\i12.png'), pygame.image.load('sprite\hero_11\Dying\i13.png'),
           pygame.image.load('sprite\hero_11\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_11 = []
idle_l_11 = []
kick_l_11 = []
dying_l_11 = []
for i in range(0, 18):
    idle_11[i] = (pygame.transform.scale(idle_11[i], (200, 200)))
    idle_l_11.append(pygame.transform.flip(idle_11[i], True, False))
for i in range(0, 24):
    walk_11[i] = (pygame.transform.scale(walk_11[i], (200, 200)))
    walk_l_11.append(pygame.transform.flip(walk_11[i], True, False))
for i in range(0, 12):
    kick_11[i] = (pygame.transform.scale(kick_11[i], (200, 200)))
    kick_l_11.append(pygame.transform.flip(kick_11[i], True, False))
for i in range(0, 15):
    dying_11[i] = (pygame.transform.scale(dying_11[i], (200, 200)))
    dying_l_11.append(pygame.transform.flip(dying_11[i], True, False))


idle_12 = [pygame.image.load('sprite\hero_12\Idle\i00.png'), pygame.image.load('sprite\hero_12\Idle\i01.png'), pygame.image.load('sprite\hero_12\Idle\i02.png'), pygame.image.load('sprite\hero_12\Idle\i03.png'), pygame.image.load('sprite\hero_12\Idle\i04.png'), pygame.image.load('sprite\hero_12\Idle\i05.png'), pygame.image.load('sprite\hero_12\Idle\i06.png'), pygame.image.load('sprite\hero_12\Idle\i07.png'), pygame.image.load('sprite\hero_12\Idle\i08.png'), pygame.image.load('sprite\hero_12\Idle\i09.png'), pygame.image.load('sprite\hero_12\Idle\i10.png'), pygame.image.load('sprite\hero_12\Idle\i11.png'), pygame.image.load('sprite\hero_12\Idle\i12.png'), pygame.image.load('sprite\hero_12\Idle\i13.png'), pygame.image.load('sprite\hero_12\Idle\i14.png'), pygame.image.load('sprite\hero_12\Idle\i15.png'), pygame.image.load('sprite\hero_12\Idle\i16.png'), pygame.image.load('sprite\hero_12\Idle\i17.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_12 = [pygame.image.load('sprite\hero_12\Walking\i00.png'), pygame.image.load('sprite\hero_12\Walking\i01.png'),
          pygame.image.load('sprite\hero_12\Walking\i02.png'), pygame.image.load('sprite\hero_12\Walking\i03.png'),
          pygame.image.load('sprite\hero_12\Walking\i04.png'), pygame.image.load('sprite\hero_12\Walking\i05.png'),
          pygame.image.load('sprite\hero_12\Walking\i06.png'), pygame.image.load('sprite\hero_12\Walking\i07.png'),
          pygame.image.load('sprite\hero_12\Walking\i08.png'), pygame.image.load('sprite\hero_12\Walking\i09.png'),
          pygame.image.load('sprite\hero_12\Walking\i10.png'), pygame.image.load('sprite\hero_12\Walking\i11.png'),
          pygame.image.load('sprite\hero_12\Walking\i12.png'), pygame.image.load('sprite\hero_12\Walking\i13.png'),
          pygame.image.load('sprite\hero_12\Walking\i14.png'), pygame.image.load('sprite\hero_12\Walking\i15.png'),
          pygame.image.load('sprite\hero_12\Walking\i16.png'), pygame.image.load('sprite\hero_12\Walking\i17.png'),
          pygame.image.load('sprite\hero_12\Walking\i18.png'), pygame.image.load('sprite\hero_12\Walking\i19.png'),
          pygame.image.load('sprite\hero_12\Walking\i20.png'), pygame.image.load('sprite\hero_12\Walking\i21.png'),
          pygame.image.load('sprite\hero_12\Walking\i22.png'), pygame.image.load('sprite\hero_12\Walking\i23.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
kick_12 = [pygame.image.load('sprite\hero_12\Kicking\i00.png'), pygame.image.load('sprite\hero_12\Kicking\i01.png'),
          pygame.image.load('sprite\hero_12\Kicking\i02.png'), pygame.image.load('sprite\hero_12\Kicking\i03.png'),
          pygame.image.load('sprite\hero_12\Kicking\i04.png'), pygame.image.load('sprite\hero_12\Kicking\i05.png'),
          pygame.image.load('sprite\hero_12\Kicking\i06.png'), pygame.image.load('sprite\hero_12\Kicking\i07.png'),
          pygame.image.load('sprite\hero_12\Kicking\i08.png'), pygame.image.load('sprite\hero_12\Kicking\i09.png'),
          pygame.image.load('sprite\hero_12\Kicking\i10.png'), pygame.image.load('sprite\hero_12\Kicking\i11.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
dying_12 = [pygame.image.load('sprite\hero_12\Dying\i00.png'), pygame.image.load('sprite\hero_12\Dying\i01.png'),
           pygame.image.load('sprite\hero_12\Dying\i02.png'), pygame.image.load('sprite\hero_12\Dying\i03.png'),
           pygame.image.load('sprite\hero_12\Dying\i04.png'), pygame.image.load('sprite\hero_12\Dying\i05.png'),
           pygame.image.load('sprite\hero_12\Dying\i06.png'), pygame.image.load('sprite\hero_12\Dying\i07.png'),
           pygame.image.load('sprite\hero_12\Dying\i08.png'), pygame.image.load('sprite\hero_12\Dying\i09.png'),
           pygame.image.load('sprite\hero_12\Dying\i10.png'), pygame.image.load('sprite\hero_12\Dying\i11.png'),
           pygame.image.load('sprite\hero_12\Dying\i12.png'), pygame.image.load('sprite\hero_12\Dying\i13.png'),
           pygame.image.load('sprite\hero_12\Dying\i14.png')]
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
walk_l_12 = []
idle_l_12 = []
kick_l_12 = []
dying_l_12 = []
for i in range(0, 18):
    idle_12[i] = (pygame.transform.scale(idle_12[i], (200, 200)))
    idle_l_12.append(pygame.transform.flip(idle_12[i], True, False))
for i in range(0, 24):
    walk_12[i] = (pygame.transform.scale(walk_12[i], (200, 200)))
    walk_l_12.append(pygame.transform.flip(walk_12[i], True, False))
for i in range(0, 12):
    kick_12[i] = (pygame.transform.scale(kick_12[i], (200, 200)))
    kick_l_12.append(pygame.transform.flip(kick_12[i], True, False))
for i in range(0, 15):
    dying_12[i] = (pygame.transform.scale(dying_12[i], (200, 200)))
    dying_l_12.append(pygame.transform.flip(dying_12[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
idle = [idle_9, idle_6, idle_12, idle_4, idle_1, idle_7, idle_2, idle_8, idle_5, idle_10, idle_3, idle_11]
walk = [walk_9, walk_6, walk_12, walk_4, walk_1, walk_7, walk_2, walk_8, walk_5, walk_10, walk_3, walk_11]
kick = [kick_9, kick_6, kick_12, kick_4, kick_1, kick_7, kick_2, kick_8, kick_5, kick_10, kick_3, kick_11]
dying = [dying_9, dying_6, dying_12, dying_4, dying_1, dying_7, dying_2, dying_8, dying_5, dying_10, dying_3, dying_11]

returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1

idle_l = [idle_l_9, idle_l_6, idle_l_12, idle_l_4, idle_l_1, idle_l_7, idle_l_2, idle_l_8, idle_l_5, idle_l_10, idle_l_3, idle_l_11]
walk_l = [walk_l_9, walk_l_6, walk_l_12, walk_l_4, walk_l_1, walk_l_7, walk_l_2, walk_l_8, walk_l_5, walk_l_10, walk_l_3, walk_l_11]
kick_l = [kick_l_9, kick_l_6, kick_l_12, kick_l_4, kick_l_1, kick_l_7, kick_l_2, kick_l_8, kick_l_5, kick_l_10, kick_l_3, kick_l_11]
dying_l = [dying_l_9, dying_l_6, dying_l_12, dying_l_4, dying_l_1, dying_l_7, dying_l_2, dying_l_8, dying_l_5, dying_l_10, dying_l_3, dying_l_11]
returned_background_index = loading_(per_cent, returned_background_index)

# 1 bot
i_b_1 = [
    pygame.image.load('sprite\_bot_1\I\i00.png'),
    pygame.image.load('sprite\_bot_1\I\i01.png'),
    pygame.image.load('sprite\_bot_1\I\i02.png'),
    pygame.image.load('sprite\_bot_1\I\i03.png'),
    pygame.image.load('sprite\_bot_1\I\i04.png'),
    pygame.image.load('sprite\_bot_1\I\i05.png'),
    pygame.image.load('sprite\_bot_1\I\i06.png'),
    pygame.image.load('sprite\_bot_1\I\i07.png'),
    pygame.image.load('sprite\_bot_1\I\i08.png'),
    pygame.image.load('sprite\_bot_1\I\i09.png'),
    pygame.image.load('sprite\_bot_1\I\i10.png'),
    pygame.image.load('sprite\_bot_1\I\i11.png')
]
i_b_l_1 = []
for i in range(0, 12):
    i_b_1[i] = (pygame.transform.scale(i_b_1[i], (240, 160)))
    i_b_l_1.append(pygame.transform.flip(i_b_1[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_1 = [
    pygame.image.load('sprite\_bot_1\A\i00.png'),
    pygame.image.load('sprite\_bot_1\A\i01.png'),
    pygame.image.load('sprite\_bot_1\A\i02.png'),
    pygame.image.load('sprite\_bot_1\A\i03.png'),
    pygame.image.load('sprite\_bot_1\A\i04.png'),
    pygame.image.load('sprite\_bot_1\A\i05.png'),
    pygame.image.load('sprite\_bot_1\A\i06.png'),
    pygame.image.load('sprite\_bot_1\A\i07.png'),
    pygame.image.load('sprite\_bot_1\A\i08.png'),
    pygame.image.load('sprite\_bot_1\A\i09.png'),
    pygame.image.load('sprite\_bot_1\A\i10.png'),
    pygame.image.load('sprite\_bot_1\A\i11.png')
]
a_b_l_1 = []
for i in range(0, 12):
    a_b_1[i] = (pygame.transform.scale(a_b_1[i], (240, 160)))
    a_b_l_1.append(pygame.transform.flip(a_b_1[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_1 = [
    pygame.image.load('sprite\_bot_1\W\i00.png'),
    pygame.image.load('sprite\_bot_1\W\i01.png'),
    pygame.image.load('sprite\_bot_1\W\i02.png'),
    pygame.image.load('sprite\_bot_1\W\i03.png'),
    pygame.image.load('sprite\_bot_1\W\i04.png'),
    pygame.image.load('sprite\_bot_1\W\i05.png'),
    pygame.image.load('sprite\_bot_1\W\i06.png'),
    pygame.image.load('sprite\_bot_1\W\i07.png'),
    pygame.image.load('sprite\_bot_1\W\i08.png'),
    pygame.image.load('sprite\_bot_1\W\i09.png'),
    pygame.image.load('sprite\_bot_1\W\i10.png'),
    pygame.image.load('sprite\_bot_1\W\i11.png'),
    pygame.image.load('sprite\_bot_1\W\i12.png'),
    pygame.image.load('sprite\_bot_1\W\i13.png'),
    pygame.image.load('sprite\_bot_1\W\i14.png'),
    pygame.image.load('sprite\_bot_1\W\i15.png'),
    pygame.image.load('sprite\_bot_1\W\i16.png'),
    pygame.image.load('sprite\_bot_1\W\i17.png')
]
w_b_l_1 = []
for i in range(0, 18):
    w_b_1[i] = (pygame.transform.scale(w_b_1[i], (240, 160)))
    w_b_l_1.append(pygame.transform.flip(w_b_1[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_1 = [
    pygame.image.load('sprite\_bot_1\D\i00.png'),
    pygame.image.load('sprite\_bot_1\D\i01.png'),
    pygame.image.load('sprite\_bot_1\D\i02.png'),
    pygame.image.load('sprite\_bot_1\D\i03.png'),
    pygame.image.load('sprite\_bot_1\D\i04.png'),
    pygame.image.load('sprite\_bot_1\D\i05.png'),
    pygame.image.load('sprite\_bot_1\D\i06.png'),
    pygame.image.load('sprite\_bot_1\D\i07.png'),
    pygame.image.load('sprite\_bot_1\D\i08.png'),
    pygame.image.load('sprite\_bot_1\D\i09.png'),
    pygame.image.load('sprite\_bot_1\D\i10.png'),
    pygame.image.load('sprite\_bot_1\D\i11.png'),
    pygame.image.load('sprite\_bot_1\D\i12.png'),
    pygame.image.load('sprite\_bot_1\D\i13.png'),
    pygame.image.load('sprite\_bot_1\D\i14.png')
]
d_b_l_1 = []
for i in range(0, 15):
    d_b_1[i] = (pygame.transform.scale(d_b_1[i], (240, 160)))
    d_b_l_1.append(pygame.transform.flip(d_b_1[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1


# 2 bot
i_b_2 = [
    pygame.image.load('sprite\_bot_2\I\i00.png'),
    pygame.image.load('sprite\_bot_2\I\i01.png'),
    pygame.image.load('sprite\_bot_2\I\i02.png'),
    pygame.image.load('sprite\_bot_2\I\i03.png'),
    pygame.image.load('sprite\_bot_2\I\i04.png'),
    pygame.image.load('sprite\_bot_2\I\i05.png'),
    pygame.image.load('sprite\_bot_2\I\i06.png'),
    pygame.image.load('sprite\_bot_2\I\i07.png'),
    pygame.image.load('sprite\_bot_2\I\i08.png'),
    pygame.image.load('sprite\_bot_2\I\i09.png'),
    pygame.image.load('sprite\_bot_2\I\i10.png'),
    pygame.image.load('sprite\_bot_2\I\i11.png')
]
i_b_l_2 = []
for i in range(0, 12):
    i_b_2[i] = (pygame.transform.scale(i_b_2[i], (240, 160)))
    i_b_l_2.append(pygame.transform.flip(i_b_2[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_2 = [
    pygame.image.load('sprite\_bot_2\A\i00.png'),
    pygame.image.load('sprite\_bot_2\A\i01.png'),
    pygame.image.load('sprite\_bot_2\A\i02.png'),
    pygame.image.load('sprite\_bot_2\A\i03.png'),
    pygame.image.load('sprite\_bot_2\A\i04.png'),
    pygame.image.load('sprite\_bot_2\A\i05.png'),
    pygame.image.load('sprite\_bot_2\A\i06.png'),
    pygame.image.load('sprite\_bot_2\A\i07.png'),
    pygame.image.load('sprite\_bot_2\A\i08.png'),
    pygame.image.load('sprite\_bot_2\A\i09.png'),
    pygame.image.load('sprite\_bot_2\A\i10.png'),
    pygame.image.load('sprite\_bot_2\A\i11.png')
]
a_b_l_2 = []
for i in range(0, 12):
    a_b_2[i] = (pygame.transform.scale(a_b_2[i], (240, 160)))
    a_b_l_2.append(pygame.transform.flip(a_b_2[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_2 = [
    pygame.image.load('sprite\_bot_2\W\i00.png'),
    pygame.image.load('sprite\_bot_2\W\i01.png'),
    pygame.image.load('sprite\_bot_2\W\i02.png'),
    pygame.image.load('sprite\_bot_2\W\i03.png'),
    pygame.image.load('sprite\_bot_2\W\i04.png'),
    pygame.image.load('sprite\_bot_2\W\i05.png'),
    pygame.image.load('sprite\_bot_2\W\i06.png'),
    pygame.image.load('sprite\_bot_2\W\i07.png'),
    pygame.image.load('sprite\_bot_2\W\i08.png'),
    pygame.image.load('sprite\_bot_2\W\i09.png'),
    pygame.image.load('sprite\_bot_2\W\i10.png'),
    pygame.image.load('sprite\_bot_2\W\i11.png'),
    pygame.image.load('sprite\_bot_2\W\i12.png'),
    pygame.image.load('sprite\_bot_2\W\i13.png'),
    pygame.image.load('sprite\_bot_2\W\i14.png'),
    pygame.image.load('sprite\_bot_2\W\i15.png'),
    pygame.image.load('sprite\_bot_2\W\i16.png'),
    pygame.image.load('sprite\_bot_2\W\i17.png')
]
w_b_l_2 = []
for i in range(0, 18):
    w_b_2[i] = (pygame.transform.scale(w_b_2[i], (240, 160)))
    w_b_l_2.append(pygame.transform.flip(w_b_2[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_2 = [
    pygame.image.load('sprite\_bot_2\D\i00.png'),
    pygame.image.load('sprite\_bot_2\D\i01.png'),
    pygame.image.load('sprite\_bot_2\D\i02.png'),
    pygame.image.load('sprite\_bot_2\D\i03.png'),
    pygame.image.load('sprite\_bot_2\D\i04.png'),
    pygame.image.load('sprite\_bot_2\D\i05.png'),
    pygame.image.load('sprite\_bot_2\D\i06.png'),
    pygame.image.load('sprite\_bot_2\D\i07.png'),
    pygame.image.load('sprite\_bot_2\D\i08.png'),
    pygame.image.load('sprite\_bot_2\D\i09.png'),
    pygame.image.load('sprite\_bot_2\D\i10.png'),
    pygame.image.load('sprite\_bot_2\D\i11.png'),
    pygame.image.load('sprite\_bot_2\D\i12.png'),
    pygame.image.load('sprite\_bot_2\D\i13.png'),
    pygame.image.load('sprite\_bot_2\D\i14.png')
]
d_b_l_2 = []
for i in range(0, 15):
    d_b_2[i] = (pygame.transform.scale(d_b_2[i], (240, 160)))
    d_b_l_2.append(pygame.transform.flip(d_b_2[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1

# 3 bot
i_b_3 = [
    pygame.image.load('sprite\_bot_3\I\i00.png'),
    pygame.image.load('sprite\_bot_3\I\i01.png'),
    pygame.image.load('sprite\_bot_3\I\i02.png'),
    pygame.image.load('sprite\_bot_3\I\i03.png'),
    pygame.image.load('sprite\_bot_3\I\i04.png'),
    pygame.image.load('sprite\_bot_3\I\i05.png'),
    pygame.image.load('sprite\_bot_3\I\i06.png'),
    pygame.image.load('sprite\_bot_3\I\i07.png'),
    pygame.image.load('sprite\_bot_3\I\i08.png'),
    pygame.image.load('sprite\_bot_3\I\i09.png'),
    pygame.image.load('sprite\_bot_3\I\i10.png'),
    pygame.image.load('sprite\_bot_3\I\i11.png')
]
i_b_l_3 = []
for i in range(0, 12):
    i_b_3[i] = (pygame.transform.scale(i_b_3[i], (240, 160)))
    i_b_l_3.append(pygame.transform.flip(i_b_3[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_3 = [
    pygame.image.load('sprite\_bot_3\A\i00.png'),
    pygame.image.load('sprite\_bot_3\A\i01.png'),
    pygame.image.load('sprite\_bot_3\A\i02.png'),
    pygame.image.load('sprite\_bot_3\A\i03.png'),
    pygame.image.load('sprite\_bot_3\A\i04.png'),
    pygame.image.load('sprite\_bot_3\A\i05.png'),
    pygame.image.load('sprite\_bot_3\A\i06.png'),
    pygame.image.load('sprite\_bot_3\A\i07.png'),
    pygame.image.load('sprite\_bot_3\A\i08.png'),
    pygame.image.load('sprite\_bot_3\A\i09.png'),
    pygame.image.load('sprite\_bot_3\A\i10.png'),
    pygame.image.load('sprite\_bot_3\A\i11.png')
]
a_b_l_3 = []
for i in range(0, 12):
    a_b_3[i] = (pygame.transform.scale(a_b_3[i], (240, 160)))
    a_b_l_3.append(pygame.transform.flip(a_b_3[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_3 = [
    pygame.image.load('sprite\_bot_3\W\i00.png'),
    pygame.image.load('sprite\_bot_3\W\i01.png'),
    pygame.image.load('sprite\_bot_3\W\i02.png'),
    pygame.image.load('sprite\_bot_3\W\i03.png'),
    pygame.image.load('sprite\_bot_3\W\i04.png'),
    pygame.image.load('sprite\_bot_3\W\i05.png'),
    pygame.image.load('sprite\_bot_3\W\i06.png'),
    pygame.image.load('sprite\_bot_3\W\i07.png'),
    pygame.image.load('sprite\_bot_3\W\i08.png'),
    pygame.image.load('sprite\_bot_3\W\i09.png'),
    pygame.image.load('sprite\_bot_3\W\i10.png'),
    pygame.image.load('sprite\_bot_3\W\i11.png'),
    pygame.image.load('sprite\_bot_3\W\i12.png'),
    pygame.image.load('sprite\_bot_3\W\i13.png'),
    pygame.image.load('sprite\_bot_3\W\i14.png'),
    pygame.image.load('sprite\_bot_3\W\i15.png'),
    pygame.image.load('sprite\_bot_3\W\i16.png'),
    pygame.image.load('sprite\_bot_3\W\i17.png')
]
w_b_l_3 = []
for i in range(0, 18):
    w_b_3[i] = (pygame.transform.scale(w_b_3[i], (240, 160)))
    w_b_l_3.append(pygame.transform.flip(w_b_3[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_3 = [
    pygame.image.load('sprite\_bot_3\D\i00.png'),
    pygame.image.load('sprite\_bot_3\D\i01.png'),
    pygame.image.load('sprite\_bot_3\D\i02.png'),
    pygame.image.load('sprite\_bot_3\D\i03.png'),
    pygame.image.load('sprite\_bot_3\D\i04.png'),
    pygame.image.load('sprite\_bot_3\D\i05.png'),
    pygame.image.load('sprite\_bot_3\D\i06.png'),
    pygame.image.load('sprite\_bot_3\D\i07.png'),
    pygame.image.load('sprite\_bot_3\D\i08.png'),
    pygame.image.load('sprite\_bot_3\D\i09.png'),
    pygame.image.load('sprite\_bot_3\D\i10.png'),
    pygame.image.load('sprite\_bot_3\D\i11.png'),
    pygame.image.load('sprite\_bot_3\D\i12.png'),
    pygame.image.load('sprite\_bot_3\D\i13.png'),
    pygame.image.load('sprite\_bot_3\D\i14.png')
]
d_b_l_3 = []
for i in range(0, 15):
    d_b_3[i] = (pygame.transform.scale(d_b_3[i], (240, 160)))
    d_b_l_3.append(pygame.transform.flip(d_b_3[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1


# 4 bot
i_b_4 = [
    pygame.image.load('sprite\_bot_4\I\i00.png'),
    pygame.image.load('sprite\_bot_4\I\i01.png'),
    pygame.image.load('sprite\_bot_4\I\i02.png'),
    pygame.image.load('sprite\_bot_4\I\i03.png'),
    pygame.image.load('sprite\_bot_4\I\i04.png'),
    pygame.image.load('sprite\_bot_4\I\i05.png'),
    pygame.image.load('sprite\_bot_4\I\i06.png'),
    pygame.image.load('sprite\_bot_4\I\i07.png'),
    pygame.image.load('sprite\_bot_4\I\i08.png'),
    pygame.image.load('sprite\_bot_4\I\i09.png'),
    pygame.image.load('sprite\_bot_4\I\i10.png'),
    pygame.image.load('sprite\_bot_4\I\i11.png')
]
i_b_l_4 = []
for i in range(0, 12):
    i_b_4[i] = (pygame.transform.scale(i_b_4[i], (240, 160)))
    i_b_l_4.append(pygame.transform.flip(i_b_4[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_4 = [
    pygame.image.load('sprite\_bot_4\A\i00.png'),
    pygame.image.load('sprite\_bot_4\A\i01.png'),
    pygame.image.load('sprite\_bot_4\A\i02.png'),
    pygame.image.load('sprite\_bot_4\A\i03.png'),
    pygame.image.load('sprite\_bot_4\A\i04.png'),
    pygame.image.load('sprite\_bot_4\A\i05.png'),
    pygame.image.load('sprite\_bot_4\A\i06.png'),
    pygame.image.load('sprite\_bot_4\A\i07.png'),
    pygame.image.load('sprite\_bot_4\A\i08.png'),
    pygame.image.load('sprite\_bot_4\A\i09.png'),
    pygame.image.load('sprite\_bot_4\A\i10.png'),
    pygame.image.load('sprite\_bot_4\A\i11.png')
]
a_b_l_4 = []
for i in range(0, 12):
    a_b_4[i] = (pygame.transform.scale(a_b_4[i], (240, 160)))
    a_b_l_4.append(pygame.transform.flip(a_b_4[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_4 = [
    pygame.image.load('sprite\_bot_4\W\i00.png'),
    pygame.image.load('sprite\_bot_4\W\i01.png'),
    pygame.image.load('sprite\_bot_4\W\i02.png'),
    pygame.image.load('sprite\_bot_4\W\i03.png'),
    pygame.image.load('sprite\_bot_4\W\i04.png'),
    pygame.image.load('sprite\_bot_4\W\i05.png'),
    pygame.image.load('sprite\_bot_4\W\i06.png'),
    pygame.image.load('sprite\_bot_4\W\i07.png'),
    pygame.image.load('sprite\_bot_4\W\i08.png'),
    pygame.image.load('sprite\_bot_4\W\i09.png'),
    pygame.image.load('sprite\_bot_4\W\i10.png'),
    pygame.image.load('sprite\_bot_4\W\i11.png'),
    pygame.image.load('sprite\_bot_4\W\i12.png'),
    pygame.image.load('sprite\_bot_4\W\i13.png'),
    pygame.image.load('sprite\_bot_4\W\i14.png'),
    pygame.image.load('sprite\_bot_4\W\i15.png'),
    pygame.image.load('sprite\_bot_4\W\i16.png'),
    pygame.image.load('sprite\_bot_4\W\i17.png')
]
w_b_l_4 = []
for i in range(0, 18):
    w_b_4[i] = (pygame.transform.scale(w_b_4[i], (240, 160)))
    w_b_l_4.append(pygame.transform.flip(w_b_4[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_4 = [
    pygame.image.load('sprite\_bot_4\D\i00.png'),
    pygame.image.load('sprite\_bot_4\D\i01.png'),
    pygame.image.load('sprite\_bot_4\D\i02.png'),
    pygame.image.load('sprite\_bot_4\D\i03.png'),
    pygame.image.load('sprite\_bot_4\D\i04.png'),
    pygame.image.load('sprite\_bot_4\D\i05.png'),
    pygame.image.load('sprite\_bot_4\D\i06.png'),
    pygame.image.load('sprite\_bot_4\D\i07.png'),
    pygame.image.load('sprite\_bot_4\D\i08.png'),
    pygame.image.load('sprite\_bot_4\D\i09.png'),
    pygame.image.load('sprite\_bot_4\D\i10.png'),
    pygame.image.load('sprite\_bot_4\D\i11.png'),
    pygame.image.load('sprite\_bot_4\D\i12.png'),
    pygame.image.load('sprite\_bot_4\D\i13.png'),
    pygame.image.load('sprite\_bot_4\D\i14.png')
]
d_b_l_4 = []
for i in range(0, 15):
    d_b_4[i] = (pygame.transform.scale(d_b_4[i], (240, 160)))
    d_b_l_4.append(pygame.transform.flip(d_b_4[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1


# 5 bot
i_b_5 = [
    pygame.image.load('sprite\_bot_5\I\i00.png'),
    pygame.image.load('sprite\_bot_5\I\i01.png'),
    pygame.image.load('sprite\_bot_5\I\i02.png'),
    pygame.image.load('sprite\_bot_5\I\i03.png'),
    pygame.image.load('sprite\_bot_5\I\i04.png'),
    pygame.image.load('sprite\_bot_5\I\i05.png'),
    pygame.image.load('sprite\_bot_5\I\i06.png'),
    pygame.image.load('sprite\_bot_5\I\i07.png'),
    pygame.image.load('sprite\_bot_5\I\i08.png'),
    pygame.image.load('sprite\_bot_5\I\i09.png'),
    pygame.image.load('sprite\_bot_5\I\i10.png'),
    pygame.image.load('sprite\_bot_5\I\i11.png')
]
i_b_l_5 = []
for i in range(0, 12):
    i_b_5[i] = (pygame.transform.scale(i_b_5[i], (240, 160)))
    i_b_l_5.append(pygame.transform.flip(i_b_5[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_5 = [
    pygame.image.load('sprite\_bot_5\A\i00.png'),
    pygame.image.load('sprite\_bot_5\A\i01.png'),
    pygame.image.load('sprite\_bot_5\A\i02.png'),
    pygame.image.load('sprite\_bot_5\A\i03.png'),
    pygame.image.load('sprite\_bot_5\A\i04.png'),
    pygame.image.load('sprite\_bot_5\A\i05.png'),
    pygame.image.load('sprite\_bot_5\A\i06.png'),
    pygame.image.load('sprite\_bot_5\A\i07.png'),
    pygame.image.load('sprite\_bot_5\A\i08.png'),
    pygame.image.load('sprite\_bot_5\A\i09.png'),
    pygame.image.load('sprite\_bot_5\A\i10.png'),
    pygame.image.load('sprite\_bot_5\A\i11.png')
]
a_b_l_5 = []
for i in range(0, 12):
    a_b_5[i] = (pygame.transform.scale(a_b_5[i], (240, 160)))
    a_b_l_5.append(pygame.transform.flip(a_b_5[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_5 = [
    pygame.image.load('sprite\_bot_5\W\i00.png'),
    pygame.image.load('sprite\_bot_5\W\i01.png'),
    pygame.image.load('sprite\_bot_5\W\i02.png'),
    pygame.image.load('sprite\_bot_5\W\i03.png'),
    pygame.image.load('sprite\_bot_5\W\i04.png'),
    pygame.image.load('sprite\_bot_5\W\i05.png'),
    pygame.image.load('sprite\_bot_5\W\i06.png'),
    pygame.image.load('sprite\_bot_5\W\i07.png'),
    pygame.image.load('sprite\_bot_5\W\i08.png'),
    pygame.image.load('sprite\_bot_5\W\i09.png'),
    pygame.image.load('sprite\_bot_5\W\i10.png'),
    pygame.image.load('sprite\_bot_5\W\i11.png'),
    pygame.image.load('sprite\_bot_5\W\i12.png'),
    pygame.image.load('sprite\_bot_5\W\i13.png'),
    pygame.image.load('sprite\_bot_5\W\i14.png'),
    pygame.image.load('sprite\_bot_5\W\i15.png'),
    pygame.image.load('sprite\_bot_5\W\i16.png'),
    pygame.image.load('sprite\_bot_5\W\i17.png')
]
w_b_l_5 = []
for i in range(0, 18):
    w_b_5[i] = (pygame.transform.scale(w_b_5[i], (240, 160)))
    w_b_l_5.append(pygame.transform.flip(w_b_5[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_5 = [
    pygame.image.load('sprite\_bot_5\D\i00.png'),
    pygame.image.load('sprite\_bot_5\D\i01.png'),
    pygame.image.load('sprite\_bot_5\D\i02.png'),
    pygame.image.load('sprite\_bot_5\D\i03.png'),
    pygame.image.load('sprite\_bot_5\D\i04.png'),
    pygame.image.load('sprite\_bot_5\D\i05.png'),
    pygame.image.load('sprite\_bot_5\D\i06.png'),
    pygame.image.load('sprite\_bot_5\D\i07.png'),
    pygame.image.load('sprite\_bot_5\D\i08.png'),
    pygame.image.load('sprite\_bot_5\D\i09.png'),
    pygame.image.load('sprite\_bot_5\D\i10.png'),
    pygame.image.load('sprite\_bot_5\D\i11.png'),
    pygame.image.load('sprite\_bot_5\D\i12.png'),
    pygame.image.load('sprite\_bot_5\D\i13.png'),
    pygame.image.load('sprite\_bot_5\D\i14.png')
]
d_b_l_5 = []
for i in range(0, 15):
    d_b_5[i] = (pygame.transform.scale(d_b_5[i], (240, 160)))
    d_b_l_5.append(pygame.transform.flip(d_b_5[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1


# 6 bot
i_b_6 = [
    pygame.image.load('sprite\_bot_6\I\i00.png'),
    pygame.image.load('sprite\_bot_6\I\i01.png'),
    pygame.image.load('sprite\_bot_6\I\i02.png'),
    pygame.image.load('sprite\_bot_6\I\i03.png'),
    pygame.image.load('sprite\_bot_6\I\i04.png'),
    pygame.image.load('sprite\_bot_6\I\i05.png'),
    pygame.image.load('sprite\_bot_6\I\i06.png'),
    pygame.image.load('sprite\_bot_6\I\i07.png'),
    pygame.image.load('sprite\_bot_6\I\i08.png'),
    pygame.image.load('sprite\_bot_6\I\i09.png'),
    pygame.image.load('sprite\_bot_6\I\i10.png'),
    pygame.image.load('sprite\_bot_6\I\i11.png')
]
i_b_l_6 = []
for i in range(0, 12):
    i_b_6[i] = (pygame.transform.scale(i_b_6[i], (240, 160)))
    i_b_l_6.append(pygame.transform.flip(i_b_6[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_6 = [
    pygame.image.load('sprite\_bot_6\A\i00.png'),
    pygame.image.load('sprite\_bot_6\A\i01.png'),
    pygame.image.load('sprite\_bot_6\A\i02.png'),
    pygame.image.load('sprite\_bot_6\A\i03.png'),
    pygame.image.load('sprite\_bot_6\A\i04.png'),
    pygame.image.load('sprite\_bot_6\A\i05.png'),
    pygame.image.load('sprite\_bot_6\A\i06.png'),
    pygame.image.load('sprite\_bot_6\A\i07.png'),
    pygame.image.load('sprite\_bot_6\A\i08.png'),
    pygame.image.load('sprite\_bot_6\A\i09.png'),
    pygame.image.load('sprite\_bot_6\A\i10.png'),
    pygame.image.load('sprite\_bot_6\A\i11.png')
]
a_b_l_6 = []
for i in range(0, 12):
    a_b_6[i] = (pygame.transform.scale(a_b_6[i], (240, 160)))
    a_b_l_6.append(pygame.transform.flip(a_b_6[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_6 = [
    pygame.image.load('sprite\_bot_6\W\i00.png'),
    pygame.image.load('sprite\_bot_6\W\i01.png'),
    pygame.image.load('sprite\_bot_6\W\i02.png'),
    pygame.image.load('sprite\_bot_6\W\i03.png'),
    pygame.image.load('sprite\_bot_6\W\i04.png'),
    pygame.image.load('sprite\_bot_6\W\i05.png'),
    pygame.image.load('sprite\_bot_6\W\i06.png'),
    pygame.image.load('sprite\_bot_6\W\i07.png'),
    pygame.image.load('sprite\_bot_6\W\i08.png'),
    pygame.image.load('sprite\_bot_6\W\i09.png'),
    pygame.image.load('sprite\_bot_6\W\i10.png'),
    pygame.image.load('sprite\_bot_6\W\i11.png'),
    pygame.image.load('sprite\_bot_6\W\i12.png'),
    pygame.image.load('sprite\_bot_6\W\i13.png'),
    pygame.image.load('sprite\_bot_6\W\i14.png'),
    pygame.image.load('sprite\_bot_6\W\i15.png'),
    pygame.image.load('sprite\_bot_6\W\i16.png'),
    pygame.image.load('sprite\_bot_6\W\i17.png')
]
w_b_l_6 = []
for i in range(0, 18):
    w_b_6[i] = (pygame.transform.scale(w_b_6[i], (240, 160)))
    w_b_l_6.append(pygame.transform.flip(w_b_6[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_6 = [
    pygame.image.load('sprite\_bot_6\D\i00.png'),
    pygame.image.load('sprite\_bot_6\D\i01.png'),
    pygame.image.load('sprite\_bot_6\D\i02.png'),
    pygame.image.load('sprite\_bot_6\D\i03.png'),
    pygame.image.load('sprite\_bot_6\D\i04.png'),
    pygame.image.load('sprite\_bot_6\D\i05.png'),
    pygame.image.load('sprite\_bot_6\D\i06.png'),
    pygame.image.load('sprite\_bot_6\D\i07.png'),
    pygame.image.load('sprite\_bot_6\D\i08.png'),
    pygame.image.load('sprite\_bot_6\D\i09.png'),
    pygame.image.load('sprite\_bot_6\D\i10.png'),
    pygame.image.load('sprite\_bot_6\D\i11.png'),
    pygame.image.load('sprite\_bot_6\D\i12.png'),
    pygame.image.load('sprite\_bot_6\D\i13.png'),
    pygame.image.load('sprite\_bot_6\D\i14.png')
]
d_b_l_6 = []
for i in range(0, 15):
    d_b_6[i] = (pygame.transform.scale(d_b_6[i], (240, 160)))
    d_b_l_6.append(pygame.transform.flip(d_b_6[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1



# 7 bot
i_b_7 = [
    pygame.image.load('sprite\_bot_7\I\i00.png'),
    pygame.image.load('sprite\_bot_7\I\i01.png'),
    pygame.image.load('sprite\_bot_7\I\i02.png'),
    pygame.image.load('sprite\_bot_7\I\i03.png'),
    pygame.image.load('sprite\_bot_7\I\i04.png'),
    pygame.image.load('sprite\_bot_7\I\i05.png'),
    pygame.image.load('sprite\_bot_7\I\i06.png'),
    pygame.image.load('sprite\_bot_7\I\i07.png'),
    pygame.image.load('sprite\_bot_7\I\i08.png'),
    pygame.image.load('sprite\_bot_7\I\i09.png'),
    pygame.image.load('sprite\_bot_7\I\i10.png'),
    pygame.image.load('sprite\_bot_7\I\i11.png')
]
i_b_l_7 = []
for i in range(0, 12):
    i_b_7[i] = (pygame.transform.scale(i_b_7[i], (193, 156)))
    i_b_l_7.append(pygame.transform.flip(i_b_7[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_7 = [
    pygame.image.load('sprite\_bot_7\A\i00.png'),
    pygame.image.load('sprite\_bot_7\A\i01.png'),
    pygame.image.load('sprite\_bot_7\A\i02.png'),
    pygame.image.load('sprite\_bot_7\A\i03.png'),
    pygame.image.load('sprite\_bot_7\A\i04.png'),
    pygame.image.load('sprite\_bot_7\A\i05.png'),
    pygame.image.load('sprite\_bot_7\A\i06.png'),
    pygame.image.load('sprite\_bot_7\A\i07.png'),
    pygame.image.load('sprite\_bot_7\A\i08.png'),
    pygame.image.load('sprite\_bot_7\A\i09.png'),
    pygame.image.load('sprite\_bot_7\A\i10.png'),
    pygame.image.load('sprite\_bot_7\A\i11.png')
]
a_b_l_7 = []
for i in range(0, 12):
    a_b_7[i] = (pygame.transform.scale(a_b_7[i], (193, 156)))
    a_b_l_7.append(pygame.transform.flip(a_b_7[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_7 = [
    pygame.image.load('sprite\_bot_7\W\i00.png'),
    pygame.image.load('sprite\_bot_7\W\i01.png'),
    pygame.image.load('sprite\_bot_7\W\i02.png'),
    pygame.image.load('sprite\_bot_7\W\i03.png'),
    pygame.image.load('sprite\_bot_7\W\i04.png'),
    pygame.image.load('sprite\_bot_7\W\i05.png'),
    pygame.image.load('sprite\_bot_7\W\i06.png'),
    pygame.image.load('sprite\_bot_7\W\i07.png'),
    pygame.image.load('sprite\_bot_7\W\i08.png'),
    pygame.image.load('sprite\_bot_7\W\i09.png'),
    pygame.image.load('sprite\_bot_7\W\i10.png'),
    pygame.image.load('sprite\_bot_7\W\i11.png'),
    pygame.image.load('sprite\_bot_7\W\i12.png'),
    pygame.image.load('sprite\_bot_7\W\i13.png'),
    pygame.image.load('sprite\_bot_7\W\i14.png'),
    pygame.image.load('sprite\_bot_7\W\i15.png'),
    pygame.image.load('sprite\_bot_7\W\i16.png'),
    pygame.image.load('sprite\_bot_7\W\i17.png')
]
w_b_l_7 = []
for i in range(0, 18):
    w_b_7[i] = (pygame.transform.scale(w_b_7[i], (193, 156)))
    w_b_l_7.append(pygame.transform.flip(w_b_7[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_7 = [
    pygame.image.load('sprite\_bot_7\D\i00.png'),
    pygame.image.load('sprite\_bot_7\D\i01.png'),
    pygame.image.load('sprite\_bot_7\D\i02.png'),
    pygame.image.load('sprite\_bot_7\D\i03.png'),
    pygame.image.load('sprite\_bot_7\D\i04.png'),
    pygame.image.load('sprite\_bot_7\D\i05.png'),
    pygame.image.load('sprite\_bot_7\D\i06.png'),
    pygame.image.load('sprite\_bot_7\D\i07.png'),
    pygame.image.load('sprite\_bot_7\D\i08.png'),
    pygame.image.load('sprite\_bot_7\D\i09.png'),
    pygame.image.load('sprite\_bot_7\D\i10.png'),
    pygame.image.load('sprite\_bot_7\D\i11.png'),
    pygame.image.load('sprite\_bot_7\D\i12.png'),
    pygame.image.load('sprite\_bot_7\D\i13.png'),
    pygame.image.load('sprite\_bot_7\D\i14.png')
]
d_b_l_7 = []
for i in range(0, 15):
    d_b_7[i] = (pygame.transform.scale(d_b_7[i], (193, 156)))
    d_b_l_7.append(pygame.transform.flip(d_b_7[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1

# 8 bot
i_b_8 = [
    pygame.image.load('sprite\_bot_8\I\i00.png'),
    pygame.image.load('sprite\_bot_8\I\i01.png'),
    pygame.image.load('sprite\_bot_8\I\i02.png'),
    pygame.image.load('sprite\_bot_8\I\i03.png'),
    pygame.image.load('sprite\_bot_8\I\i04.png'),
    pygame.image.load('sprite\_bot_8\I\i05.png'),
    pygame.image.load('sprite\_bot_8\I\i06.png'),
    pygame.image.load('sprite\_bot_8\I\i07.png'),
    pygame.image.load('sprite\_bot_8\I\i08.png'),
    pygame.image.load('sprite\_bot_8\I\i09.png'),
    pygame.image.load('sprite\_bot_8\I\i10.png'),
    pygame.image.load('sprite\_bot_8\I\i11.png')
]
i_b_l_8 = []
for i in range(0, 12):
    i_b_8[i] = (pygame.transform.scale(i_b_8[i], (193, 156)))
    i_b_l_8.append(pygame.transform.flip(i_b_8[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_8 = [
    pygame.image.load('sprite\_bot_8\A\i00.png'),
    pygame.image.load('sprite\_bot_8\A\i01.png'),
    pygame.image.load('sprite\_bot_8\A\i02.png'),
    pygame.image.load('sprite\_bot_8\A\i03.png'),
    pygame.image.load('sprite\_bot_8\A\i04.png'),
    pygame.image.load('sprite\_bot_8\A\i05.png'),
    pygame.image.load('sprite\_bot_8\A\i06.png'),
    pygame.image.load('sprite\_bot_8\A\i07.png'),
    pygame.image.load('sprite\_bot_8\A\i08.png'),
    pygame.image.load('sprite\_bot_8\A\i09.png'),
    pygame.image.load('sprite\_bot_8\A\i10.png'),
    pygame.image.load('sprite\_bot_8\A\i11.png')
]
a_b_l_8 = []
for i in range(0, 12):
    a_b_8[i] = (pygame.transform.scale(a_b_8[i], (193, 156)))
    a_b_l_8.append(pygame.transform.flip(a_b_8[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_8 = [
    pygame.image.load('sprite\_bot_8\W\i00.png'),
    pygame.image.load('sprite\_bot_8\W\i01.png'),
    pygame.image.load('sprite\_bot_8\W\i02.png'),
    pygame.image.load('sprite\_bot_8\W\i03.png'),
    pygame.image.load('sprite\_bot_8\W\i04.png'),
    pygame.image.load('sprite\_bot_8\W\i05.png'),
    pygame.image.load('sprite\_bot_8\W\i06.png'),
    pygame.image.load('sprite\_bot_8\W\i07.png'),
    pygame.image.load('sprite\_bot_8\W\i08.png'),
    pygame.image.load('sprite\_bot_8\W\i09.png'),
    pygame.image.load('sprite\_bot_8\W\i10.png'),
    pygame.image.load('sprite\_bot_8\W\i11.png'),
    pygame.image.load('sprite\_bot_8\W\i12.png'),
    pygame.image.load('sprite\_bot_8\W\i13.png'),
    pygame.image.load('sprite\_bot_8\W\i14.png'),
    pygame.image.load('sprite\_bot_8\W\i15.png'),
    pygame.image.load('sprite\_bot_8\W\i16.png'),
    pygame.image.load('sprite\_bot_8\W\i17.png')
]
w_b_l_8 = []
for i in range(0, 18):
    w_b_8[i] = (pygame.transform.scale(w_b_8[i], (193, 156)))
    w_b_l_8.append(pygame.transform.flip(w_b_8[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_8 = [
    pygame.image.load('sprite\_bot_8\D\i00.png'),
    pygame.image.load('sprite\_bot_8\D\i01.png'),
    pygame.image.load('sprite\_bot_8\D\i02.png'),
    pygame.image.load('sprite\_bot_8\D\i03.png'),
    pygame.image.load('sprite\_bot_8\D\i04.png'),
    pygame.image.load('sprite\_bot_8\D\i05.png'),
    pygame.image.load('sprite\_bot_8\D\i06.png'),
    pygame.image.load('sprite\_bot_8\D\i07.png'),
    pygame.image.load('sprite\_bot_8\D\i08.png'),
    pygame.image.load('sprite\_bot_8\D\i09.png'),
    pygame.image.load('sprite\_bot_8\D\i10.png'),
    pygame.image.load('sprite\_bot_8\D\i11.png'),
    pygame.image.load('sprite\_bot_8\D\i12.png'),
    pygame.image.load('sprite\_bot_8\D\i13.png'),
    pygame.image.load('sprite\_bot_8\D\i14.png')
]
d_b_l_8 = []
for i in range(0, 15):
    d_b_8[i] = (pygame.transform.scale(d_b_8[i], (193, 156)))
    d_b_l_8.append(pygame.transform.flip(d_b_8[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1



# 9 bot
i_b_9 = [
    pygame.image.load('sprite\_bot_9\I\i00.png'),
    pygame.image.load('sprite\_bot_9\I\i01.png'),
    pygame.image.load('sprite\_bot_9\I\i02.png'),
    pygame.image.load('sprite\_bot_9\I\i03.png'),
    pygame.image.load('sprite\_bot_9\I\i04.png'),
    pygame.image.load('sprite\_bot_9\I\i05.png'),
    pygame.image.load('sprite\_bot_9\I\i06.png'),
    pygame.image.load('sprite\_bot_9\I\i07.png'),
    pygame.image.load('sprite\_bot_9\I\i08.png'),
    pygame.image.load('sprite\_bot_9\I\i09.png'),
    pygame.image.load('sprite\_bot_9\I\i10.png'),
    pygame.image.load('sprite\_bot_9\I\i11.png')
]
i_b_l_9 = []
for i in range(0, 12):
    i_b_9[i] = (pygame.transform.scale(i_b_9[i], (193, 156)))
    i_b_l_9.append(pygame.transform.flip(i_b_9[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_9 = [
    pygame.image.load('sprite\_bot_9\A\i00.png'),
    pygame.image.load('sprite\_bot_9\A\i01.png'),
    pygame.image.load('sprite\_bot_9\A\i02.png'),
    pygame.image.load('sprite\_bot_9\A\i03.png'),
    pygame.image.load('sprite\_bot_9\A\i04.png'),
    pygame.image.load('sprite\_bot_9\A\i05.png'),
    pygame.image.load('sprite\_bot_9\A\i06.png'),
    pygame.image.load('sprite\_bot_9\A\i07.png'),
    pygame.image.load('sprite\_bot_9\A\i08.png'),
    pygame.image.load('sprite\_bot_9\A\i09.png'),
    pygame.image.load('sprite\_bot_9\A\i10.png'),
    pygame.image.load('sprite\_bot_9\A\i11.png')
]
a_b_l_9 = []
for i in range(0, 12):
    a_b_9[i] = (pygame.transform.scale(a_b_9[i], (193, 156)))
    a_b_l_9.append(pygame.transform.flip(a_b_9[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_9 = [
    pygame.image.load('sprite\_bot_9\W\i00.png'),
    pygame.image.load('sprite\_bot_9\W\i01.png'),
    pygame.image.load('sprite\_bot_9\W\i02.png'),
    pygame.image.load('sprite\_bot_9\W\i03.png'),
    pygame.image.load('sprite\_bot_9\W\i04.png'),
    pygame.image.load('sprite\_bot_9\W\i05.png'),
    pygame.image.load('sprite\_bot_9\W\i06.png'),
    pygame.image.load('sprite\_bot_9\W\i07.png'),
    pygame.image.load('sprite\_bot_9\W\i08.png'),
    pygame.image.load('sprite\_bot_9\W\i09.png'),
    pygame.image.load('sprite\_bot_9\W\i10.png'),
    pygame.image.load('sprite\_bot_9\W\i11.png'),
    pygame.image.load('sprite\_bot_9\W\i12.png'),
    pygame.image.load('sprite\_bot_9\W\i13.png'),
    pygame.image.load('sprite\_bot_9\W\i14.png'),
    pygame.image.load('sprite\_bot_9\W\i15.png'),
    pygame.image.load('sprite\_bot_9\W\i16.png'),
    pygame.image.load('sprite\_bot_9\W\i17.png')
]
w_b_l_9 = []
for i in range(0, 18):
    w_b_9[i] = (pygame.transform.scale(w_b_9[i], (193, 156)))
    w_b_l_9.append(pygame.transform.flip(w_b_9[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_9 = [
    pygame.image.load('sprite\_bot_9\D\i00.png'),
    pygame.image.load('sprite\_bot_9\D\i01.png'),
    pygame.image.load('sprite\_bot_9\D\i02.png'),
    pygame.image.load('sprite\_bot_9\D\i03.png'),
    pygame.image.load('sprite\_bot_9\D\i04.png'),
    pygame.image.load('sprite\_bot_9\D\i05.png'),
    pygame.image.load('sprite\_bot_9\D\i06.png'),
    pygame.image.load('sprite\_bot_9\D\i07.png'),
    pygame.image.load('sprite\_bot_9\D\i08.png'),
    pygame.image.load('sprite\_bot_9\D\i09.png'),
    pygame.image.load('sprite\_bot_9\D\i10.png'),
    pygame.image.load('sprite\_bot_9\D\i11.png'),
    pygame.image.load('sprite\_bot_9\D\i12.png'),
    pygame.image.load('sprite\_bot_9\D\i13.png'),
    pygame.image.load('sprite\_bot_9\D\i14.png')
]
d_b_l_9 = []
for i in range(0, 15):
    d_b_9[i] = (pygame.transform.scale(d_b_9[i], (193, 156)))
    d_b_l_9.append(pygame.transform.flip(d_b_9[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1



# 10 bot
i_b_10 = [
    pygame.image.load('sprite\_bot_10\I\i00.png'),
    pygame.image.load('sprite\_bot_10\I\i01.png'),
    pygame.image.load('sprite\_bot_10\I\i02.png'),
    pygame.image.load('sprite\_bot_10\I\i03.png'),
    pygame.image.load('sprite\_bot_10\I\i04.png'),
    pygame.image.load('sprite\_bot_10\I\i05.png'),
    pygame.image.load('sprite\_bot_10\I\i06.png'),
    pygame.image.load('sprite\_bot_10\I\i07.png'),
    pygame.image.load('sprite\_bot_10\I\i08.png'),
    pygame.image.load('sprite\_bot_10\I\i09.png'),
    pygame.image.load('sprite\_bot_10\I\i10.png'),
    pygame.image.load('sprite\_bot_10\I\i11.png')
]
i_b_l_10 = []
for i in range(0, 12):
    i_b_10[i] = (pygame.transform.scale(i_b_10[i], (193, 156)))
    i_b_l_10.append(pygame.transform.flip(i_b_10[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_10 = [
    pygame.image.load('sprite\_bot_10\A\i00.png'),
    pygame.image.load('sprite\_bot_10\A\i01.png'),
    pygame.image.load('sprite\_bot_10\A\i02.png'),
    pygame.image.load('sprite\_bot_10\A\i03.png'),
    pygame.image.load('sprite\_bot_10\A\i04.png'),
    pygame.image.load('sprite\_bot_10\A\i05.png'),
    pygame.image.load('sprite\_bot_10\A\i06.png'),
    pygame.image.load('sprite\_bot_10\A\i07.png'),
    pygame.image.load('sprite\_bot_10\A\i08.png'),
    pygame.image.load('sprite\_bot_10\A\i09.png'),
    pygame.image.load('sprite\_bot_10\A\i10.png'),
    pygame.image.load('sprite\_bot_10\A\i11.png')
]
a_b_l_10 = []
for i in range(0, 12):
    a_b_10[i] = (pygame.transform.scale(a_b_10[i], (193, 156)))
    a_b_l_10.append(pygame.transform.flip(a_b_10[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_10 = [
    pygame.image.load('sprite\_bot_10\W\i00.png'),
    pygame.image.load('sprite\_bot_10\W\i01.png'),
    pygame.image.load('sprite\_bot_10\W\i02.png'),
    pygame.image.load('sprite\_bot_10\W\i03.png'),
    pygame.image.load('sprite\_bot_10\W\i04.png'),
    pygame.image.load('sprite\_bot_10\W\i05.png'),
    pygame.image.load('sprite\_bot_10\W\i06.png'),
    pygame.image.load('sprite\_bot_10\W\i07.png'),
    pygame.image.load('sprite\_bot_10\W\i08.png'),
    pygame.image.load('sprite\_bot_10\W\i09.png'),
    pygame.image.load('sprite\_bot_10\W\i10.png'),
    pygame.image.load('sprite\_bot_10\W\i11.png')
]
w_b_l_10 = []
for i in range(0, 12):
    w_b_10[i] = (pygame.transform.scale(w_b_10[i], (193, 156)))
    w_b_l_10.append(pygame.transform.flip(w_b_10[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_10 = [
    pygame.image.load('sprite\_bot_10\D\i00.png'),
    pygame.image.load('sprite\_bot_10\D\i01.png'),
    pygame.image.load('sprite\_bot_10\D\i02.png'),
    pygame.image.load('sprite\_bot_10\D\i03.png'),
    pygame.image.load('sprite\_bot_10\D\i04.png'),
    pygame.image.load('sprite\_bot_10\D\i05.png'),
    pygame.image.load('sprite\_bot_10\D\i06.png'),
    pygame.image.load('sprite\_bot_10\D\i07.png'),
    pygame.image.load('sprite\_bot_10\D\i08.png'),
    pygame.image.load('sprite\_bot_10\D\i09.png'),
    pygame.image.load('sprite\_bot_10\D\i10.png'),
    pygame.image.load('sprite\_bot_10\D\i11.png'),
    pygame.image.load('sprite\_bot_10\D\i12.png'),
    pygame.image.load('sprite\_bot_10\D\i13.png'),
    pygame.image.load('sprite\_bot_10\D\i14.png')
]
d_b_l_10 = []
for i in range(0, 15):
    d_b_10[i] = (pygame.transform.scale(d_b_10[i], (193, 156)))
    d_b_l_10.append(pygame.transform.flip(d_b_10[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1


# 11 bot
i_b_11 = [
    pygame.image.load('sprite\_bot_11\I\i00.png'),
    pygame.image.load('sprite\_bot_11\I\i01.png'),
    pygame.image.load('sprite\_bot_11\I\i02.png'),
    pygame.image.load('sprite\_bot_11\I\i03.png'),
    pygame.image.load('sprite\_bot_11\I\i04.png'),
    pygame.image.load('sprite\_bot_11\I\i05.png'),
    pygame.image.load('sprite\_bot_11\I\i06.png'),
    pygame.image.load('sprite\_bot_11\I\i07.png'),
    pygame.image.load('sprite\_bot_11\I\i08.png'),
    pygame.image.load('sprite\_bot_11\I\i09.png'),
    pygame.image.load('sprite\_bot_11\I\i10.png'),
    pygame.image.load('sprite\_bot_11\I\i11.png')
]
i_b_l_11 = []
for i in range(0, 12):
    i_b_11[i] = (pygame.transform.scale(i_b_11[i], (193, 156)))
    i_b_l_11.append(pygame.transform.flip(i_b_11[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_11 = [
    pygame.image.load('sprite\_bot_11\A\i00.png'),
    pygame.image.load('sprite\_bot_11\A\i01.png'),
    pygame.image.load('sprite\_bot_11\A\i02.png'),
    pygame.image.load('sprite\_bot_11\A\i03.png'),
    pygame.image.load('sprite\_bot_11\A\i04.png'),
    pygame.image.load('sprite\_bot_11\A\i05.png'),
    pygame.image.load('sprite\_bot_11\A\i06.png'),
    pygame.image.load('sprite\_bot_11\A\i07.png'),
    pygame.image.load('sprite\_bot_11\A\i08.png'),
    pygame.image.load('sprite\_bot_11\A\i09.png'),
    pygame.image.load('sprite\_bot_11\A\i10.png'),
    pygame.image.load('sprite\_bot_11\A\i11.png')
]
a_b_l_11 = []
for i in range(0, 12):
    a_b_11[i] = (pygame.transform.scale(a_b_11[i], (193, 156)))
    a_b_l_11.append(pygame.transform.flip(a_b_11[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_11 = [
    pygame.image.load('sprite\_bot_11\W\i00.png'),
    pygame.image.load('sprite\_bot_11\W\i01.png'),
    pygame.image.load('sprite\_bot_11\W\i02.png'),
    pygame.image.load('sprite\_bot_11\W\i03.png'),
    pygame.image.load('sprite\_bot_11\W\i04.png'),
    pygame.image.load('sprite\_bot_11\W\i05.png'),
    pygame.image.load('sprite\_bot_11\W\i06.png'),
    pygame.image.load('sprite\_bot_11\W\i07.png'),
    pygame.image.load('sprite\_bot_11\W\i08.png'),
    pygame.image.load('sprite\_bot_11\W\i09.png'),
    pygame.image.load('sprite\_bot_11\W\i10.png'),
    pygame.image.load('sprite\_bot_11\W\i11.png')
]
w_b_l_11 = []
for i in range(0, 12):
    w_b_11[i] = (pygame.transform.scale(w_b_11[i], (193, 156)))
    w_b_l_11.append(pygame.transform.flip(w_b_11[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_11 = [
    pygame.image.load('sprite\_bot_11\D\i00.png'),
    pygame.image.load('sprite\_bot_11\D\i01.png'),
    pygame.image.load('sprite\_bot_11\D\i02.png'),
    pygame.image.load('sprite\_bot_11\D\i03.png'),
    pygame.image.load('sprite\_bot_11\D\i04.png'),
    pygame.image.load('sprite\_bot_11\D\i05.png'),
    pygame.image.load('sprite\_bot_11\D\i06.png'),
    pygame.image.load('sprite\_bot_11\D\i07.png'),
    pygame.image.load('sprite\_bot_11\D\i08.png'),
    pygame.image.load('sprite\_bot_11\D\i09.png'),
    pygame.image.load('sprite\_bot_11\D\i10.png'),
    pygame.image.load('sprite\_bot_11\D\i11.png'),
    pygame.image.load('sprite\_bot_11\D\i12.png'),
    pygame.image.load('sprite\_bot_11\D\i13.png'),
    pygame.image.load('sprite\_bot_11\D\i14.png')
]
d_b_l_11 = []
for i in range(0, 15):
    d_b_11[i] = (pygame.transform.scale(d_b_11[i], (193, 156)))
    d_b_l_11.append(pygame.transform.flip(d_b_11[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1


# 12 bot
i_b_12 = [
    pygame.image.load('sprite\_bot_12\I\i00.png'),
    pygame.image.load('sprite\_bot_12\I\i01.png'),
    pygame.image.load('sprite\_bot_12\I\i02.png'),
    pygame.image.load('sprite\_bot_12\I\i03.png'),
    pygame.image.load('sprite\_bot_12\I\i04.png'),
    pygame.image.load('sprite\_bot_12\I\i05.png'),
    pygame.image.load('sprite\_bot_12\I\i06.png'),
    pygame.image.load('sprite\_bot_12\I\i07.png'),
    pygame.image.load('sprite\_bot_12\I\i08.png'),
    pygame.image.load('sprite\_bot_12\I\i09.png'),
    pygame.image.load('sprite\_bot_12\I\i10.png'),
    pygame.image.load('sprite\_bot_12\I\i11.png')
]
i_b_l_12 = []
for i in range(0, 12):
    i_b_12[i] = (pygame.transform.scale(i_b_12[i], (193, 156)))
    i_b_l_12.append(pygame.transform.flip(i_b_12[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
a_b_12 = [
    pygame.image.load('sprite\_bot_12\A\i00.png'),
    pygame.image.load('sprite\_bot_12\A\i01.png'),
    pygame.image.load('sprite\_bot_12\A\i02.png'),
    pygame.image.load('sprite\_bot_12\A\i03.png'),
    pygame.image.load('sprite\_bot_12\A\i04.png'),
    pygame.image.load('sprite\_bot_12\A\i05.png'),
    pygame.image.load('sprite\_bot_12\A\i06.png'),
    pygame.image.load('sprite\_bot_12\A\i07.png'),
    pygame.image.load('sprite\_bot_12\A\i08.png'),
    pygame.image.load('sprite\_bot_12\A\i09.png'),
    pygame.image.load('sprite\_bot_12\A\i10.png'),
    pygame.image.load('sprite\_bot_12\A\i11.png')
]
a_b_l_12 = []
for i in range(0, 12):
    a_b_12[i] = (pygame.transform.scale(a_b_12[i], (193, 156)))
    a_b_l_12.append(pygame.transform.flip(a_b_12[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
w_b_12 = [
    pygame.image.load('sprite\_bot_12\W\i00.png'),
    pygame.image.load('sprite\_bot_12\W\i01.png'),
    pygame.image.load('sprite\_bot_12\W\i02.png'),
    pygame.image.load('sprite\_bot_12\W\i03.png'),
    pygame.image.load('sprite\_bot_12\W\i04.png'),
    pygame.image.load('sprite\_bot_12\W\i05.png'),
    pygame.image.load('sprite\_bot_12\W\i06.png'),
    pygame.image.load('sprite\_bot_12\W\i07.png'),
    pygame.image.load('sprite\_bot_12\W\i08.png'),
    pygame.image.load('sprite\_bot_12\W\i09.png'),
    pygame.image.load('sprite\_bot_12\W\i10.png'),
    pygame.image.load('sprite\_bot_12\W\i11.png')
]
w_b_l_12 = []
for i in range(0, 12):
    w_b_12[i] = (pygame.transform.scale(w_b_12[i], (193, 156)))
    w_b_l_12.append(pygame.transform.flip(w_b_12[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1
d_b_12 = [
    pygame.image.load('sprite\_bot_12\D\i00.png'),
    pygame.image.load('sprite\_bot_12\D\i01.png'),
    pygame.image.load('sprite\_bot_12\D\i02.png'),
    pygame.image.load('sprite\_bot_12\D\i03.png'),
    pygame.image.load('sprite\_bot_12\D\i04.png'),
    pygame.image.load('sprite\_bot_12\D\i05.png'),
    pygame.image.load('sprite\_bot_12\D\i06.png'),
    pygame.image.load('sprite\_bot_12\D\i07.png'),
    pygame.image.load('sprite\_bot_12\D\i08.png'),
    pygame.image.load('sprite\_bot_12\D\i09.png'),
    pygame.image.load('sprite\_bot_12\D\i10.png'),
    pygame.image.load('sprite\_bot_12\D\i11.png'),
    pygame.image.load('sprite\_bot_12\D\i12.png'),
    pygame.image.load('sprite\_bot_12\D\i13.png'),
    pygame.image.load('sprite\_bot_12\D\i14.png')
]
d_b_l_12 = []
for i in range(0, 15):
    d_b_12[i] = (pygame.transform.scale(d_b_12[i], (193, 156)))
    d_b_l_12.append(pygame.transform.flip(d_b_12[i], True, False))
returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1




idle_bot = [i_b_1, i_b_2, i_b_3, i_b_4, i_b_5, i_b_6, i_b_7, i_b_8, i_b_9, i_b_10, i_b_11, i_b_12]
attack_bot = [a_b_1, a_b_2, a_b_3, a_b_4, a_b_5, a_b_6, a_b_7, a_b_8, a_b_9, a_b_10, a_b_11, a_b_12]
walk_bot = [w_b_1, w_b_2, w_b_3, w_b_4, w_b_5, w_b_6, w_b_7, w_b_8, w_b_9, w_b_10, w_b_11, w_b_12]
dying_bot = [d_b_1, d_b_2, d_b_3, d_b_4, d_b_5, d_b_6, d_b_7, d_b_8, d_b_9, d_b_10, d_b_11, d_b_12]

returned_background_index = loading_(per_cent, returned_background_index)
per_cent += 1

idle_l_bot = [i_b_l_1, i_b_l_2, i_b_l_3, i_b_l_4, i_b_l_5, i_b_l_6, i_b_l_7, i_b_l_8, i_b_l_9, i_b_l_10, i_b_l_11, i_b_l_12]
attack_l_bot = [a_b_l_1, a_b_l_2, a_b_l_3, a_b_l_4, a_b_l_5, a_b_l_6, a_b_l_7, a_b_l_8, a_b_l_9, a_b_l_10, a_b_l_11, a_b_l_12]
walk_l_bot = [w_b_l_1, w_b_l_2, w_b_l_3, w_b_l_4, w_b_l_5, w_b_l_6, w_b_l_7, w_b_l_8, w_b_l_9, w_b_l_10, w_b_l_11, w_b_l_12]
dying_l_bot = [d_b_l_1, d_b_l_2, d_b_l_3, d_b_l_4, d_b_l_5, d_b_l_6, d_b_l_7, d_b_l_8, d_b_l_9, d_b_l_10, d_b_l_11, d_b_l_12]

per_cent += 1
returned_background_index = loading_(per_cent, returned_background_index)


del menu_background
del menu_button
del Canvas
del Button
shadow = pygame.transform.scale(pygame.image.load("sprite\shadow.png"), (91, 12))
