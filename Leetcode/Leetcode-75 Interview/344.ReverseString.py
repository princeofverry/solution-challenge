class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return s.reverse()

        # another solution
        leng = len(s)
        i = 0
        j = leng - 1
        # for save string
        temp = []

        while (i < j):
            #misal "hello"
            temp = s[j]
            # simpan elemen terakhir di j
            # temp = 'o'
            s[j] = s[i]
            #  karakter di posisi j ditukar dengan posisi i
            # s[4] = 'h'
            # Hasil     sementara: s = "hellh"
            s[i] = temp
            # s[0] = 'o'
            # Hasil:    s = "oellh"
            i +=1 
            j -= 1