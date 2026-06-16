class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [1] * (len(nums))

        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= res[i]

        postfix = 1
        for i in range(len(nums)):
            res[i] *= postfix
            postfix *= nums[i] 
        return res



        