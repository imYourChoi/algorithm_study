// https://www.acmicpc.net/problem/2559

const fs = require("fs");
// const [n, input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, input] = fs
  .readFileSync(__dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = n.split(" ").map((n) => +n);
const numbers = input.split(" ").map((n) => +n);

let index = 0;
let temp = 0;
let answer = -Number.MAX_SAFE_INTEGER;
if (N == K) {
  answer = numbers.reduce((acc, cur) => acc + cur, 0);
} else {
  numbers.forEach((num) => {
    temp += num;
    if (index == K - 1) answer = temp;
    else if (index >= K) {
      temp -= numbers[index - K];
      if (temp > answer) answer = temp;
    }
    index += 1;
  });
}
console.log(answer);
