# https://www.acmicpc.net/problem/14888

n = int(input())
arr = list(map(int, input().split()))
op_count = list(map(int, input().split()))
maxi = -float("inf")
mini = float("inf")

ops = ["+", "-", "*", "/"]

def dfs(index, num):
    global maxi, mini
    if index+1 == n:
        for count, op in zip(op_count, ops):
            if count:
                exec('global temp; temp=int(num%sarr[index])' % op)
                if temp > maxi:
                    maxi = temp
                if temp < mini:
                    mini = temp
    elif index > 0:
        for idx, info in enumerate(zip(op_count, ops)):
            count, op = info
            if count:
                exec('global temp; temp=int(num%sarr[index])' % op)
                op_count[idx] -= 1
                # print(op_count, idx, temp)
                dfs(index+1,temp)
                op_count[idx] += 1

dfs(1, arr[0])
print(maxi)
print(mini)