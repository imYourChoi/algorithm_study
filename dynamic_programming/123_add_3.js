// https://www.acmicpc.net/problem/15988

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
const dp = [0, 1, 2, 4, 7];

for (let t = 0; t < T; t++) {
  const n = +input();
  if (dp[n]) {
    console.log(dp[n] % 1000000009);
    continue;
  }
  for (let i = dp.length; i <= n; i++) {
    dp.push((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009);
  }
  console.log(dp[n] % 1000000009);
}

// console.log(dp);
