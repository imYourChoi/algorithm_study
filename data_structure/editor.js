// https://www.acmicpc.net/problem/1406

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const text = input();
const M = +input();
const left = [...text];
const right = [];

for (let i = 0; i < M; i++) {
  const [com, ...letter] = input().split(" ");
  switch (com) {
    case "L": {
      let popped = left.pop();
      if (popped) right.push(popped);
      break;
    }
    case "D": {
      let popped = right.pop();
      if (popped) left.push(popped);
      break;
    }
    case "B": {
      if (left.length) left.pop();
      break;
    }
    case "P": {
      left.push(letter[0]);
      break;
    }
  }
}

console.log(left.join("") + right.reverse().join(""));
