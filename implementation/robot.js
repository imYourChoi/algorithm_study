// https://www.acmicpc.net/problem/14503

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
let [r, c, d] = input().split(" ").map(Number);
const room = Array.from({ length: N }, () => input().split(" ").map(Number));
const visited = Array.from({ length: N }, () => Array(M).fill(false));

const directions = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];
let answer = 0;

function count(y, x) {
  return room[y][x] === 0 && !visited[y][x];
}

function valid(y, x) {
  return y >= 0 && y < N && x >= 0 && x < M;
}

function clean(y, x) {
  if (room[y][x] === 0 && !visited[y][x]) {
    visited[y][x] = true;
    answer += 1;
  }

  let empty = 0;
  for (let t = 0; t < 4; t++) {
    let [dy, dx] = directions[(d + 4 - t) % 4];
    if (valid(y + dy, x + dx)) empty += count(y + dy, x + dx);
  }
  if (!empty) {
    let [dy, dx] = directions[d];
    if (valid(y - dy, x - dx) && room[y - dy][x - dx] === 0) {
      clean(y - dy, x - dx);
    } else return;
  } else {
    d = (d + 4 - 1) % 4;
    let [dy, dx] = directions[d];
    if (valid(y + dy, x + dx) && room[y + dy][x + dx] === 0 && !visited[y + dy][x + dx]) clean(y + dy, x + dx);
    else clean(y, x);
  }
}

clean(r, c);

console.log(answer);
