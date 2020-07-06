#Os Munchkins são sempre tão amigáveis...

# O cleave está em uma recarga de 10 segundos.
# Use uma declaração else para se defender durante o tempo de recarga do cleave.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave()
    # Escreva um else, para que seu herói possa fazer algo enquanto o cleave não estiver pronto:
    else:
        # Certifique-se de atacar o inimigo:
        hero.attack(enemy)
        