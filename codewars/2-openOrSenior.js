function openOrSenior(data) {
  //result untuk masukin output
  let output = [];

  for (let i = 0; i < data.length; i++) {
    let arrayIndex0 = data[i][0]; //perhatikan untuk ambil data array ada nama var dan []
    let arrayIndex1 = data[i][1];

    if (arrayIndex0 >= 55 && arrayIndex1 > 7) {
      output.push("Senior");
    } else {
      output.push("Open");
    }
  }
  return output;
}
