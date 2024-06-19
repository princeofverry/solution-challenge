# easy 

# array of nums 0 1 1 2 2 3 3 
# return 4, nums = [0, 1, 2, 3]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)


        if n == 1:
            return 1

        # angka awal pasti uniq terus
        output = 1

        for i in range (1,n):
            if nums[i] != nums[i-1]:
                # masukin output yang uniq di
                nums[output] = nums[i]
                output += 1

            
        
        return output
            
        