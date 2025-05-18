from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, K):
    # 큐 초기화
    queue = deque([(N, 0)])
    visited = set()

    while queue:
        current, steps = queue.popleft()

        # 목표에 도달한 경우 시도 횟수 반환
        if current == K:
            return steps

        # 방문한 위치는 다시 방문하지 않음
        if current in visited:
            continue

        visited.add(current)

        if current * 2 <= 100000:
            queue.appendleft((current * 2, steps))
        if current + 1 <= 100000:
            queue.append((current + 1, steps + 1))
        if current - 1 >= 0:
            queue.append((current - 1, steps + 1))

N, K = map(int, input().split())
print(bfs(N, K))
