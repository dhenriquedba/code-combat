#Patrulhe as entradas da aldeia, mas fique na defensiva.

# Fique no meio e defenda!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Ataque o inimigo...
        hero.attack(enemy)
        hero.attack(enemy)
        pass
    else:
        # ... ou retorne à sua posição de defesa.
        hero.moveXY(40, 34)
        pass