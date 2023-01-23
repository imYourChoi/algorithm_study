# https://www.acmicpc.net/problem/15650

n,m = map(int, input().split())

def nm(array, seq, index):
    if not array:
        return
    if index == 1:
        for x in array:
            if not seq or (seq and x > seq[-1]):
                print(*seq, x)
    else:
        for x in array:
            if not seq or (seq and x > seq[-1]):
                new = array[:]
                new.remove(x)
                nm(new, seq + [x], index - 1)

nm([x+1 for x in range(n)], [], m)