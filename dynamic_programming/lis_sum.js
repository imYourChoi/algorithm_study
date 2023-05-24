// https://www.acmicpc.net/problem/11055

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
const arr = input().split(" ").map(Number);
const dp = Array(N).fill(0);
dp[0] = arr[0];

for (let i = 1; i < N; i++) {
  for (let j = 0; j < i; j++) {
    if (arr[i] > arr[j]) dp[i] = Math.max(dp[i], dp[j] + arr[i]);
    else dp[i] = Math.max(dp[i], arr[i]);
  }
}

console.log(Math.max(...dp));
