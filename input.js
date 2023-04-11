const stdin = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt')
  .toString()
  .split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

module.exports = input;
