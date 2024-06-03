// https://www.acmicpc.net/problem/2981

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

const nums = Array.from({ length: N }, () => +input());
nums.sort((a, b) => a - b);

const diffs = Array.from({ length: N - 1 }, (_, i) => nums[i + 1] - nums[i]);

const get_gcd = (a, b) => {
  const R = a % b;
  if (R === 0) return b;
  return get_gcd(b, R);
};

let gcd = diffs[0];

for (let i = 1; i < N - 1; i++) gcd = get_gcd(gcd, diffs[i]);

const result = new Set([gcd]);
for (let i = 2; i < Math.floor(gcd ** 0.5) + 1; i++) {
  if (gcd % i === 0) {
    result.add(i);
    result.add(gcd / i);
  }
}

const answer = Array.from(result);
answer.sort((a, b) => a - b);

console.log(answer.join(" "));
