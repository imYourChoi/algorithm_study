// https://www.acmicpc.net/problem/13023

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
const relations = Array.from({ length: N }, () => new Set());
const visited = Array.from({ length: N }, () => false);

for (let i = 0; i < M; i++) {
  const [a, b] = input().split(" ").map(Number);
  relations[a].add(b);
  relations[b].add(a);
}

const back_track = current => {
  if (current.length === 5) return 1;

  const last = current.at(-1);
  let temp = 0;

  for (let friend of relations[last]) {
    if (visited[friend]) continue;
    visited[friend] = true;
    temp ||= back_track([...current, friend]);
    visited[friend] = false;
  }
  return temp;
};

let answer = 0;

for (let i = 0; i < N; i++) {
  visited[i] = true;
  answer ||= back_track([i]);
  visited[i] = false;
}

console.log(answer);
