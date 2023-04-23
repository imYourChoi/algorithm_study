// https://www.acmicpc.net/problem/3015

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
const people = Array.from({ length: N }, () => +input());
const stack = [];
let answer = 0;

for (let person of people) {
  while (stack.length && stack.at(-1)[0] < person) {
    answer += stack.pop()[1];
  }
  if (!stack.length) {
    stack.push([person, 1]);
    continue;
  }

  if (stack.at(-1)[0] === person) {
    let count = stack.pop()[1];
    answer += count;
    if (stack.length) answer += 1;
    stack.push([person, count + 1]);
  } else {
    stack.push([person, 1]);
    answer += 1;
  }
}

console.log(answer);
