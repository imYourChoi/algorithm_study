// https://www.acmicpc.net/problem/2559

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K] = input().split(" ").map(Number);
const numbers = input().split(" ").map(Number);

let index = 0;
let temp = 0;
let answer = -Number.MAX_SAFE_INTEGER;
if (N == K) {
  answer = numbers.reduce((acc, cur) => acc + cur, 0);
} else {
  numbers.forEach(num => {
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
