const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [a, b, c] = input().split(" ").map(Number);
if (b >= c) console.log(-1);
else console.log(Math.floor(a / (c - b)) + 1);
