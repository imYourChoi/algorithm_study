// https://www.acmicpc.net/problem/9084

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

for (let i = 0; i < N; i++) {
  const N = +input();
  const prices = input().split(" ").map(Number);
  const M = +input();

  const dp = Array(M + 1).fill(0);

  dp[0] = 1;

  for (let price of prices) {
    for (let m = price; m <= M; m++) {
      dp[m] += dp[m - price];
    }
  }

  console.log(dp[M]);
}
