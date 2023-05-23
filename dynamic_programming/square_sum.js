// https://www.acmicpc.net/problem/1699

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
const dp = Array(N + 1).fill(Number.MAX_SAFE_INTEGER);
dp[N] = 0;

for (let i = N; i > 0; i--) {
  if (dp[i] === Number.MAX_SAFE_INTEGER) continue;
  for (let j = 1; i - j ** 2 >= 0; j++) {
    dp[i - j ** 2] = Math.min(dp[i - j ** 2], dp[i] + 1);
  }
}

console.log(dp[0]);
