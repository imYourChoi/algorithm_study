// https://www.acmicpc.net/problem/1759

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [L, C] = input().split(" ").map(Number);
const letters = input().split(" ").sort();

const vowel = ["a", "e", "i", "o", "u"];
function isValid(arr) {
  if (arr.filter(val => vowel.includes(val)).length >= 1 && arr.filter(val => !vowel.includes(val)).length >= 2)
    return true;
  return false;
}

function backTrack(index, remain, arr = []) {
  if (!index) {
    if (isValid(arr)) {
      console.log(arr.join(""));
    } else {
      return;
    }
  }

  for (let i = 0; i < remain.length; i++) {
    backTrack(index - 1, remain.slice(i + 1), arr.concat(remain[i]));
  }
}

backTrack(L, letters);
