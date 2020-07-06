#Combine cleave e escudada para aguentar a investida ogre.

# Soreviva as duas hordas com `shield` e `cleave`.
# Quando "fender" não estiver pronto, use sua habilidade de escudo.
# Você vai precisar de pelo menos 142 de vida para sobreviver.
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.shield()
