def nested_loops(n, combinations):
    if len(combinations) == n:
        print(*combinations, sep=" ")
        return

    for idx in range(1, n + 1):
        combinations.append(idx)
        nested_loops(n, combinations)
        combinations.pop()


number = int(input())

nested_loops(number, [])