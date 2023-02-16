# https://www.acmicpc.net/problem/2437

n = int(input())
weights = sorted(list(map(int, input().split())))

def scale():
    answer = 0
    for weight in weights:
        if weight > answer + 1:
            break
        answer += weight
    return answer + 1

print(scale())