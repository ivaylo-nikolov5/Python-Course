from collections import deque

firework_effects = deque(int(x) for x in input().split(", ") if int(x) > 0)
explosive_powers = list(int(x) for x in input().split(", ") if int(x) > 0)

crossette_fireworks = 0
willow_fireworks = 0
palm_fireworks = 0
ready = False

while firework_effects and explosive_powers:
    firework_effect = firework_effects.popleft()
    explosive_power = explosive_powers.pop()

    mix = firework_effect + explosive_power

    if mix % 3 == 0 and mix % 5 == 0:
        crossette_fireworks += 1
    elif mix % 5 == 0:
        willow_fireworks += 1
    elif mix % 3 == 0:
        palm_fireworks += 1
    else:
        firework_effects.append(firework_effect - 1)
        explosive_powers.append(explosive_power)

    if crossette_fireworks >= 3 and palm_fireworks >= 3 and willow_fireworks >= 3:
        ready = True
        break

if ready:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effects)}")

if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_powers)}")

print(f"Palm Fireworks: {palm_fireworks}\nWillow Fireworks: {willow_fireworks}\nCrossette Fireworks: {crossette_fireworks}")
