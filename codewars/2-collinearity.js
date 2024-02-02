//solusi 1

function collinearity(x1, y1, x2, y2) {
  if (x1 * y2 - x2 * y1 === 0) {
    //rumus kolinaer cuyyy
    return true;
  }
  return false;
}
