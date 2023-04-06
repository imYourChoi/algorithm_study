// https://www.acmicpc.net/problem/1269

const fs = require("fs");
// const [n, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, first, second] = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n");

const firstSet = new Set(first.split(" "));
const secondSet = new Set(second.split(" "));

const symmetricSet = new Set([...firstSet].filter((x) => secondSet.has(x)));
console.log(firstSet.size + secondSet.size - 2 * symmetricSet.size);
