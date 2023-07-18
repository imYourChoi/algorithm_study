// https://www.acmicpc.net/problem/1244

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const switches = [0, ...input().split(" ").map(Number)];
const S = +input();

for (let i = 0; i < S; i++) {
  const [student, position] = input().split(" ").map(Number);
  if (student === 1) {
    for (let x = position; x <= N; x += position) {
      switches[x] = 1 - switches[x];
    }
  } else {
    let x = 1;
    switches[position] = 1 - switches[position];
    while (position + x <= N && position - x >= 1 && switches[position - x] === switches[position + x]) {
      switches[position + x] = 1 - switches[position + x];
      switches[position - x] = 1 - switches[position - x];
      x++;
    }
  }
}
switches.splice(0, 1);
for (let i = 0; i < N; i += 20) {
  console.log(switches.slice(i, Math.min(i + 20, N)).join(" "));
}
