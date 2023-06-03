// https://www.acmicpc.net/problem/2512

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
  .map(Number)
  .sort((a, b) => a - b);
const budget = +input();

let start = 0,
  end = nums.reduce((a, b) => Math.max(a, b));

while (start <= end) {
  const mid = Math.floor((start + end) / 2);
  let total = 0;
  for (let num of nums) {
    if (num > mid) total += mid;
    else total += num;
  }
  if (total <= budget) start = mid + 1;
  else end = mid - 1;
}

console.log(end);
