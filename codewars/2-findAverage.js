function findAverage(array) {
  let length = array.length;
  let total = 0;
  if (array.length === 0) {
    return 0; // Mengembalikan 0 jika array kosong
  } else {
    for (let i = 0; i < length; i++) {
      total += Number(array[i]);
    }
  }

  let average = total / length;

  return average;
}
