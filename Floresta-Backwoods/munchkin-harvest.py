#Junte forças com um novo herói: Amara Arrowhead.

# Use 'cleave' nos munchkins para sobreviver!
# Tenha certeza de possuir armadura suficiente.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
        
