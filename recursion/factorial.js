// https://www.acmicpc.net/problem/27433

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const factorial = (acc, num) => {
  if (num === 0 || num === 1) return 1 * acc;
  return factorial(acc * num, num - 1);
};

console.log(factorial(1, +input()));
