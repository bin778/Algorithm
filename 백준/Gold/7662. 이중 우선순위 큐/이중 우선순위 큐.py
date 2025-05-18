import sys, heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  K = int(input())
  max_Q = []
  min_Q = []
  check = [1] * K

  for i in range(K):
    cmd, num = input().split()
    num = int(num)

    if cmd == "I":
      heapq.heappush(min_Q, (num, i))
      heapq.heappush(max_Q, (-num, i))
    elif cmd == "D":
      if num == 1:
        if max_Q:
          check[heapq.heappop(max_Q)[1]] = 0
      elif num == -1:
        if min_Q:
          check[heapq.heappop(min_Q)[1]] = 0

    while min_Q and check[min_Q[0][1]] == 0:
      heapq.heappop(min_Q)
    while max_Q and check[max_Q[0][1]] == 0:
      heapq.heappop(max_Q)

  if not max_Q and not min_Q:
    print("EMPTY")
  else:
    print(-max_Q[0][0], min_Q[0][0])