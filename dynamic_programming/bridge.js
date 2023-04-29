// https://www.acmicpc.net/problem/1010

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();

for (let i = 0; i < T; i++) {
  const [N, M] = input().split(" ").map(Number);
  const dp = Array.from({ length: N }, () => Array(M).fill(0));

  for (let i in dp) {
    i = Number(i);
    const row = dp[i];
    if (i) for (let j = i; j < M - (N - 1 - i); j++) row[j] = dp[i - 1].slice(0, j).reduce((acc, cur) => acc + cur, 0);
    else for (let j = 0; j <= M - N; j++) row[j] = 1;
  }
  console.log(dp.at(-1).reduce((acc, cur) => acc + cur, 0));
}
