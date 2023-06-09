// https://www.acmicpc.net/problem/11004

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
const Array = input()
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

console.log(Array[K - 1]);
