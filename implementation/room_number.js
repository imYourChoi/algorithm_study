// https://www.acmicpc.net/problem/1475

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const num = input();
const arr = Array(10).fill(0);

for (let char of num) {
  arr[+char] += 1;
}

console.log(
  Math.max(
    Math.ceil((arr.splice(9, 1)[0] + arr.splice(6, 1)[0]) / 2),
    arr.reduce((acc, cur) => Math.max(acc, cur))
  )
);
