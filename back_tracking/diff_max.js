// https://www.acmicpc.net/problem/10819

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
const nums = input().split(" ").map(Number);
let answer = 0;

function back_track(index, remain, array = []) {
  if (index === N) {
    answer = Math.max(
      answer,
      array.reduce((acc, cur, idx, arr) => {
        if (idx === 0) return 0;
        return acc + Math.abs(arr[idx] - arr[idx - 1]);
      }, 0)
    );
    return;
  }
  for (let i = 0; i < remain.length; i++) {
    back_track(
      index + 1,
      remain.filter((_, idx) => idx != i),
      array.concat(remain[i])
    );
  }
}

back_track(0, nums);

console.log(answer);
