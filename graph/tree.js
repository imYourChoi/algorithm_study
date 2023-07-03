// https://www.acmicpc.net/problem/1068

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
const nodes = input().split(" ").map(Number);
const deleted = +input();

let children = Array.from({ length: N }, () => new Set());

for (let i = 0; i < N; i++) {
  if (nodes[i] < 0 || i == deleted) continue;
  children[nodes[i]].add(i);
}

const visited = Array(N).fill(false);
const root = nodes.indexOf(-1);
visited[deleted] = true;

let answer = 0;
function dfs(from) {
  if (visited[from]) return;
  if (!children[from].size) {
    answer++;
    return;
  }
  visited[from] = true;
  for (let node of children[from]) {
    if (visited[node]) continue;
    dfs(node);
  }
}

dfs(root);

console.log(answer);
