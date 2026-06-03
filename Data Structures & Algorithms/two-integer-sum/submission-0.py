class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # required = {}
        # res = []

        # for i in range(len(nums)):
        #     req = target - nums[i]
        #     if req in required:
        #         return [required[req], i]
        #     required[nums[i]] = i
        prevMap = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i ]
            prevMap[n] = i 

                 

        