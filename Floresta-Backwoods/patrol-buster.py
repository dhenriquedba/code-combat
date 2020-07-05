#Derrote a patrulha de ogros com as novas habilidades de seleção.

# Lembre-se que os inimigos podem não existir ainda.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Se existir um inimigo, ataque-o!
        hero.attack(enemy)
        hero.attack(enemy)
        pass
