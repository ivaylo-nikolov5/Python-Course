def print_func(l_materials: dict, j_items: dict):
    for x in l_materials:
        print(f"{x}: {l_materials[x]}")

    if len(j_items) > 0:
        for x in j_items:
            print(f"{x}: {j_items[x]}")


def legendary_farming():
    command = input().lower().split(" ")
    is_break = False
    legendary_materials = {"shards": 0, "fragments": 0, "motes": 0}
    junk_items = {}

    while True:
        for i in range(1, len(command)+1, 2):
            material = command[i]
            quantity = int(command[i - 1])
            if material in legendary_materials:
                legendary_materials[material] += quantity
                for j in legendary_materials:
                    if j == "shards" and legendary_materials[j] >= 250:
                        print("Shadowmourne obtained!")
                        legendary_materials[j] -= 250
                        is_break = True
                        break
                    elif j == "fragments" and legendary_materials[j] >= 250:
                        print("Valanyr obtained!")
                        legendary_materials[j] -= 250
                        is_break = True
                        break
                    elif j == "motes" and legendary_materials[j] >= 250:
                        print("Dragonwrath obtained!")
                        legendary_materials[j] -= 250
                        is_break = True
                        break
            else:
                if material not in junk_items:
                    junk_items[material] = quantity
                else:
                    junk_items[material] += quantity

            if is_break:
                break

        if is_break:
            break

        command = input().lower().split(" ")

    print_func(legendary_materials, junk_items)


legendary_farming()
