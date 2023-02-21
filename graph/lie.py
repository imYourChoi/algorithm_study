# https://www.acmicpc.net/problem/1043

from collections import deque

N,M = map(int,input().split())
truthCount, *truePeople = list(map(int,input().split()))

byPeople = [set() for _ in range(N+1)]
byParty = [[] for _ in range(M)]
for i in range(M):
    count, *people = list(map(int, input().split()))
    for person in people:
        byParty[i].append(person)
        byPeople[person].add(i)

lieParties = [1] * M
visitedPerson = [False] * (N+1)
answer = M
queue = deque(truePeople)

while queue:
    for _ in range(len(queue)):
        person = queue.popleft()
        if visitedPerson[person]:
            continue
        visitedPerson[person] = True
        for party in byPeople[person]:
            if not lieParties[party]:
                continue
            lieParties[party] = 0
            for person in byParty[party]:
                if visitedPerson[person]:
                    continue
                queue.append(person)
print(sum(lieParties))


