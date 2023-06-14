// https://www.acmicpc.net/problem/2573

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
const ocean = Array.from({ length: N }, () => input().split(" ").map(Number));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

function isValid(y, x) {
  return y >= 0 && y < N && x >= 0 && x < M;
}

function melt(y, x, visited) {
  visited[y][x] = true;
  let queue = [[y, x]];

  while (queue.length) {
    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      let [ny, nx] = queue[i];
      for (let [dy, dx] of directions) {
        let Y = ny + dy,
          X = nx + dx;
        if (!isValid(Y, X) || (ocean[Y][X] === 0 && visited[Y][X])) continue;
        visited[Y][X] = true;
        if (ocean[Y][X] === 0) temp.push([Y, X]);
        else ocean[Y][X] -= 1;
      }
    }
    queue = temp;
  }
}

function check(y, x, visited) {
  visited[y][x] = true;
  let queue = [[y, x]];

  while (queue.length) {
    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      let [ny, nx] = queue[i];
      for (let [dy, dx] of directions) {
        let Y = ny + dy,
          X = nx + dx;
        if (!isValid(Y, X) || ocean[Y][X] === 0 || visited[Y][X]) continue;
        visited[Y][X] = true;
        temp.push([Y, X]);
      }
    }
    queue = temp;
  }
}

function solve() {
  let answer = 0;
  while (true) {
    answer++;
    let visited = Array.from({ length: N }, () => Array(M).fill(false));
    for (let y = 0; y < N; y++) {
      for (let x = 0; x < M; x++) {
        if (visited[y][x] || !(ocean[y][x] === 0)) continue;
        melt(y, x, visited);
      }
    }
    visited = Array.from({ length: N }, () => Array(M).fill(false));
    let count = 0;
    for (let y = 0; y < N; y++) {
      for (let x = 0; x < M; x++) {
        if (visited[y][x]) continue;
        if (ocean[y][x] === 0) {
          visited[y][x] = true;
          continue;
        }
        check(y, x, visited);
        count++;
      }
    }
    if (count >= 2) return answer;
    else if (count == 0) return 0;
  }
}

console.log(solve());
