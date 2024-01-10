// https://www.acmicpc.net/problem/11758

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [x1, y1] = input().split(" ").map(Number);
const [x2, y2] = input().split(" ").map(Number);
const [x3, y3] = input().split(" ").map(Number);

const external1 = x1 * y2 + x2 * y3 + x3 * y1;
const external2 = y1 * x2 + y2 * x3 + y3 * x1;

if (external1 > external2) console.log(1);
else if (external1 < external2) console.log(-1);
else console.log(0);
