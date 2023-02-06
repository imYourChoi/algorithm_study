# https://www.acmicpc.net/problem/1929

m,n=map(int,input().split())
nums = [x for x in range(n+1)]

for i in range(2,int(n**0.5)+1):
    if nums[i]:
        for idx in range(2*i,n+1,i):
            nums[idx] = 0

print(*[x for x in nums[m:] if x > 1], sep="\n")
