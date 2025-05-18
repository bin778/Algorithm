def solution(money):
    DP1 = money[:len(money) - 1]
    DP2 = money[1:len(money)]
    
    for i in range(1, len(DP1)):
        if i == 1:
            DP1[i] = max(DP1[i], DP1[i - 1])
            DP2[i] = max(DP2[i], DP2[i - 1])
        else:
            DP1[i] = max(DP1[i - 1], DP1[i - 2] + DP1[i])
            DP2[i] = max(DP2[i - 1], DP2[i - 2] + DP2[i])
    
    return max(max(DP1), max(DP2))