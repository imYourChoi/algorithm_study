// https://www.acmicpc.net/problem/4344

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();

for (let i = 0; i < T; i++) {
  const [N, ...nums] = input().split(" ").map(Number);
  let average = nums.reduce((a, b) => a + b, 0) / nums.length;
  let over = nums.filter(num => num > average);
  console.log(Math.round((over.length / N) * 100 * 1000) / 1000 + "%");
}

// for _ in range(int(input())):
//     N, *score = map(int, input().split())
//     average = sum(score) / len(score)
//     print("%.3f%%" % (len([x for x in score if x > average])/N*100))
