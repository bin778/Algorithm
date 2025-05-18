from collections import deque

N, K = map(int, input().split())
result = []
queue = deque([])
for i in range(0, N):
    queue.append(i + 1)

while len(queue):
    queue.rotate(-K)
    num = queue.pop()
    result.append(num)

print(str(result).replace('[', '<').replace(']', '>'))