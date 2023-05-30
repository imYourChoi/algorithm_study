// https://www.acmicpc.net/problem/14499

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [N, M, y, x, K] = input().split(" ").map(Number);
const board = Array.from({ length: N }, () => input().split(" ").map(Number));
const commands = input().split(" ").map(Number);

let dice = Array(6).fill(0);
const directions = [0, [0, 1], [0, -1], [-1, 0], [1, 0]];
let answer = [];

function turn(direction) {
  let [a, b, c, d, e, f] = dice;
  switch (direction) {
    case 1:
      dice = [c, b, f, a, e, d];
      break;
    case 2:
      dice = [d, b, a, f, e, c];
      break;
    case 3:
      dice = [b, f, c, d, a, e];
      break;
    case 4:
      dice = [e, a, c, d, f, b];
      break;
  }
}

for (let command of commands) {
  let [dy, dx] = directions[command];
  let Y = y + dy,
    X = x + dx;
  if (Y < 0 || Y >= N || X < 0 || X >= M) continue;
  turn(command);
  answer.push(dice.at(-1));
  if (board[Y][X] === 0) board[Y][X] = dice[0];
  else {
    dice[0] = board[Y][X];
    board[Y][X] = 0;
  }
  y = Y;
  x = X;
}

console.log(answer.join("\n"));
