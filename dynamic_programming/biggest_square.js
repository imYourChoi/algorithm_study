// https://www.acmicpc.net/problem/1915

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++].trim();
})();

const [n, m] = input().split(" ").map(Number);
const list = Array.from({ length: n }, () => input().split("").map(Number));

for (let y = 1; y < n; y++) {
  for (let x = 1; x < m; x++) {
    if (!list[y][x]) continue;
    list[y][x] = Math.min(list[y - 1][x - 1], list[y][x - 1], list[y - 1][x]) + 1;
  }
}

let answer = Math.max(...list.flat());
console.log(answer ** 2);
