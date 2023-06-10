// https://www.acmicpc.net/problem/2004

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, m] = input().split(" ").map(Number);

function two_count(n) {
  let two = 0;
  while (n != 0) {
    n = Math.floor(n / 2);
    two += n;
  }
  return two;
}

function five_count(n) {
  let five = 0;
  while (n != 0) {
    n = Math.floor(n / 5);
    five += n;
  }
  return five;
}

console.log(
  Math.min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m))
);
