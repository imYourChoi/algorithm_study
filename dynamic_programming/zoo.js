// https://www.acmicpc.net/problem/1309

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
const dp = Array.from({ length: N }, () => Array(3).fill(0));
dp[0] = [1, 1, 1];

for (let i = 1; i < N; i++) {
  dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901;
  dp[i][1] = (dp[i - 1][2] + dp[i - 1][0]) % 9901;
  dp[i][2] = (dp[i - 1][1] + dp[i - 1][0]) % 9901;
}

console.log(dp.at(-1).reduce((a, b) => a + b) % 9901);
