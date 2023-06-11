// https://www.acmicpc.net/problem/15655

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
  for (let i = 0; i < remain.length; i++) {
    let copy = remain.slice();
    let [elem] = copy.splice(i, 1);
    if (elem > (current.at(-1) ?? 0)) back_track(index - 1, copy, [...current, elem]);
  }
}

back_track(M, array);
console.log(answer.join("\n"));
