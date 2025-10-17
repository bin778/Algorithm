import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
root = [i for i in range(N + 1)]

def find(node):
    if root[node] == node:
        return node
    root[node] = find(root[node])
    return root[node]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        root[a_root] = b_root

for _ in range(M):
    com, a, b = map(int, input().split())
    if com == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")