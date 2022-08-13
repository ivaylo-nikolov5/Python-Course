from collections import deque

succeed = False
cherry_bombs = 0
datura_bombs = 0
smoke_decoy_bombs = 0
remove = False

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]

while bomb_effects and bomb_casings:
    remove = False
    if cherry_bombs >= 3 and datura_bombs >= 3 and smoke_decoy_bombs >= 3:
        succeed = True
        break

    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]

    bomb = bomb_effect + bomb_casing

    if bomb == 40:
        datura_bombs += 1
        remove = True
    elif bomb == 60:
        cherry_bombs += 1
        remove = True
    elif bomb == 120:
        smoke_decoy_bombs += 1
        remove = True
    else:
        bomb_casings[-1] -= 5

    if remove:
        bomb_effects.popleft()
        bomb_casings.pop()

if succeed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings)}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}\nDatura Bombs: {datura_bombs}\nSmoke Decoy Bombs: {smoke_decoy_bombs}")