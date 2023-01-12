import sys
input=sys.stdin.readline
n,m=map(int,input().split())
d={}
count=0
answer=[]
for i in range(n+m):
    s = input()
    if s in d:
        count+=1
        answer.append(s)
    else:
        d[s]=1
print(count)
print("".join(sorted(answer)))