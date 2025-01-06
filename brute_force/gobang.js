// https://www.acmicpc.net/problem/2615

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const board = Array.from({ length: 19 }, () => input().split(" ").map(Number));

function isValid(y, x) {
  return y >= 0 && y < 19 && x >= 0 && x < 19;
}

function check(y, x) {
  if (board[y][x] === 0) return { ended: false };

  let temp = false;

  const stone = board[y][x];
  let isSameStone = true;

  if (y < 15) {
    for (let ny = y + 1; ny < y + 5; ny++) {
      if (board[ny][x] !== stone) {
        isSameStone = false;
        break;
      }
    }
    if (isSameStone) {
      if ((!isValid(y + 5, x) || board[y + 5][x] !== stone) && (!isValid(y - 1, x) || board[y - 1][x] !== stone))
        temp = true;
    }
  }

  if (y < 15 && x < 15) {
    isSameStone = true;
    for (let i = 1; i < 5; i++) {
      if (board[y + i][x + i] !== stone) {
        isSameStone = false;
        break;
      }
    }
    if (isSameStone) {
      if (
        (!isValid(y + 5, x + 5) || board[y + 5][x + 5] !== stone) &&
        (!isValid(y - 1, x - 1) || board[y - 1][x - 1] !== stone)
      )
        temp = true;
    }
  }

  if (y > 3 && x < 15) {
    isSameStone = true;
    for (let i = 1; i < 5; i++) {
      if (board[y - i][x + i] !== stone) {
        isSameStone = false;
        break;
      }
    }
    if (isSameStone) {
      if (
        (!isValid(y + 1, x - 1) || board[y + 1][x - 1] !== stone) &&
        (!isValid(y - 5, x + 5) || board[y - 5][x + 5] !== stone)
      )
        temp = true;
    }
  }

  if (x < 15) {
    isSameStone = true;
    for (let nx = x + 1; nx < x + 5; nx++) {
      if (board[y][nx] !== stone) {
        isSameStone = false;
        break;
      }
    }
    if (isSameStone) {
      if ((!isValid(y, x - 1) || board[y][x - 1] !== stone) && (!isValid(y, x + 5) || board[y][x + 5] !== stone))
        temp = true;
    }
  }

  if (temp) return { ended: true, winner: stone, location: { y, x } };
  else return { ended: false };
}

function solve() {
  for (let y = 0; y < 19; y++) {
    for (let x = 0; x < 19; x++) {
      const { ended, winner, location } = check(y, x);
      if (ended) {
        console.log(winner);
        console.log(location.y + 1, location.x + 1);
        return;
      }
    }
  }
  console.log(0);
}

solve();
