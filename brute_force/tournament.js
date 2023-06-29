// https://www.acmicpc.net/problem/1057

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [N, kim, lim] = input().split(" ").map(Number);
let answer = 0;
while (kim !== lim) {
  kim = Math.floor((kim + 1) / 2);
  lim = Math.floor((lim + 1) / 2);
  answer++;
}
console.log(answer);
