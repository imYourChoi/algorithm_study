// https://www.acmicpc.net/problem/17298

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = input();
const nums = input()
  .split(" ")
  .map((e, i) => [+e, i]);

const stack = [];
const answer = [];

for (let [num, index] of nums) {
  while (stack.length && stack.at(-1)[0] < num) {
    const [_, popIndex] = stack.pop();
    answer[popIndex] = num;
  }
  stack.push([num, index]);
}

for (let [_, index] of stack) {
  answer[index] = -1;
}

console.log(...answer);
