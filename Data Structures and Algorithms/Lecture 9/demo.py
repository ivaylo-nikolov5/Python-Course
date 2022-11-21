from collections import deque

words = input().split()

size = [0] * len(words)
size[0] = 1
parent = [None] * len(words)
best_idx = 0
best_size = 0

for idx in range(1, len(words)):
    current_word = words[idx]
    current_best_size = 0
    current_parent = None
    for prev in range(idx - 1, -1 , -1):
        prev_word = words[prev]
        if len(prev_word) >= len(current_word):
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[idx] = current_best_size
    parent[idx] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = idx


result = deque()

while best_idx is not None:
    result.appendleft(words[best_idx])
    best_idx = parent[best_idx]

print(*result)