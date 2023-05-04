// https://www.acmicpc.net/problem/1011
// https://ooyoung.tistory.com/91

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();

for (let i = 0; i < T; i++) {
  const [x, y] = input().split(" ").map(Number);
  const dist = y - x;
  let count = 0;
  let move = 1;
  let moved = 0;
  while (moved < dist) {
    count++;
    moved += move;
    if (!(count % 2)) move += 1;
  }
  console.log(count);
}
