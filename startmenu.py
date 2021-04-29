import pygame
# ЭТО ФАЙЛ С МЕНЮ КОТОРОЕ НЕ РАБОТАЕТ
from utils import *
from utils import *
pygame.init()

def load_and_scale(img, scale):
    imgg = load_img(img)
    imgg = pygame.transform.scale(imgg, (int(imgg.get_width() * scale), int(imgg.get_height() * scale)))
    return imgg

my_font = pygame.font.Font(f"resources/Dimbo Regular.ttf", 48)

class Button:
    def __init__(self, x, y, imgs):
        self.x = x
        self.y = y
        self.x1 = x
        self.y1 = y
        self.img = imgs

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def on_click(self, pos, bw, bh):
        # print(pos)
        pass




screen = pygame.display.set_mode((1200, 900))

bg = load_img(f"images/Background/Fon1200x900.png")
bg = pygame.transform.scale(bg, (1200, 900))

text_TD = my_font.render("TOWER DEFENSE", False, (105, 105, 105))
button = load_and_scale(f"images/Buttons/button4.png", 0.8)
buttonvihod = load_and_scale(f"images/buttons/vihod0.1.png", 1)
l = 0
# print(pygame.font.get_fonts()) # - получение шрифтов

class StartButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, button)

    def on_click(self, pos, bw, bh):
        # print(pos)
        if pos[0] >= self.x and pos[0] <= self.x + bw and pos[1] >= self.y and pos[1] <= self.y + bh:
            import TowerDefense
            quit()
class VihodButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, buttonvihod)

    def on_click(self, pos, bw, bh):
        if self.x <= pos[0] <= self.x + bw and self.y <= pos[1] <= self.y + bh:
            print("Quit")
            quit()


bw = button.get_width()
bh = button.get_height()
vihodw = buttonvihod.get_width()
vihodh = buttonvihod.get_height()
class StartMenu:
    def __init__(self):
        self.buttonsstart = StartButton(450, 400)
        self.buttonsvihod = VihodButton(1000, 700)
    def draw(self, screen):
        self.buttonsstart.draw(screen)
        self.buttonsvihod.draw(screen)
    def on_click(self, pos):
        self.buttonsstart.on_click(pos, bw, bh)
        self.buttonsvihod.on_click(pos, vihodw, vihodh)


menus = StartMenu()

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = list(pos)
            menus.on_click(pos)

    screen.blit(bg, (0, 0))
    # pygame.draw.rect(screen, (240, 255, 255), (410, 80, 500, 120))
    # pygame.draw.rect(screen, (152, 251, 152), (410, 80, 500, 120), 5)
    pygame.draw.rect(screen, (127, 255, 212), (0, 0, 1200, 900), 15)
    # screen.blit(text_TD, (515, 120))
    # screen.blit(button, (450, 400))
    menus.draw(screen)
    pygame.display.flip()
    pygame.time.delay(10)