#Explore a floresta Backwoods, mas verifique todos os cantos para garantir sua segurança.
 
# Explore a floresta, mas fique atento.
# Estes cubículos da floresta podem esconder ogros.

hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# A declaração if irá veificar se uma variável possui um ogro.
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(49, 51)
enemy = hero.findNearestEnemy()
if enemy:
    # Ataque o inimigo aqui:
    hero.attack(enemy)
    hero.attack(enemy)
    # O parentese não significa nada. Isso ajuda a fechar uma declaração if.
    pass

hero.moveXY(58, 14)
enemy = hero.findNearestEnemy()
# Use uma declaração if para verificar se um inimigo existe:
if enemy:
    # Se o inimigo existir, ataque-o:
    hero.attack(enemy)
    hero.attack(enemy)
    