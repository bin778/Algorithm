import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]

tree1 = [0] * (N + 1)
tree2 = [0] * (N + 1)

def query(tree, idx):
    sum = 0
    while idx > 0:
        sum += tree[idx]
        idx -= (idx & -idx)
    return sum

def update(tree, idx, val):
    while idx <= N:
        tree[idx] += val
        idx += (idx & -idx)

def range_update(b, c, d):
    update(tree1, b, d)
    if c + 1 <= N:
        update(tree1, c + 1, -d)
    
    update(tree2, b, d * (b - 1))
    if c + 1 <= N:
        update(tree2, c + 1, -d * c)

def get_sum(idx):
    return query(tree1, idx) * idx - query(tree2, idx)

for i in range(1, N + 1):
    range_update(i, i, arr[i])

for _ in range(M + K):
    a, *rest = map(int, input().split())
    if a == 1:
        b, c, d = rest
        range_update(b, c, d)
    elif a == 2:
        b, c = rest
        print(get_sum(c) - get_sum(b - 1))
