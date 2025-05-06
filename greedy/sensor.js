// https://www.acmicpc.net/problem/2212

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

const sensors = input().split(" ").map(Number);
sensors.sort((a, b) => a - b);

const distances = [];
for (let i = 1; i < N; i++) {
  distances.push(sensors[i] - sensors[i - 1]);
}

distances.sort((a, b) => a - b);

console.log(distances.slice(0, N - K).reduce((a, b) => a + b, 0));
