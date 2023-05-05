// https://www.acmicpc.net/problem/2468

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
const rains = Array.from({ length: N }, () => input().split(" ").map(Number));
const max = rains.reduce((max, row) => {
  const rowMax = row.reduce((temp, cur) => Math.max(temp, cur), 0);
  return Math.max(max, rowMax);
}, 0);

const directions = [
  [-1, 0],
  [0, -1],
  [0, 1],
  [1, 0],
];

function dfs(y, x, visited, h) {
  for (let [dy, dx] of directions) {
    const Y = y + dy;
    const X = x + dx;
    if (Y < 0 || Y >= N || X < 0 || X >= N || visited[Y][X] || rains[Y][X] <= h) continue;
    visited[Y][X] = true;
    dfs(Y, X, visited, h);
  }
}

let answer = 1;

for (let h = 0; h < max; h++) {
  let temp = 0;
  let visited = Array.from({ length: N }, () => Array(N).fill(false));
  for (let y in Array(N).fill()) {
    for (let x in Array(N).fill()) {
      y = +y;
      x = +x;
      if (visited[y][x] || rains[y][x] <= h) continue;
      dfs(y, x, visited, h);
      temp++;
    }
  }
  answer = Math.max(temp, answer);
}

console.log(answer);
