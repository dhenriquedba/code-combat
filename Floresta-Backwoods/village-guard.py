#Defenda a aldeia do saque dos Munchkins.

# Patrulhe as entradas da aldeia.
# Se houver um inimigo, ataque-o.
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    # Agora mova-se para a entrada da direita.
    hero.moveXY(60, 31)
    rightEnemy = hero.findNearestEnemy()
    # Encontre o inimigo do lado direito.
    if rightEnemy:
        # Use "if" para atacar, se houver um inimigo à direita.
        hero.attack(rightEnemy)
        hero.attack(rightEnemy)
