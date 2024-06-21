class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # bentuk tanpa spasi dan koma, hanya mengambil char
        sConvert = ''.join(char.lower() for char in s if char.isalnum())

        # membalikkan aja
        sInverse = sConvert[::-1]

        if sConvert == sInverse:
            return True
        False
        
        
        
        # solusi lain
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # penggunaan 2 pointer
        # selama pointer l < r
        # pointer l sama r bakal ngecek selama periode perulangan
        
        N = len(s)
        L = 0
        R = N - 1

        while L < R:
            # ngecek apakah dia ini huruf pa bukan
            if not s[L].isalnum():
                L += 1
                # lanjut ke iterasi selanjutnya
                continue

            if not s[R].isalnum():
                R -= 1
                # lanjut ke iterasi selanjutnya
                continue

            # ngecek kesamaan 2 pointer
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1

        return True


        


        