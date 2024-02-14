// * Input: [1,2,3,4,5], output = [2,3,4,5]
// * Input: [5,3,2,1,4], output = [5,3,2,4]
// * Input: [2,2,1,2,1], output = [2,2,2,1]

function removeSmallest(numbers) {
  if (numbers.length === 0) {
    return [];
  }

  let minIndex = 0;
  let minValue = numbers[0];

  //cari index minimum
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < minValue) {
      minIndex = i; //diperlukan untuk menghapus / pop
      minValue = numbers[i];
    }
  }

  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (i !== minIndex) {
      //disini cuyy kepakenya minIndex
      result.push(numbers[i]);
    }
  }
  // solusi lain
  // const result = numbers.slice(); // Create a shallow copy of the original array
  //   result.splice(minIndex, 1);
  return result;
}
