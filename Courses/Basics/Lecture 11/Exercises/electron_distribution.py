def electron_distribution(num):
    electrons = []
    for i in range(1, num+1):
        cell = 2 * (i ** 2)
        if num - sum(electrons) > cell:
            electrons.append(cell)
        else:
            electrons.append(num - sum(electrons))
            break

    return electrons


print(electron_distribution(num=int(input())))
