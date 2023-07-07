// https://www.acmicpc.net/problem/2589

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [H, W] = input().split(" ").map(Number);
const map = Array.from({ length: H }, () => input().split(""));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

let answer = 0;

for (let y = 0; y < H; y++) {
  for (let x = 0; x < W; x++) {
    if (map[y][x] === "L") {
      answer = Math.max(find(y, x), answer);
    }
  }
}

function isValid(y, x) {
  return y >= 0 && x >= 0 && y < H && x < W;
}

function find(y, x) {
  let visited = Array.from({ length: H }, () => Array(W).fill(false));
  let queue = [[y, x]];
  visited[y][x] = true;
  let value = 0;
  while (queue.length) {
    let temp = [];
    for (let [ny, nx] of queue) {
      for (let [dy, dx] of directions) {
        let Y = ny + dy,
          X = nx + dx;
        if (!isValid(Y, X) || map[Y][X] === "W" || visited[Y][X]) continue;
        visited[Y][X] = true;
        temp.push([Y, X]);
      }
    }
    queue = temp;
    if (!queue.length) break;
    value++;
  }
  return value;
}

console.log(answer);
