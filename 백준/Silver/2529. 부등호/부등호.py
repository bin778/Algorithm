import sys
input = sys.stdin.readline

K = int(input())
arr = list(input().split())
visited = [False] * 10 # 숫자 0 ~ 9 체크
result = ["", ""] # 최댓값, 최솟값

def sign(i, j, k):
  if k == '<':
    return i < j
  else:
    return i > j

def dfs(v, num_str):
  if v == K + 1:
    if not result[0]:
      result[1] = num_str
    result[0] = num_str
    return
  
  for i in range(10):
    if not visited[i]:
      if v == 0 or sign(num_str[-1], str(i), arr[v - 1]):
        visited[i] = True
        dfs(v + 1, num_str + str(i))
        visited[i] = False

dfs(0, "")
print(*result, sep="\n")