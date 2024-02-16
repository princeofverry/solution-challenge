function yearDays(year) {
  if (year % 400 === 0) {
    return `${year} has 366 days`;
  } else if (year % 100 === 0) {
    return `${year} has 365 days`;
  } else if (year % 4 === 0) {
    return `${year} has 366 days`;
  } else {
    return `${year} has 365 days`;
  }
}

function yearDays(year) {
  var result = 365;
  if (year % 400 == 0 || (year % 4 == 0 && year % 100 !== 0)) {
    result = 366;
  }

  return year + " has " + result + " days";
}
