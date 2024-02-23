function pillars(numPill, dist, width) {
  if (numPill == 1 || numPill == 0) {
    return 0;
  } else if (numPill == 2) {
    return dist * 100;
  } else if (numPill >= 3) {
    return (numPill - 1) * dist * 100 + (numPill - 2) * width;
  }
}
