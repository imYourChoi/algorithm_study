// https://www.acmicpc.net/problem/20920

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ");
const words = Array.from({ length: N }, () => input());
const map = new Map();

for (let word of words) {
  if (word.length < M) continue;
  if (map.has(word)) {
    map.set(word, map.get(word) + 1);
  } else {
    map.set(word, 1);
  }
}

console.log(
  Array.from(map.entries())
    .sort((a, b) => {
      if (a[1] !== b[1]) {
        return b[1] - a[1];
      } else if (a[0].length !== b[0].length) {
        return b[0].length - a[0].length;
      } else {
        return a[0].localeCompare(b[0]);
      }
    })
    .map(a => a[0])
    .join("\n")
);
