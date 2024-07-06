class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # init
        x = len(haystack)
        y = len(needle)

        # ngecek sepanjang haystack
        for i in range(x): 
            # ambil haystack (slicing) kalo sama == needle baru
            if haystack[i:i+y] == needle: 
                return i
        
        return -1
