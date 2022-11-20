from collections import deque

strings = [x for x in input().split()]

size = [0] * len(strings)
size[0] = 1

parent = [None] * len(strings)
best_idx = 0
best_size = 1

for current in range(1, len(strings)):
    current_word = strings[current]
    current_best_size = 0
    current_parent = None
    for prev in range(current - 1, -1, -1):
        prev_word = strings[prev]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = current

result = deque()

while best_idx is not None:
    result.appendleft(strings[best_idx])
    best_idx = parent[best_idx]


print(*result, sep=" ")
