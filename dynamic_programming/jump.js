// https://www.acmicpc.net/problem/1890

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
const board = Array.from({ length: N }, () => input().split(" ").map(Number));
const count = Array.from({ length: N }, () => Array(N).fill(0n));
count[0][0] = 1n;

function move(y, x) {
  if (!board[y][x]) return;
  if (y + board[y][x] < N) count[y + board[y][x]][x] += count[y][x];
  if (x + board[y][x] < N) count[y][x + board[y][x]] += count[y][x];
}

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    move(y, x);
  }
}

console.log(count.at(-1).at(-1).toString());
