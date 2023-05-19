def generate_vectors(number, idx, result):
    if len(result) == number:
        print(*result, sep="")
        return

    for idx in range(2):
        result.append(idx)
        generate_vectors(number, idx, result)
        result.pop()


number = int(input())

generate_vectors(number, 0, [])