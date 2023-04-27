// https://www.acmicpc.net/problem/1193

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

const line = Math.ceil(Math.sqrt(2 * N + 0.25) - 0.5);
const sum = (line * (line + 1)) / 2;
console.log(line % 2 ? `${sum - N + 1}/${line - (sum - N)}` : `${line - (sum - N)}/${sum - N + 1}`);
