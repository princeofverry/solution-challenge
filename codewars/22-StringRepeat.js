// 6, "I"     -> "IIIIII"
// 5, "Hello" -> "HelloHelloHelloHelloHello"

function repeatStr(n, s) {
  let hasil = "";

  for (let i = 0; i < n; i++) {
    hasil += s;
  }

  return hasil;
}

repeatStr = (n, s) => s.repeat(n);
