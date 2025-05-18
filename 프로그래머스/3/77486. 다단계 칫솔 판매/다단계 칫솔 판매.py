def solution(enroll, referral, seller, amount):
    result = []
    parent = {}
    money = {}
    
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        money[enroll[i]] = 0
    
    for i in range(len(seller)):
        name = seller[i]
        m = amount[i] * 100
        checked = False
        while parent[name] != '-':
            bonus = int(m * 0.1)
            money[name] += m - bonus
            name = parent[name]
            m = bonus
            if bonus == 0:
                checked = True
                break
            
        if checked:
            continue
        bonus = int(m * 0.1)
        money[name] += m - bonus
                   
    return list(money.values())