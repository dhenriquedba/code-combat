#Se houver condição, faça uma emboscada para alguns ogros em Backwoods.

hero.moveXY(24, 42)
enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(27, 60)
enemy = hero.findNearestEnemy()
if enemy:
    # Ataque o inimigo, se existir!
    hero.attack(enemy)
    hero.attack(enemy)
    pass # Pass é um espaço reservado.

hero.moveXY(42, 50)
enemy = hero.findNearestEnemy()
# Use uma declaração if para verificar se existe um inimigo.
if enemy:
    # Ataque o inimigo, se existir!
    hero.attack(enemy)
    hero.attack(enemy)
    
    

hero.moveXY(39, 24)
# Encontre o inimigo mais próximo:
enemy = hero.findNearestEnemy()
# Verifique se o inimigo existe:
if enemy:
    # Ataque o inimigo, se existir!
    hero.attack(enemy)
    hero.attack(enemy)

