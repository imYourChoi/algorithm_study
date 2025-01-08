// https://www.acmicpc.net/problem/1914

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = +input();

const array = [];
const moves = Array(101).fill(0);
moves[1] = 1;

const hanoi = (num, start, end) => {
  if (moves[num] !== 0 && N > 20) return moves[num];
  if (num === 1) {
    if (N <= 20) array.push(`${start} ${end}`);
    return 1;
  }

  const move1 = BigInt(hanoi(num - 1, start, 6 - start - end));
  if (moves[num - 1] === 0) moves[num - 1] = move1;

  if (N <= 20) array.push(`${start} ${end}`);

  const move2 = BigInt(hanoi(num - 1, 6 - start - end, end));
  return move1 + BigInt(1) + move2;
};

console.log(String(hanoi(N, 1, 3)));
if (N <= 20) console.log(array.join("\n"));
