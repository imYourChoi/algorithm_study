# https://www.acmicpc.net/problem/1700

N,K = map(int, input().split())

order = list(map(int,input().split()))
strip = set()
dic = {}
for p in order:
    dic[p] = dic.get(p,0) + 1

answer = 0

for idx, p in enumerate(order):
    # print("before\t", strip, p, dic, [answer])
    dic[p] -= 1
    if p in strip:
        # print("after\t", strip, p, dic, [answer])
        continue
    if len(strip) < N:
        strip.add(p)
    else:
        answer += 1
        # toRemove = min(strip, key=dic.get)
        # least = dic[min(strip, key=dic.get)]
        # toRemoves = set([x for x in strip if dic[x] == least])
        toRemoves = strip.copy()
        # print(strip, dic, toRemoves)
        while len(toRemoves) > 1 and idx < K:
            toRemoves.discard(order[idx])
            idx += 1
        toRemove = toRemoves.pop()
        strip.remove(toRemove)
        if dic[toRemove] == 0:
            dic.pop(toRemove, None)
        strip.add(p)

print(answer)