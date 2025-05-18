def floydWarshall(n, results):
    dist = [[float('INF')] * n for i in range(n)]

    for i in range(n):
        dist[i][i] = 0
    
    for u, v in results:
        dist[u - 1][v - 1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
    
def solution(n, results):
    result = 0
    dist = floydWarshall(n, results)
    
    for i in range(n):
        win_count = sum(1 for j in range(n) if dist[i][j] != float('INF'))
        lose_count = sum(1 for j in range(n) if dist[j][i] != float('INF'))
        
        if win_count + lose_count == n + 1:
            result += 1
    
    return result