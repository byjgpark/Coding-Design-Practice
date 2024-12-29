from typing import List
from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             res[tuple(count)].append(s)
#         return list(res.values()) 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                ordFirst = ord(c)
                ordSecond = ord('a')
                ordThird = ordFirst - ordSecond
                count[ordThird] += 1
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)
        return list(res.values())    
    
    
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs)) 