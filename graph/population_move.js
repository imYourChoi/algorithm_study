// https://www.acmicpc.net/problem/16234

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, L, R] = input().split(" ").map(Number);
const land = Array.from({ length: N }, () => input().split(" ").map(Number));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

function isValid(y, x) {
  return y >= 0 && y < N && x >= 0 && x < N;
}

function isOpen(y1, x1, y2, x2) {
  let value = Math.abs(land[y1][x1] - land[y2][x2]);
  return value >= L && value <= R;
}

function bfs(y, x, visited) {
  let record = [[y, x]];
  let count = 1;
  let sum = land[y][x];
  let queue = [[y, x]];
  visited[y][x] = true;
  while (queue.length) {
    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      const [y, x] = queue[i];
      for (let [dy, dx] of directions) {
        const Y = y + dy,
          X = x + dx;
        if (!isValid(Y, X) || visited[Y][X] || !isOpen(Y, X, y, x)) continue;
        visited[Y][X] = true;
        record.push([Y, X]);
        temp.push([Y, X]);
        count += 1;
        sum += land[Y][X];
      }
    }
    queue = temp;
  }

  for (let [ny, nx] of record) {
    land[ny][nx] = Math.floor(sum / count);
  }
  return count > 1 ? true : false;
}

let answer = 0;
while (true) {
  let moved = false;
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  for (let y = 0; y < N; y++) {
    for (let x = 0; x < N; x++) {
      if (visited[y][x]) continue;
      let result = bfs(y, x, visited);
      if (result) {
        moved = true;
      }
    }
  }
  if (!moved) break;
  answer++;
}

console.log(answer);
