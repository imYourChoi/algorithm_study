// https://www.acmicpc.net/problem/2225

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K] = input().split(" ").map(Number);
const dp = Array.from({ length: N + 1 }, () => Array(K + 1).fill(0));

dp[0][0] = 1;

for (let k = 1; k <= K; k++) {
  for (let i = 0; i <= N; i++) {
    for (let j = i; j <= N; j++) {
      dp[j][k] = (dp[j][k] + dp[j - i][k - 1]) % 1000000000;
    }
  }
}

console.log(dp.at(-1).at(-1));
