// https://www.acmicpc.net/problem/2143

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();
const n = +input();
const A = input().split(" ").map(Number);
const m = +input();
const B = input().split(" ").map(Number);

let ASum = [];
let BSum = [];

let Atemp = 0;
let Btemp = 0;
for (let i = 0; i < n; i++) {
  for (let j = i; j < n; j++) {
    Atemp += A[j];
    ASum.push(Atemp);
  }
  Atemp = 0;
}
for (let i = 0; i < m; i++) {
  for (let j = i; j < m; j++) {
    Btemp += B[j];
    BSum.push(Btemp);
  }
  Btemp = 0;
}

ASum.sort((a, b) => a - b);
BSum.sort((a, b) => a - b);

const findIndex = (array, element) => {
  let left = 0;
  let right = array.length - 1;
  while (left < right) {
    const mid = Math.floor((right + left) / 2);
    if (array[mid] === element) right = mid;
    else if (array[mid] > element) right = mid - 1;
    else left = mid + 1;
  }
  if (array[left] !== element) return -1;
  return left;
};

const findLastIndex = (array, element) => {
  let left = 0;
  let right = array.length - 1;
  while (left < right) {
    const mid = Math.ceil((right + left) / 2);
    if (array[mid] === element) left = mid;
    else if (array[mid] > element) right = mid - 1;
    else left = mid + 1;
  }
  if (array[right] !== element) return -1;
  return right;
};

let answer = 0;

ASum.forEach(sum => {
  const left = findIndex(BSum, T - sum);
  const right = findLastIndex(BSum, T - sum);

  if (left !== -1) answer += right - left + 1;
});

console.log(answer);
