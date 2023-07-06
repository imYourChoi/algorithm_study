// https://www.acmicpc.net/problem/2636

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
const board = Array.from({ length: H }, () => input().split(" ").map(Number));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

let total = 0;
for (let y = 0; y < H; y++) {
  for (let x = 0; x < W; x++) {
    if (board[y][x]) total++;
  }
}

let round = 0;
while (true) {
  round++;
  let visited = Array.from({ length: H }, () => Array(W).fill(false));
  let temp = 0;
  temp += cheese(0, 0, visited);
  if (total - temp == 0) break;
  total -= temp;
}
console.log(round);
console.log(total);

function isValid(y, x) {
  return y >= 0 && y < H && x >= 0 && x < W;
}

function cheese(y, x, visited) {
  let queue = [[y, x]];
  let amount = 0;
  while (queue.length) {
    let temp = [];
    for (let [ny, nx] of queue) {
      for (let [dy, dx] of directions) {
        let Y = ny + dy,
          X = nx + dx;
        if (!isValid(Y, X) || visited[Y][X]) continue;
        visited[Y][X] = true;
        if (board[Y][X] === 1) {
          board[Y][X] = 0;
          amount++;
        } else {
          temp.push([Y, X]);
        }
      }
    }
    queue = temp;
  }
  return amount;
}
