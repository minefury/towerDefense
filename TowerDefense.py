from enemyTD import *
from towerTD import *
from utils import *
from Buttons import *
import random
llifes = input("Введите кол-во жизней:" + "\n")
snow=[]
time=pygame.time.get_ticks()
snowY=0
SnowTicks = 0
for i in range(200,round(1200*IMG_ScalingRegulation),5):
    ls=[]
    ls.append(i-random.randint(-2,2))
    ls.append(random.randint(1, 900 * IMG_ScalingRegulation))
    snow.append(ls)
print(snow)
Widths=int(1200*IMG_ScalingRegulation)
Heights=int(900*IMG_ScalingRegulation)
pygame.init()
screen = pygame.display.set_mode((Widths, Heights))

bg = load_img(f"images/Background/Tower_Defense_fon.png")
bg = pygame.transform.scale(bg, (int(1200*IMG_ScalingRegulation), int(900*IMG_ScalingRegulation)))

snow_bat = [snow_bat_imgs, snow_bat_die_imgs, snow_bat_hurt_imgs, 15]
skull_troll=[skull_troll_imgs, skull_troll_die_imgs, skull_troll_hurt_imgs, 20]
troll_bat=[troll_bat_imgs, troll_bat_die_imgs, troll_bat_hurt_imgs, 30]
stone_towers = []
enemies = []
stones = []
places = [[520*IMG_ScalingRegulation, 303*IMG_ScalingRegulation], [773*IMG_ScalingRegulation, 303*IMG_ScalingRegulation],
          [1022*IMG_ScalingRegulation, 301*IMG_ScalingRegulation], [437*IMG_ScalingRegulation, 547*IMG_ScalingRegulation],
          [711*IMG_ScalingRegulation, 558*IMG_ScalingRegulation], [975*IMG_ScalingRegulation, 564*IMG_ScalingRegulation],
          [304*IMG_ScalingRegulation, 758*IMG_ScalingRegulation]]
enemy_gen_snow_bat = EnemyGen(snow_bat,10)
enemy_gen_skull_troll = EnemyGen(skull_troll,12)
enemy_gen_troll_bat = EnemyGen(troll_bat,18)
menu = GameMenu()
lifes = ZhizniKolVo()

tick = 0
while True:


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = list(pos)
            #print(pos)
            pos[0] -= 50
            pos[1] -= 90
            stone_tower = StoneTower(pos[0], pos[1], tower_imgs)
            stone_towers.append(stone_tower)
    screen.blit(bg, (0, 0))
    time = pygame.time.get_ticks()
    menu.draw(screen)
    if time>=10000:
        enemy_gen_troll_bat.update()
        new_enemy_troll_bat = enemy_gen_troll_bat.new_enemy()
        if new_enemy_troll_bat:
            enemies.append(new_enemy_troll_bat)
    if time>=30000:
        enemy_gen_skull_troll.update()
        new_enemy_skull_troll = enemy_gen_skull_troll.new_enemy()
        if new_enemy_skull_troll:
            enemies.append(new_enemy_skull_troll)
    enemy_gen_snow_bat.update()
    new_enemy_snow_bat = enemy_gen_snow_bat.new_enemy()
    if new_enemy_snow_bat:
        enemies.append(new_enemy_snow_bat)
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
                x, y = enemy.x*IMG_ScalingRegulation, enemy.y*IMG_ScalingRegulation
                tx, ty = stone_tower.x*IMG_ScalingRegulation + stone_tower.w // 2*IMG_ScalingRegulation, stone_tower.y*IMG_ScalingRegulation + stone_tower.h // 2*IMG_ScalingRegulation
                if ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5 <= stone_tower.range:
                    stones.append(Stone(enemy, stone_tower.x + 43*IMG_ScalingRegulation, stone_tower.y + 56*IMG_ScalingRegulation, stone_img, 1))
                    stone_tower.ready = False
                    break

    for i, stone in enumerate(stones):
        s = stone.update(stone_bang_imgss)
        if s:
            del stones[i]
        else:
            stone.draw(screen)
    snowY+=1
    if SnowTicks==len(snow):
        SnowTicks=0
    for i in snow:
        pygame.draw.rect(screen, (255,255,255), (i[0], (i[1]+snowY)%Heights, 5, 5))

    lifes.draw(screen, llifes)
    pygame.display.flip()
    pygame.time.delay(10)

