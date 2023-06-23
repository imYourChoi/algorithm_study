// https://www.acmicpc.net/problem/17413

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const S = input().split("");
const answer = [];
let stack = [];
let tag = false;
for (let letter of S) {
  if (letter === "<") {
    if (stack.length) {
      answer.push(stack.reverse().join(""));
      stack = [];
    }
    tag = true;
    stack.push("<");
  } else if (letter === ">") {
    stack.push(">");
    answer.push(stack.join(""));
    stack = [];
    tag = false;
  } else if (letter === " ") {
    if (tag) {
      stack.push(letter);
    } else {
      answer.push(stack.reverse().join("") + " ");
      stack = [];
    }
  } else {
    stack.push(letter);
  }
}

if (stack.length) answer.push(stack.reverse().join(""));

console.log(answer.join(""));
