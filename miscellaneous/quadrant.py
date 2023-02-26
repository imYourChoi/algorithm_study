# https://www.acmicpc.net/problem/14681

x,y=int(input()), int(input())
print((1 if y>0 else 4) if x>0 else 2 if y>0 else 3)