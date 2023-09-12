from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)

for i in q:
    print(i)

q.popleft()

for i in q:
    print(i)