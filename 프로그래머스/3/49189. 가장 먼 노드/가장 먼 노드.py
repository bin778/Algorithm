import heapq
INF = float('inf')

def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if visited[node]:
            continue
            
        visited[node] = True
    
        for next_node in graph[node]:
            if visited[next_node]:
                continue
    
            new_distance = dist + 1
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
    
    return distance
        
def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    
    for u, v in vertex:
        graph[u].append(v)
        graph[v].append(u)
    
    distance = dijkstra(1, n, graph)  
    max_distance = max(distance[1:])
    return distance.count(max_distance)