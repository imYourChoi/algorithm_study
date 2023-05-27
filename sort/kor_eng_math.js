// https://www.acmicpc.net/problem/10825

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
const students = Array.from({ length: N }, () =>
  input()
    .split(" ")
    .map((x, i) => {
      if (i > 0) return Number(x);
      else return x;
    })
);

console.log(
  students
    .sort((a, b) => {
      if (a[1] !== b[1]) return b[1] - a[1];
      if (a[2] !== b[2]) return a[2] - b[2];
      if (a[3] !== b[3]) return b[3] - a[3];

      return a[0] > b[0] ? 1 : -1;
    })
    .map(a => a[0])
    .join("\n")
);
