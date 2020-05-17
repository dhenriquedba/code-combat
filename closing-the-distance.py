#Alguns inimigos vão precisar de técnicas de batalha diferentes.

hero.moveRight()

# Como foi visto no nível anterior:
enemy1 = hero.findNearestEnemy()
# Agora ataque o enemy1.
hero.attack(enemy1)
hero.attack(enemy1)

hero.moveRight(2)

enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.attack(enemy2)

hero.moveDown()
hero.moveRight()
