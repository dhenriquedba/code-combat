#Recupere o tesouro roubado pelos ogros.

# Se houver um inimigo, ataque-o.
# Caso contrário, ataque "Chest" (baú)!

while True:
    # Use if/else.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    else:
        hero.attack("Chest")
    
    