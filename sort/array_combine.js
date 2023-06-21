// https://www.acmicpc.net/problem/11728

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

input();
console.log([...input().split(" ").map(Number), ...input().split(" ").map(Number)].sort((a, b) => a - b).join(" "));
