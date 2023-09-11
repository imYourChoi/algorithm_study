// https://www.acmicpc.net/problem/2146

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
const map = Array.from({ length: N }, () => input().split(" ").map(Number));
const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

let answer = Number.MAX_SAFE_INTEGER;

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (map[y][x] <= 0) continue;
    answer = Math.min(answer, find_bridge(y, x));
  }
}

console.log(answer);

function find_bridge(y, x) {
  const beach = [];
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  visited[y][x] = true;
  let queue = [[y, x]];
  while (queue.length) {
    let temp = [];
    for (let [ny, nx] of queue) {
      for (let [dy, dx] of directions) {
        let Y = ny + dy;
        let X = nx + dx;
        if (!isValid(Y, X) || visited[Y][X]) continue;
        visited[Y][X] = true;
        if (map[Y][X] === 1) {
          temp.push([Y, X]);
          map[Y][X] = -1;
        } else if (map[Y][X] === -1) {
        } else {
          beach.push([Y, X]);
        }
      }
    }
    queue = temp;
  }
  let bridge = find_land(beach, visited);
  return bridge;
}

function find_land(beach, visited) {
  let bridge = 1;
  let queue = beach;
  while (queue.length) {
    let temp = [];
    for (let [ny, nx] of queue) {
      for (let [dy, dx] of directions) {
        let Y = ny + dy;
        let X = nx + dx;
        if (!isValid(Y, X) || visited[Y][X]) continue;
        visited[Y][X] = true;
        if (map[Y][X] === 1 || map[Y][X] === -1) {
          return bridge;
        } else {
          temp.push([Y, X]);
        }
      }
    }
    queue = temp;
    bridge++;
  }
}

function isValid(y, x) {
  return y >= 0 && y < N && x >= 0 && x < N;
}
