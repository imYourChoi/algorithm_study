// https://www.acmicpc.net/problem/2294

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, k] = input().split(" ").map(Number);
const nums = Array.from({ length: n }, () => +input());
const dp = Array(k + 1).fill(Number.MAX_VALUE);
dp[0] = 0;

for (let num of nums) {
  for (let i = num; i <= k; i++) {
    dp[i] = Math.min(dp[i - num] + 1, dp[i]);
  }
}

console.log(dp.at(-1) === Number.MAX_VALUE ? -1 : dp.at(-1));
