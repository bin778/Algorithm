const [n, ...arr] = require('fs').readFileSync("/dev/stdin").toString().trim().split('\n');
let result = 0;

const time = arr
    .map((num) => num.split(' ').map((num) => +num))
    .sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    } else {
      return a[1] - b[1];
    }
  });

let finish = 0;
time.forEach((time) => {
    if (time[0] >= finish) {
        result++;
        finish = time[1];
    }
});

console.log(result);