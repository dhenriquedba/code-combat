#Use todas as suas habilidades para sobreviver.

# Use o que você aprendeu para vencer os ogros.
# Lembre-se: são necessários dois ataques para derrotar um Ogro Munchkin!
while True:
    enemy = hero.findNearestEnemy()
    hero.moveLeft()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
