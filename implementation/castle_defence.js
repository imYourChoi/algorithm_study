// https://www.acmicpc.net/problem/17135

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, D] = input().split(" ").map(Number);

const board = Array.from({ length: N }, () => input().split(" ").map(Number));

const directions = [
  [0, -1],
  [-1, 0],
  [0, 1],
];

const isValid = (y, x, Y, X) => y >= 0 && y < Y && x >= 0 && x < X;

const findEnermy = (Y, X, copyBoard) => {
  const visited = Array.from({ length: Y }, () => Array(M).fill(false));
  let queue = [[Y, X]];

  let distance = 1;
  while (queue.length > 0 && distance <= D) {
    const temp = [];

    for (let [y, x] of queue) {
      for (let [dy, dx] of directions) {
        const nY = y + dy;
        const nX = x + dx;

        if (!isValid(nY, nX, Y, M) || visited[nY][nX]) continue;

        if (copyBoard[nY][nX] === 1) return [nY, nX];

        visited[nY][nX] = true;
        temp.push([nY, nX]);
      }
    }
    queue = temp;
    distance++;
  }

  return null;
};

const getCombinations = c => {
  const result = [];

  const backTrack = (start, arr) => {
    if (arr.length === 3) return result.push([...arr]);
    for (let i = start; i < c; i++) {
      arr.push(i);
      backTrack(i + 1, arr);
      arr.pop();
    }
  };

  backTrack(0, []);
  return result;
};

const combinations = getCombinations(M);

let answer = 0;

for (const combination of combinations) {
  const copyBoard = board.map(v => [...v]);

  let temp = 0;
  for (let y = N; y > 0; y--) {
    let defeateds = [];
    for (let x of combination) {
      const enermy = findEnermy(y, x, copyBoard);
      if (enermy) defeateds.push(enermy);
    }
    for (const [dy, dx] of defeateds) {
      if (copyBoard[dy][dx] === 1) {
        temp += 1;
        copyBoard[dy][dx] = 0;
      }
    }
  }

  answer = Math.max(answer, temp);
}

console.log(answer);
