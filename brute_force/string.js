// https://www.acmicpc.net/problem/1120

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [A, B] = input().split(" ");

let shorter = A.length < B.length ? A : B;
let longer = shorter === A ? B : A;
let len = Math.min(A.length, B.length);

let answer = 50;
for (let i = 0; i <= Math.abs(A.length - B.length); i++) {
  let temp = 0;
  for (let j = 0; j < len; j++) {
    if (shorter[j] !== longer[i + j]) temp++;
  }
  answer = Math.min(answer, temp);
}

console.log(answer);
