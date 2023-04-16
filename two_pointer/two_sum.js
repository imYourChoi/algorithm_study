// https://www.acmicpc.net/problem/3273

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = +input();
const nums = input()
  .split(" ")
  .map(e => +e)
  .sort((a, b) => a - b);
const x = +input();

if (n == 1) {
  console.log(0);
} else {
  let answer = 0;
  let left = 0;
  let right = n - 1;
  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum === x) {
      answer++;
      left++;
      right--;
    } else if (sum < x) {
      left++;
    } else {
      right--;
    }
  }
  console.log(answer);
}
