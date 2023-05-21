// https://www.acmicpc.net/problem/2482

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
const K = +input();
const dp = Array.from({ length: N + 1 }, () => Array(K + 1).fill(0));

for (let i = 0; i < N; i++) {
  dp[i][0] = 1;
  dp[i][1] = i;
}

for (let i = 2; i < N + 1; i++) {
  for (let j = 2; j < K + 1; j++) {
    dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % 1000000003;
  }
}

console.log((dp[N - 1][K] + dp[N - 3][K - 1]) % 1000000003);
