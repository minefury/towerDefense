import pygame
import math
from utils import *


def load_and_scale(img, scale):
    imgg = load_img(img)
    imgg = pygame.transform.scale(imgg, (int(imgg.get_width() * scale), int(imgg.get_height() * scale)))
    return imgg


stone_tower_btn = load_and_scale(f"images/buttons/ico_12.png", 0.8)
pause_btn = load_and_scale(f"images/buttons/button6.png", 0.8)
support_tower_btn = load_and_scale(f"images/buttons/ico_23.png", 0.8)
cost_img = load_and_scale(f"images/buttons/button5.png", 0.8)
button_bg = load_and_scale(f"images/buttons/button2.png", 1.1)
heart = load_img(f"images/Buttons/heart.png")
my_font = pygame.font.SysFont("Arial", 32)


class Button:
    def __init__(self, x, y, imgs, cost, cost_img):
        self.x = x
        self.y = y
        self.x1 = x
        self.y1 = y
        self.img = imgs
        self.cost_img = cost_img
        self.cost = cost
        self.cost_text = my_font.render(str(self.cost), True, (219, 200, 153))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        if self.cost > 0:
            screen.blit(self.cost_img, (self.x+60, self.y+100))
            screen.blit(self.cost_text, (self.x+75, self.y+115))

    def on_click(self, x, y):
        ...


class StoneTowerButton(Button):
    def __init__(self, x, y, cost):
        super().__init__(x, y, stone_tower_btn, cost, cost_img)


class PauseButton(Button):
    def __init__(self, x, y, cost):
        super().__init__(x, y, pause_btn, cost, cost_img)


class SupportTowerButton(Button):
    def __init__(self, x, y, cost):
        super().__init__(x, y, support_tower_btn, cost, cost_img)

class ZhizniKolVo:
    def __init__(self):

        pass
    def draw(self, screen, llifes):
        self.life = my_font.render(llifes, True, (180, 0, 0))
        screen.blit(heart, (1150, 20))
        screen.blit(self.life, (1115, 20))



class GameMenu:
    def __init__(self):
        self.buttons = [StoneTowerButton(30, 30, 25), SupportTowerButton(30, 200, 40), PauseButton(30, 670, 0)]

    def draw(self, screen):
        screen.blit(button_bg, (5, 25))
        for button in self.buttons:
            button.draw(screen)
