// https://www.acmicpc.net/problem/2583

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [M, N, K] = input().split(" ").map(Number);
const visited = Array.from({ length: M }, () => Array(N).fill(false));

for (let i = 0; i < K; i++) {
  const [x1, y1, x2, y2] = input().split(" ").map(Number);
  for (let y = y1; y < y2; y++) {
    for (let x = x1; x < x2; x++) visited[y][x] = true;
  }
}

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

function isValid(y, x) {
  return y >= 0 && y < M && x >= 0 && x < N && !visited[y][x];
}

function bfs(y, x) {
  let area = 1;
  let locations = [[y, x]];
  visited[y][x] = true;
  while (locations.length) {
    let temp = [];
    for (let i = 0; i < locations.length; i++) {
      const [y, x] = locations[i];
      for (let [dy, dx] of directions) {
        const [Y, X] = [y + dy, x + dx];
        if (!isValid(Y, X)) continue;
        area++;
        visited[Y][X] = true;
        temp.push([Y, X]);
      }
    }
    locations = temp;
  }
  return area;
}

let answer = [];
for (let y = 0; y < M; y++) {
  for (let x = 0; x < N; x++) {
    if (!visited[y][x]) answer.push(bfs(y, x));
  }
}

console.log(answer.length);
console.log(answer.sort((a, b) => a - b).join(" "));
