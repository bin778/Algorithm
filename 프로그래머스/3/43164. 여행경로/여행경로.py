from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for start, end in sorted(tickets):
        routes[start].append(end)
    
    result = []
    
    def dfs(current_airport):
        if len(result) == len(tickets) + 1:
            return True
        
        if current_airport in routes:
            for i in range(len(routes[current_airport])):
                next_airport = routes[current_airport][i]
                routes[current_airport].remove(next_airport)
                result.append(next_airport)
                
                if dfs(next_airport):
                    return True
                
                routes[current_airport].insert(i, next_airport)
                result.pop()
        return False
    
    result.append("ICN")
    dfs("ICN")
    
    return result