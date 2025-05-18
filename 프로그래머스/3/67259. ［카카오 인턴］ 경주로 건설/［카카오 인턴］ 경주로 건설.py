import heapq

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(board):
    n = len(board)
    INF = float('inf')
    
    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
    heap = []
    
    for i in range(4):
        cost[0][0][i] = 0
    
    for i in range(4):
        dx, dy = directions[i]
        nx, ny = dx, dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            cost[nx][ny][i] = 100
            heapq.heappush(heap, (100, nx, ny, i))  
    
    while heap:
        cur_cost, x, y, direction = heapq.heappop(heap)
        
        if x == n - 1 and y == n - 1:
            return min(cost[x][y])
        
        for new_dir in range(4):
            dx, dy = directions[new_dir]
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if direction == new_dir:
                    new_cost = cur_cost + 100
                else:
                    new_cost = cur_cost + 600
                
                if new_cost < cost[nx][ny][new_dir]:
                    cost[nx][ny][new_dir] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny, new_dir))
    
    return INF