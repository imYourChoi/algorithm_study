// https://www.acmicpc.net/problem/3036

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
const [first, ...rings] = input().split(" ").map(Number);
const answer = [];

function getGCD(a, b) {
  if (!b) return a;
  return getGCD(b, a % b);
}

for (let ring of rings) {
  let gcd = getGCD(first, ring);
  if (gcd === ring) answer.push(`${first / gcd}/1`);
  else if (gcd === 1) answer.push(`${first}/${ring}`);
  else answer.push(`${first / gcd}/${ring / gcd}`);
}

console.log(answer.join("\n"));
