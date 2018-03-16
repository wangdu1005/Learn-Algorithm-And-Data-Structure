__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"
# Reference: http://bookshadow.com/weblog/2015/09/19/leetcode-move-zeroes/

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # My stupid wrong version:
        # zeroCount = 0
        # numsLen = len(nums)
        # for i in range(numsLen):
        #     if nums[i] == 0:
        #         rightLen = numsLen - i
        #         for j in range(rightLen):
        #             nextInx = i + j + 1
                    
        #             if nextInx < numsLen:
        #                 if nums[nextInx] == 0:
        #                     currInx = i
        #                     continue
                        
        #             if nextInx < numsLen:
        #                 tmp = nums[nextInx]
        #                 nums[nextInx] = nums[currInx]
        #                 nums[currInx] = tmp
        
        # Correct version:
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                
                # sweet syntax version:
                nums[x], nums[y] = nums[y], nums[x]
                
                # traditional version:
                # tmp = nums[x]
                # nums[x] = nums[y]
                # nums[y] = tmp
                
                y += 1