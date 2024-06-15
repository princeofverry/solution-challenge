class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)

        if s[0] =='-':
            reversed_s = '-' + s[:0:-1]
        
        # langsung reverse
        else:
            reversed_s = s[::-1]
        
        reversed_x = int(reversed_s)

        # cek overflow
        if reversed_x < -2**31 or reversed_x> 2**31 -1:
            return 0

        return reversed_x