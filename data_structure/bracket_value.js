// https://www.acmicpc.net/problem/2504

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const string = input();
const stack = [];

let answer = 0;
let temp = 1;

let openInfo = { "(": 2, "[": 3 };
let closeInfo = { ")": { score: 2, pair: "(", other: "[" }, "]": { score: 3, pair: "[", other: "(" } };

function solve() {
  for (let i = 0; i < string.length; i++) {
    let each = string[i];
    if (["(", "["].includes(each)) {
      stack.push(each);
      temp *= openInfo[each];
    } else {
      if (!stack.length || stack.at(-1) === closeInfo[each]["other"]) return 0;
      else if (string[i - 1] === closeInfo[each]["pair"]) answer += temp;
      stack.pop();
      temp /= closeInfo[each]["score"];
    }
  }
  if (stack.length) return 0;
  return answer;
}

console.log(solve());
