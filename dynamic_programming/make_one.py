# https://www.acmicpc.net/problem/1463

n = int(input())

def one(n):
    store = {n}
    count = 0
    while True:
        new = set()
        for _ in range(len(store)):
            temp = store.pop()
            if temp == 1:
                return count
            if temp % 3 == 0:
                new.add(temp//3)
            if temp % 2 == 0:
                new.add(temp//2)
            new.add(temp-1)
        store = new
        count += 1

print(one(n))