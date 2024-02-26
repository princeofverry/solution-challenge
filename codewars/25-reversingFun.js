/*
Let's say you start with this: "012345"

The first thing you do is reverse it:"543210"
Then you will take the string from the 1st position and reverse it again:"501234"
Then you will take the string from the 2nd position and reverse it again:"504321"
Then you will take the string from the 3rd position and reverse it again:"504123"

Continue this pattern until you have done every single position, and then you will return the string you have created.
 For this particular number, you would return:"504132"
*/

function flipNumber(str) {
  let result = str.split(""); // Convert the string to an array of characters
  for (let i = 0; i < str.length; i++) {
    let substring = result.slice(i); // Extract substring starting from index i
    substring.reverse(); // Reverse the substring
    result = result.slice(0, i).concat(substring); // Concatenate the reversed substring with the unchanged prefix
  }
  return result.join(""); // Convert the array back to a string and return
}

// solusi lain paling masuk akal
function flipNumber(string) {
  let out = [];
  let chars = string.split("");

  while (chars.length) {
    out.push(chars.reverse().shift());
  }

  return out.join("");
}

// solusi rekursif
function flipNumber(n) {
  if (n.length === 1) return n;

  n = n.split("").reverse().join("");
  return n[0] + flipNumber(n.substr(1));
}
