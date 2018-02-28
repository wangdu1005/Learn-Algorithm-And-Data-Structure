import copy

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsCount = dict()        
        numsCount[nums[0]] = 1
        numsLen = len(nums)

        for i in range(1, numsLen):        
            if not numsCount.get(nums[i]):
                numsCount[nums[i]] = 1
            else:
                numsCount[nums[i]] = numsCount.get(nums[i]) + 1           
        
        preCha = 0
        sumCha = 1
        nexCha = 0
        
        res = []
        
        for key, val in numsCount.items():
            preCha = sumCha
            sumCha = sumCha * (val + 1)
            
            if preCha == 1:
                nexCha = sumCha
            else:
                nexCha = sumCha - preCha
            
            for i in range(0, nexCha):
                if len(res) == i and i == 0:
                    # the first empty change, pass [] to res == [[]]
                    res.append([])
                elif len(res) == i and i != 0:
                    singleSub = []
                    if len(res) == 1: #which mean res must only have one empty arr == [[]]
                        singleSub.append(key)
                        res.append(singleSub)
                    else:
                        cpSub = copy.deepcopy(res[i - 1])
                        cpSub.append(key)
                        res.append(cpSub)
                elif len(res) > i and i == 0:
                    cpSub2 = []
                    cpSub2.append(key)
                    res.append(cpSub2)
                elif len(res) > i and i != 0:
                    cpSub3 = copy.deepcopy(res[i])
                    cpSub3.append(key)
                    res.append(cpSub3)
        return res
        