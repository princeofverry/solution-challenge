function cubeChecker(volume, side) {
  if (volume <= 0 || side <= 0) {
    return false;
  }

  let cubeVol = side ** 3;

  return volume === cubeVol;
}
