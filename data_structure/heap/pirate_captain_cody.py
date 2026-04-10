# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy/description

import heapq

T = int(input())

shipDict = {}
heap = []
reload = [[] for _ in range(10)]
reloadSet = set()


def attack_prepare(args):
    N, *shipInfo = args

    for i in range(N):
        id, p, r = shipInfo[i*3], shipInfo[i*3+1], shipInfo[i*3+2]
        shipDict[id] = [p, r]
        heapq.heappush(heap, (-p, id))


def request_support(args):
    id, p, r = args

    shipDict[id] = [p, r]
    heapq.heappush(heap, (-p, id))


def gun_change(args):
    id, pw = args

    shipDict[id][0] = pw
    heapq.heappush(heap, (-pw, id))


def attack_execute():
    count = 0
    damage = 0
    firedShips = []
    while heap and count < 5:
        p, id = heapq.heappop(heap)
        p *= -1

        if id in reloadSet:
            continue
        if shipDict[id][0] != p:
            heapq.heappush(heap, (-shipDict[id][0], id))
            continue

        count += 1
        damage += p
        firedShips.append(str(id))

        reload[shipDict[id][1]-1].append(id)
        reloadSet.add(id)

    print(damage, len(firedShips), " ".join(firedShips))


def reload_to_prepare():
    first = reload.pop(0)

    for id in first:
        heapq.heappush(heap, (-shipDict[id][0], id))
        reloadSet.remove(id)

    reload.append([])


for i in range(T):
    reload_to_prepare()

    command, *rest = map(int, input().split())

    if command == 100:
        attack_prepare(rest)
    elif command == 200:
        request_support(rest)
    elif command == 300:
        gun_change(rest)
    else:
        attack_execute()
