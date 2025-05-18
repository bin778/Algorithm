from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
  N, M = map(int, input().split())
  impo_deque = deque(map(int, input().split()))
  idx_deque = deque(range(0, N))

  result = 0

  while True:
    if (impo_deque[0] == max(impo_deque)):
      result += 1
      impo_deque.popleft()
      idx = idx_deque.popleft()
      if (M == idx):
        print(result)
        break
    else:
      impo_deque.rotate(-1)
      idx_deque.rotate(-1)