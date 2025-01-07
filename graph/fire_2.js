// https://www.acmicpc.net/problem/5427

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
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const T = +input();

function isValid(y, x, w, h) {
  return y >= 0 && y < h && x >= 0 && x < w;
}

function dfs(initF, initS, building, w, h) {
  let answer = 1;
  let queueS = initS;
  let queueF = initF;

  while (queueS.length) {
    answer++;

    const tempS = [];
    const tempF = [];

    for (let i = 0; i < queueF.length; i++) {
      const [y, x] = queueF[i];

      for (let [dy, dx] of directions) {
        const ny = y + dy;
        const nx = x + dx;
        if (!isValid(ny, nx, w, h) || ["#", "*"].includes(building[ny][nx])) continue;

        building[ny][nx] = "*";
        tempF.push([ny, nx]);
      }
    }

    for (let i = 0; i < queueS.length; i++) {
      const [y, x] = queueS[i];

      for (let [dy, dx] of directions) {
        const ny = y + dy;
        const nx = x + dx;
        if (!isValid(ny, nx, w, h) || building[ny][nx] !== ".") continue;

        if (ny === 0 || ny === h - 1 || nx === 0 || nx === w - 1) return answer;
        building[ny][nx] = "@";
        tempS.push([ny, nx]);
      }
    }

    queueF = tempF;
    queueS = tempS;
  }

  return "IMPOSSIBLE";
}

function solve() {
  const [w, h] = input().split(" ").map(Number);
  const building = Array.from({ length: h }, () => input().split(""));

  let initS = [];
  let initF = [];

  building.forEach((row, y) => {
    row.forEach((space, x) => {
      if (space === "@") initS.push([y, x]);
      if (space === "*") initF.push([y, x]);
    });
  });

  if (initS[0][0] === 0 || initS[0][0] === h - 1 || initS[0][1] === 0 || initS[0][1] === w - 1) return console.log(1);
  console.log(dfs(initF, initS, building, w, h));
}

for (let t = 0; t < T; t++) solve();
