// https://www.acmicpc.net/problem/4386

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = +input();

const stars = Array.from({ length: n }, () => input().split(" ").map(Number));

const calculateDistance = (first, second) => ((second[1] - first[1]) ** 2 + (second[0] - first[0]) ** 2) ** 0.5;

const edges = stars.flatMap((star, index) =>
  stars.slice(index + 1).map((_star, _index) => {
    return [index, index + _index + 1, calculateDistance(star, _star)];
  })
);

edges.sort((a, b) => a[2] - b[2]);

const parents = Array.from({ length: n }, (_, i) => i);

const getParent = x => {
  if (parents[x] === x) return x;

  parents[x] = getParent(parents[x]);
  return parents[x];
};

const unionParent = (a, b) => {
  const pA = getParent(a);
  const pB = getParent(b);

  if (pA > pB) parents[pA] = pB;
  else parents[pB] = pA;
};

const checkSameParent = (a, b) => getParent(a) === getParent(b);

let answer = 0;

for (const [a, b, cost] of edges) {
  if (checkSameParent(a, b)) continue;

  unionParent(a, b);
  answer += cost;
}

console.log(Math.round(answer * 100) / 100);
