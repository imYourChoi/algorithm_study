// https://www.acmicpc.net/problem/11559

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const field = Array.from({ length: 12 }, () => input().split(""));

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const isValid = (y, x) => y >= 0 && y < 12 && x >= 0 && x < 6;

const find_puyo = (y, x) => {
  let queue = [[y, x]];
  let puyo_count = 1;
  const aggregate = [[y, x]];

  const visited = Array.from({ length: 12 }, () => Array(6).fill(false));
  visited[y][x] = true;

  while (queue.length) {
    let temp = [];
    for ([ny, nx] of queue) {
      for ([dy, dx] of directions) {
        let Y = ny + dy;
        let X = nx + dx;
        if (!isValid(Y, X) || visited[Y][X]) continue;
        visited[Y][X] = true;
        if (field[Y][X] === field[y][x] && field[Y][X] !== ".") {
          temp.push([Y, X]);
          aggregate.push([Y, X]);
          puyo_count += 1;
        }
      }
    }
    queue = temp;
  }

  return { is_puyo: puyo_count >= 4, aggregate };
};

const clean_puyo = aggregate => {
  for ([py, px] of aggregate) field[py][px] = ".";
};

const drop_puyo = () => {
  for (let x = 0; x < 6; x++) {
    for (let y = 11; y > 0; y--) {
      if (field[y][x] === "." && field[y - 1][x] !== ".") {
        for (let ty = y; ty < 12; ty++) {
          if (field[ty][x] !== ".") break;
          field[ty][x] = field[ty - 1][x];
          field[ty - 1][x] = ".";
        }
      }
    }
  }
};

const solution = () => {
  let answer = 0;
  while (true) {
    let flag = false;
    for (let y = 0; y < 12; y++) {
      for (let x = 0; x < 6; x++) {
        if (field[y][x] === ".") continue;

        const { is_puyo, aggregate } = find_puyo(y, x);
        if (is_puyo) {
          clean_puyo(aggregate);
          flag = true;
        }
      }
    }
    if (flag) answer++;
    else return answer;

    drop_puyo();
  }
};

console.log(solution());
