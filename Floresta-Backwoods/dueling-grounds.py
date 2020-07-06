#Batalhe diretamente contra outro herói nesta arena de combates básica para iniciantes.

# Derrote o herói inimigo em um duelo!

while True:
    # Encontre e ataque o inimigo dentro de um laço.
    # Quando tiver terminado, envie para a escada multijogado!
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    
