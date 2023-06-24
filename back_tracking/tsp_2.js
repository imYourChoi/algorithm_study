// https://www.acmicpc.net/problem/10971

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
const costs = Array.from({ length: N }, () => input().split(" ").map(Number));
let visited = Array(N).fill(false);
let answer = Number.MAX_SAFE_INTEGER;

function dfs(start, end, sum, count) {
  if (count === N && costs[end][start]) {
    let newSum = sum + costs[end][start];
    if (answer > newSum) answer = newSum;
    return;
  }
  if (sum > answer) return;

  for (let i = 0; i < N; i++) {
    if (!visited[i] && costs[end][i]) {
      visited[i] = true;
      dfs(start, i, sum + costs[end][i], count + 1);
      visited[i] = false;
    }
  }
}

for (let i = 0; i < N; i++) {
  visited[i] = true;
  dfs(i, i, 0, 1);
  visited[i] = false;
}

console.log(answer);
