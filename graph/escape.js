// https://www.acmicpc.net/problem/3055

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
const map = Array.from({ length: R }, () => input().split(""));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

function isValid(y, x) {
  return y >= 0 && y < R && x >= 0 && x < C;
}

function water(y, x, visited) {
  for (let [dy, dx] of directions) {
    let Y = y + dy;
    let X = x + dx;
    if (!isValid(Y, X) || visited[Y][X] || map[Y][X] === "X" || map[Y][X] === "*" || map[Y][X] === "D") continue;
    visited[Y][X] = true;
    map[Y][X] = "*";
  }
}
function dochi(y, x, visited) {
  for (let [dy, dx] of directions) {
    let Y = y + dy;
    let X = x + dx;
    if (!isValid(Y, X) || visited[Y][X] || map[Y][X] === "X" || map[Y][X] === "*" || map[Y][X] === "S") continue;
    if (map[Y][X] === "D") return true;
    visited[Y][X] = true;
    map[Y][X] = "S";
  }
  return false;
}

let answer = 0;

function solve() {
  while (true) {
    answer++;
    let visited = Array.from({ length: R }, () => Array(C).fill(false));
    let flag = false;
    for (let y = 0; y < R; y++) {
      for (let x = 0; x < C; x++) {
        if (map[y][x] === "S" && !visited[y][x]) {
          if (dochi(y, x, visited)) return answer;
          flag = true;
        }
      }
    }
    if (!flag) return false;
    visited = Array.from({ length: R }, () => Array(C).fill(false));
    for (let y = 0; y < R; y++) {
      for (let x = 0; x < C; x++) {
        if (map[y][x] === "*" && !visited[y][x]) water(y, x, visited);
      }
    }
  }
}

console.log(solve() || "KAKTUS");
