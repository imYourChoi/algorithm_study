// https://www.acmicpc.net/problem/11057

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
const dp = Array.from({ length: N }, () => Array(10).fill(0));

dp[0] = Array(10).fill(1);

for (let i = 1; i < N; i++) {
  for (let j = 0; j < 10; j++) {
    dp[i][j] = dp[i - 1].slice(0, j + 1).reduce((a, b) => a + b) % 10007;
  }
}

console.log(dp.at(-1).reduce((a, b) => a + b) % 10007);
