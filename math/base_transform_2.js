// https://www.acmicpc.net/problem/11005

const fs = require("fs");
// const [input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [input] = fs
  .readFileSync(__dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");

let [N, B] = input.split(" ").map((e) => +e);
let answer = [];
while (N) {
  const rest = N % B;
  if (rest >= 10) {
    answer.push(String.fromCharCode(rest + 55));
  } else {
    answer.push(rest);
  }
  N = Math.floor(N / B);
}
console.log(answer.reverse().join(""));
