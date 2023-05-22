// https://www.acmicpc.net/problem/2644

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = +input();
const [a, b] = input().split(" ").map(Number);
const m = +input();
const graph = Array.from({ length: n + 1 }, () => []);

for (let i = 0; i < m; i++) {
  const [x, y] = input().split(" ").map(Number);
  graph[x].push(y);
  graph[y].push(x);
}

function bfs() {
  let answer = 0;
  const visited = Array(n + 1).fill(false);
  let queue = [a];
  visited[a] = true;
  while (queue.length) {
    answer++;
    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      const current = queue[i];
      for (let member of graph[current]) {
        if (visited[member]) continue;
        visited[member] = true;
        if (member === b) return answer;
        temp.push(member);
      }
    }
    queue = temp;
  }
  return -1;
}

console.log(bfs());
