// https://www.acmicpc.net/problem/17143
// https://velog.io/@sunkyuj/python-백준-17143-낚시왕

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [R, C, M] = input().split(" ").map(Number);
const sharks = Array.from({ length: M }, () => input().split(" ").map(Number));

let ocean = sharks.reduce((acc, cur) => {
  let [r, c, s, d, z] = cur;
  const nr = r - 1;
  const nc = c - 1;
  const shark = { r: nr, c: nc, s, d, z };
  if (nc in acc) acc[nc].push(shark);
  else acc[nc] = [shark];

  return acc;
}, {});

let answer = 0;

function catchShark(x) {
  ocean[x].sort((a, b) => b.r - a.r);
  answer += ocean[x].pop().z;
}

function getNextLocation(r, c, s, d) {
  let temp = s;
  if ([1, 2].includes(d)) {
    const cycle = R * 2 - 2;
    if (d === 1) temp += cycle - r;
    else temp += r;

    temp %= cycle;
    if (temp >= R) return [cycle - temp, c, 1];
    return [temp, c, 2];
  } else {
    const cycle = C * 2 - 2;
    if (d === 4) temp += cycle - c;
    else temp += c;

    temp %= cycle;
    if (temp >= C) return [r, cycle - temp, 4];
    return [r, temp, 3];
  }
}

function moveShark() {
  let temp = {};
  Object.values(ocean)
    .flat()
    .forEach(shark => {
      const [nr, nc, nd] = getNextLocation(shark.r, shark.c, shark.s, shark.d);
      const newShark = { r: nr, c: nc, s: shark.s, d: nd, z: shark.z };
      if (nc in temp) {
        const sameRowSharkIndex = temp[nc].findIndex(v => v.r === nr);
        if (sameRowSharkIndex > -1) {
          if (temp[nc][sameRowSharkIndex].z < newShark.z) temp[nc][sameRowSharkIndex] = newShark;
        } else temp[nc].push(newShark);
      } else temp[nc] = [newShark];
    });
  ocean = temp;
}

for (let x = 0; x < C; x++) {
  if (ocean[x]) catchShark(x);
  moveShark();
}

console.log(answer);
