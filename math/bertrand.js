// https://www.acmicpc.net/problem/4948

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const arr = Array(246912 + 1).fill(true);
for (let i = 2; i <= 123456; i++) {
  if (!arr[i]) continue;
  for (let j = i * 2; j <= 246912; j += i) {
    arr[j] = false;
  }
}

let answer = [];

while (true) {
  const n = +input();
  if (!n) break;
  answer.push(arr.slice(n + 1, 2 * n + 1).reduce((acc, cur) => acc + cur, 0));
}

console.log(answer.join("\n"));
