// multiply(3) == 15 // 3 * 5¹
// multiply(10) == 250 // 10 * 5²
// multiply(200) == 25000 // 200 * 5³
// multiply(0) == 0 // 0 * 5¹
// multiply(-3) == -15 // -3 * 5¹

function multiply(number) {
  let panjang = Math.abs(number).toString().length;
  return number * 5 ** panjang;
}
