// https://www.acmicpc.net/problem/17471

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
const populations = [0].concat(input().split(" ").map(Number));
const graph = [[]].concat(Array.from({ length: N }, () => input().split(" ").map(Number).slice(1)));

const getCombinations = arr => {
  const result = [];

  const backtrack = (start, current) => {
    if (current.length > 0 && current.length < N) result.push([...current]);

    for (let i = start; i < arr.length; i++) {
      current.push(arr[i]);
      backtrack(i + 1, current);
      current.pop();
    }
  };

  backtrack(0, []);
  return result;
};

const areas = Array.from({ length: N }, (_, i) => i + 1);

const combinations = getCombinations(areas);

const checkConnected = citySet => {
  const visited = Array(N + 1).fill(false);

  const first = Array.from(citySet)[0];
  let queue = [first];
  visited[first] = true;

  let count = 1;

  while (queue.length > 0) {
    const temp = [];

    for (let city of queue) {
      for (let nearCity of graph[city]) {
        if (visited[nearCity] || !citySet.has(nearCity)) continue;
        visited[nearCity] = true;
        count++;
        temp.push(nearCity);
      }
    }
    queue = temp;
  }

  return count === citySet.size;
};

let answer = Infinity;

for (const comb of combinations) {
  const firstAreaSet = new Set(comb);
  const secondAreaSet = (() => {
    let temp = new Set(areas);
    for (const node of comb) temp.delete(node);
    return temp;
  })();

  if (checkConnected(firstAreaSet) && checkConnected(secondAreaSet)) {
    const firstAreaPopulation = Array.from(firstAreaSet).reduce((acc, cur) => acc + populations[cur], 0);
    const secondAreaPopulation = Array.from(secondAreaSet).reduce((acc, cur) => acc + populations[cur], 0);
    answer = Math.min(answer, Math.abs(firstAreaPopulation - secondAreaPopulation));
  }
}

console.log(answer === Infinity ? -1 : answer);
