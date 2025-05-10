// https://www.acmicpc.net/problem/2812

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
const number = input();

const stack = [];
let removedCount = 0;

for (let _char of number) {
  const char = Number(_char);

  while (stack.at(-1) < char && removedCount < K) {
    stack.pop();
    removedCount++;
  }

  stack.push(char);
}

console.log(stack.slice(0, N - K).join(""));
