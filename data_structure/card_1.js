// https://www.acmicpc.net/problem/2161

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
const arr = Array.from({ length: N }, (_, i) => i + 1);
const answer = [];

while (arr.length > 1) {
  answer.push(arr.shift());
  arr.push(arr.shift());
}
answer.push(arr.shift());

console.log(...answer);
