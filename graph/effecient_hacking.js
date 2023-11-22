// https://www.acmicpc.net/problem/1325

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
const count = Array(N + 1).fill(0);

for (let i = 0; i < M; i++) {
  const [A, B] = input().split(" ").map(Number);
  graph[B].push(A);
}

for (let i = 1; i <= N; i++) {
  const visited = Array(N + 1).fill(false);
  count[i] = dfs(i, visited);
}

function dfs(node, visited) {
  visited[node] = true;
  let value = 1;
  for (let i = 0; i < graph[node].length; i++) {
    const neighbor = graph[node][i];
    if (!visited[neighbor]) {
      value += dfs(neighbor, visited);
    }
  }
  return value;
}

const max = Math.max(...count);
console.log(
  count
    .reduce((acc, cur, idx) => {
      if (cur === max) acc.push(idx);
      return acc;
    }, [])
    .join(" ")
);
