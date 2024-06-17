class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # base checking
        if len(s) != len(t):
            return False

        # buat dictionary
        a = {}
        b = {}

        # masukin char ke dictionary s
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        
        # masukin char ke dictionary b
        for i in t:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        
        # check kesamaan dictionary
        if a == b:
            return True
        else:
            return False 


        