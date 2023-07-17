// https://www.acmicpc.net/problem/13913

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

let queue = [N];
const visited = Array(100001).fill(false);
const move = Array(100001).fill(0);
visited[N] = true;

function isValid(point) {
  return point >= 0 && point <= 100000 && !visited[point];
}

function solve() {
  while (true) {
    let temp = [];
    while (queue.length) {
      let point = queue.pop();
      for (let next of [point + 1, point - 1, point * 2]) {
        if (isValid(next)) {
          move[next] = point;
          if (next === M) return;
          visited[next] = true;
          temp.push(next);
        }
      }
    }
    queue = temp;
  }
}

if (N === M) {
  console.log(0);
  console.log(N);
} else {
  solve();
  const answer = [M];
  let cur = M;
  while (cur !== N) {
    answer.push(move[cur]);
    cur = move[cur];
  }
  console.log(answer.length - 1);
  console.log(answer.reverse().join(" "));
}
