// https://www.acmicpc.net/problem/2170

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

const points = Array.from({ length: N }, () => input().split(" ").map(Number));
points.sort((a, b) => a[0] - b[0]);

let start = -1000000001;
let end = -1000000001;

let answer = 0;

for (let [x, y] of points) {
  if (end < x) {
    answer += end - start;

    start = x;
    end = y;
  } else if (end < y) {
    end = y;
  }
}
answer += end - start;

console.log(answer);
