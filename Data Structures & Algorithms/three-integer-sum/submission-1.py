class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            l , r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else :
                    res.append([a,nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l+1] and l < r :
                        l += 1
        return res








        # nums.sort()
        # l , r = 0 , len(nums) -1 
        # res = []

        # while l < r :
        #     for i in range(len(nums)) :
        #         curSum = nums[l] + nums[r] + nums[i]
        #         if nums[i] == nums[l]:
        #             continue
        #         elif nums[i] == nums[r] :
        #             continue

        #         elif curSum  == 0 :
        #             res.append([nums[l],nums[r],nums[i]])
        #         elif (curSum > 0):
        #             r -= 1 
        #         else:
        #             l += 1
        #     # l += 1
        #     # r -= 1
        # # res = [list(x) for x in set(tuple(sorted(x)) for x in res)]
        # return res
        # # return res
        