// https://www.acmicpc.net/problem/2960

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K] = input().split(" ").map(Number);
const nums = Array(N + 1)
  .fill(0)
  .map((_, i) => i);

let count = 0;
function solve() {
  for (let i = 2; i <= N; i++) {
    for (let v = i; v <= N; v += i) {
      if (nums[v]) {
        nums[v] = 0;
        count += 1;
        if (count === K) return v;
      }
    }
  }
}

console.log(solve());
