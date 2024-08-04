// https://www.acmicpc.net/problem/1600

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const K = +input();
const [W, H] = input().split(" ").map(Number);

const MAP = Array.from({ length: H }, () => input().split(" ").map(Number));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
const horse_directions = [
  [-2, 1],
  [-1, 2],
  [1, 2],
  [2, 1],
  [2, -1],
  [1, -2],
  [-1, -2],
  [-2, -1],
];

const visited = Array.from({ length: K + 1 }, () => Array.from({ length: H }, () => Array(W).fill(false)));

const isValid = (y, x) => y >= 0 && y < H && x >= 0 && x < W;

const bfs = () => {
  visited[0][0][0] = true;
  let queue = [[0, 0, 0]];

  let answer = 0;

  while (queue.length) {
    answer += 1;
    let temp = [];

    for (let i = 0; i < queue.length; i++) {
      let [ny, nx, count] = queue[i];
      if (count < K) {
        for ([dy, dx] of horse_directions) {
          let Y = ny + dy,
            X = nx + dx;
          if (!isValid(Y, X) || MAP[Y][X] === 1 || visited[count + 1][Y][X]) continue;
          if (Y === H - 1 && X === W - 1) return answer;
          visited[count + 1][Y][X] = true;
          temp.push([Y, X, count + 1]);
        }
      }
      for ([dy, dx] of directions) {
        let Y = ny + dy,
          X = nx + dx;
        if (!isValid(Y, X) || MAP[Y][X] === 1 || visited[count][Y][X]) continue;
        if (Y === H - 1 && X === W - 1) return answer;
        visited[count][Y][X] = true;
        temp.push([Y, X, count]);
      }
    }
    queue = temp;
  }
};

console.log(W === 1 && H === 1 ? 0 : bfs() ?? -1);
