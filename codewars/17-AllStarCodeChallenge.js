// str_count("Hello", 'o'); // returns 1
// str_count("Hello", 'l'); // returns 2
// str_count("", 'z'); // returns 0

function strCount(str, letter) {
  counter = 0;
  for (let i = 0; i < str.length; i++) {
    if (letter == str[i]) {
      counter++;
    }
  }
  return counter;
}
