#Seja sábio. Criado pelo jogador Lai Manh Tuan.

# Se você pisar em uma armadilha de fogo , você vai ser explodido.
hero.moveUp(2);
# Dica 1: Quanto maior o inimigo mais forte ele é .
# Dica 2 ::
# Arrombe a porta usando este comando "this.attack('NomedaPorta')
hero.attack("Door A")
hero.moveUp(2)
enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)
hero.moveDown(3)
hero.moveRight(2)

hero.moveUp()
hero.attack("Door B")
hero.moveUp(2)
enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)
hero.moveDown(2)

hero.moveRight(2)
hero.attack("Door C")
hero.moveUp(2)
enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)
hero.moveDown(2)

hero.moveRight(2)
enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

# Vamos escapar agora (mova para o ''X'' marcado)
hero.moveUp(3)
hero.moveRight()
hero.moveDown(4)
hero.moveLeft(3)
hero.moveDown()
hero.moveLeft(2)
