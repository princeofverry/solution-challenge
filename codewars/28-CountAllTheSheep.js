/*
Example 1: Input: {1, 2}, {3, 4}, 15 --> Output: 5

Example 2: Input: {3, 1, 2}, {4, 5}, 21 --> Output: 6
*/

function lostSheep(friday, saturday, total) {
  let resultSheepF = 0;
  let resultSheepS = 0;

  for (let i = 0; i < friday.length; i++) {
    resultSheepF += friday[i];
  }

  for (let i = 0; i < saturday.length; i++) {
    resultSheepS += saturday[i];
  }

  let resultSheep = resultSheepF + resultSheepS;
  return total - resultSheep;
}
