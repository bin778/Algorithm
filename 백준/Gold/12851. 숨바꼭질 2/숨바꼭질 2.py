from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, K):
  # 큐 초기화
  queue = deque([(N, 0)])
  visited = [-1] * 100001
  cnt = 0
  min_time = float('inf')

  while queue:
    current, steps = queue.popleft()

    # 목표에 도달한 경우 시도 횟수 반환한다
    if current == K:
      if steps < min_time:
        min_time = steps
        cnt = 1
      elif steps == min_time:
        cnt += 1
    
    # 이미 더 짧은 시간에 방문했으면 건너뛴다
    if steps > min_time:
      continue

    # 가능한 다음 상태로 이동
    for next in (current + 1, current - 1, current * 2):
      if 0 <= next <= 100000:
        # 아직 방문하지 않았거나 더 빠른 시간에 방문 가능한 경우
        if visited[next] == -1 or visited[next] >= steps + 1:
          visited[next] = steps + 1
          queue.append((next, steps + 1))
  return min_time, cnt

N, K = map(int, input().split())
result = bfs(N, K)
print(*result, sep="\n")