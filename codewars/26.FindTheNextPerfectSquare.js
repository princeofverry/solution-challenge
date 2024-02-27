function findNextSquare(sq) {
  let resultSq = Math.sqrt(sq);

  if (Number.isInteger(resultSq)) {
    let resultAns = resultSq + 1;
    return resultAns ** 2;
  } else {
    return -1;
  }
}
