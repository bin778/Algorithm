def solution(n, money):
    DP = [0] * (n + 1)
    DP[0] = 1
    for i in range(len(money)):
        for j in range(money[i], n + 1):
            DP[j] += DP[j - money[i]]
    return DP[n]