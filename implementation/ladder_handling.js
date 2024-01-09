// https://www.acmicpc.net/problem/15684

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, H] = input().split(" ").map(Number);
const ladders = Array.from({ length: H + 1 }, () => Array(N + 1).fill(0));

for (let i = 0; i < M; i++) {
  const [a, b] = input().split(" ").map(Number);
  ladders[a][b] = 1;
}

const check_line = n => {
  let x = n;
  let y = 1;
  while (y <= H) {
    if (x < N && ladders[y][x]) x++;
    else if (x > 1 && ladders[y][x - 1]) x--;
    y++;
  }
  return x === n ? true : false;
};

const check_all = () => {
  for (let n = 1; n <= N; n++) {
    if (!check_line(n)) return false;
  }
  return true;
};

const can_draw = (y, x) => {
  if (ladders[y][x]) return false;
  if (x > 1 && ladders[y][x - 1]) return false;
  if (x < N - 1 && ladders[y][x + 1]) return false;

  return true;
};

const back_track = (count, end, last) => {
  if (count === end) {
    if (check_all()) return process.exit(console.log(end));
  } else {
    for (let i = last; i < H * N; i++) {
      const y = Math.ceil(i / N);
      const x = i % N;
      if (!can_draw(y, x)) continue;
      ladders[y][x] = 1;
      back_track(count + 1, end, i + 2);
      ladders[y][x] = 0;
    }
  }
};

for (let i = 0; i <= 3; i++) {
  back_track(0, i, 1);
}
console.log(-1);
