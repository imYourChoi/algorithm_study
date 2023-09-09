// https://www.acmicpc.net/problem/9372

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();
const arr = [];

for (let i = 0; i < T; i++) {
  const [a, _] = input().split(" ").map(Number);
  arr.push(a - 1);
  for (let j = 0; j < _; j++) input();
}
console.log(arr.join("\n"));
