// https://www.acmicpc.net/problem/2668

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

const nums = [0, ...Array.from({ length: N }, () => +input())];

let selected = [];
let visited;

const dfs = (current, start) => {
  visited[current] = true;
  const value = nums[current];
  if (!visited[value]) dfs(value, start);
  else if (visited[value] && value === start) selected.push(value);
};

for (let t = 1; t <= N; t++) {
  visited = Array(N + 1).fill(false);
  dfs(t, t);
}

selected.sort((a, b) => a - b);

console.log(selected.length);
console.log(selected.join("\n"));
