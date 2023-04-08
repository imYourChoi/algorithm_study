// https://www.acmicpc.net/problem/25192

const fs = require("fs");
// const [n, enter, ...lines] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, enter, ...lines] = fs
  .readFileSync(__dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");

const set = new Set();
let answer = 0;
for (let line of lines) {
  if (line === "ENTER") {
    set.clear();
    continue;
  } else if (set.has(line)) {
    continue;
  } else {
    set.add(line);
    answer++;
  }
}

console.log(answer);
