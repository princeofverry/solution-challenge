function quadratic(x1, x2) {
  let arr = [];
  arr.push(1);

  arr.push(-x1 + -x2);

  arr.push(-x1 * -x2);

  return arr;
}

// cara lain
function quadratic(x1, x2) {
  return [1, -x1 - x2, x1 * x2];
}
