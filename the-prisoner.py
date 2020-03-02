#Liberte o prisioneiro e você ganhará um aliado.

# Free the prisoner, defeat the guard and grab the gem.

# Liberte Patrick que está atrás da "Weak Door".
hero.moveRight()
hero.attack("Weak Door")
# Mate o guarda, chamado "Two".
hero.moveRight(2)
hero.attack("Two")
hero.attack("Two")
# Pegue o diamante.
hero.moveDown(3)
hero.moveRight()
