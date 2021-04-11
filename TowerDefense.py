from enemyTD import *
from towerTD import *
from utils import *
from Buttons import *

pygame.init()
screen = pygame.display.set_mode((1200, 900))

bg = load_img(f"images/Background/Tower_Defense_fon.png")
bg = pygame.transform.scale(bg, (1200, 900))

waves_enemies = [[snow_bat_imgs, snow_bat_die_imgs, snow_bat_hurt_imgs, 15],
                 [skull_troll_imgs, skull_troll_die_imgs, skull_troll_hurt_imgs, 20],
                 [troll_bat_imgs, troll_bat_die_imgs, troll_bat_hurt_imgs, 30]]
stone_towers = []
enemies = []
stones = []
places = [[520, 303], [773, 303], [1022, 301], [437, 547], [711, 558], [975, 564], [304, 758]]
enemy_gen = EnemyGen(waves_enemies)
menu = GameMenu()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

        # if e.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     pos = list(pos)
        #     #print(pos)
        #     pos[0] -= 30
        #     pos[1] -= 60
        #     stone_tower = StoneTower(pos[0], pos[1], tower_imgs)
        #     stone_towers.append(stone_tower)

    screen.blit(bg, (0, 0))

    menu.draw(screen)

    enemy_gen.update()
    new_enemy = enemy_gen.new_enemy()
    if new_enemy:
        enemies.append(new_enemy)

    for e in reversed(enemies):
        remove_me = e.update()
        if remove_me:
            enemies.remove(e)
        else:
            e.draw(screen)
            e.move()

    for j in places:
        radius = 50
        x, y = j[0] - 20, j[1] - 25
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (0, 255, 0, 100), (radius, radius), radius, 0)
        screen.blit(surface, (x, y))

    for stone_tower in stone_towers:
        stone_tower.draw(screen)
        stone_tower.update()
        if stone_tower.ready:
            for enemy in enemies:
                x, y = enemy.x, enemy.y
                tx, ty = stone_tower.x + stone_tower.w // 2, stone_tower.y + stone_tower.h // 2
                if ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5 <= stone_tower.range:
                    stones.append(Stone(enemy, stone_tower.x + 43, stone_tower.y + 56, stone_img, 1))
                    stone_tower.ready = False
                    break

    for i, stone in enumerate(stones):
        s = stone.update(stone_bang_imgss)
        if s:
            del stones[i]
        else:
            stone.draw(screen)

    pygame.display.flip()
    pygame.time.delay(10)
