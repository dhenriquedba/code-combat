#Você está cercado por todos os lados por ogros invasores! Espere o momento certo para atacar, então PEGUE-OS!

# Derrote os ogros de dentro de seu próprio acampamento!
while True:
    enemy = hero.findNearestEnemy()
    # Use uma declaração if para verificar se existe um inimigo:
    if enemy:
        # Ataque se o inimigo existir: 
        hero.attack(enemy)
        hero.attack(enemy)
