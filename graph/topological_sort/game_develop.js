// https://www.acmicpc.net/problem/1516

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

const times = Array.from({ length: N + 1 }, () => []);
const graph = Array.from({ length: N + 1 }, () => []);
const degrees = Array.from({ length: N + 1 }, () => 0);
const dp = Array.from({ length: N + 1 }, () => 0);

for (let i = 1; i <= N; i++) {
  const [time, ...nums] = input().split(" ").map(Number).slice(0, -1);

  times[i] = time;
  degrees[i] = nums.length;

  for (const num of nums) {
    graph[num].push(i);
  }
}

let queue = [];

for (let i = 1; i <= N; i++) {
  if (degrees[i] === 0) queue.push(i);
}

while (queue.length > 0) {
  const building = queue.shift();
  const dependents = graph[building];
  dp[building] += times[building];

  for (const dependent of dependents) {
    degrees[dependent]--;

    dp[dependent] = Math.max(dp[dependent], dp[building]);
    if (degrees[dependent] === 0) {
      queue.push(dependent);
    }
  }
}

console.log(dp.slice(1).join("\n"));
