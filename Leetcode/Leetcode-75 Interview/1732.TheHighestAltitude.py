# easy

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        # started with 0
        path = 0
        highest = 0
        
        # misalkan gain = 2, 3, -5, -7
        # path = 0 + 2, 2 > 0. sehingga highest = 2
        # 2 + 3 = 5, highest ganti 5
        # 5 - 5 = 0 higest masih sama
        # 0 - 7 = -7 higest stuck di 5
        
        for value in gain:
            path += value
            
            if path > highest:
                highest = path
        
        return highest
        
        