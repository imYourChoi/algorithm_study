// https://www.acmicpc.net/problem/1748

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = +input();
let digit = N.toString().length - 1;
let answer = 0;

for (let i = 0; i < digit; i += 1) {
  answer += 9 * 10 ** i * (i + 1);
}
answer += (N - 10 ** digit + 1) * (digit + 1);

console.log(answer);
