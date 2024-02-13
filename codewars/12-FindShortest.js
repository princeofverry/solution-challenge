// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.

function findShort(s) {
  const words = s.split(" "); // Change variable name to "words" instead of "word"

  let shortestLength = Infinity;

  for (let word of words) {
    if (word.length < shortestLength) {
      shortestLength = word.length;
    }
  }
  return shortestLength;
}
