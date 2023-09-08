const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const M = +input();
const N = +input();

const arr = [];

for (let i = M; i <= N; i++) {
  let flag = false;
  if (i <= 1) continue;
  for (let j = 2; j < i; j++) {
    if (i % j === 0) {
      flag = true;
      break;
    }
  }
  if (!flag) arr.push(i);
}

if (arr.length) {
  console.log(arr.reduce((a, b) => a + b, 0));
  console.log(arr.reduce((a, b) => (a < b ? a : b), 100001));
} else console.log(-1);
