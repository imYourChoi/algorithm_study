// https://www.acmicpc.net/problem/5397

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
let answer = [];

for (let t = 0; t < T; t++) solve();

function solve() {
  let S = input();
  let leftStack = [];
  let rightStack = [];
  for (let char of S) {
    if (char === "<") {
      if (leftStack.length) {
        rightStack.push(leftStack.pop());
      }
    } else if (char === ">") {
      if (rightStack.length) {
        leftStack.push(rightStack.pop());
      }
    } else if (char === "-") {
      if (leftStack.length) leftStack.pop();
    } else {
      leftStack.push(char);
    }
  }
  rightStack.reverse();
  answer.push(leftStack.join("") + rightStack.join(""));
}

console.log(answer.join("\n"));
