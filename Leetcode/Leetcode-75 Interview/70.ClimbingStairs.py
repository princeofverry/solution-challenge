# pake dynamic programming
# https://aaronice.gitbook.io/lintcode/dynamic_programming/climbing-stairs

class Solution(object):
    def climbStairs(self, n):
        """
        Fungsi ini menghitung jumlah cara untuk menaiki tangga dengan n anak tangga,
        di mana pada setiap langkah Anda dapat naik 1 atau 2 anak tangga.
        
        :type n: int
        :rtype: int
        """
        # Jika jumlah anak tangga adalah 0, tidak ada cara untuk menaiki tangga
        if n == 0: return 0
        
        # Jika jumlah anak tangga adalah 1, hanya ada satu cara untuk menaiki tangga (1 langkah)
        if n == 1: return 1
        
        # Jika jumlah anak tangga adalah 2, ada dua cara untuk menaiki tangga (1+1 atau 2)
        if n == 2: return 2
        
        # Membuat array 'steps' dengan ukuran n+1 untuk menyimpan jumlah cara mencapai setiap anak tangga
        steps = [0] * (n + 1)
        
        # Inisialisasi dasar:
        # steps[0] = 0: Tidak ada cara untuk menaiki 0 anak tangga (tidak masuk akal dalam konteks ini)
        steps[0] = 0
        
        # steps[1] = 1: Hanya ada satu cara untuk menaiki 1 anak tangga
        steps[1] = 1
        
        # steps[2] = 2: Ada dua cara untuk menaiki 2 anak tangga (1+1 atau 2)
        steps[2] = 2
        
        # Mengisi array 'steps' untuk setiap anak tangga dari 3 hingga n
        for i in range(3, n + 1):
            # Jumlah cara mencapai anak tangga ke-i adalah jumlah cara mencapai anak tangga ke-(i-1) 
            # ditambah jumlah cara mencapai anak tangga ke-(i-2)
            steps[i] = steps[i - 1] + steps[i - 2]
        
        # Mengembalikan jumlah cara untuk mencapai anak tangga ke-n
        return steps[n]