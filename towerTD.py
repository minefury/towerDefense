import pygame
from utils import *


def load_and_scale(img, scale):
    imgg = load_img(img)
    imgg = pygame.transform.scale(imgg, (int(imgg.get_width() * scale), int(imgg.get_height() * scale)))
    return imgg


tower_imgs = [[], [], []]
for i in 1, 3, 2:
    img = load_and_scale(f"images/Towers/Stone_Tower/{str(i)}.png", 0.8)
    tower_imgs[0].append(img)
for i in 1, 6, 2:
    img = load_and_scale(f"images/Towers/Stone_Tower/{str(i)}.png", 0.8)
    tower_imgs[1].append(img)

for i in 4, 7, 5:
    img = load_and_scale(f"images/Towers/Stone_Tower/{str(i)}.png", 0.8)
    tower_imgs[2].append(img)

stone_img = load_and_scale(f"images/Towers/Stone_Tower/40.png", 0.8)
bang1_img = load_and_scale(f"images/Towers/Stone_Tower/41.png", 0.8)
bang2_img = load_and_scale(f"images/Towers/Stone_Tower/42.png", 0.8)
bang3_img = load_and_scale(f"images/Towers/Stone_Tower/42.png", 0.8)
bang4_img = load_and_scale(f"images/Towers/Stone_Tower/43.png", 0.8)
stone_bang_imgss = [bang1_img, bang2_img, bang3_img, bang4_img]


class Tower:
    def __init__(self, x, y, imgs):
        self.x = x
        self.y = y
        self.x1 = x
        self.y1 = y
        self.img = imgs

    def draw(self, screen):
        ...

    def update(self):
        ...


class StoneTower(Tower):
    def __init__(self, x, y, imgs):
        super().__init__(x, y, imgs)
        self.img = imgs
        self.level = 0
        self.ready = True
        self.q = False
        self.range = 175
        self.w, self.h = self.img[self.level][1].get_size()

    def draw(self, screen):
        screen.blit(self.img[self.level][0], (self.x1, self.y1 + 56*IMG_ScalingRegulation))
        screen.blit(self.img[self.level][1], (self.x, self.y))
        screen.blit(self.img[self.level][2], (self.x1, self.y1 + 56*IMG_ScalingRegulation + self.img[self.level][0].get_height() - 2))

    def update(self):
        if not self.ready:
            if self.q:
                self.y1 += 2
            else:
                self.y1 -= 2
            if self.y1 >= self.y:
                self.q = False
                self.ready = True
            if self.y1 <= self.y - 56*IMG_ScalingRegulation:
                self.q = True


class Stone:
    def __init__(self, target_enemy, x, y, imggg, state):
        goal_x, goal_y = target_enemy.next_pos()
        self.enemy = target_enemy
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.x = x
        self.y = y
        self.img = imggg
        self.state = state
        self.start_y = y
        self.cnt = 0
        self.c = 40
        self.a = 0.2
        self.vx, self.vy = (goal_x - x) / self.c, (goal_y - (y - 56*IMG_ScalingRegulation) - self.a * self.c ** 2 / 2) / self.c
        self.t = 0

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.circle(screen, (255, 0, 0), (int(self.goal_x), int(self.goal_y)), 5)

    def update(self, imgs):
        if self.state == 1:
            self.y -= 2
            if self.start_y - 50*IMG_ScalingRegulation >= self.y:
                self.state = 2
        elif self.state == 2:
            self.t += 1
            self.x += self.vx
            self.y += self.vy
            self.vy += self.a

            if self.t >= self.c:
                self.state = 3

        elif self.state == 3:
            self.img = imgs[self.cnt // 3]
            self.cnt += 1
            self.y -= 2
            self.x -= 1
            if self.cnt >= len(imgs)*3:
                self.state = 4
                self.enemy.hit()
                return True

        return False

