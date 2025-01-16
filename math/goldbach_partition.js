// https://www.acmicpc.net/problem/17103

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

const limit = 1000001;

const primes = Array(limit).fill(true);
primes[0] = primes[1] = false;

for (let i = 2; i < limit; i++) {
  if (!primes[i]) continue;
  for (let j = i * 2; j < limit; j += i) {
    primes[j] = false;
  }
}

const primeSet = new Set(
  primes.reduce((acc, cur, idx) => {
    if (cur) acc.push(idx);
    return acc;
  }, [])
);

const answers = [];

for (let t = 0; t < T; t++) {
  const N = +input();
  let answer = 0;
  for (let num of primeSet) {
    if (num > N / 2) break;
    if (primeSet.has(N - num)) answer++;
  }
  answers.push(answer);
}

console.log(answers.join("\n"));
