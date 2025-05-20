import sys, math
input = sys.stdin.readline

def init(A, tree, node, start, end):
  if start == end:
    tree[node] = A[start]
  else:
    init(A, tree, node * 2, start, (start + end) // 2)
    init(A, tree, node * 2 + 1, (start + end) // 2 + 1, end)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def update(a, tree, node, start, end, index, val):
  if index < start or index > end:
    return
  if start == end:
    a[index] = val
    tree[node] = val
    return
  update(a, tree, node * 2, start, (start + end) // 2, index, val)
  update(a, tree, node * 2 + 1, (start + end) // 2 + 1, end, index, val)
  tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query(tree, node, start, end, left, right):
  if left > end or right < start:
    return -1
  if left <= start and end <= right:
    return tree[node]
  lmin = query(tree, node * 2, start, (start + end) // 2, left, right)
  rmin = query(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)
  if lmin == -1:
    return rmin
  elif rmin == -1:
    return lmin
  else:
    return min(lmin, rmin)

N = int(input())
A = list(map(int, input().split()))
H = math.ceil(math.log2(N))
tree_size = 1 << (H + 1)
tree = [0] * tree_size
init(A, tree, 1, 0, N - 1)
M = int(input())

for _ in range(M):
  Q = list(map(int, input().split()))
  if Q[0] == 1:
    idx, val = Q[1], Q[2]
    update(A, tree, 1, 0, N - 1, idx - 1, val)
  else:
    print(A.index(query(tree, 1, 0, N - 1, 0, N - 1)) + 1)