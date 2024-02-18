function countPositivesSumNegatives(input) {
  let positive = 0;
  let negative = 0;
  let result = [];

  // Check if input is null or empty array
  if (!input || input.length === 0) {
    return result;
  }

  for (let i = 0; i < input.length; i++) {
    if (input[i] > 0) {
      positive++;
    } else {
      negative += input[i];
    }
  }

  // Push positive count and sum of negatives to result array
  result.push(positive, negative);

  return result;
}
