from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
card = [i for i in range(1, N + 1)]
card_q = deque(card)
result = []

while card_q:
  # 카드를 버린다
  result.append(card_q.popleft())

  # 카드를 아래로 옮긴다
  card_q.rotate(-1)

print(*result)