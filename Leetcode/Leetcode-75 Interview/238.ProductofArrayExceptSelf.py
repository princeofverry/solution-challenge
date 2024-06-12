class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # base case
        if n == 1:
            return []

        # inisiasilasi semuanya
        leftProduct = [1] * n
        rightProduct = [1] * n
        result = [1] * n

        # left array product 1 inklusif = 1
        for i in range(1, n):
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
        
        # right array product, -1 tengah maksudnya itu eksklusif
        # ibaratnya kayak >-1
        # kl yg paling kanan maksudnya stepnya
        for i in range(n-2, -1, -1):
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1]
        
        for i in range(n):
            result[i] = rightProduct[i] * leftProduct[i]

        return result

