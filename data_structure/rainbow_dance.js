// https://www.acmicpc.net/problem/26069

const fs = require("fs");
// const [n, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, ...input] = fs
  .readFileSync(__dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");

const set = new Set(["ChongChong"]);

input.forEach((line) => {
  const [A, B] = line.split(" ");
  const hasA = set.has(A);
  const hasB = set.has(B);
  if (hasA && hasB) return;
  if (hasA) set.add(B);
  else if (hasB) set.add(A);
});

console.log(set.size);
