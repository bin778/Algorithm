import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    pos_movie = [0] + [M + i for i in range(1, N + 1)]
    tree_size = N + M + 1
    tree = [0] * tree_size
    seq_movie = list(map(int, input().split()))

    def query(idx):
        sum = 0
        while idx > 0:
            sum += tree[idx]
            idx -= (idx & -idx)
        return sum

    def update(idx, val):
        while idx < len(tree):
            tree[idx] += val
            idx += (idx & -idx)

    for i in range(1, N + 1):
        update(pos_movie[i], 1)

    rank = M
    result = []
    for seq in seq_movie:
        result.append(query(pos_movie[seq] - 1))
        update(pos_movie[seq], -1)
        pos_movie[seq] = rank
        update(pos_movie[seq], 1)
        rank -= 1
    
    print(*result)