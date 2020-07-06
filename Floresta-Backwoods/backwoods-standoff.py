#Grite e abra seu caminho para a vitória, como um verdadeiro bárbaro.

# Esses Munchkins estão assustados com o herói!
# Os ogros vem em intervalos regulares e se agrupam para emboscá-lo! Cuidado!
# Sempre que puder, *cleave* para derrotar uma boa quantidade de inimigos.

while True:
    enemy = hero.findNearestEnemy()
    # Use uma declaração if com isReady para verificar o "cleave".
    if hero.isReady("cleave"):
        # Cleave!
        hero.cleave(enemy)
        # Senão (else), se o cleave não estiver pronto:
    else:
        # Ataque o ogro mais próximo!
        hero.attack(enemy)
