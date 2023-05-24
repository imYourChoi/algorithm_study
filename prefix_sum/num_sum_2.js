// https://www.acmicpc.net/problem/2003

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
const array = input().split(" ").map(Number);
const accumulative = array.reduce(
  (acc, cur) => {
    acc.push(acc.at(-1) + cur);
    return acc;
  },
  [0]
);

let answer = 0;

for (let i = 0; i < N + 1; i++) {
  for (let j = 0; j < i; j++) {
    if (accumulative[i] - accumulative[j] === M) answer++;
  }
}

console.log(answer);
