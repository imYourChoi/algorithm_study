const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const original = input();
let N = original.padStart(2, "0");
let count = 0;

while (true) {
  count += 1;
  const sum = +N[0] + +N[1];
  const newN = `${+N[1] * 10 + (sum % 10)}`;
  if (newN === original) break;
  else N = newN.padStart(2, "0");
}

console.log(count);
