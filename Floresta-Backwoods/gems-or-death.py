#Use uma declaração if para decidir: você quer as gemas, ou a morte?

# O código da declaração if só será executado quando a condição do if for verdadeira.
# Corrija todas as declarações if para vencer o nível.

# == significa "é igual a".
if 1 + 1 + 1 == 4:  # ∆ Torne isto falso.
    hero.moveXY(5, 15)  # Mova-se para as primeiras minas.

if 2 + 2 == 4:  # ∆ Torne isto verdadeiro.
	hero.moveXY(15, 40)  # Mova-se para a primeira gema.

# != significa "não é igual a".
if 2 + 2 != 5:  # ∆ Torne isto verdadeiro.
	hero.moveXY(25, 15)  # Mova-se para a segunda gema.
	
# < significa "é menor que".
if 2 + 2 < 5:  # ∆ Torne isto verdadeiro.
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

if 2 > 4:  # ∆ Torne isto falso.
	hero.moveXY(40, 55)

if False:  # ∆ Torne isto falso.
	hero.moveXY(50, 10)

if True:  # ∆ Torne isto verdadeiro.
	hero.moveXY(55, 25)
