// https://www.acmicpc.net/problem/15486

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
const info = [[0, 0]].concat(Array.from({ length: N }, () => input().split(" ").map(Number)));
const dp = Array(N + 1).fill(0);

for (let i = N; i > 0; i--) {
  const [days, value] = info[i];
  if (i + days - 1 > N) {
    if (i + 1 > N) dp[i] = 0;
    else dp[i] = dp[i + 1];
  } else {
    if (i + 1 > N) dp[i] = value;
    else {
      dp[i] = Math.max(dp[i + 1], (dp[i + days] ?? 0) + value);
    }
  }
}

console.log(dp[1]);
