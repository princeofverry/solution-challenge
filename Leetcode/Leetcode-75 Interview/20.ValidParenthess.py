class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # define stack
        stack = []
        # define dictionary with key and value
        d = {"(":")", "{":"}", "[":"]"}
        
        # check 
        for char in s:
            if char in d:
                stack.append(char)
            else:
                # jika stack kosong atau
                # stack paling atas itu pasangannya
                # ga seusai dengan char selanjutnya maka 
                # return false
                if stack == [] or d[stack.pop()] != char:
                    return False
        return True if stack == [] else False