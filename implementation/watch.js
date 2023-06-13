// https://www.acmicpc.net/problem/15683

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
const office = Array.from({ length: N }, () => input().split(" ").map(Number));

let blind = 0;
let cctvArr = office.reduce((acc, cur, idx) => {
  for (let i = 0; i < M; i++) {
    if (cur[i] == 0) blind++;
    if (cur[i] > 0 && cur[i] < 6) {
      acc.push([[idx, i], cur[i]]);
    }
  }
  return acc;
}, []);

function deepcopy(obj) {
  if (typeof obj !== "object" || obj === null) {
    return obj;
  }
  const result = [];
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      result[key] = deepcopy(obj[key]);
    }
  }
  return result;
}

const directions = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

function watch(office, direction, y, x) {
  let [dy, dx] = directions[direction];
  let count = 0;
  for (let Y = y + dy, X = x + dx; Y >= 0 && Y < N && X >= 0 && X < M; Y += dy, X += dx) {
    if (office[Y][X] === 0) {
      office[Y][X] = "#";
      count++;
    } else if (office[Y][X] === "#") continue;
    else if (office[Y][X] === 6) break;
  }
  return count;
}

function count_watch(office, direction, type, y, x) {
  let count = 0;
  switch (type) {
    case 1: {
      count += watch(office, direction, y, x);
      break;
    }
    case 2: {
      count += watch(office, direction, y, x);
      count += watch(office, (direction + 2) % 4, y, x);
      break;
    }
    case 3: {
      count += watch(office, direction, y, x);
      count += watch(office, (direction + 3) % 4, y, x);
      break;
    }
    case 4: {
      count += watch(office, direction, y, x);
      count += watch(office, (direction + 2) % 4, y, x);
      count += watch(office, (direction + 3) % 4, y, x);
      break;
    }
    case 5: {
      count += watch(office, direction, y, x);
      count += watch(office, (direction + 1) % 4, y, x);
      count += watch(office, (direction + 2) % 4, y, x);
      count += watch(office, (direction + 3) % 4, y, x);
      break;
    }
  }
  return count;
}

let answer = N * M;

function back_track(office, blind, cctvArr) {
  answer = Math.min(answer, blind);
  if (!cctvArr.length) return;
  let cctvArrCopy = cctvArr.slice();
  let [[y, x], cctv] = cctvArrCopy.splice(0, 1)[0];
  for (let d = 0; d < 4; d++) {
    let officeCopy = deepcopy(office);
    let count = count_watch(officeCopy, d, cctv, y, x);
    back_track(officeCopy, blind - count, cctvArrCopy);
  }
}

back_track(office, blind, cctvArr);

console.log(answer);
