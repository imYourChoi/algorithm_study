// https://www.acmicpc.net/problem/10867

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
const numbers = new Set(input().split(" ").map(Number));

console.log([...numbers].sort((a, b) => a - b).join(" "));
