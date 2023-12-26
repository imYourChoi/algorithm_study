// https://www.acmicpc.net/problem/9205

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

const solve = (start, finish, shops) => {
  let visited = new Set();
  let queue = [start];
  visited.add(start.toString());

  while (queue.length) {
    let temp = [];

    for (let i = 0; i < queue.length; i++) {
      const cur = queue[i];
      if (Math.abs(cur[0] - finish[0]) + Math.abs(cur[1] - finish[1]) <= 1000) return "happy";

      for (shop of shops) {
        if (visited.has(shop.toString())) continue;
        if (Math.abs(cur[0] - shop[0]) + Math.abs(cur[1] - shop[1]) <= 1000) {
          visited.add(shop.toString());
          temp.push(shop);
        }
      }
    }
    queue = temp;
  }
  return "sad";
};

let answer = [];
for (let T = 0; T < t; T++) {
  const n = +input();

  let start = input().split(" ").map(Number);

  let shops = [];
  for (let i = 0; i < n; i++) {
    const shop = input().split(" ").map(Number);
    shops.push(shop);
  }
  let finish = input().split(" ").map(Number);

  answer.push(solve(start, finish, shops));
}

console.log(answer.join("\n"));
