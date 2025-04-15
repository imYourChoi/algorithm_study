// https://www.acmicpc.net/problem/5557

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const nums = input().split(" ").map(Number);

const dp = Array.from({ length: N - 1 }, () => Array(21).fill(0n));

dp[0][nums[0]] = 1n;

for (let n = 1; n < N - 1; n++) {
  const num = nums[n];
  for (let i = num; i <= 20; i++) {
    dp[n][i] += dp[n - 1][i - num];
  }
  for (let i = 0; i <= 20 - num; i++) {
    dp[n][i] += dp[n - 1][i + num];
  }
}

console.log(dp.at(-1)[nums.at(-1)]);
