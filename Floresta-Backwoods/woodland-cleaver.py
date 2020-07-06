#Use a sua nova habilidade Cleave (Fender) para afastar os Munchkins.

# Use a sua nova habilidade "cleave" sempre que possível.

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        # Cleave!
        hero.cleave(enemy)
        pass
    else:
        # Ou (se "cleave" não estiver pronto),  use o ataque normal.
        hero.attack(enemy)
        hero.attack(enemy)
        pass
