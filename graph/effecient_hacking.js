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
const graph = Array.from({ length: N + 1 }, () => new Set());
const count = Array(N + 1).fill(0);

for (let i = 0; i < M; i++) {
  const [A, B] = input().split(" ").map(Number);
  graph[B].add(A);
}

for (let i = 1; i <= N; i++) {
  count[i] = bfs(i);
}

function bfs(node) {
  const visited = Array(N + 1).fill(false);
  visited[node] = true;
  let value = 1;
  let queue = [node];
  while (queue.length) {
    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      let current = queue[i];
      for (let computer of graph[current]) {
        if (visited[computer]) continue;
        visited[computer] = true;
        value += 1;
        temp.push(computer);
      }
    }
    queue = temp;
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
