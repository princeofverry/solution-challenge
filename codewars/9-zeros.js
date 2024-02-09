// zeros(6) = 1
// # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

// zeros(12) = 2
// # 12! = 479001600 --> 2 trailing zeros

function zeros(n) {
  let count = 0;

  // Count the number of factors of 5 in the range [1, n]
  for (let i = 5; n / i >= 1; i *= 5) {
    count += Math.floor(n / i);
  }

  return count;
}
