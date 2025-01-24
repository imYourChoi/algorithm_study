// https://www.acmicpc.net/problem/1747

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
const length = 1003001 + 1;

const array = Array(length).fill(true);
array[1] = false;

function isPalindrome(n) {
  for (let i = Math.floor(n.length / 2); i < n.length; i++) {
    if (n[i] !== n[n.length - i - 1]) return false;
  }
  return true;
}

for (let i = 2; i < length; i++) {
  for (let j = i * 2; j < length; j += i) {
    array[j] = false;
  }
}

for (let i = N; i < length; i++) {
  if (array[i] && isPalindrome(String(i))) {
    console.log(i);
    break;
  }
}
