# vertical scaning easy problem

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        
        # checking first array
        base = strs[0]
        # checking next array 
        for i in range(len(base)):
            # lanjutin untuk cek another array
            for word in strs[1:]:
                # cek kalo si i == panjang base return base 0-i
                # kalo ga cek, kl hurufnya beda 
                # word[i] != base[i] return jua
                if (i == len(word) or word[i] != base[i]):
                    return base[0:i]
        return base