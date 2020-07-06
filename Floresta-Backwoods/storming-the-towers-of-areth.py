#Disable a artilharia e sabote os suprimentos ogre atrás da linha inimiga. Criado pelo jogador Kevon Hohhand.

# Fique no meio e defenda!

# The ogres are holed up in their camp
# Break through their defenses with a calculated strike!

hero.moveXY(55, 14)
hero.moveXY(92, 9)

# Construção uma armadilha de fogo no X vermelho.
hero.buildXY("fire-trap", 94, 19)
# Volte para o X de madeira para evitar a explosão.
hero.moveXY(55, 14)
# Espere o peão investigar a armadilha de fogo brilhante.
# Entre no campo e posicione armadilhas de fogo em cada X.
hero.moveXY(92, 9)
hero.moveXY(81, 42)
hero.buildXY("fire-trap", 60, 62)
hero.buildXY("fire-trap", 90, 53)
# Use o método say para dizer as suas tropas para "retreat".
hero.say("retreat")
# Volte ao ponto de encontro no X de de madeira a esquerda.
hero.moveXY(-16, 39)
