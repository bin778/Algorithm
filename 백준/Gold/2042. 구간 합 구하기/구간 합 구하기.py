import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
tree = [0] * (N + 1)

def query(idx):
    sum = 0
    while idx > 0:
        sum += tree[idx]
        idx -= (idx & -idx)
    return sum

def update(idx, val):
    while idx <= N:
        tree[idx] += val
        idx += (idx & -idx)

for i in range(1, N + 1):
    update(i, arr[i])

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)
    elif a == 2:
        print(query(c) - query(b - 1))