class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevVal = set()

        for i in nums:
            if i in prevVal:
                return True 
            else : 
                prevVal.add(i)
        return False  
         