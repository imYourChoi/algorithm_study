// https://www.acmicpc.net/problem/10974

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
const answer = [];

function back_track(remain, array = []) {
  if (remain.length === 0) answer.push(array);
  else {
    for (let i = 0; i < remain.length; i++) {
      let cur = remain.slice();
      let next = cur.splice(i, 1);
      back_track(cur.slice(), array.concat(next));
    }
  }
}

back_track(Array.from({ length: N }, (_, i) => i + 1));

console.log(answer.map(x => x.join(" ")).join("\n"));
