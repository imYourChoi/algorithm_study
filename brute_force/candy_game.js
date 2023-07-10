// https://www.acmicpc.net/problem/3085

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const board = Array.from({ length: N }, () => input().split(""));

function check(y, x) {
  let returnValue = 1;
  let temp = board[y][0];
  let value = 1;
  for (let i = 1; i < N; i++) {
    if (board[y][i] === temp) value++;
    else {
      temp = board[y][i];
      value = 1;
    }
    returnValue = Math.max(returnValue, value);
  }
  temp = board[0][x];
  value = 1;
  for (let j = 1; j < N; j++) {
    if (board[j][x] === temp) value++;
    else {
      temp = board[j][x];
      value = 1;
    }
    returnValue = Math.max(returnValue, value);
  }
  return returnValue;
}

let answer = 0;

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    swap(y, x);
  }
}

console.log(answer);

function swap(y, x) {
  if (y + 1 < N) {
    [board[y + 1][x], board[y][x]] = [board[y][x], board[y + 1][x]];
    answer = Math.max(answer, check(y, x));
    answer = Math.max(answer, check(y + 1, x));
    [board[y + 1][x], board[y][x]] = [board[y][x], board[y + 1][x]];
  }
  if (x + 1 < N) {
    [board[y][x + 1], board[y][x]] = [board[y][x], board[y][x + 1]];
    answer = Math.max(answer, check(y, x));
    answer = Math.max(answer, check(y, x + 1));
    [board[y][x + 1], board[y][x]] = [board[y][x], board[y][x + 1]];
  }
}
