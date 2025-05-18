def solution(people, limit):
    result = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        result += 1
    
    return result