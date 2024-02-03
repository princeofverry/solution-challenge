function persistence(num) {
  //buat variabel penghitung persistence
  let persistenceCount = 0;

  //ulangi digit sampe hanya ada 1 digit
  while (num >= 10) {
    let result = 1;

    while (num > 0) {
      //ambil digit terakhir
      let lastDigit = num % 10;

      //   kalikan result dengna digit terakhir
      result *= lastDigit;

      // lanjut ke digit berikutnya dengan pembagian
      num = Math.floor(num / 10);
    }

    num = result;
    persistenceCount++;
  }
  return persistenceCount;
}

//solusi 2 diubah ke string

function persistence2(num) {
  // Convert the number to a string to extract its digits
  let numStr = num.toString();

  // Initialize a variable to keep track of the number of multiplications
  let persistenceCount = 0;

  // Repeat until the number has only one digit
  while (numStr.length > 1) {
    // Multiply the digits of the current number
    let result = 1;
    for (let i = 0; i < numStr.length; i++) {
      result *= parseInt(numStr[i]);
    }

    // Update the number with the result and increment the persistence count
    numStr = result.toString();
    persistenceCount++;
  }
  return persistenceCount;
}
