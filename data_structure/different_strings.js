// https://www.acmicpc.net/problem/11478

const fs = require("fs");
// const [string] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [string] = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n");

const set = new Set();
for (let i = 0; i < string.length; i++) {
  for (let j = i + 1; j <= string.length; j++) {
    set.add(string.slice(i, j));
  }
}
console.log(set.size);
