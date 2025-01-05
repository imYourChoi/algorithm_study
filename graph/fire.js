// https://www.acmicpc.net/problem/4179

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [R, C] = input().split(" ").map(Number);
const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const maze = Array.from({ length: R }, () => input().split(""));

let initJ = [];
let initF = [];

for (let y = 0; y < R; y++) {
  for (let x = 0; x < C; x++) {
    if (maze[y][x] === "J") initJ.push([y, x]);
    if (maze[y][x] === "F") initF.push([y, x]);
  }
}

function isValid(y, x) {
  return y >= 0 && y < R && x >= 0 && x < C;
}

function checkEscape() {
  for (let y = 0; y < R; y++) {
    if (maze[y][0] === "J" || maze[y][C - 1] === "J") return true;
  }
  for (let x = 0; x < C; x++) {
    if (maze[0][x] === "J" || maze[R - 1][x] === "J") return true;
  }
  return false;
}

function bfs(jihoon, fire) {
  let answer = 1;
  let queueJ = jihoon;
  let queueF = fire;

  while (queueJ.length) {
    if (checkEscape()) return answer;

    let tempJ = [];
    let tempF = [];
    answer++;

    for (let i = 0; i < queueJ.length; i++) {
      const [y, x] = queueJ[i];
      if (maze[y][x] !== "J") continue;

      for (let [dy, dx] of directions) {
        const nY = y + dy;
        const nX = x + dx;
        if (!isValid(nY, nX) || maze[nY][nX] !== ".") continue;

        maze[nY][nX] = "J";
        tempJ.push([nY, nX]);
      }
    }
    queueJ = tempJ;

    for (let i = 0; i < queueF.length; i++) {
      const [y, x] = queueF[i];
      for (let [dy, dx] of directions) {
        const nY = y + dy;
        const nX = x + dx;
        if (!isValid(nY, nX) || maze[nY][nX] === "#" || maze[nY][nX] === "F") continue;

        maze[nY][nX] = "F";
        tempF.push([nY, nX]);
      }
    }
    queueF = tempF;
  }

  return "IMPOSSIBLE";
}

console.log(bfs(initJ, initF));
