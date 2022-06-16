sheep = input().split(", ")
wolf = sheep.index("wolf")
me = len(sheep) - 1

if wolf != me:
    print(f"Oi! Sheep number {len(sheep) - wolf-1}! You are about to be eaten by a wolf!")
else:
    print("Please go away and stop eating my sheep")
