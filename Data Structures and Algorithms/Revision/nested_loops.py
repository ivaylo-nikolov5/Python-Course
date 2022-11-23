def nested_loops(number, result):
    if len(result) == number:
        print(*result)
        return

    for idx in range(1, number + 1):
        result.append(idx)
        nested_loops(number, result)
        result.pop()


number = int(input())

nested_loops(number, [])