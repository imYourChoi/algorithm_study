// https://www.acmicpc.net/problem/1725

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
const heights = Array.from({ length: N }, () => +input());
let answer = 0;
let stack = [];

for (let index in heights) {
  const height = heights[index];
  let temp;
  while (stack.length && stack.at(-1)[1] > height) {
    const [curIndex, curHeight] = stack.pop();
    const area = (index - curIndex) * curHeight;
    answer = Math.max(area, answer);
    temp = [curIndex, height];
  }
  if (temp) stack.push(temp);
  stack.push([index, height]);
}

while (stack.length) {
  const [curIndex, curHeight] = stack.pop();
  const area = (N - curIndex) * curHeight;
  answer = Math.max(area, answer);
}

console.log(answer);
