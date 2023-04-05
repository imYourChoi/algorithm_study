// https://www.acmicpc.net/problem/7785

const fs = require("fs");
// const [n, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, ...input] = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n");

const map = new Set();
for (let line of input) {
  const [name, status] = line.split(" ");
  if (status === "enter") {
    map.add(name);
  } else {
    map.delete(name);
  }
}

const sorted = [...map].sort().reverse();
console.log(sorted.join("\n"));
