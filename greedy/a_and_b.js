// https://www.acmicpc.net/problem/12904

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
let T = input();

let answer = false;

while (T.length > S.length) {
  if (T.at(-1) === "A") T = T.slice(0, -1);
  else if (T.at(-1) === "B") T = T.slice(0, -1).split("").reverse().join("");

  if (T === S) {
    answer = true;
    break;
  }
}

console.log(answer ? 1 : 0);
