// https://www.acmicpc.net/problem/5014

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [F, S, G, U, D] = input().split(" ").map(Number);

const array = Array(F + 1).fill(0);
const visited = Array(F + 1).fill(false);
visited[S] = true;

let queue = [S];

while (queue.length) {
  let temp = [];
  for (let i = 0; i < queue.length; i++) {
    const cur = queue[i];
    const up = cur + U;
    const down = cur - D;
    if (up <= F && !visited[up]) {
      visited[up] = true;
      array[up] = array[cur] + 1;
      temp.push(up);
    }
    if (down >= 1 && !visited[down]) {
      visited[down] = true;
      array[down] = array[cur] + 1;
      temp.push(down);
    }
  }
  queue = temp;
}

console.log(S === G ? 0 : array[G] || "use the stairs");
