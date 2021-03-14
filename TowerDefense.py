from towerDefense.enemyTD import *
from towerDefense.towerTD import *

pygame.init()
screen = pygame.display.set_mode((1200, 900))

bg = pygame.image.load(f"images/Tower_Defense_fon.png")
bg = pygame.transform.scale(bg, (1200, 900))


path = []
f_way = open("level_1_path.txt")
for line in f_way:
    path.append(tuple(map(int, line.split())))

snow_bat = Enemy(snow_bat_imgs, snow_bat_die_imgs, snow_bat_hurt_imgs, path)
skull_troll = Enemy(skull_troll_imgs, skull_troll_die_imgs, skull_troll_hurt_imgs, path)
stone_towers = []
enemies = [snow_bat]
stones = []
places = [[520, 303], [773, 303], [1022, 301], [437, 547], [711, 558], [975, 564], [304, 758]]
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = list(pos)
            print(pos)
            pos[0] -= 30
            pos[1] -= 60
            stone_tower = StoneTower(pos[0], pos[1], tower_imgs)
            stone_towers.append(stone_tower)

    screen.blit(bg, (0, 0))

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

    for j in places:
        pygame.draw.circle(screen, (255, 20, 147), (j[0], j[1]), 10)

    for i, enemy in enumerate(enemies):
        remove_me = enemy.update()
        if remove_me:
            del enemies[i]
        else:
            enemy.draw(screen)
            enemy.move()

    pygame.display.flip()
    pygame.time.delay(10)
