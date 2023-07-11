// https://www.acmicpc.net/problem/1735

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [A, B] = input().split(" ").map(Number);
const [C, D] = input().split(" ").map(Number);

const N = gcd(A * D + B * C, B * D);
console.log((A * D + C * B) / N, (B * D) / N);

function gcd(x, y) {
  let mod = x % y;
  while (mod > 0) {
    x = y;
    y = mod;
    mod = x % y;
  }
  return y;
}
