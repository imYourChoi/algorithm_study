// https://www.acmicpc.net/problem/1016

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [min, max] = input().split(" ").map(Number);

let nums = Array(max - min + 1).fill(false);
let answer = max - min + 1;

const max_square = Math.floor(Math.sqrt(max));

let prime = Array(max_square + 1).fill(true);
const temp_sqrt = Math.ceil(Math.sqrt(max_square));

const check_prime = num => {
  for (let j = 2; j < num; j++) if (num % j === 0) return false;
  return true;
};

prime[0] = false;
prime[1] = false;
for (let i = 2; i <= temp_sqrt; i++) {
  if (!prime[i]) continue;
  if (check_prime(i)) for (let k = 2 * i; k <= max_square; k += i) prime[k] = false;
}

const primes_list = [];

prime.forEach((v, i) => v && primes_list.push(i * i));

primes_list.forEach(v => {
  let start_min = min;
  if (start_min % v !== 0) {
    start_min = Math.ceil(start_min / v) * v;
  }

  for (let i = start_min; i <= max; i += v) {
    if (!nums[i - min]) {
      nums[i - min] = true;
      answer--;
    }
  }
});

console.log(answer);
