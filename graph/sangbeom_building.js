// https://www.acmicpc.net/problem/6593

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const directions = [
  [0, 1, 0],
  [1, 0, 0],
  [0, -1, 0],
  [-1, 0, 0],
  [0, 0, 1],
  [0, 0, -1],
];

const isValid = (x, y, z, C, R, L) => x >= 0 && x < C && y >= 0 && y < R && z >= 0 && z < L;

const answers = [];

const solve = (L, R, C) => {
  const building = Array.from({ length: L }, () => {
    return Array.from({ length: R + 1 }, () => input().split("")).slice(0, R);
  });

  const visited = Array.from({ length: L }, () => Array.from({ length: R }, () => Array(C).fill(false)));

  const start = (() => {
    for (let z = 0; z < L; z++) {
      for (let y = 0; y < R; y++) {
        for (let x = 0; x < C; x++) {
          if (building[z][y][x] === "S") return { x, y, z };
        }
      }
    }
  })();

  visited[start.z][start.y][start.x] = true;
  let queue = [[start.x, start.y, start.z]];

  let answer = 0;
  while (queue.length) {
    answer++;
    let temp = [];

    for (let [x, y, z] of queue) {
      for (let [dx, dy, dz] of directions) {
        const X = x + dx;
        const Y = y + dy;
        const Z = z + dz;

        if (!isValid(X, Y, Z, C, R, L) || visited[Z][Y][X] || building[Z][Y][X] === "#") continue;

        if (building[Z][Y][X] === "E") return answers.push(`Escaped in ${answer} minute(s).`);
        visited[Z][Y][X] = true;
        temp.push([X, Y, Z]);
      }
    }
    queue = temp;
  }
  answers.push("Trapped!");
};

while (true) {
  const [L, R, C] = input().split(" ").map(Number);
  if (L === 0) break;

  solve(L, R, C);
}

console.log(answers.join("\n"));
