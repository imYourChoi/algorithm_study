// https://www.acmicpc.net/problem/1976

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const M = +input();

const graph = Array.from({ length: N }, () => input().split(" ").map(Number));
const plan = input().split(" ").map(Number);
const parent = Array(N)
  .fill(0)
  .map((_, i) => i);

function find(a) {
  if (parent[a] === a) return a;
  parent[a] = find(parent[a]);
  return parent[a];
}
function union(a, b, check = false) {
  const A = find(a);
  const B = find(b);
  if (A === B) return;
  if (A > B) parent[B] = A;
  else parent[A] = B;
}

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (graph[y][x] && parent[y] !== parent[x]) union(y, x);
  }
}

const set = new Set();
for (let i = 0; i < M; i++) {
  set.add(find(plan[i] - 1));
}

console.log(set.size === 1 ? "YES" : "NO");
