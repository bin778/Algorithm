import sys
input = sys.stdin.readline

N = int(input())
result = 0
rows = [0] * N
diag1 = [0] * (2 * N - 1)
diag2 = [0] * (2 * N - 1)

def dfs(col):
    global result
    if col == N:
        result += 1
        return
    
    for row in range(N):
        if not rows[row] and not diag1[row - col + N - 1] and not diag2[row + col]:
            rows[row] = diag1[row - col + N - 1] = diag2[row + col] = 1
            dfs(col + 1)
            rows[row] = diag1[row - col + N - 1] = diag2[row + col] = 0

dfs(0)
print(result)