// https://www.acmicpc.net/problem/15685

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
const board = Array.from({ length: 101 }, () => Array(101).fill(false));

let dx = [1, 0, -1, 0];
let dy = [0, -1, 0, 1];

for (let i = 0; i < N; i++) {
  let [x, y, d, g] = input().split(" ").map(Number);
  board[y][x] = true;
  let curve = [d];
  for (let j = 0; j < g; j++) {
    for (let k = curve.length - 1; k >= 0; k--) {
      curve.push((curve[k] + 1) % 4);
    }
  }
  for (let j = 0; j < curve.length; j++) {
    x += dx[curve[j]];
    y += dy[curve[j]];
    if (x < 0 || x > 100 || y < 0 || y > 100) continue;
    board[y][x] = true;
  }
}

let answer = 0;
for (let y = 0; y < 100; y++) {
  for (let x = 0; x < 100; x++) {
    if (board[y][x] && board[y + 1][x] && board[y][x + 1] && board[y + 1][x + 1]) answer++;
  }
}

console.log(answer);
