// https://www.acmicpc.net/problem/4195
// https://www.acmicpc.net/source/55497489

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();
const answer = [];

function find(a, parent) {
  if (parent.get(a) === a) return a;
  const p = find(parent.get(a), parent);
  parent.set(a, p);
  return p;
}
function union(a, b, parent, number, answer) {
  const A = find(a, parent);
  const B = find(b, parent);

  if (A !== B) {
    parent.set(B, A);
    number.set(A, number.get(A) + number.get(B));
  }
  answer.push(number.get(A));
}

function friend() {
  const F = +input();
  const parent = new Map();
  const number = new Map();
  for (let f = 0; f < F; f++) {
    const [one, two] = input().split(" ");
    if (!parent.has(one)) {
      parent.set(one, one);
      number.set(one, 1);
    }
    if (!parent.has(two)) {
      parent.set(two, two);
      number.set(two, 1);
    }
    union(one, two, parent, number, answer);
  }
}

for (let t = 0; t < T; t++) friend();

console.log(answer.join("\n"));
