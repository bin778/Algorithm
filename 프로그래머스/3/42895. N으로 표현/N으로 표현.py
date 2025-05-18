def solution(N, number):
    cnt = [[] for i in range(9)]
    chk = set()
    
    for i in range(1, 9):
        val = int(str(N) * i)
        if val == number:
            return i
        cnt[i] = [val]
        chk.add(val)
    
    chk.add(0)
    
    for i in range(2, 9):
        for j in range(1, i):
            k = i - j
            for num_j in cnt[j]:
                for num_k in cnt[k]:
                    opers = [num_j + num_k, abs(num_j - num_k), num_j * num_k, num_j // num_k, num_k // num_j]
                    for oper in opers:
                        if oper in chk:
                            continue
                        elif oper == number:
                            return i
                        cnt[i].append(oper)
                        chk.add(oper)
    
    return -1