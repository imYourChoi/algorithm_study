// https://www.acmicpc.net/problem/18352

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, K, X] = input().split(" ").map(Number);
const map = Array.from({ length: N + 1 }, () => new Set());

for (let i = 0; i < M; i++) {
  const [A, B] = input().split(" ").map(Number);
  map[A].add(B);
}

let visited = Array(N + 1).fill(false);
visited[X] = true;
let queue = [X];
let distance = 1;

while (queue.length) {
  let temp = [];
  for (city of queue) {
    for (dest of map[city]) {
      if (visited[dest]) continue;
      visited[dest] = true;
      temp.push(dest);
    }
  }
  queue = temp;
  if (distance === K) break;
  distance++;
}

if (queue.length) console.log(queue.sort((a, b) => a - b).join("\n"));
else console.log(-1);
