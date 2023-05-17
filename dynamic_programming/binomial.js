// https://www.acmicpc.net/problem/11051

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [N, K] = input().split(" ").map(BigInt);

answer = 1n;

for (let i = 0n; i < K; i++) {
  answer = answer * N;
  N -= 1n;
}

divisor = 1n;
for (let i = 1n; i < K + 1n; i++) {
  divisor = divisor * i;
}

console.log(Number((answer / divisor) % 10007n));
