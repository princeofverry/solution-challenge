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

// There are a few assumptions we will accept the year 0, even though there is no year 0 in the Gregorian Calendar.

// Also the basic rule for validating a leap year are as follows

// Most years that can be divided evenly by 4 are leap years.

// Exception: Century years are NOT leap years UNLESS they can be evenly divided by 400.
// Exception: 100 gtahun sekali gabisa cuy, yang bisa itu 499 tauhn sekali sama 4 tahun sekali
// So the years 0, -64 and 2016 will return 366 days. Whilst 1974, -10 and 666 will return 365 days.
