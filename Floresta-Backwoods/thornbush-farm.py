#Proteja os camponeses das mãos dos ogros, enquanto defende a fazenda.

# Patrulhe as entradas da fazenda.
# Construa uma "fire-trap (armadilha de fogo)" quando você vir um Ogro.
# Não exploda nenhum dos camponeses!

while True:
    hero.moveXY(43, 50)
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 43, 50)

    hero.moveXY(25, 34)
    left = hero.findNearestEnemy()
    # Verifique se existe um inimigo na entrada da esquerda (left).
    if left:
        # Construa uma armadilha se o inimigo existir.
        hero.buildXY("fire-trap", 25, 34)
        
    
    hero.moveXY(43, 20)
    # Defina uma variável para o inimigo da entrada de baixo.
    down = hero.findNearestEnemy()
    # Verifique se existe um inimigo na entrada de baixo (bottom).
    if down:
        # Construa uma armadilha se existir um inimigo.
        hero.buildXY("fire-trap", 43, 20)
