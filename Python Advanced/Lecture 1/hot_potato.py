from collections import deque

kids = deque(input().split())
toss = int(input())

while len(kids) > 1:
    kids.rotate(-toss)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.popleft()}")