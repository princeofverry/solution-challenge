//solusi 1

function grow(x) {
  let total = 1;
  let growLenght = x.length;
  for (let i = 0; i < growLenght; i++) {
    total *= x[i];
  }
  return total;
}

function grow2(x) {
  x.reduce((a, b) => a * b);
}
