// https://www.acmicpc.net/problem/2470

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const solutions = input()
  .split(" ")
  .map(e => +e)
  .sort((a, b) => a - b);

let start = 0,
  end = N - 1;
let answer = [solutions[start] + solutions[end], start, end];

while (start < end) {
  let [current] = answer;
  const sum = solutions[start] + solutions[end];
  if (Math.abs(sum) < Math.abs(current)) answer = [sum, start, end];

  if (sum > 0) end--;
  else if (sum < 0) start++;
  else break;
}

console.log(solutions[answer[1]], solutions[answer[2]]);
