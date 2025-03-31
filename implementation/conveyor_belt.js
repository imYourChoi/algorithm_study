// https://www.acmicpc.net/problem/20055

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K] = input().split(" ").map(Number);
const durability = input().split(" ").map(Number);

const lastIndex = 2 * N - 1;
let left = 0;
let right = N - 1;
let robotStays = Array(N * 2).fill(false);

const getNextIndex = i => {
  if (i === lastIndex) return 0;
  else return i + 1;
};

const solve = () => {
  let zeroCount = 0;
  let answer = 0;

  while (zeroCount < K) {
    answer += 1;

    // 1
    left = (left - 1 + 2 * N) % (2 * N);
    right = (right - 1 + 2 * N) % (2 * N);
    robotStays[right] = false;

    // 2

    let index = right === 0 ? lastIndex : right - 1;
    while (index !== left) {
      const nextIndex = getNextIndex(index);
      if (robotStays[index] && !robotStays[nextIndex] && durability[nextIndex] > 0) {
        robotStays[index] = false;
        if (nextIndex !== right) robotStays[nextIndex] = true;
        durability[nextIndex] -= 1;
        if (durability[nextIndex] === 0) zeroCount += 1;
      }

      if (index > 0) index -= 1;
      else index = lastIndex;
    }

    // 3
    if (durability[left] > 0) {
      robotStays[left] = true;
      durability[left] -= 1;
      if (durability[left] === 0) zeroCount += 1;
    }

    // 4
  }
  return answer;
};

console.log(solve());
