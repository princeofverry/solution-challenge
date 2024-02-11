// [true,  true,  true,  false,
//     true,  true,  true,  true ,
//     true,  false, true,  false,
//     true,  false, false, true ,
//     true,  true,  true,  true ,
//     false, false, true,  true]
//   The correct answer would be 17

function countSheeps(sheep) {
  let result = 0;

  for (let i = 0; i < sheep.length; i++) {
    if (sheep[i] === true) {
      result += 1;
    }
  }
  return result;
}
