def string_explosion(string):
    filtered = [x for x in string]
    strength = 0
    explosions = ""
    for x in range(len(filtered)):
        if filtered[x] == ">":
            power = int(filtered[x + 1])
            for y in range(1, power + strength + 1):
                current_index = filtered[x + y]
                if current_index != ">":
                    filtered[x + y] = ""
                else:
                    strength += int(explosions[-1])
                    break
            explosions += str(power)
    print("".join(filtered))


text = input()
string_explosion(text)