class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain_duplicate_set = set()
        for i in nums:
            if i in contain_duplicate_set:
                return True 
            else :
                contain_duplicate_set.add(i)
        return False 