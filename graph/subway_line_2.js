// https://www.acmicpc.net/problem/16947

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
const graph = Array.from({ length: N + 1 }, () => []);
const cycles = Array(N + 1).fill(false);
const answer = Array(N + 1).fill(-1);

for (let i = 0; i < N; i++) {
  const [a, b] = input().split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

function detect_cycle(start, index, count, visited, isCycle) {
  if (start === index && count >= 2) {
    isCycle[0] = true;
    return;
  }
  visited[index] = true;
  for (let i of graph[index]) {
    if (!visited[i]) {
      detect_cycle(start, i, count + 1, visited, isCycle);
    } else if (start === i && count >= 2) {
      detect_cycle(start, i, count, visited, isCycle);
    }
  }
}

function calculate_distance() {
  let queue = [];
  for (let i = 1; i < N + 1; i++) {
    if (cycles[i]) {
      answer[i] = 0;
      queue.push(i);
    }
  }

  while (queue.length) {
    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      const current = queue[i];
      for (let station of graph[current]) {
        if (answer[station] === -1) {
          temp.push(station);
          answer[station] = answer[current] + 1;
        }
      }
    }
    queue = temp;
  }

  console.log(answer.slice(1).join(" "));
}

for (let i = 1; i < N + 1; i++) {
  const visited = Array(N + 1).fill(false);
  let isCycle = [false];
  detect_cycle(i, i, 0, visited, isCycle);
  if (isCycle[0]) cycles[i] = true;
}

calculate_distance();
