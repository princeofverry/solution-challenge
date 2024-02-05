function expandedForm(num) {
  // Your code here
  const numStr = num.toString();
  const result = [];

  for (let i = 0; i < numStr.length; i++) {
    const digit = numStr[i];

    if (digit !== "0") {
      result.push(digit + "0".repeat(numStr.length - i - 1));
    }
  }
  return result.join(" + ");
}

//solusi lain
function expandedForm(num) {
  return num
    .toString()
    .split("")
    .map(
      (digit, index, array) => digit * Math.pow(10, array.length - index - 1)
    )
    .filter((value) => value !== 0)
    .join(" + ");
}
