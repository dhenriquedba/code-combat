#Fique mais forte comendo cogumelos, e então derrote o Guardião da Caverna! Criado pelo jogador Kevin Holland.

hero.moveDown()
hero.moveRight()
hero.moveDown()

# Mamãe sempre disse para comer cogumelos aleatórios que você encontra nas cavernas.
hero.moveDown()
hero.moveRight(2)
hero.moveRight()
hero.moveUp()
hero.moveLeft()
hero.moveUp()
hero.moveRight()
hero.moveLeft()
hero.moveUp()
hero.moveRight()

# Encontre uma maneira de vencer o Guardião da Caverna.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    