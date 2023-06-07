// https://www.acmicpc.net/problem/14891

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let wheels = Array.from({ length: 4 }, () => input().split("").map(Number));
const K = +input();
const rotations = Array.from({ length: K }, () => input().split(" ").map(Number));

function rotate(array, clockwise = 1) {
  if (clockwise === 1) array.unshift(array.pop());
  else array.push(array.shift());
}

// console.log(wheels.join("\n") + "\n");
for (let [number, direction] of rotations) {
  let rotation = [0, 0, 0, 0];
  rotation[number - 1] = direction;
  let temp = direction;
  for (let i = number - 2; i >= 0; i--) {
    temp *= -1;
    if (wheels[i][2] !== wheels[i + 1][6]) rotation[i] = temp;
    else break;
  }
  temp = direction;
  for (let i = number; i < 4; i++) {
    temp *= -1;
    if (wheels[i][6] !== wheels[i - 1][2]) rotation[i] = temp;
    else break;
  }
  for (let i = 0; i < 4; i++) {
    let rot = rotation[i];
    if (rot) rotate(wheels[i], rot);
  }
  //   console.log(wheels.join("\n") + "\n");
}

console.log(wheels.reduce((acc, cur, ind) => acc + cur[0] * 2 ** ind, 0));
