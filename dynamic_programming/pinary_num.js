// https://www.acmicpc.net/problem/2193

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
const arr = Array.from({ length: N }, () => [0n, 0n]);
arr[0][1] = 1n;
if (N > 1) arr[1][0] = 1n;

for (let i = 2; i < N; i++) {
  arr[i][0] = arr[i - 1][0] + arr[i - 1][1];
  arr[i][1] = arr[i - 1][0];
}

console.log((arr.at(-1)[0] + arr.at(-1)[1]).toString());
