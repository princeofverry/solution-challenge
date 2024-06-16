# easy
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        
        numToStr = str(x)
        # reverse
        reverseNum = numToStr[::-1]

        return numToStr == reverseNum


        