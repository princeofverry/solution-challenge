function maps(x) {
  let xLength = x.length;
  let result = [];

  for (let i = 0; i < xLength; i++) {
    result.push(x[i] * 2);
  }
  return result;
}

function maps2(x) {
  return x.map((n) => n * 2);
}
