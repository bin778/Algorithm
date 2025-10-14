import sys, re
input = sys.stdin.readline

polynomial = input()

if 'x' not in polynomial:
    print(0)
else:
    re_polynomial = re.findall(r'[+-]?\d*x?\^?\d*|\d+', polynomial.replace(' ', ''))[:-1]
    result = 0

    for num in re_polynomial:
        if 'x' in num:
          if num == 'x' or num == '+x':
              result += 1
          elif num == '-x':
              result -= 1
          else: result += int(num.replace('x', ''))

    print(result)