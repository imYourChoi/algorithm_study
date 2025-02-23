// https://www.acmicpc.net/problem/17142

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

const institute = Array.from({ length: N }, () => input().split(" ").map(Number));

const viruses = [];
let spaces = 0;

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (institute[y][x] === 2) viruses.push([y, x]);
    if (institute[y][x] !== 1) spaces++;
  }
}

const getCombinations = (array, length) => {
  const result = [];

  const combine = (start, path) => {
    if (path.length === length) {
      result.push([...path]);
      return;
    }

    for (let i = start; i < array.length; i++) {
      path.push(i);
      combine(i + 1, path);
      path.pop();
    }
  };

  combine(0, []);
  return result;
};

const virusCombinations = getCombinations(viruses, M);

const directions = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const isValid = (y, x) => y >= 0 && y < N && x >= 0 && x < N;

const solve = combination => {
  let queue = combination.map(i => viruses[i]);
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  queue.forEach(([y, x]) => (visited[y][x] = true));

  let infected = viruses.length;
  let time = 0;

  while (queue.length && infected < spaces) {
    time++;

    let temp = [];
    for (let i = 0; i < queue.length; i++) {
      const [y, x] = queue[i];

      for (let [dy, dx] of directions) {
        const [ny, nx] = [y + dy, x + dx];

        if (!isValid(ny, nx) || visited[ny][nx] || institute[ny][nx] === 1) continue;
        visited[ny][nx] = true;
        if (institute[ny][nx] === 0) infected++;
        temp.push([ny, nx]);
      }
    }
    queue = temp;
  }

  if (infected === spaces) return time;
  return Infinity;
};

let answer = Infinity;

for (combination of virusCombinations) {
  answer = Math.min(solve(combination), answer);
}

console.log(answer === Infinity ? -1 : answer);
