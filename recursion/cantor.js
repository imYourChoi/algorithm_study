// https://www.acmicpc.net/problem/4779

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");

const recursion = number => {
  if (number === 1) return "-";
  const result = recursion(number / 3);
  return result + " ".repeat(number / 3) + result;
};

input.forEach(num => console.log(recursion(3 ** num)));
