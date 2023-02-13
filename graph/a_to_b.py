# https://www.acmicpc.net/problem/16953

from collections import deque

a,b=map(int,input().split())
queue=deque([a])
answer = 1
flag = False
while queue:
    answer += 1
    mini = 1000000001
    for _ in range(len(queue)):
        curr = queue.popleft()
        c=int(str(curr)+"1")
        d=curr*2
        if c <= b:
            queue.append(c)
        if d <= b:
            queue.append(d)
        mini = min(mini, c, d)
        if b in [c,d]:
            flag = True
            break
    if mini > b: break
    if flag: break

if b not in queue:
    print(-1)
else:
    print(answer)