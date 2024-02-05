function sum(numbers) {
  "use strict";

  const length = numbers.length;
  let total = 0;

  for (let i = 0; i < length; i++) {
    total += numbers[i];
  }

  return total;
}

// solusi lain

sum2 = (numbers) => {
  return numbers.reduce((a, b) => a + b, 0);
};

// solusi 3
const sum = (num) => num.reduce((acc, curr) => acc + curr, 0);
//kudu belajar seehh
