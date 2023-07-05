// https://www.acmicpc.net/problem/14890

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, L] = input().split(" ").map(Number);
const map = Array.from({ length: N }, () => input().split(" ").map(Number));
let answer = 0;

for (let c = 0; c < N; c++) {
  let valid = check(c, "column");
  answer += valid;
  //   valid && console.log("###### column", c + 1, answer);
  //   !valid && console.log("###### column", c + 1, "invalid");
}

for (let r = 0; r < N; r++) {
  let valid = check(r, "row");
  answer += valid;
  //   valid && console.log("###### row", r + 1, answer);
  //   !valid && console.log("###### row", r + 1, "invalid");
}

function check(nth, dir) {
  let cur = map[dir === "column" ? 0 : nth][dir === "column" ? nth : 0];
  let slope = false;
  let downTemp = 0;
  let upTemp = 1;
  for (let i = 1; i < N; i++) {
    if (slope && map[dir === "column" ? i : nth][dir === "column" ? nth : i] !== cur) return 0;
    else if (slope && map[dir === "column" ? i : nth][dir === "column" ? nth : i] === cur) {
      downTemp++;
      if (downTemp === L) {
        slope = false;
        downTemp = 0;
        upTemp = 0;
      }
    } else if (cur - map[dir === "column" ? i : nth][dir === "column" ? nth : i] === 0) upTemp++;
    else if (Math.abs(cur - map[dir === "column" ? i : nth][dir === "column" ? nth : i]) > 1) return 0;
    else if (cur - 1 === map[dir === "column" ? i : nth][dir === "column" ? nth : i]) {
      cur = map[dir === "column" ? i : nth][dir === "column" ? nth : i];
      slope = true;
      downTemp = 1;
      upTemp = 0;
      if (downTemp === L) {
        slope = false;
        downTemp = 0;
        upTemp = 0;
      }
    } else if (cur + 1 === map[dir === "column" ? i : nth][dir === "column" ? nth : i]) {
      if (upTemp < L) return 0;
      cur = map[dir === "column" ? i : nth][dir === "column" ? nth : i];
      upTemp = 1;
    }
    // console.log(i, slope, downTemp, upTemp);
  }
  if (slope && downTemp < L) return 0;
  else return 1;
}

console.log(answer);
