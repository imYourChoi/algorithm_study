// https://www.acmicpc.net/problem/1644

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

const nums = [false, false].concat(Array(N - 1).fill(true));
const primes = [];

for (let i = 2; i <= N; i++) {
  if (nums[i]) {
    primes.push(i);
    for (let j = i * 2; j <= N; j += i) {
      nums[j] = false;
    }
  }
}

let answer = 0,
  start = 0,
  end = 0;

while (end <= primes.length) {
  const temp = primes.slice(start, end).reduce((acc, cur) => acc + cur, 0);
  if (temp === N) {
    answer++;
    end++;
  } else if (temp < N) {
    end++;
  } else {
    start++;
  }
}

console.log(answer);
