// https://www.acmicpc.net/problem/14940

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const [n, m] = input().split(" ").map(Number);

const map = Array.from({ length: n }, () => input().split(" ").map(Number));

let target;

for ([y, row] of map.entries()) {
  const x = row.indexOf(2);
  if (x > -1) {
    target = [y, x];
    break;
  }
}

for (let y = 0; y < n; y++) {
  for (let x = 0; x < m; x++) {
    if (map[y][x] === 1) map[y][x] = -1;
  }
}

[].repla;

function isValid(y, x, N, M) {
  return y >= 0 && y < N && x >= 0 && x < M;
}

function bfs(target, map, n, m) {
  const visited = Array.from({ length: n }, () => Array(m).fill(false));
  let distance = 0;

  const [ty, tx] = target;
  map[ty][tx] = distance;

  let queue = [[ty, tx]];

  while (queue.length) {
    const temp = [];
    for (let i = 0; i < queue.length; i++) {
      const [y, x] = queue[i];
      if (visited[y][x]) continue;

      visited[y][x] = true;
      map[y][x] = distance;

      for (let [dy, dx] of directions) {
        let ny = y + dy;
        let nx = x + dx;
        if (!isValid(ny, nx, n, m) || map[ny][nx] === 0 || visited[ny][nx]) continue;
        temp.push([ny, nx]);
      }
    }
    queue = temp;
    distance++;
  }
}

bfs(target, map, n, m);

map.forEach(row => console.log(row.join(" ")));
