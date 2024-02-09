function invert(array) {
  let result = [];

  for (let i = 0; i < array.length; i++) {
    if (array[i] == null) {
      result.push(null);
    } else {
      result.push(array[i] * -1);
    }
  }
  return result;
}

// solusi 2 dengan map jadi semua elemen dikali -1
function invert(array) {
  return array.map((e) => e * -1);
}
