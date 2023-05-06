// https://www.acmicpc.net/problem/6603

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

while (true) {
  const string = input();
  if (string === "0") break;
  const [k, ...nums] = string.split(" ").map(Number);
  back_track(nums);
  console.log();
}

function back_track(nums, arr = []) {
  if (arr.length === 6) {
    console.log(arr.join(" "));
    return;
  }
  for (let i = 0; i < nums.length; i++) {
    back_track(nums.slice(i + 1), [...arr, nums[i]]);
  }
}
