// https://www.acmicpc.net/problem/1717

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
const parent = Array(N)
  .fill(0)
  .map((_, i) => i);

function find(a) {
  if (parent[a] === a) return a;
  return (parent[a] = find(parent[a]));
}
function union(a, b) {
  const A = find(a);
  const B = find(b);

  if (A > B) parent[B] = A;
  else parent[A] = B;
}

for (let i = 0; i < M; i++) {
  const [op, a, b] = input().split(" ").map(Number);
  if (op === 1) {
    console.log(find(a) == find(b) ? "YES" : "NO");
  } else {
    union(a, b);
  }
}
