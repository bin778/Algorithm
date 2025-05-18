import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 요소를 하나 제거할 때의 배열과 요소를 제거하지 않는 배열 2개를 만듬
dp = [0] * (N)
dp_remove = [0] * (N)

dp[0] = arr[0]
dp_remove[0] = float('-inf') # 첫 번째 요소에서 제거할 수 없으므로 매우 작은 값으로 초기화
result = arr[0]

for i in range(1, N):
  # 요소를 제거하지 않은 경우의 최대 연속합 계산
  dp[i] = max(dp[i - 1] + arr[i], arr[i])

  # 요소를 하나 제거한 경우의 최대 연속합 계산
  dp_remove[i] = max(dp[i - 1], dp_remove[i - 1] + arr[i])

  # 최댓값 갱신
  result = max(result, dp[i], dp_remove[i])

print(result)