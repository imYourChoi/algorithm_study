# https://www.acmicpc.net/problem/12852

n = int(input())

def make_one():
    visited = [False] * (n+1)
    dp = [[n]]
    while dp:
        new = []
        for each in dp:
            if not each[-1] % 3:
                if not visited[v:=each[-1]//3]:
                    new.append(each[:] + [v])
                    visited[v] = True
                    if v == 1:
                        return new[-1]
            if not each[-1] % 2:
                if not visited[v:=each[-1]//2]:
                    new.append(each[:] + [v])
                    visited[v] = True
                    if v == 1:
                        return new[-1]
            if not visited[v:=each[-1]-1]:
                new.append(each[:] + [v])
                visited[v] = True
                if v == 1:
                    return new[-1]
        dp = new
if n == 1:
    print(0)
    print(1)
else:
    answer = make_one()
    print(len(answer)-1)
    print(*answer)