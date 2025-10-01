import sys
sys.setrecursionlimit(10**7)
from collections import deque
input = sys.stdin.readline

N, R = map(int, input().split())
tree_vertex = [list(map(int, input().split())) for _ in range(N - 1)]
L = int(input())
node_leef = {x: y for x, y in [list(map(int, input().split())) for _ in range(L)]}
Q = int(input())
node_num = [int(input()) for _ in range(Q)]

tree = [[] for _ in range(N + 1)]
for u, v in tree_vertex:
    tree[u].append(v)
    tree[v].append(u)

parent_map = {R: 0}
depth_map = {R: 1}
order = []
queue = deque([R])
visited = {R}

while queue:
    curr = queue.popleft()
    order.append(curr)
    for neighbor in tree[curr]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent_map[neighbor] = curr
            depth_map[neighbor] = depth_map[curr] + 1
            queue.append(neighbor)

dp = [0] * (N + 1)

for node in reversed(order):
    if node in node_leef:
        dp[node] = node_leef[node]
    else:
        children = [child for child in tree[node] if parent_map.get(child) == node]
        
        if not children:
            dp[node] = 0
            continue
            
        current_depth = depth_map[node]
        if current_depth % 2 == 1:
            best_value = -float('inf')
            for child in children:
                best_value = max(best_value, dp[child])
            dp[node] = best_value
        else:
            best_value = float('inf')
            for child in children:
                best_value = min(best_value, dp[child])
            dp[node] = best_value

for start_node in node_num:
    print(dp[start_node])
