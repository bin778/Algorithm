import sys
input = sys.stdin.readline

N = int(input())
dp_min = list(map(int, input().split()))
dp_max = dp_min[:]

for _ in range(1, N):
    x, y, z = map(int, input().split())
    
    # 현재 단계의 최솟값 계산
    sum_min = [x + min(dp_min[0], dp_min[1]), y + min(dp_min[0], dp_min[1], dp_min[2]), z + min(dp_min[1], dp_min[2])]
    
    # 현재 단계의 최댓값 계산
    sum_max = [x + max(dp_max[0], dp_max[1]), y + max(dp_max[0], dp_max[1], dp_max[2]), z + max(dp_max[1], dp_max[2])]
    
    # 현재 단계의 결과를 다음 단계의 이전 결과로 갱신
    dp_min = sum_min
    dp_max = sum_max

print(max(dp_max), min(dp_min))