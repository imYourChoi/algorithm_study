// https://www.acmicpc.net/problem/1021

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ");
let numbers = Array.from({ length: N }, (_, i) => i + 1);
const order = input()
  .split(" ")
  .map(e => +e);
answer = 0;
order.forEach(wanted => {
  if (numbers[0] === wanted) {
    numbers = numbers.slice(1);
  } else {
    let right = 1;
    let left = numbers.length - 1;
    let temp = 1;
    while (!(numbers[left] === wanted || numbers[right] === wanted)) {
      right = (right + 1) % numbers.length;
      left = (left - 1) % numbers.length;
      temp++;
    }
    answer += temp;
    let index = numbers[left] === wanted ? left : right;
    numbers = numbers.slice(index + 1).concat(numbers.slice(0, index));
  }
});

console.log(answer);
