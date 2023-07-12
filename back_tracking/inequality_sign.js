// https://www.acmicpc.net/problem/2529

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const k = +input();
const signs = input().split(" ");
let answer = [];

for (let i = 0; i < 10; i++) {
  back_track(
    [i],
    Array(10)
      .fill(0)
      .map((_, idx) => idx)
      .filter((_, idx) => idx !== i),
    1
  );
}

console.log(answer.at(-1));
console.log(answer[0]);

function check(array, index, comp) {
  if (signs[index - 1] === ">") return array.at(-1) > comp;
  else return array.at(-1) < comp;
}

function back_track(current, remain, index) {
  if (index === k) {
    for (let i = 0; i < remain.length; i++) {
      if (!check(current, index, remain[i])) continue;
      answer.push(current.join("") + remain[i]);
    }
    return;
  }
  for (let i = 0; i < remain.length; i++) {
    if (!check(current, index, remain[i])) continue;
    back_track(
      [...current, remain[i]],
      remain.filter((_, idx) => idx !== i),
      index + 1
    );
  }
}
