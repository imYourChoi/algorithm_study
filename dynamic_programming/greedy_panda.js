// https://www.acmicpc.net/problem/1937

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = +input();
const forest = Array.from({ length: n }, () => input().split(" ").map(Number));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
const dp = Array.from({ length: n }, () => Array(n).fill(0));

const isValid = (y, x) => 0 <= y && y < n && 0 <= x && x < n;
const dfs = (y, x) => {
  if (dp[y][x]) return dp[y][x];

  dp[y][x] = 1;
  let temp = 0;

  for (let [dy, dx] of directions) {
    const Y = y + dy;
    const X = x + dx;
    if (!isValid(Y, X)) continue;
    if (forest[y][x] > forest[Y][X]) temp = Math.max(temp, dfs(Y, X));
  }
  dp[y][x] += temp;
  return dp[y][x];
};

let answer = 0;

for (let y = 0; y < n; y++) {
  for (let x = 0; x < n; x++) {
    if (!dp[y][x]) answer = Math.max(answer, dfs(y, x));
  }
}

console.log(answer);
