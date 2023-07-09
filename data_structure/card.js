// https://www.acmicpc.net/problem/11652

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

const dict = new Map();

for (let i = 0; i < N; i++) {
  let num = BigInt(input());
  if (dict.has(num)) dict.set(num, dict.get(num) + 1);
  else dict.set(num, 1);
}

console.log(
  [...dict.entries()]
    .sort((a, b) => {
      if (a[1] === b[1]) return a[0] < b[0] ? -1 : 1;
      else return a[1] > b[1] ? -1 : 1;
    })[0][0]
    .toString()
);
