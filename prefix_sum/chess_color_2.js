// https://www.acmicpc.net/problem/25682

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, K] = input().split(" ").map(Number);
const board = Array.from({ length: N }, () => input().split(""));
const accumulative = Array.from({ length: N }, () => Array(M).fill(0));

function check(y, x) {
  if ((y + x) % 2) return +(board[y][x] === "W");
  return +(board[y][x] === "B");
}

for (let y in board) {
  for (let x in board[y]) {
    y = +y;
    x = +x;
    if (!y && !x) accumulative[y][x] = check(y, x);
    else if (!y) accumulative[y][x] = accumulative[y][x - 1] + check(y, x);
    else if (!x) accumulative[y][x] = accumulative[y - 1][x] + check(y, x);
    else
      accumulative[y][x] = accumulative[y - 1][x] + accumulative[y][x - 1] - accumulative[y - 1][x - 1] + check(y, x);
  }
}
let answer = Number.MAX_SAFE_INTEGER;
for (let y = K - 1; y < N; y++) {
  for (let x = K - 1; x < M; x++) {
    if (!(y - K + 1) && !(x - K + 1))
      answer = Math.min(answer, Math.min(accumulative[y][x], K * K - accumulative[y][x]));
    else if (!(y - K + 1)) {
      let value = accumulative[y][x] - accumulative[y][x - K];
      answer = Math.min(answer, Math.min(value, K * K - value));
    } else if (!(x - K + 1)) {
      let value = accumulative[y][x] - accumulative[y - K][x];
      answer = Math.min(answer, Math.min(value, K * K - value));
    } else {
      let value = accumulative[y][x] - accumulative[y - K][x] - accumulative[y][x - K] + accumulative[y - K][x - K];
      answer = Math.min(answer, Math.min(value, K * K - value));
    }
  }
}

console.log(answer);
