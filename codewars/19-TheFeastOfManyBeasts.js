function feast(beast, dish) {
  let first = beast[0];
  let last = beast[beast.length - 1];

  if (dish[0] === first && dish[dish.length - 1] === last) {
    return true;
  } else {
    return false;
  }
}
