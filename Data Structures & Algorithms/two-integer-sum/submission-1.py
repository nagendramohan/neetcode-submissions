class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitSet = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in visitSet :
                return [ visitSet[required] , i  ]
            else :
                visitSet[[nums]] = i 
        return [] 

        