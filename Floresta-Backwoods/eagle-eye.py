#Localize os ogros com a ajuda de um filhote de Grifo!

# Lembre-se que os inimigos podem aparecer aleatoriamente.

while True:
    enemy = hero.findNearestEnemy()
    # Se existir um inimigo, ataque-o!
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
