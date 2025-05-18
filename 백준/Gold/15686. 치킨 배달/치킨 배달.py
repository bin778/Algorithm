from itertools import combinations
import sys
input = sys.stdin.readline

# 거리 계산 함수
def dis_cal(home, selected):
  total_dis = 0
  for hx, hy in home:
    # 각 집에서 가장 가까운 치킨집과의 거리 계산
    min_dis = float('inf')
    for cx, cy in selected:
      min_dis = min(min_dis, abs(hx - cx) + abs(hy - cy))
    total_dis += min_dis
  return total_dis

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []

# 집과 치킨집 위치 저장
for i in range(N):
  for j in range(N):
    if city[i][j] == 1: home.append([i + 1, j + 1])
    if city[i][j] == 2: chicken.append([i + 1, j + 1])

# 치킨집 M개를 선택하는 모든 조합을 탐색(combinations 함수 활용)
result = float('inf')
for selected in combinations(chicken, M):
  # 선택된 치킨집들에 대해 집과의 거리를 계산
  result = min(result, dis_cal(home, selected))

print(result)