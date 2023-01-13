# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    array = [0, 1, 2, 4]

    for i in range(4, num+1):
        array.append(array[i-1]+array[i-2]+array[i-3])
    print(array[num])