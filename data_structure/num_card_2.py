# https://www.acmicpc.net/problem/10816

input()
card = {}
for num in map(int, input().split()):
    if num in card:
        card[num] +=1
    else:
        card[num] = 1
    
input()
for num in map(int, input().split()):
    if num in card:
        print(card[num], end=" ")
    else:
        print(0, end=" ")
print()