// https://www.acmicpc.net/problem/9020

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
let primes = Array(10001).fill(true);
primes[0] = primes[1] = false;

for (let i = 2; i <= 10000; i++) {
  if (!primes[i]) continue;
  for (let j = i * 2; j <= 10000; j += i) {
    primes[j] = false;
  }
}

primes = new Set(
  primes.reduce((acc, cur, idx) => {
    if (cur) acc.push(idx);
    return acc;
  }, [])
);

for (let i = 0; i < T; i++) {
  const n = +input();
  small = n / 2;
  big = n / 2;
  while (!(primes.has(small) && primes.has(big))) {
    small -= 1;
    big += 1;
  }
  console.log(small, big);
}
