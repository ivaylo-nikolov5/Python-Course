def cs(energy):
    battle = input()
    wins = 0
    is_failed = False
    while battle != "End of battle":
        battle = int(battle)
        if battle > energy:
            print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
            is_failed = True
            break

        energy -= battle
        wins += 1

        if wins % 3 == 0:
            energy += wins

        battle = input()

    if not is_failed:
        print(f"Won battles: {wins}. Energy left: {energy}")


initial_energy = int(input())
cs(initial_energy)