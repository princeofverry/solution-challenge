function repeats(arr) {
  let count = {}; //objek kosong

  for (let num of arr) {
    //engiterasi setiap elemen num dalam arr
    count[num] = (count[num] || 0) + 1;
  }

  let sum = 0;
  for (let num in count) {
    if (count[num] === 1) {
      sum += parseInt(num, 10);
    }
  }
  return sum;
}

//sedikit bingung
