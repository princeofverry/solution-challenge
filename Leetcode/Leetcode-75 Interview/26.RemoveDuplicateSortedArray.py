# easy 

# array of nums 0 1 1 2 2 3 3 
# return 4, nums = [0, 1, 2, 3]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)  # Menghitung panjang array nums

        if n == 1:
            return 1  # Jika hanya ada satu elemen, itu pasti unik, maka kembalikan 1

        output = 1  # Menandai posisi elemen unik terakhir, dimulai dari elemen kedua

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                # Jika elemen saat ini berbeda dengan elemen sebelumnya yang sudah diverifikasi sebagai unik
                # Masukkan elemen saat ini ke posisi output untuk menyimpan elemen unik
                nums[output] = nums[i]
                output += 1  # Tandai penambahan elemen unik baru
        
        return output  # Mengembalikan jumlah elemen unik dalam array nums
