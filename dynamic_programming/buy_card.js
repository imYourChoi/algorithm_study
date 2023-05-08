// https://www.acmicpc.net/problem/11052

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
const prices = input().split(" ").map(Number);
const dp = Array(N + 1).fill(0);

for (let index in prices) {
  index = +index;
  const price = prices[index];
  for (let j = index + 1; j <= N; j++) {
    dp[j] = Math.max(dp[j - index - 1] + price, dp[j]);
  }
}

console.log(dp.at(-1));
