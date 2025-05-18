def floydWarshall(n, graph):
    dist =[[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    for edge in graph:
        dist[edge[0]][edge[1]] = dist[edge[1]][edge[0]] = edge[2]
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dist[i][j] = 0
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def solution(n, s, a, b, fares):
    dist = floydWarshall(n, fares)
    result = dist[s][a] + dist[s][b]
    
    for i in range(1, n + 1):
        result = min(result, dist[s][i] + dist[i][a] + dist[i][b])
    
    return result