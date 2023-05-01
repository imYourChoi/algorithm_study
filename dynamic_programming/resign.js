// https://www.acmicpc.net/problem/14501

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
const schedule = Array.from({ length: N }, () => input().split(" ").map(Number));
const dp = Array(N + 1).fill(0);

let today = 1;
for (let [days, money] of schedule) {
  dp[today] = Math.max(dp[today], dp[today - 1]);
  if (today + days - 1 > N) {
    today += 1;
    continue;
  }
  dp[today + days - 1] = Math.max(dp[today + days - 1], dp[today - 1] + money);
  today += 1;
}

console.log(dp.at(-1));
