function howMuchILoveYou(nbPetals) {
  const phrases = [
    "I love you",
    "a little",
    "a lot",
    "passionately",
    "madly",
    "not at all",
  ];

  const choose = (nbPetals - 1) % phrases.length;
  //misal kita menggunakan ini petalsnya ambil 9
  //terus 9-1 = 8 % 7 = 1 jadi balik lagi sob

  return phrases[choose];
}
