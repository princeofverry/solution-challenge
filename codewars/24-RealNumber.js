/*
is valid? 'In with a chance'
isnt valid? || 'empty string' ? : 'Plenty more fish in the sea'

valid category
+44 / 07
only 9 digit 
start on index[2]
and split '--'
*/

function validateNumber(str) {
  // untuk replace '+' jika ada
  let cleaned = str.replace(/[-\s]/g, "");

  if (cleaned == "") {
    return "Plety more fish in the sea";
  }

  if (
    (cleaned.startsWith("07") && cleaned.length === 11) ||
    (cleaned.startsWith("+447") && cleaned.length === 13)
  ) {
    for (let i = 2; i < cleaned.length; i++) {
      if (!/\d/.test(cleaned[i])) {
        return "Plenty more fish in the sea";
      }
    }
    return "In with a chance";
  } else {
    return "Plenty more fish in the sea";
  }
}

// solusi masuk akal
function validateNumber(str) {
  //Your code here
  let strSplit = str.split("-").join("").split("+").join("");
  let temp1 = strSplit.slice(0, 3);
  let temp2 = strSplit.slice(0, 2);

  if (temp1 === "447" && strSplit.length === 12) return "In with a chance";
  else if (temp2 === "07" && strSplit.length === 11) return "In with a chance";
  else return "Plenty more fish in the sea";
}
