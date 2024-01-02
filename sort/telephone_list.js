// https://www.acmicpc.net/problem/5052

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const t = +input();

const answer = [];

for (let i = 0; i < t; i++) {
  const n = +input();
  const list = Array.from({ length: n }, () => input()).sort();

  let temp = "YES";
  list.reduce((prev, curr, _, arr) => {
    if (curr.startsWith(prev)) {
      temp = "NO";
      arr.splice(1);
    }
    return curr;
  }, "haha");
  answer.push(temp);
}

console.log(answer.join("\n"));
