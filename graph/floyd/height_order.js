// https://www.acmicpc.net/problem/2458

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
const distances = Array.from({ length: N + 1 }, () => Array(N + 1).fill(false));

for (let i = 0; i < M; i++) {
  const [a, b] = input().split(" ").map(Number);
  distances[a][b] = true;
}

for (let via = 1; via < N + 1; via++) {
  for (let start = 1; start < N + 1; start++) {
    for (let end = 1; end < N + 1; end++) {
      if (start === end) distances[start][end] = false;
      else distances[start][end] ||= distances[start][via] && distances[via][end];
    }
  }
}

let answer = 0;
for (let i = 1; i < N + 1; i++) {
  const higher = distances[i].filter(_ => _).length;
  const lower = distances.reduce((prev, curr) => {
    return prev + curr[i];
  }, 0);

  if (higher + lower === N - 1) answer++;
}

console.log(answer);
