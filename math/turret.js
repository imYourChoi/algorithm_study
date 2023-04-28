// https://www.acmicpc.net/problem/1002

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();

for (let i = 0; i < T; i++) {
  const [x1, y1, r1, x2, y2, r2] = input().split(" ").map(Number);
  const distance = Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
  if (distance === 0 && r1 === r2) console.log(-1);
  else if (Math.abs(r1 - r2) === distance || r1 + r2 === distance) console.log(1);
  else if (Math.abs(r1 - r2) < distance && distance < r1 + r2) console.log(2);
  else console.log(0);
}
