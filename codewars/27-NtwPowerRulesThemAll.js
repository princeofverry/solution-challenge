function modifiedSum(a, n) {
  let resultA = 0;

  for (let i = 0; i < a.length; i++) {
    resultA += a[i] ** n;
  }

  let resultB = 0;
  for (let i = 0; i < a.length; i++) {
    resultB += a[i];
  }

  return resultA - resultB;
}
