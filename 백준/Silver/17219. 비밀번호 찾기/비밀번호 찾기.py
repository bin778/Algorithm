import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_pw = {}

for _ in range(N):
  site, pw = input().split()
  dict_pw[site] = pw

for _ in range(M):
  site = input().replace("\n","")
  print(dict_pw.get(site))