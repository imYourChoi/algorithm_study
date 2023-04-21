// https://www.acmicpc.net/problem/17299

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
const nums = input()
  .split(" ")
  .map(e => +e);

const stack = [];
const answer = [];
const counts = nums.reduce((map, num) => {
  return map.set(num, map.has(num) ? map.get(num) + 1 : 1);
}, new Map());

for (let index in nums) {
  const count = counts.get(nums[index]);
  while (stack.length && counts.get(nums[stack.at(-1)]) < count) {
    answer[stack.pop()] = nums[index];
  }
  stack.push(index);
}

for (let index of stack) {
  answer[index] = -1;
}

console.log(...answer);
