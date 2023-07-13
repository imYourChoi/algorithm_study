// https://www.acmicpc.net/problem/6588

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let primes = Array(1000001).fill(true);
primes[0] = primes[1] = false;

for (let i = 2; i < 1000001; i++) {
  if (!primes[i]) continue;
  for (let j = i * 2; j < 1000001; j += i) {
    primes[j] = false;
  }
}

primes = new Set(
  primes.reduce((acc, cur, idx) => {
    if (cur) acc.push(idx);
    return acc;
  }, [])
);

let answer = [];

while (true) {
  const n = +input();
  if (!n) break;

  for (let num of primes) {
    if (primes.has(n - num)) {
      answer.push(`${n} = ${num} + ${n - num}`);
      break;
    }
  }
}

console.log(answer.join("\n"));
