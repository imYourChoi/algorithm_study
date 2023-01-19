# https://www.acmicpc.net/problem/2629

num_weight = int(input())
weights = [0] + list(map(int, input().split()))
num_gem = int(input())
gems = list(map(int, input().split()))

dp = [{} for _ in range(num_weight+1)]

for i in range(1,num_weight+1):
    for j in range(-sum(weights)-1,sum(weights)+1):
        weight = weights[i]

        dp[i].update(dp[i-1])
        
        dp[i][weight] = 1
        dp[i][-weight] = 1

        if v:=dp[i-1].get(j-weight,0) | dp[i-1].get(j+weight,0):
            dp[i][j] = v
print(dp)
for gem in gems:
    print("Y" if dp[-1].get(gem,0) else "N", end=" ")
print()