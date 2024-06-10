/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let n = nums.length;
  // base case
  if (n == 1) {
    return [];
  }

  //   if nums [1,2,3,4]

  //   inisialisasi array left dan right (as pref and suf)
  let leftProduct = new Array(n).fill(1);
  let rightProduct = new Array(n).fill(1);
  let result = new Array(n);

  //   buat array left products dimulai dari left[1] karena left[0] = 1 sudah pasti
  for (let i = 1; i < n; i++) {
    leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
  } // ini bakal ngisi seluruhnya misal nums diatas maka [1, 1, 2, 6]

  //   buat array right product ingat kalo letProd[n-1] = 1 karena memang begitu perhitungannya
  for (let i = n - 2; i >= 0; i--) {
    rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
  }
  //output [1,1,4,1] i = 2
  //   [1,12,4,1] i =1
  // [24, 12, 4, 1] i =0

  //   kaliin cross dua array itu
  for (let i = 0; i < n; i++) {
    result[i] = rightProduct[i] * leftProduct[i];
  }

  return result;
};
