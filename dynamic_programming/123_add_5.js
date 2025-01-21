// https://www.acmicpc.net/problem/15990

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

const div = 1_000_000_009;
const dp = [
  [0, 0, 0],
  [1, 0, 0],
  [0, 1, 0],
  [1, 1, 1],
  [2, 0, 1],
];

const answers = [];

for (let t = 0; t < T; t++) {
  const n = +input();
  if (dp[n]) {
    answers.push((dp[n][0] + dp[n][1] + dp[n][2]) % div);
    continue;
  }
  for (let i = dp.length; i <= n; i++) {
    dp.push([
      (dp[i - 1][1] + dp[i - 1][2]) % div,
      (dp[i - 2][0] + dp[i - 2][2]) % div,
      (dp[i - 3][0] + dp[i - 3][1]) % div,
    ]);
  }
  answers.push((dp[n][0] + dp[n][1] + dp[n][2]) % div);
}

console.log(answers.join("\n"));
