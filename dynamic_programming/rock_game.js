// https://www.acmicpc.net/problem/9655

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
const dp = Array(N + 1).fill(-1);

dp[1] = 1;
dp[2] = 0;
dp[3] = 1;

for (let i = 4; i <= N; i++) {
  if (dp[i - 1] || dp[i - 3]) dp[i] = 0;
  else dp[i] = 1;
}

console.log(dp[N] ? "SK" : "CY");
