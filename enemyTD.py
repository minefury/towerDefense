import pygame
import math
from utils import *

snow_bat_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/SnowBat/2_enemies_1_WALK_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (150, 150))
    img = pygame.transform.flip(img, True, False)
    snow_bat_imgs.append(img)

snow_bat_die_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/SnowBat/2_enemies_1_DIE_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (150, 150))
    img = pygame.transform.flip(img, True, False)
    snow_bat_die_imgs.append(img)

snow_bat_hurt_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/SnowBat/2_enemies_1_HURT_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (150, 150))
    img = pygame.transform.flip(img, True, False)
    snow_bat_hurt_imgs.append(img)

skull_troll_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/SkullTroll/2_enemies_1_WALK_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (150, 150))
    img = pygame.transform.flip(img, True, False)
    skull_troll_imgs.append(img)

skull_troll_die_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/SkullTroll/2_enemies_1_DIE_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (150, 150))
    img = pygame.transform.flip(img, True, False)
    skull_troll_die_imgs.append(img)

skull_troll_hurt_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/SkullTroll/2_enemies_1_HURT_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (150, 150))
    img = pygame.transform.flip(img, True, False)
    skull_troll_hurt_imgs.append(img)

troll_bat_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/TrollBat/2_enemies_1_WALK_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (200, 200))
    img = pygame.transform.flip(img, True, False)
    troll_bat_imgs.append(img)

troll_bat_hurt_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/TrollBat/2_enemies_1_HURT_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (200, 200))
    img = pygame.transform.flip(img, True, False)
    troll_bat_hurt_imgs.append(img)

troll_bat_die_imgs = []
for i in range(10):
    img = load_img(f"images/enemies/TrollBat/2_enemies_1_DIE_0{i if i > 9 else '0' + str(i)}.png")
    img = pygame.transform.scale(img, (200, 200))
    img = pygame.transform.flip(img, True, False)
    troll_bat_die_imgs.append(img)


path = []
f_way = open_file("images/level_1_path.txt")
for line in f_way:
    path.append(tuple(map(int, line.split())))


class Enemy:
    def __init__(self, imgs_walk, imgs_die, imgs_hurt, path, hp):
        self.x = path[0][0]
        self.y = path[0][1]
        self.width = imgs_walk[0].get_width()
        self.height = imgs_walk[0].get_height()
        self.imgs_walk = imgs_walk
        self.imgs_die = imgs_die
        self.imgs_hurt = imgs_hurt
        self.imgs = self.imgs_walk
        self.cadr = 0
        self.path = path
        self.pos = 0
        self.max_hp = hp
        self.hp = self.max_hp
        self.cnt = 0
        self.was_hurt = False
        self.was_dead = False
        self.cadr_dead = 0
        self.cadr_hurt = 0

    def hit(self):
        self.hp -= 5
        if self.hp <= 0:
            self.imgs = self.imgs_die
            if not self.was_dead:
                self.cadr = 0
                self.was_dead = True
        else:
            self.imgs = self.imgs_hurt
            if not self.was_hurt:
                self.cadr = 0
                self.was_hurt = True

    def next_pos(self):
        pos = self.pos
        x, y = self.x, self.y
        for i in range(1, 30):
            x1, y1 = self.path[pos]
            if pos + 1 >= len(self.path):
                return x, y
            else:
                x2, y2 = self.path[pos + 1]

            dir_x, dir_y = x2 - x1, y2 - y1
            len_dir = math.sqrt(dir_x * dir_x + dir_y * dir_y)
            dir_x /= len_dir
            dir_y /= len_dir

            x += dir_x * 6
            y += dir_y * 6

            if dir_x <= 0 <= dir_y:
                if x <= x2 and y >= y2:
                    pos += 1

            if dir_x >= 0 >= dir_y:
                if x >= x2 and y <= y2:
                    pos += 1

            if dir_x >= 0 and dir_y >= 0:
                if x >= x2 and y >= y2:
                    pos += 1

            if dir_x <= 0 and dir_y <= 0:
                if x <= x2 and y <= y2:
                    pos += 1
        return x, y

    def draw_hp(self, screen):
        green = (0, 255, 0)
        green_width = self.hp * self.width // 2 // self.max_hp
        if green_width != 0:
            pygame.draw.rect(screen, green, (self.x, self.y, green_width, 10))
        red = (255, 0, 0)
        red_width = self.width // 2 - green_width
        if red_width != 0:
            pygame.draw.rect(screen, red, (self.x + green_width, self.y, red_width, 10))

    def draw(self, screen):
        (dx, dy) = (self.x - (self.width // 2), self.y - (self.height // 2))
        screen.blit(self.imgs[self.cadr], (dx, dy))
        self.draw_hp(screen)

    def move(self):
        x1, y1 = self.path[self.pos]
        if self.pos + 1 >= len(self.path):
            return False
        else:
            x2, y2 = self.path[self.pos + 1]

        dir_x, dir_y = x2 - x1, y2 - y1
        len_dir = math.sqrt(dir_x * dir_x + dir_y * dir_y)
        dir_x /= len_dir
        dir_y /= len_dir

        self.x += dir_x * 2
        self.y += dir_y * 2

        if dir_x <= 0 <= dir_y:
            if self.x <= x2 and self.y >= y2:
                self.pos += 1

        if dir_x >= 0 >= dir_y:
            if self.x >= x2 and self.y <= y2:
                self.pos += 1

        if dir_x >= 0 and dir_y >= 0:
            if self.x >= x2 and self.y >= y2:
                self.pos += 1

        if dir_x <= 0 and dir_y <= 0:
            if self.x <= x2 and self.y <= y2:
                self.pos += 1

        return True

    def update(self):
        incr = 1
        if self.was_dead:
            self.cadr_dead = (self.cadr_dead + 1) % 3
            if self.cadr_dead < 2:
                incr = 0

        if self.was_hurt:
            self.cadr_hurt = (self.cadr_hurt + 1) % 3
            if self.cadr_hurt < 2:
                incr = 0

        self.cadr = (self.cadr + incr) % len(self.imgs)

        if self.was_dead and self.cadr + 1 >= len(self.imgs_die):
            return True

        if self.was_hurt and self.cadr + 1 >= len(self.imgs_hurt):
            self.imgs = self.imgs_walk
            self.was_hurt = False

        if self.pos + 1 >= len(self.path):
            return True
        return False


class EnemyGen:
    def __init__(self, wave_enemies):
        self.tic = 0
        self.count = 0
        self.wave = 0
        self.wave_tic = [10, 520, 1020]
        self.wave_enemies = wave_enemies

    def new_enemy(self):
        if self.count < 5 and self.tic % 50 == 0:
            self.count += 1
            return Enemy(self.wave_enemies[self.wave][0],
                         self.wave_enemies[self.wave][1],
                         self.wave_enemies[self.wave][2], path, self.wave_enemies[self.wave][3])

        return None

    def update(self):
        self.tic += 1
        if self.tic == self.wave_tic[0]:
            self.count = 0
            self.wave = 0
        elif self.tic == self.wave_tic[1]:
            self.count = 0
            self.wave = 1
        elif self.tic == self.wave_tic[2]:
            self.count = 0
            self.wave = 2

