#Quem sabe que horrores espreitam nos Armários de Kithgard?

# Talvez tenha algo por perto para te ajudar!
# Primeiro, mova-se para o Cupboard (Armário).
hero.moveDown()
hero.moveLeft(2)
hero.moveUp(2)

# Em seguida, ataque o "Cupboard"  dentro de um loop while-true.
while True:
    hero.attack("Cupboard")