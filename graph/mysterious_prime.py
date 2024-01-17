# https://www.acmicpc.net/problem/2023

# const stdin = require("fs")
#   .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
#   .toString();

# const N = +stdin;

# const isPrime = num => {
#   for (let i = 2; i <= Math.floor(num ** 0.5); i++) {
#     if (num % i === 0) return false;
#   }
#   return true;
# };

# const dfs = num => {
#   if (!isPrime(num)) return;
#   if (String(num).length === N) console.log(num);
#   for (let i = 1; i < 10; i += 2) {
#     dfs(num * 10 + i);
#   }
# };

# for (let i of [2, 3, 5, 7]) dfs(i);

import sys

n = int(input())


def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False

    return True


def dfs(number):
    if not isPrime(number):
        return

    if len(str(number)) == n:
        print(number)

    for i in range(1, 10, 2):
        dfs(number*10 + i)

    return


for i in [2, 3, 5, 7]:
    dfs(i)
