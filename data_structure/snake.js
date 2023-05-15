// https://www.acmicpc.net/problem/3190

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
const K = +input();
let apples = Array.from({ length: K }, () => input().split(" ").map(Number));
const L = +input();
let rotateInfo = Array.from({ length: L }, () => input().split(" ")).map(info => {
  info[0] = +info[0];
  return info;
});
let second = 0;

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
let curDirection = 0;
const paths = [[1, 1]];

function isWall(y, x) {
  return !(y >= 1 && y <= N && x >= 1 && x <= N);
}
function isSelf(y, x) {
  return !!paths.find(path => path[0] === y && path[1] === x);
}
function rotate(direction) {
  if (direction === "L") curDirection = (curDirection - 1 + 4) % 4;
  else if (direction === "D") curDirection = (curDirection + 1 + 4) % 4;
}
function eatApple(y, x) {
  paths.push([y, x]);
}
function noApple(y, x) {
  paths.splice(0, 1);
  paths.push([y, x]);
}

while (true) {
  if (rotateInfo.length && second === rotateInfo[0][0]) {
    rotate(rotateInfo[0][1]);
    rotateInfo.splice(0, 1);
  }
  second++;
  const [dy, dx] = directions[curDirection];
  const [y, x] = paths.at(-1);
  const [Y, X] = [y + dy, x + dx];
  if (isWall(Y, X) || isSelf(Y, X)) break;
  if (apples.find(apple => apple[0] === Y && apple[1] === X)) {
    eatApple(Y, X);
    apples = apples.filter(apple => !(apple[0] === Y && apple[1] === X));
  } else {
    noApple(Y, X);
  }
}

console.log(second);
