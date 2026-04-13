# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/perfume-workshop/description

Q = int(input())

N = 0
added = 0
scentDict = {}


def one_init(args):
    N, *scents = args

    for id, scent in enumerate(scents):
        scentDict[id+1] = scent

    return len(scents)


def two_add(args):
    global added
    added += 1
    scent = args[0]
    scentDict[N + added] = scent


def three_discard(args):
    id = args[0]

    if id not in scentDict:
        print(-1)
        return

    print(scentDict.pop(id))


def four_blend(args):
    k = args[0]
    sortedKeys = sorted(scentDict.keys(), key=lambda x: -scentDict[x])

    dp = [0] * (k + 1)

    def backtracking(remain):
        if dp[remain] > 0:
            return dp[remain]

        minimum = float('inf')

        for key in sortedKeys:
            scent = scentDict[key]

            if scent > remain:
                continue

            if scent == remain:
                dp[remain] = 1
                return 1

            result = backtracking(remain - scent)

            minimum = min(minimum, result + 1)

        dp[remain] = minimum

        return minimum

    backtracking(k)

    if dp[k] == float('inf'):
        print(-1)
    else:
        print(dp[k])


def five_configure(args):
    k = args[0]
    sortedKeys = sorted(scentDict.keys(), key=lambda x: scentDict[x])
    n = len(sortedKeys)

    def two_pointer(left):
        count = 0

        mid = 0
        right = n - 1

        while mid < n and right >= 0:
            scentSum = scentDict[sortedKeys[left]] + \
                scentDict[sortedKeys[mid]] + scentDict[sortedKeys[right]]

            if scentSum >= k:
                count += n - mid
                right -= 1
            else:
                mid += 1
        return count

    answer = 0
    for left in range(n):
        answer += two_pointer(left)

    print(answer)


for i in range(Q):
    cmd, *rest = map(int, input().split())

    if cmd == 1:
        N = one_init(rest)
    elif cmd == 2:
        two_add(rest)
    elif cmd == 3:
        three_discard(rest)
    elif cmd == 4:
        four_blend(rest)
    else:
        five_configure(rest)
