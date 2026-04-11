# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/submissions?page=1&page_size=20

Q = int(input())

houses = []
destroyed = []

for _ in range(Q):
    cmd, *rest = map(int, input().split())

    if cmd == 100:
        N = rest[0]
        for i in range(N):
            houses.append(rest[i+1])
            destroyed.append(False)

    elif cmd == 200:
        p = rest[0]
        houses.append(p)
        destroyed.append(False)

    elif cmd == 300:
        q = rest[0]
        destroyed[q - 1] = True

    elif cmd == 400:
        r = rest[0]

        active_houses = [houses[i]
                         for i in range(len(houses)) if not destroyed[i]]

        if r == len(active_houses):
            print(0)
            continue

        left = 0
        right = active_houses[-1] - active_houses[0]
        ans = right

        while left <= right:
            mid = (left + right) // 2

            count = 0
            limit = -1

            for pos in active_houses:
                if pos > limit:
                    count += 1
                    limit = pos + mid

            if count <= r:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        print(ans)
