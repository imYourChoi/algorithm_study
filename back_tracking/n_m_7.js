// https://www.acmicpc.net/problem/15656

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let answer = [];

const [N, M] = input().split(" ").map(Number);
const array = input()
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

function back_track(index, remain, current = []) {
  if (index === 0) {
    answer.push(current.join(" "));
    return;
  }
  for (let elem of remain) back_track(index - 1, remain, [...current, elem]);
}

back_track(M, array);
console.log(answer.join("\n"));
