// https://www.acmicpc.net/problem/10986

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
const numbers = input().split(" ").map(Number);

let total = 0;
const accumulative = numbers.reduce(
  (acc, num) => {
    total += num;
    const remainder = total % M;
    acc[remainder] = acc[remainder] ? acc[remainder] + 1 : 1;
    return acc;
  },
  [1]
);

let answer = 0;

for (let remainder of accumulative) {
  answer += remainder ? (remainder * (remainder - 1)) / 2 : 0;
}

console.log(answer);
