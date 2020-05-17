#Um esqueleto gigante! Sua espada é cega, mas bem pesada.

# Utilize um loop para atacar o esqueleto.
# Sua espada cega praticamente não causa nenhum dano, mas tem um grande golpe.
while True:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
