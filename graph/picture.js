// https://www.acmicpc.net/problem/1926

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, m] = input().split(" ").map(Number);
const paper = Array.from({ length: n }, () => input().split(" ").map(Number));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
let visited = Array.from({ length: n }, () => Array(m).fill(false));

let count = 0;
let area = 0;

for (let y = 0; y < n; y++) {
  for (let x = 0; x < m; x++) {
    if (!visited[y][x] && paper[y][x]) {
      count++;
      area = Math.max(picture(y, x), area);
    }
  }
}

console.log(count);
console.log(area);

function isValid(y, x) {
  return y >= 0 && x >= 0 && y < n && x < m;
}

function picture(y, x) {
  let queue = [[y, x]];
  visited[y][x] = true;
  let tempCount = 1;

  while (queue.length) {
    let temp = [];
    for (let [ny, nx] of queue) {
      for (let [dy, dx] of directions) {
        let Y = ny + dy,
          X = nx + dx;
        if (!isValid(Y, X) || visited[Y][X] || !paper[Y][X]) continue;
        visited[Y][X] = true;
        tempCount++;
        temp.push([Y, X]);
      }
    }
    queue = temp;
  }

  return tempCount;
}
