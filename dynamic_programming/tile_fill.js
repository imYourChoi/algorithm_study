// https://www.acmicpc.net/problem/2133

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
const dp = Array(N + 1).fill(0);
dp[0] = 1;
dp[2] = 3;

for (let i = 4; i < N + 1; i++) {
  dp[i] = dp[i - 2] * 3;
  for (let j = i - 4; j >= 0; j -= 2) dp[i] += dp[j] * 2;
}

console.log(dp[N]);
