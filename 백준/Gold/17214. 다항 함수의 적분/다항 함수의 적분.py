import sys, re
input = sys.stdin.readline
polynomial = input().strip()

if polynomial == '0':
    print('W')
else:
    re_polynomial = re.findall(r'[+-]?\d*x?\^?\d*|\d+', polynomial.replace(' ', ''))[:-1]
    result = ''
    
    for num in re_polynomial:
        if 'x' in num:
            re_num = int(int(re.findall(r"-?\d+", num)[0]) / 2)
            if re_num == 1:
                result += 'xx'
            elif re_num == -1:
                result += '-xx'
            else:
                result += (str(re_num) + 'xx')
        else:
            re_num = int(re.findall(r"-?\d+", num)[0])
            if re_num == 1:
                if '+' in num:
                    result += '+x'
                else:
                    result += 'x'
            elif re_num == -1:
                result += '-x'
            else:
                if '+' in num:
                    result += ('+' + str(re_num) + 'x')
                else:
                    result += (str(re_num) + 'x')
    result += '+W'
    print(result)