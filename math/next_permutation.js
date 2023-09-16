// https://www.acmicpc.net/problem/10972

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
const perm = input().split(" ").map(Number);

console.log(solve());

function solve() {
  for (let i = N - 1; i >= 0; i--) {
    if (perm[i - 1] < perm[i]) {
      for (let j = N - 1; j >= i; j--) {
        if (perm[i - 1] < perm[j]) {
          let temp = perm[j];
          perm[j] = perm[i - 1];
          perm[i - 1] = temp;
          return [...perm.slice(0, i), ...perm.slice(i).sort((a, b) => a - b)].join(" ");
        }
      }
    }
  }
  return -1;
}
