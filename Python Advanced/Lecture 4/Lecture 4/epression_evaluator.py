from collections import deque

expression = deque(input().split())

result = deque()

while expression:
    element = expression.popleft()
    if element in "+-*/":
        while len(result) > 1:
            if element == "+":
                result.appendleft(result.popleft() + result.popleft())
            elif element == "-":
                result.appendleft(result.popleft() - result.popleft())
            elif element == "*":
                result.appendleft(result.popleft() * result.popleft())
            else:
                result.appendleft(result.popleft() // result.popleft())

    else:
        result.append(int(element))

print(result.popleft())


