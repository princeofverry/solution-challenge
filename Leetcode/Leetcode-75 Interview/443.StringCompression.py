class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0  # track the chars in array
        counter = 1

        for j in range(1, len(chars) + 1):
            # pengecekan karakter skrng apa sama kek sblmnya
            if j < len(chars) and chars[j] == chars[j-1]:
                counter += 1

            # jika karakter beda
            else:
                # Menulis karakter pada posisi j-1 ke posisi i karena kelompok karakter berulang telah berakhir.
                chars[i] = chars[j-1]
                # majuin 1 step untuk angka
                i = i + 1
                if counter > 1:
                    # ubah counter jadi string
                    for k in str(counter):
                        chars[i] = k
                        # majuin 1 step untuk persiapan huruf yang beda selanjutnya
                        i += 1
                # reset
                counter = 1
        return i
