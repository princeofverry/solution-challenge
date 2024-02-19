String.prototype.isUpperCase = function () {
  return (
    this.valueOf()
      .split("")
      .filter((char) => char.toUpperCase() === char).length === this.length
  );
};

//solusi lain
String.prototype.isUpperCase = function () {
  return this.toUpperCase() === this.toString();
};

//define the string prototype here
String.prototype.isUpperCase = function () {
  if (this.toString() == this.toUpperCase()) {
    return true;
  } else {
    return false;
  }
};
