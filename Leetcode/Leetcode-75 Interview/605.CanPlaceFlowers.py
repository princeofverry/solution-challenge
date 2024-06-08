class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # misal [0] maka
        # 0 [0] 0 makanya return true
        if n == 0:
            return True

        # as a count penhitung tanaman
        planted = 0

        for i in range(len(flowerbed)):
            # definisiin apa itu kanan dan kiri untuk semua kasus
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

            # kalo kanan kiri dan pointernya 0 maka tanaman bisa dimasupin 1
            if (flowerbed[i] == 0 and left and right):
                # kalo kasus sesuai pointer jadi 1
                flowerbed[i] = 1
                planted += 1

                if (planted == n):
                    return True
        return False
