#Para escapar você precisa atravessar o labirinto do velho Kithman.

# Use um loop while-true para mover-se e atacar.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    hero.moveRight()
    hero.moveUp()
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()
    pass

