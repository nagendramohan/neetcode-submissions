from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in ana:
                ana[sorted_s] = [ana[sorted_s], s]
            else :
                ana[sorted_s] = [s]
        return list(ana.values())


        