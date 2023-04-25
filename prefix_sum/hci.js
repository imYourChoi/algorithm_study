// https://www.acmicpc.net/problem/16139

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const s = input();
const q = input();
const answer = [];
const cumulative = [];

for (let i in s) {
  let temp;
  if (!cumulative.length) temp = Array(26).fill(0);
  else temp = [...cumulative.at(-1)];

  temp[s[i].charCodeAt(0) - 97] += 1;
  cumulative.push(temp);
}

for (let n = 0; n < q; n++) {
  let [alpha, from, to] = input().split(" ");
  answer.push(
    cumulative[to][alpha.charCodeAt(0) - 97] - (Number(from) && cumulative[from - 1][alpha.charCodeAt(0) - 97])
  );
}

console.log(answer.join("\n"));
