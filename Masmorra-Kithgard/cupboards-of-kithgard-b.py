#Quem sabe que horrores se escondem nos armários de Kithgard?

# Talvez tenha algo por perto para te ajudar!
# Primeiro, mova-se para o Cupboard.
hero.moveRight()
hero.moveDown()
hero.moveRight()
hero.moveDown(2)

# Em seguida, ataque o "Cupboard"  dentro de um while-true loop (loop while verdadeiro).
while True:
    hero.attack("Cupboard")
