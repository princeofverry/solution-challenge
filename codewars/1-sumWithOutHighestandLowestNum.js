//cara pertama

function sumArray(array) {
  if (array == null) {
    return 0;
  } else if (array.length < 2) {
    return 0;
  } else {
    array = array.sort(function (a, b) {
      return a - b; //untuk pengurutan dari yg terkecil atau terbesar
    });
    var total = 0;
    //memulai pada iterasi 2 atau indeks pertama dan menghindari indeks terakhir
    for (var i = 1; i < array.length - 1; i++) {
      //
      total += array[i];
    }
    return total;
  }
}
