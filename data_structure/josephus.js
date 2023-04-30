// https://www.acmicpc.net/problem/1158

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
let arr = Array(N)
  .fill(undefined)
  .map((_, i) => i + 1);

let answer = [];
let index = 0;
while (arr.length) {
  index += K - 1;
  index %= arr.length;
  answer.push(arr[index]);
  arr.splice(index, 1);
}

console.log("<" + answer.join(", ") + ">");
