import copy

__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsCount = dict()        
        numsCount[nums[0]] = 1
        numsLen = len(nums)
        # print(numsLen)

        for i in range(1, numsLen):        
            # print("nums: {}".format(nums[i]))
            if not numsCount.get(nums[i]):
                numsCount[nums[i]] = 1
            else:
                numsCount[nums[i]] = numsCount.get(nums[i]) + 1           
        # print(numsCount)
        
        preCha = 0
        sumCha = 1
        nexCha = 0
        
        res = []
        newSub = []
        # print("newSub init len: ", len(newSub))
        
        for key, val in numsCount.items():
            # print("key: ", key, ",val: ", val)
            preCha = sumCha
            sumCha = sumCha * (val + 1)
            
            if preCha == 1:
                nexCha = sumCha
            else:
                nexCha = sumCha - preCha
            
            for i in range(0, nexCha):
                if len(res) == i and i == 0:
                    print("the len of res: ", len(res))
                    # the first empty change, pass [] to res == [[]]
                    res.append(newSub)
                    # newSub.clear()
                    # print("if len(res) == i and i == 0: res: ", res)
                elif len(res) <= i and i != 0:
                    cpNewSub = []
                    if len(res) == 1: #which mean res must only have one empty arr == [[]]
                        cpNewSub.append(key)
                        res.append(cpNewSub)
                    else:
                        cpSub = copy.deepcopy(res[i - 1])
                        cpSub.append(key)
                        res.append(cpSub)
                    # print("elif len(res) <= i and i != 0: res: ", res)
                elif len(res) > i and i == 0:
                    cpSub2 = []
                    cpSub2.append(key)
                    res.append(cpSub2)
                    # print("elif len(res) > i and i == 0: res: ", res)
                elif len(res) > i and i != 0:
                    cpSub3 = copy.deepcopy(res[i])
                    cpSub3.append(key)
                    res.append(cpSub3)
                    # print("elif len(res) > i and i != 0: res: ", res)
        return res
        