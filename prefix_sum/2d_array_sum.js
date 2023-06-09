// https://www.acmicpc.net/problem/2167

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
const nums = Array.from({ length: N }, () => input().split(" ").map(Number));
const accumulative = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
const K = +input();
const cases = Array.from({ length: K }, () => input().split(" ").map(Number));

for (let y = 1; y <= N; y++) {
  for (let x = 1; x <= M; x++) {
    if (!y || !x) continue;
    else if (y === 1 && x === 1) accumulative[y][x] = nums[y - 1][x - 1];
    else if (y === 1) accumulative[y][x] = accumulative[y][x - 1] + nums[y - 1][x - 1];
    else if (x === 1) accumulative[y][x] = accumulative[y - 1][x] + nums[y - 1][x - 1];
    else
      accumulative[y][x] =
        accumulative[y][x - 1] + accumulative[y - 1][x] - accumulative[y - 1][x - 1] + nums[y - 1][x - 1];
  }
}

let answer = [];
for (let [i, j, x, y] of cases) {
  answer.push(accumulative[x][y] - accumulative[x][j - 1] - accumulative[i - 1][y] + accumulative[i - 1][j - 1]);
}

console.log(answer.join("\n"));
