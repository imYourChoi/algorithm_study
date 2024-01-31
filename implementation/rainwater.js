// https://www.acmicpc.net/problem/14719

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [_, W] = input().split(" ").map(Number);
const blocks = input().split(" ").map(Number);

const left = Array(W).fill(0);
const right = Array(W).fill(0);

let max = 0;
for (let i = 0; i < W; i++) {
  let block = blocks[i];
  left[i] = max = Math.max(max, block);
}

max = 0;
for (let i = W - 1; i >= 0; i--) {
  let block = blocks[i];
  right[i] = max = Math.max(max, block);
}

let answer = 0;
for (let i = 0; i < W; i++) answer += Math.min(left[i], right[i]) - blocks[i];

console.log(answer);
