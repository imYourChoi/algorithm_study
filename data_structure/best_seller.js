// https://www.acmicpc.net/problem/1302

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
const map = new Map();

for (let i = 0; i < N; i++) {
  const book = input();
  if (map.has(book)) map.set(book, map.get(book) + 1);
  else map.set(book, 1);
}

console.log(
  Array.from(map.entries())
    .sort((a, b) => {
      if (a[1] !== b[1]) return a[1] - b[1];
      else return a[0] > b[0] ? -1 : 1;
    })
    .at(-1)[0]
);
