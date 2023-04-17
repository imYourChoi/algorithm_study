// https://www.acmicpc.net/problem/4963

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
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
  [0, -1],
  [-1, -1],
];

const bfs = (visited, map, origin, w, h) => {
  let queue = [origin];

  while (queue.length) {
    let temp = [];
    for (let [y, x] of queue) {
      if (visited[y][x]) continue;
      visited[y][x] = true;
      for (let [dy, dx] of directions) {
        let Y = y + dy,
          X = x + dx;
        if (0 > Y || Y >= h || 0 > X || X >= w) continue;
        if (!map[Y][X] || visited[Y][X]) continue;
        temp.push([Y, X]);
      }
    }
    queue = temp;
  }
  return;
};

let answer = [];

while (true) {
  const [w, h] = input()
    .split(" ")
    .map(e => +e);
  if (!w) break;
  const visited = Array.from({ length: h }, () => Array(w).fill(false));
  const map = Array.from({ length: h }, () =>
    input()
      .split(" ")
      .map(e => +e)
  );

  let value = 0;
  for (let y in map) {
    for (let x in map[y]) {
      if (map[y][x] && !visited[y][x]) {
        bfs(visited, map, [+y, +x], w, h);
        value++;
      }
    }
  }
  answer.push(value);
}

console.log(answer.join("\n"));
