// https://www.acmicpc.net/problem/1004

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();
let answer = [];

function solve() {
  const [x1, y1, x2, y2] = input().split(" ").map(Number);
  const n = +input();
  const planets = Array.from({ length: n }, () => input().split(" ").map(Number));
  let count = 0;
  for (let [cx, cy, r] of planets) {
    const d1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5;
    const d2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5;
    if (!((d1 < r && d2 < r) || (d1 > r && d2 > r))) count++;
  }
  answer.push(count);
}

for (let t = 0; t < T; t++) solve();

console.log(answer.join("\n"));
