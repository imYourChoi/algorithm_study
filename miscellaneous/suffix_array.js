// https://www.acmicpc.net/problem/11656

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const S = input();

const array = [S];
for (let i = 0; i < S.length - 1; i++) {
  array.push(array.at(-1).slice(1));
}
console.log(array.sort().join("\n"));
