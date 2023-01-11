# https://www.acmicpc.net/problem/11729

answer = []

def hanoi(n, fr, by, to):
    if n == 1:
        answer.append([fr, to])
        return
    
    hanoi(n-1, fr, to, by)
    answer.append([fr, to])
    hanoi(n-1, by, fr, to)
    
hanoi(int(input()), 1, 2, 3)
print(len(answer))
for a, b in answer:
    print(a,b)