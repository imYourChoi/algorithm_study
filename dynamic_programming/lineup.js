// https://www.acmicpc.net/problem/2631

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

const array = Array.from({ length: N }, () => +input());

const dp = Array(N).fill(1);

for (let i = 0; i <= N; i++) {
  for (let j = 0; j < i; j++) {
    if (array[j] < array[i]) dp[i] = Math.max(dp[j] + 1, dp[i]);
  }
}

console.log(N - Math.max(...dp));
