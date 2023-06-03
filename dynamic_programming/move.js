// https://www.acmicpc.net/problem/11048

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
const miro = Array.from({ length: N }, () => input().split(" ").map(Number));
let dp = Array.from({ length: N }, () => Array(M).fill(0));

for (let y = 0; y < N; y++) {
  for (let x = 0; x < M; x++) {
    if (!x && !y) dp[y][x] = miro[y][x];
    else if (!y) dp[y][x] = dp[y][x - 1] + miro[y][x];
    else if (!x) dp[y][x] = dp[y - 1][x] + miro[y][x];
    else dp[y][x] = Math.max(dp[y][x - 1], dp[y - 1][x]) + miro[y][x];
  }
}

console.log(dp.at(-1).at(-1));
