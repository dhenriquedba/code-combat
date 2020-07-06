#Sobreviva as ondas de inimigos que ficam mais difíceis cada vez que você ganha. Mas se você perder, 
#terá que esperar um dia para fazer novamente. 
#Este é um nível de desafio OPCIONAL! Você não precisar jogar esse nível para continuar a campanha.

# Sobreviva as ondas de ogros.
# Se você ganhar, o nível ficará mais difícil, e te dará mais recompensas.
# Se você perder, deverá esperar um dia para que possa enviar novamente.
# Toda vez que você envia,  o nível irá te criar em um local diferente.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
